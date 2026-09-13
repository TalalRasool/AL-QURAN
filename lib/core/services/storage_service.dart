import 'dart:convert';

import 'package:get/get.dart';
import 'package:get_storage/get_storage.dart';

import '../data/json_utils.dart';
import '../data/models/last_read.dart';
import '../data/offline_translations.dart';

class StorageService extends GetxService {
  static const lastReadKey = 'last_read';
  static const mushafLastPageKey = 'mushaf_last_page';
  static const bookmarksKey = 'bookmarks';
  static const hadithBookmarksKey = 'hadith_bookmarks';
  static const duaBookmarksKey = 'dua_bookmarks';
  static const unifiedBookmarksKey = 'unified_bookmarks';
  static const reciterIdKey = 'selected_reciter_id';
  static const reciterNameKey = 'selected_reciter_name';
  static const tasbihCountKey = 'tasbih_count';
  static const tasbihMaxCount = 100000;
  static const translationIdKey = 'selected_translation_id';
  static const translationNameKey = 'selected_translation_name';
  static const translationLanguageKey = 'selected_translation_language';
  static const translationDirectionKey = 'selected_translation_direction';
  static const defaultReciterId = 'ar.alafasy';
  static const defaultReciterName = 'Mishary Rashid Alafasy';
  static const defaultTranslationId = 'en.asad';
  static const defaultTranslationName = 'Muhammad Asad';
  static const defaultTranslationLanguage = 'English';
  static const defaultTranslationDirection = 'ltr';
  static const onboardingCompleteKey = 'onboarding_complete';
  static const userNameKey = 'user_name';
  static const userCountryKey = 'user_country';
  static const notificationsKey = 'notifications_enabled';
  static const prayerNotificationsKey = 'prayer_notifications_enabled';
  static const prayerLatitudeKey = 'prayer_latitude';
  static const prayerLongitudeKey = 'prayer_longitude';

  late final GetStorage _box;

  final lastRead = Rxn<LastRead>();
  final bookmarks = <int>[].obs;
  final hadithBookmarks = <int>[].obs;
  final duaBookmarks = <String>[].obs;
  final selectedReciterId = defaultReciterId.obs;
  final selectedReciterName = defaultReciterName.obs;
  final tasbihCount = 0.obs;
  final selectedTranslationId = defaultTranslationId.obs;
  final selectedTranslationName = defaultTranslationName.obs;
  final selectedTranslationLanguage = defaultTranslationLanguage.obs;
  final selectedTranslationDirection = defaultTranslationDirection.obs;
  final hasCompletedOnboarding = false.obs;
  final userName = ''.obs;
  final userCountry = ''.obs;
  final notificationsEnabled = true.obs;
  final prayerNotificationsEnabled = false.obs;
  final prayerLatitude = RxnDouble();
  final prayerLongitude = RxnDouble();

  Future<StorageService> init() async {
    _box = GetStorage();
    lastRead.value = _readLastRead();
    bookmarks.assignAll(_readBookmarks());
    hadithBookmarks.assignAll(_readHadithBookmarks());
    duaBookmarks.assignAll(_readDuaBookmarks());
    selectedReciterId.value =
        _box.read(reciterIdKey) as String? ?? defaultReciterId;
    selectedReciterName.value =
        _box.read(reciterNameKey) as String? ?? defaultReciterName;
    tasbihCount.value = _readTasbihCount();
    selectedTranslationId.value = OfflineTranslations.canonicalId(
      _box.read(translationIdKey) as String? ?? defaultTranslationId,
    );
    final edition = OfflineTranslations.editionFor(selectedTranslationId.value);
    selectedTranslationName.value = _box.read(translationNameKey) as String? ??
        edition.authorName;
    selectedTranslationLanguage.value =
        _box.read(translationLanguageKey) as String? ?? edition.languageLabel;
    selectedTranslationDirection.value =
        _box.read(translationDirectionKey) as String? ?? edition.direction;
    hasCompletedOnboarding.value =
        _box.read(onboardingCompleteKey) as bool? ?? false;
    userName.value = _box.read(userNameKey) as String? ?? '';
    userCountry.value = _box.read(userCountryKey) as String? ?? '';
    notificationsEnabled.value =
        _box.read(notificationsKey) as bool? ?? true;
    prayerNotificationsEnabled.value =
        _box.read(prayerNotificationsKey) as bool? ?? false;
    prayerLatitude.value = _readDouble(prayerLatitudeKey);
    prayerLongitude.value = _readDouble(prayerLongitudeKey);
    return this;
  }

  LastRead? getLastRead() => lastRead.value;

  int get lastMushafPage {
    final stored = _box.read(mushafLastPageKey);
    if (stored != null) {
      return asInt(stored, fallback: 1).clamp(1, 604);
    }
    final page = lastRead.value?.mushafPage;
    if (page != null && page > 0) return page.clamp(1, 604);
    return 1;
  }

  Future<void> saveLastRead({
    required int surahNumber,
    required int ayahNumber,
    String source = LastRead.sourceSurah,
    int? mushafPage,
  }) async {
    final value = LastRead(
      surahNumber: surahNumber,
      ayahNumber: ayahNumber,
      source: source,
      mushafPage: source == LastRead.sourceMushaf ? mushafPage : null,
    );
    lastRead.value = value;
    await _box.write(lastReadKey, value.toJson());
  }

  Future<void> saveMushafLastPage({
    required int page,
    int surahNumber = 1,
    int ayahNumber = 1,
  }) async {
    final clamped = page.clamp(1, 604);
    await _box.write(mushafLastPageKey, clamped);
    await saveLastRead(
      surahNumber: surahNumber,
      ayahNumber: ayahNumber,
      source: LastRead.sourceMushaf,
      mushafPage: clamped,
    );
  }

  List<int> getBookmarks() => List<int>.from(bookmarks);

  Future<void> replaceBookmarks(List<int> ids) async {
    bookmarks.assignAll(ids);
    await _box.write(bookmarksKey, List<int>.from(bookmarks));
  }

  bool isBookmarked(int surahNumber) => bookmarks.contains(surahNumber);

  Future<bool> toggleBookmark(int surahNumber) async {
    final added = !isBookmarked(surahNumber);
    if (added) {
      bookmarks.add(surahNumber);
    } else {
      bookmarks.remove(surahNumber);
    }
    await _box.write(bookmarksKey, List<int>.from(bookmarks));
    return added;
  }

  bool isHadithBookmarked(int hadithId) => hadithBookmarks.contains(hadithId);

  Future<bool> toggleHadithBookmark(int hadithId) async {
    final added = !isHadithBookmarked(hadithId);
    if (added) {
      hadithBookmarks.add(hadithId);
    } else {
      hadithBookmarks.remove(hadithId);
    }
    await _box.write(hadithBookmarksKey, List<int>.from(hadithBookmarks));
    return added;
  }

  bool isDuaBookmarked(String duaId) => duaBookmarks.contains(duaId);

  Future<bool> toggleDuaBookmark(String duaId) async {
    final added = !isDuaBookmarked(duaId);
    if (added) {
      duaBookmarks.add(duaId);
    } else {
      duaBookmarks.remove(duaId);
    }
    await _box.write(duaBookmarksKey, List<String>.from(duaBookmarks));
    return added;
  }

  Future<void> replaceHadithBookmarks(List<int> ids) async {
    hadithBookmarks.assignAll(ids);
    await _box.write(hadithBookmarksKey, List<int>.from(hadithBookmarks));
  }

  Future<void> replaceDuaBookmarks(List<String> ids) async {
    duaBookmarks.assignAll(ids);
    await _box.write(duaBookmarksKey, List<String>.from(duaBookmarks));
  }

  List<Map<String, dynamic>> loadUnifiedBookmarks() {
    return _mapsFromBookmarkJson(_box.read(unifiedBookmarksKey));
  }

  Future<void> saveUnifiedBookmarks(List<Map<String, dynamic>> value) {
    return saveUnifiedBookmarksJson(jsonEncode(value));
  }

  Future<void> saveUnifiedBookmarksJson(String json) {
    return _box.write(unifiedBookmarksKey, json);
  }

  String? readUnifiedBookmarksJson() {
    final raw = _box.read(unifiedBookmarksKey);
    if (raw is String) return raw;
    if (raw is List) return jsonEncode(raw);
    return null;
  }

  List<Map<String, dynamic>> _mapsFromBookmarkJson(dynamic raw) {
    List<dynamic>? list;
    if (raw is String && raw.trim().isNotEmpty) {
      try {
        final decoded = jsonDecode(raw);
        if (decoded is List) list = decoded;
      } catch (_) {
        return [];
      }
    } else if (raw is List) {
      list = raw;
    }
    if (list == null) return [];
    return [
      for (final item in list)
        if (item is Map) Map<String, dynamic>.from(item),
    ];
  }

  Future<void> saveReciter({
    required String identifier,
    required String name,
  }) async {
    selectedReciterId.value = identifier;
    selectedReciterName.value = name;
    await _box.write(reciterIdKey, identifier);
    await _box.write(reciterNameKey, name);
  }

  Future<void> saveTranslation({
    required String identifier,
    required String name,
    required String language,
    String direction = defaultTranslationDirection,
  }) async {
    final canonical = OfflineTranslations.editionFor(identifier);
    selectedTranslationId.value = canonical.identifier;
    selectedTranslationName.value = name.trim().isEmpty
        ? canonical.authorName
        : name;
    selectedTranslationLanguage.value = language.trim().isEmpty
        ? canonical.languageLabel
        : language;
    selectedTranslationDirection.value = direction.trim().isEmpty
        ? canonical.direction
        : direction;
    await _box.write(translationIdKey, selectedTranslationId.value);
    await _box.write(translationNameKey, selectedTranslationName.value);
    await _box.write(translationLanguageKey, selectedTranslationLanguage.value);
    await _box.write(translationDirectionKey, selectedTranslationDirection.value);
  }

  Future<void> saveProfile({
    required String name,
    required String country,
  }) async {
    userName.value = name.trim();
    userCountry.value = country.trim();
    await _box.write(userNameKey, userName.value);
    await _box.write(userCountryKey, userCountry.value);
  }

  Future<void> saveNotificationsEnabled(bool value) async {
    notificationsEnabled.value = value;
    await _box.write(notificationsKey, value);
  }

  Future<void> savePrayerNotificationsEnabled(bool value) async {
    prayerNotificationsEnabled.value = value;
    await _box.write(prayerNotificationsKey, value);
  }

  Future<void> savePrayerCoordinates({
    required double latitude,
    required double longitude,
  }) async {
    prayerLatitude.value = latitude;
    prayerLongitude.value = longitude;
    await _box.write(prayerLatitudeKey, latitude);
    await _box.write(prayerLongitudeKey, longitude);
  }

  Future<void> completeOnboarding() async {
    hasCompletedOnboarding.value = true;
    await _box.write(onboardingCompleteKey, true);
  }

  int getTasbihCount() => tasbihCount.value;

  Future<void> saveTasbihCount(int count) async {
    final clamped = count.clamp(0, tasbihMaxCount);
    tasbihCount.value = clamped;
    await _box.write(tasbihCountKey, clamped);
  }

  LastRead? _readLastRead() {
    final raw = _box.read(lastReadKey);
    if (raw is Map) {
      return LastRead.fromJson(Map<String, dynamic>.from(raw));
    }
    return null;
  }

  List<int> _readBookmarks() {
    final raw = _box.read(bookmarksKey);
    if (raw is! List) return [];
    return [
      for (final item in raw)
        asInt(item),
    ].where((number) => number > 0).toList();
  }

  List<int> _readHadithBookmarks() {
    final raw = _box.read(hadithBookmarksKey);
    if (raw is! List) return [];
    return [
      for (final item in raw)
        if (item is int)
          item
        else if (item is num)
          item.toInt(),
    ];
  }

  List<String> _readDuaBookmarks() {
    final raw = _box.read(duaBookmarksKey);
    if (raw is! List) return [];
    return [
      for (final item in raw)
        if ('$item'.trim().isNotEmpty) '$item',
    ];
  }

  int _readTasbihCount() {
    final raw = _box.read(tasbihCountKey);
    final parsed = raw is int
        ? raw
        : raw is num
            ? raw.toInt()
            : int.tryParse('$raw') ?? 0;
    return parsed.clamp(0, tasbihMaxCount);
  }

  double? _readDouble(String key) {
    final raw = _box.read(key);
    if (raw is double) return raw;
    if (raw is num) return raw.toDouble();
    return double.tryParse('$raw');
  }
}
