import 'dart:async';

import 'package:flutter/widgets.dart';
import 'package:get/get.dart';

import '../../core/controllers/bookmark_controller.dart';
import '../../core/data/json_utils.dart';
import '../../core/data/models/app_bookmark.dart';
import '../../core/services/storage_service.dart';
import 'data/hadith_db_helper.dart';
import 'data/hadith_l10n.dart';
import 'data/hadith_models.dart';

class HadithReadController extends GetxController {
  static const pageSize = HadithDbHelper.pageSize;

  final ahadith = <Hadith>[].obs;
  final searchQuery = ''.obs;
  final isLoading = false.obs;
  final isLoadingMore = false.obs;
  final hasMore = true.obs;
  final errorMessage = RxnString();
  final englishChapterName = ''.obs;
  final englishBookName = ''.obs;
  final scrollController = ScrollController();

  final HadithDbHelper _db = Get.find<HadithDbHelper>();
  final StorageService _storage = Get.find<StorageService>();
  Timer? _searchDebounce;
  int _offset = 0;
  int _requestId = 0;

  int get chapterId {
    final args = Get.arguments;
    if (args is Map) return asInt(args['chapterId']);
    if (args is int) return args;
    return 0;
  }

  int get bookId {
    final args = Get.arguments;
    if (args is Map) return asInt(args['bookId']);
    return 0;
  }

  String get bookName =>
      HadithL10n.bookName(bookId, fallback: englishBookName.value);

  String get chapterName {
    final english = englishChapterName.value.trim();
    if (english.isEmpty) return HadithL10n.ui('hadith');
    return HadithL10n.chapterName(english);
  }

  String get activeTranslationKey =>
      '${_storage.selectedTranslationId.value}|${_storage.selectedTranslationLanguage.value}';

  String get languageCode => HadithL10n.languageCode();

  /// Selected translation, or English when that book has no text for this hadith.
  String translationOf(Hadith hadith) => hadith.textFor(languageCode);

  /// Language of [translationOf]. English when the selected edition is missing.
  String translationLanguageOf(Hadith hadith) =>
      hadith.resolvedLanguage(languageCode);

  bool translationIsRtl(Hadith hadith) =>
      HadithL10n.isRtl(translationLanguageOf(hadith));

  RxList<AppBookmark> get bookmarks => Get.find<BookmarkController>().items;

  Future<void> toggleBookmark(Hadith hadith) {
    return Get.find<BookmarkController>().toggle(
      AppBookmark.hadith(
        hadithId: hadith.id,
        bookId: hadith.bookId > 0 ? hadith.bookId : bookId,
        chapterId: hadith.chapterId > 0 ? hadith.chapterId : chapterId,
        hadithNumber: hadith.hadithNumber,
        bookName: englishBookName.value,
        chapterName: englishChapterName.value,
      ),
    );
  }

  @override
  void onInit() {
    super.onInit();
    final args = Get.arguments;
    if (args is Map) {
      final name = '${args['chapterName'] ?? ''}'.trim();
      if (name.isNotEmpty) englishChapterName.value = name;
      final book = '${args['bookName'] ?? ''}'.trim();
      if (book.isNotEmpty) englishBookName.value = book;
      final hadithNumber = args['hadithNumber'];
      if (hadithNumber != null && '$hadithNumber'.trim().isNotEmpty) {
        searchQuery.value = '$hadithNumber';
      }
    }
    scrollController.addListener(_onScroll);
    load();
  }

  @override
  void onClose() {
    _searchDebounce?.cancel();
    scrollController.dispose();
    super.onClose();
  }

  Future<void> load() => _load(reset: true);

  void onSearch(String value) {
    searchQuery.value = value;
    _searchDebounce?.cancel();
    _searchDebounce = Timer(const Duration(milliseconds: 280), () {
      _load(reset: true);
    });
  }

  Future<void> loadMore() => _load(reset: false);

  Future<void> _load({required bool reset}) async {
    if (reset) {
      if (ahadith.isEmpty) isLoading.value = true;
      errorMessage.value = null;
      _offset = 0;
      hasMore.value = true;
    } else {
      if (isLoading.value || isLoadingMore.value || !hasMore.value) return;
      isLoadingMore.value = true;
    }

    final requestId = ++_requestId;
    try {
      if (reset) await _resolveCanonicalNames();
      final page = await _db.getAhadithPage(
        chapterId: chapterId,
        bookId: bookId > 0 ? bookId : null,
        query: searchQuery.value,
        limit: pageSize,
        offset: _offset,
      );
      if (requestId != _requestId) return;

      if (reset) {
        ahadith.assignAll(page);
      } else {
        ahadith.addAll(page);
      }
      _offset += page.length;
      hasMore.value = page.length >= pageSize;
    } catch (_) {
      if (requestId != _requestId) return;
      errorMessage.value = _db.initError ?? 'Unable to load ahadith.';
    } finally {
      if (requestId == _requestId) {
        isLoading.value = false;
        isLoadingMore.value = false;
      }
    }
  }

  Future<void> _resolveCanonicalNames() async {
    if (englishBookName.value.trim().isEmpty && bookId > 0) {
      final book = await _db.getBookById(bookId);
      if (book != null && book.name.trim().isNotEmpty) {
        englishBookName.value = book.name;
      }
    }
    if (englishChapterName.value.trim().isEmpty && chapterId > 0) {
      final chapter = await _db.getChapterById(chapterId);
      if (chapter != null && chapter.name.trim().isNotEmpty) {
        englishChapterName.value = chapter.name;
      }
    }
  }

  void _onScroll() {
    if (!scrollController.hasClients) return;
    final position = scrollController.position;
    if (position.pixels >= position.maxScrollExtent - 480) {
      loadMore();
    }
  }
}
