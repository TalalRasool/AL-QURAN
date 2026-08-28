import 'package:get/get.dart';
import 'package:get_storage/get_storage.dart';

import '../data/models/last_read.dart';
import '../data/offline_translations.dart';

class StorageService extends GetxService {
  static const lastReadKey = 'last_read';
  static const bookmarksKey = 'bookmarks';
  static const reciterIdKey = 'selected_reciter_id';
  static const reciterNameKey = 'selected_reciter_name';
  static const tasbihCountKey = 'tasbih_count';
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

  late final GetStorage _box;

  final lastRead = Rxn<LastRead>();
  final bookmarks = <int>[].obs;
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

  Future<StorageService> init() async {
    _box = GetStorage();
    lastRead.value = _readLastRead();
    bookmarks.assignAll(_readBookmarks());
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
    return this;
  }

  LastRead? getLastRead() => lastRead.value;

  Future<void> saveLastRead({
    required int surahNumber,
    required int ayahNumber,
  }) async {
    final value = LastRead(surahNumber: surahNumber, ayahNumber: ayahNumber);
    lastRead.value = value;
    await _box.write(lastReadKey, value.toJson());
  }

  List<int> getBookmarks() => List<int>.from(bookmarks);

  Future<void> replaceBookmarks(List<int> ids) async {
    bookmarks.assignAll(ids);
    await _box.write(bookmarksKey, List<int>.from(bookmarks));
  }

  bool isBookmarked(int surahNumber) => bookmarks.contains(surahNumber);

  Future<void> toggleBookmark(int surahNumber) async {
    if (isBookmarked(surahNumber)) {
      bookmarks.remove(surahNumber);
    } else {
      bookmarks.add(surahNumber);
    }
    await _box.write(bookmarksKey, List<int>.from(bookmarks));
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

  Future<void> completeOnboarding() async {
    hasCompletedOnboarding.value = true;
    await _box.write(onboardingCompleteKey, true);
  }

  int getTasbihCount() => tasbihCount.value;

  Future<void> saveTasbihCount(int count) async {
    tasbihCount.value = count;
    await _box.write(tasbihCountKey, count);
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
    if (raw is List) {
      return raw.whereType<int>().toList();
    }
    return [];
  }

  int _readTasbihCount() {
    final raw = _box.read(tasbihCountKey);
    if (raw is int) return raw;
    if (raw is num) return raw.toInt();
    return int.tryParse('$raw') ?? 0;
  }
}
