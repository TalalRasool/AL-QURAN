import 'dart:async';
import 'dart:convert';

import 'package:get/get.dart';

import '../../features/hadith/data/hadith_db_helper.dart';
import '../data/json_utils.dart';
import '../data/models/app_bookmark.dart';
import '../data/quran_repository.dart';
import '../routes/app_routes.dart';
import '../services/storage_service.dart';
import '../widgets/bookmark_icon_button.dart';

class BookmarkController extends GetxService {
  final items = <AppBookmark>[].obs;

  late StorageService _storage;
  Worker? _legacyWorker;
  bool _syncingLegacy = false;
  var _didLoad = false;

  Future<BookmarkController> init() async {
    _storage = Get.find<StorageService>();
    _loadFromStorage();
    await _migrateLegacyIfNeeded();
    _legacyWorker = ever(_storage.bookmarks, (_) {
      if (_syncingLegacy) return;
      _reconcileTranslationSurahs(_storage.bookmarks.toList());
    });
    unawaited(_enrichMetadata());
    return this;
  }

  @override
  void onInit() {
    super.onInit();
    if (_didLoad || !Get.isRegistered<StorageService>()) return;
    _storage = Get.find<StorageService>();
    _loadFromStorage();
  }

  /// Decodes the JSON bookmark list from local storage after a cold start.
  void _loadFromStorage() {
    final decoded = _decodeBookmarksJson(
      _storage.readUnifiedBookmarksJson() ?? '',
    );
    if (decoded.isNotEmpty) {
      items.assignAll(decoded);
    } else {
      items.assignAll(
        _storage
            .loadUnifiedBookmarks()
            .map(AppBookmark.fromJson)
            .where((item) => item.id.isNotEmpty),
      );
    }
    _didLoad = true;
  }

  /// Encodes bookmarked items (surah, ayah/page, ids) as a JSON string.
  String encodeBookmarksJson() {
    return jsonEncode(items.map((item) => item.toJson()).toList());
  }

  List<AppBookmark> _decodeBookmarksJson(String json) {
    if (json.trim().isEmpty) return const [];
    try {
      final decoded = jsonDecode(json);
      if (decoded is! List) return const [];
      return [
        for (final item in decoded)
          if (item is Map)
            AppBookmark.fromJson(Map<String, dynamic>.from(item)),
      ].where((item) => item.id.isNotEmpty).toList();
    } catch (_) {
      return const [];
    }
  }

  @override
  void onClose() {
    _legacyWorker?.dispose();
    super.onClose();
  }

  List<AppBookmark> ofType(BookmarkType type) =>
      items.where((item) => item.type == type).toList();

  bool has(String id) => items.any((item) => item.id == id);

  bool isTranslationBookmarked(int surahNumber) =>
      has(AppBookmark.translationId(surahNumber));

  bool isMushafBookmarked(int page) => has(AppBookmark.mushafId(page));

  bool isHadithBookmarked(int hadithId) => has(AppBookmark.hadithId(hadithId));

  bool isDuaBookmarked(String duaId) => has(AppBookmark.duaId(duaId));

  Future<bool> toggle(AppBookmark bookmark) async {
    final added = !has(bookmark.id);
    if (added) {
      items.insert(0, bookmark);
    } else {
      items.removeWhere((item) => item.id == bookmark.id);
    }
    await _persist();
    showBookmarkSnackbar(added: added);
    return added;
  }

  Future<void> remove(String id) async {
    if (!has(id)) return;
    items.removeWhere((item) => item.id == id);
    await _persist();
  }

  Future<void> open(AppBookmark bookmark) async {
    switch (bookmark.type) {
      case BookmarkType.translation:
        final surahNumber = asInt(bookmark.payload['surahNumber']);
        if (surahNumber < 1) return;
        await Get.toNamed(AppRoutes.surahDetail, arguments: surahNumber);
      case BookmarkType.mushaf:
        final page = asInt(bookmark.payload['page']);
        if (page < 1) return;
        await Get.toNamed(AppRoutes.mushaf, arguments: {'page': page});
      case BookmarkType.hadith:
        await _openHadith(bookmark);
      case BookmarkType.dua:
        final duaId = '${bookmark.payload['duaId'] ?? ''}'.trim();
        if (duaId.isEmpty) return;
        await Get.toNamed(
          AppRoutes.tasbih,
          arguments: {'tab': 1, 'duaId': duaId},
        );
    }
  }

  Future<void> _openHadith(AppBookmark bookmark) async {
    var bookId = asInt(bookmark.payload['bookId']);
    var chapterId = asInt(bookmark.payload['chapterId']);
    var bookName = '${bookmark.payload['bookName'] ?? bookmark.title}'.trim();
    var chapterName = '${bookmark.payload['chapterName'] ?? ''}'.trim();
    final hadithNumber = bookmark.payload['hadithNumber'];
    final hadithId = asInt(bookmark.payload['hadithId']);

    if (chapterId < 1 && hadithId > 0 && Get.isRegistered<HadithDbHelper>()) {
      final hadith = await Get.find<HadithDbHelper>().getHadithById(hadithId);
      if (hadith != null) {
        bookId = hadith.bookId;
        chapterId = hadith.chapterId;
        await _enrichHadithNames(
          bookmark.id,
          hadith.bookId,
          hadith.chapterId,
        );
        final updated = items.cast<AppBookmark?>().firstWhere(
          (item) => item?.id == bookmark.id,
          orElse: () => null,
        );
        bookName = '${updated?.payload['bookName'] ?? bookName}'.trim();
        chapterName = '${updated?.payload['chapterName'] ?? chapterName}'.trim();
      }
    }

    if (chapterId < 1) return;
    await Get.toNamed(
      AppRoutes.hadithRead,
      arguments: {
        'bookId': bookId,
        'chapterId': chapterId,
        'bookName': bookName,
        'chapterName': chapterName,
        'hadithNumber': ?hadithNumber,
      },
    );
  }

  Future<void> _migrateLegacyIfNeeded() async {
    final seen = items.map((item) => item.id).toSet();
    var changed = false;

    for (final surahNumber in _storage.bookmarks) {
      final id = AppBookmark.translationId(surahNumber);
      if (seen.contains(id)) continue;
      items.add(AppBookmark.translation(surahNumber: surahNumber));
      seen.add(id);
      changed = true;
    }

    for (final hadithId in _storage.hadithBookmarks) {
      final id = AppBookmark.hadithId(hadithId);
      if (seen.contains(id)) continue;
      items.add(
        AppBookmark.hadith(
          hadithId: hadithId,
          bookId: 0,
          chapterId: 0,
          hadithNumber: 0,
        ),
      );
      seen.add(id);
      changed = true;
    }

    for (final duaId in _storage.duaBookmarks) {
      final id = AppBookmark.duaId(duaId);
      if (seen.contains(id)) continue;
      items.add(AppBookmark.dua(duaId: duaId, title: duaId));
      seen.add(id);
      changed = true;
    }

    if (changed) await _persist();
  }

  void _reconcileTranslationSurahs(List<int> surahs) {
    final wanted = surahs.toSet();
    final existing = <int>{};
    var changed = false;

    items.removeWhere((item) {
      if (item.type != BookmarkType.translation) return false;
      final number = asInt(item.payload['surahNumber']);
      existing.add(number);
      final drop = !wanted.contains(number);
      if (drop) changed = true;
      return drop;
    });

    for (final number in wanted) {
      if (existing.contains(number)) continue;
      items.insert(0, AppBookmark.translation(surahNumber: number));
      changed = true;
    }

    if (changed) {
      unawaited(_persistUnifiedOnly());
      unawaited(_enrichMetadata());
    }
  }

  Future<void> _enrichMetadata() async {
    var changed = false;

    if (Get.isRegistered<QuranRepository>()) {
      try {
        final surahs = await Get.find<QuranRepository>().getAllSurahs();
        final byNumber = {for (final surah in surahs) surah.number: surah};
        items.assignAll(
          items.map((item) {
            if (item.type != BookmarkType.translation) return item;
            final number = asInt(item.payload['surahNumber']);
            final surah = byNumber[number];
            if (surah == null) return item;
            final enriched = item.copyWith(
              title: surah.englishName,
              subtitle: [
                if (surah.arabicName.trim().isNotEmpty) surah.arabicName,
                if (surah.verseCount > 0) '${surah.verseCount} ayahs',
              ].join(' · '),
              payload: {
                ...item.payload,
                'englishName': surah.englishName,
                'arabicName': surah.arabicName,
                'verseCount': surah.verseCount,
              },
            );
            if (enriched.title != item.title ||
                enriched.subtitle != item.subtitle) {
              changed = true;
              return enriched;
            }
            return item;
          }),
        );
      } catch (_) {}
    }

    if (Get.isRegistered<HadithDbHelper>()) {
      final db = Get.find<HadithDbHelper>();
      for (var i = 0; i < items.length; i++) {
        final item = items[i];
        if (item.type != BookmarkType.hadith) continue;
        final hadithId = asInt(item.payload['hadithId']);
        if (hadithId < 1) continue;
        final needsMeta = asInt(item.payload['chapterId']) < 1 ||
            '${item.payload['bookName'] ?? ''}'.trim().isEmpty;
        if (!needsMeta) continue;
        try {
          final hadith = await db.getHadithById(hadithId);
          if (hadith == null) continue;
          final book = await db.getBookById(hadith.bookId);
          final chapter = await db.getChapterById(hadith.chapterId);
          items[i] = AppBookmark.hadith(
            hadithId: hadith.id,
            bookId: hadith.bookId,
            chapterId: hadith.chapterId,
            hadithNumber: hadith.hadithNumber,
            bookName: book?.name ?? '',
            chapterName: chapter?.name ?? '',
          );
          changed = true;
        } catch (_) {}
      }
    }

    if (changed) await _persistUnifiedOnly();
  }

  Future<void> _enrichHadithNames(
    String bookmarkId,
    int bookId,
    int chapterId,
  ) async {
    if (!Get.isRegistered<HadithDbHelper>()) return;
    try {
      final db = Get.find<HadithDbHelper>();
      final book = await db.getBookById(bookId);
      final chapter = await db.getChapterById(chapterId);
      final index = items.indexWhere((item) => item.id == bookmarkId);
      if (index < 0) return;
      final current = items[index];
      items[index] = current.copyWith(
        title: (book?.name ?? current.title),
        subtitle: [
          current.subtitle,
          if (chapter != null && chapter.name.trim().isNotEmpty) chapter.name,
        ].join(' · '),
        payload: {
          ...current.payload,
          'bookId': bookId,
          'chapterId': chapterId,
          'bookName': book?.name ?? '',
          'chapterName': chapter?.name ?? '',
        },
      );
      await _persistUnifiedOnly();
    } catch (_) {}
  }

  Future<void> _persist() async {
    await _persistUnifiedOnly();
    await _writeLegacy();
  }

  Future<void> _persistUnifiedOnly() {
    return _storage.saveUnifiedBookmarksJson(encodeBookmarksJson());
  }

  Future<void> _writeLegacy() async {
    _syncingLegacy = true;
    try {
      final surahs = [
        for (final item in items)
          if (item.type == BookmarkType.translation)
            asInt(item.payload['surahNumber']),
      ].where((number) => number > 0).toList();
      await _storage.replaceBookmarks(surahs);

      final hadithIds = [
        for (final item in items)
          if (item.type == BookmarkType.hadith)
            asInt(item.payload['hadithId']),
      ].where((id) => id > 0).toList();
      await _storage.replaceHadithBookmarks(hadithIds);

      final duaIds = [
        for (final item in items)
          if (item.type == BookmarkType.dua)
            '${item.payload['duaId'] ?? ''}'.trim(),
      ].where((id) => id.isNotEmpty).toList();
      await _storage.replaceDuaBookmarks(duaIds);
    } finally {
      _syncingLegacy = false;
    }
  }
}
