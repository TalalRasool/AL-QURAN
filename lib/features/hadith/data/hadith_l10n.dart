import 'package:get/get.dart';

import '../../../core/controllers/settings_controller.dart';
import '../../../core/services/storage_service.dart';
import '../../../screens/study/study_models.dart';
import 'hadith_chapter_names.dart';

/// Localized Hadith book names, chapter names, and short UI labels
/// for the five offline languages: English, Urdu, Hindi, Bengali, Indonesian.
class HadithL10n {
  HadithL10n._();

  static const _books = <int, Map<String, String>>{
    1: {
      'en': 'Sahih al-Bukhari',
      'ur': 'صحیح البخاری',
      'hi': 'सहीह अल-बुखारी',
      'bn': 'সহীহ আল-বুখারী',
      'id': 'Shahih al-Bukhari',
    },
    2: {
      'en': 'Sahih Muslim',
      'ur': 'صحیح مسلم',
      'hi': 'सहीह मुस्लिम',
      'bn': 'সহীহ মুসলিম',
      'id': 'Shahih Muslim',
    },
    3: {
      'en': 'Sunan Abu Dawud',
      'ur': 'سنن ابو داؤد',
      'hi': 'सुनन अबू दाऊद',
      'bn': 'সুনান আবু দাউদ',
      'id': 'Sunan Abu Dawud',
    },
    4: {
      'en': 'Jami at-Tirmidhi',
      'ur': 'جامع الترمذی',
      'hi': 'जामी अत-तिर्मिज़ी',
      'bn': 'জামে আত-তিরমিযী',
      'id': "Jami' at-Tirmidzi",
    },
    5: {
      'en': "Sunan an-Nasa'i",
      'ur': 'سنن النسائی',
      'hi': 'सुनन अन-नसाई',
      'bn': 'সুনান আন-নাসাঈ',
      'id': "Sunan an-Nasa'i",
    },
    6: {
      'en': 'Sunan Ibn Majah',
      'ur': 'سنن ابن ماجہ',
      'hi': 'सुनन इब्न माजा',
      'bn': 'সুনান ইবনে মাজাহ',
      'id': 'Sunan Ibnu Majah',
    },
  };

  static const _ui = <String, Map<String, String>>{
    'hadith': {
      'en': 'Hadith',
      'ur': 'حدیث',
      'hi': 'हदीस',
      'bn': 'হাদিস',
      'id': 'Hadis',
    },
    'subtitle': {
      'en': 'Read the Sihah Sittah with Arabic and translation.',
      'ur': 'صحاح ستہ کو عربی اور ترجمہ کے ساتھ پڑھیں۔',
      'hi': 'सिहाह सित्तह को अरबी और अनुवाद के साथ पढ़ें।',
      'bn': 'সিহাহ সিত্তাহ আরবি ও অনুবাদসহ পড়ুন।',
      'id': 'Baca Sihah Sittah dengan Arab dan terjemahan.',
    },
    'edition_line': {
      'en': 'Arabic and translation',
      'ur': 'عربی اور ترجمہ',
      'hi': 'अरबी और अनुवाद',
      'bn': 'আরবি ও অনুবাদ',
      'id': 'Arab dan terjemahan',
    },
    'search_chapters': {
      'en': 'Search chapters',
      'ur': 'ابواب تلاش کریں',
      'hi': 'अध्याय खोजें',
      'bn': 'অধ্যায় খুঁজুন',
      'id': 'Cari bab',
    },
    'search_ahadith': {
      'en': 'Search ahadith',
      'ur': 'احادیث تلاش کریں',
      'hi': 'हदीस खोजें',
      'bn': 'হাদিস খুঁজুন',
      'id': 'Cari hadis',
    },
    'introduction': {
      'en': 'Introduction',
      'ur': 'مقدمہ',
      'hi': 'भूमिका',
      'bn': 'ভূমিকা',
      'id': 'Pendahuluan',
    },
    'no_books': {
      'en': 'No Hadith books found.',
      'ur': 'حدیث کی کتابیں نہیں ملیں۔',
      'hi': 'हदीस की पुस्तकें नहीं मिलीं।',
      'bn': 'হাদিসের কিতাব পাওয়া যায়নি।',
      'id': 'Kitab hadis tidak ditemukan.',
    },
    'no_chapters': {
      'en': 'No chapters found.',
      'ur': 'ابواب نہیں ملے۔',
      'hi': 'अध्याय नहीं मिले।',
      'bn': 'অধ্যায় পাওয়া যায়নি।',
      'id': 'Bab tidak ditemukan.',
    },
    'no_match_chapters': {
      'en': 'No matching chapters.',
      'ur': 'کوئی باب نہیں ملا۔',
      'hi': 'कोई अध्याय मेल नहीं खाता।',
      'bn': 'কোনো অধ্যায় মেলেনি।',
      'id': 'Tidak ada bab yang cocok.',
    },
    'no_ahadith': {
      'en': 'No ahadith in this chapter.',
      'ur': 'اس باب میں احادیث نہیں ہیں۔',
      'hi': 'इस अध्याय में हदीस नहीं हैं।',
      'bn': 'এই অধ্যায়ে হাদিস নেই।',
      'id': 'Tidak ada hadis di bab ini.',
    },
    'no_match_ahadith': {
      'en': 'No matching ahadith.',
      'ur': 'کوئی حدیث نہیں ملی۔',
      'hi': 'कोई हदीस मेल नहीं खाती।',
      'bn': 'কোনো হাদিস মেলেনি।',
      'id': 'Tidak ada hadis yang cocok.',
    },
    'retry': {
      'en': 'Retry',
      'ur': 'دوبارہ کوشش',
      'hi': 'फिर कोशिश करें',
      'bn': 'আবার চেষ্টা',
      'id': 'Coba lagi',
    },
  };

  static String languageCode() {
    if (Get.isRegistered<SettingsController>()) {
      return OfflineLanguage.normalize(
        Get.find<SettingsController>().translationLanguageCode,
      );
    }
    return 'en';
  }

  /// Read the selected translation so Obx rebuilds when language changes.
  static String watchLanguage() {
    if (Get.isRegistered<StorageService>()) {
      Get.find<StorageService>().selectedTranslationId.value;
    }
    return languageCode();
  }

  static bool isRtl([String? languageCode]) =>
      OfflineLanguage.isRtl(languageCode ?? HadithL10n.languageCode());

  static String ui(String key, [String? languageCode]) {
    final code = OfflineLanguage.normalize(languageCode ?? HadithL10n.languageCode());
    final map = _ui[key];
    if (map == null) return key;
    return _pick(map, code);
  }

  static String bookName(int id, {String fallback = '', String? languageCode}) {
    final code = OfflineLanguage.normalize(languageCode ?? HadithL10n.languageCode());
    final map = _books[id];
    if (map != null) return _pick(map, code, fallback: fallback);
    return fallback.isNotEmpty ? fallback : ui('hadith', code);
  }

  static String chapterName(
    String english, {
    String? languageCode,
    int number = 0,
  }) {
    final code = OfflineLanguage.normalize(languageCode ?? HadithL10n.languageCode());
    final trimmed = english.trim();
    if (trimmed.isEmpty || trimmed.toLowerCase() == 'introduction') {
      return ui('introduction', code);
    }
    if (code == 'en') return trimmed;
    final mapped = hadithChapterNames[trimmed];
    if (mapped != null) {
      final value = _pick(mapped, code, fallback: trimmed);
      if (value.trim().isNotEmpty) return value;
    }
    return trimmed;
  }

  static String chapterLabel(int number, {String? languageCode}) {
    final code = OfflineLanguage.normalize(languageCode ?? HadithL10n.languageCode());
    if (number <= 0) return ui('introduction', code);
    return switch (code) {
      'ur' => 'باب $number',
      'hi' => 'अध्याय $number',
      'bn' => 'অধ্যায় $number',
      'id' => 'Bab $number',
      _ => 'Chapter $number',
    };
  }

  static String hadithNumberLabel(String number, {String? languageCode}) {
    final code = OfflineLanguage.normalize(languageCode ?? HadithL10n.languageCode());
    final label = ui('hadith', code);
    return '$label $number';
  }

  static bool matchesQuery({
    required String query,
    required String englishName,
    required int number,
    String? languageCode,
  }) {
    final q = query.trim().toLowerCase();
    if (q.isEmpty) return true;
    final code = OfflineLanguage.normalize(languageCode ?? HadithL10n.languageCode());
    final localized = chapterName(englishName, languageCode: code, number: number);
    return englishName.toLowerCase().contains(q) ||
        localized.toLowerCase().contains(q) ||
        chapterLabel(number, languageCode: code).toLowerCase().contains(q) ||
        '$number'.contains(q);
  }

  static String _pick(
    Map<String, String> values,
    String languageCode, {
    String fallback = '',
  }) {
    final direct = values[languageCode];
    if (direct != null && direct.trim().isNotEmpty) return direct;
    final english = values['en'];
    if (english != null && english.trim().isNotEmpty) return english;
    if (fallback.trim().isNotEmpty) return fallback;
    for (final value in values.values) {
      if (value.trim().isNotEmpty) return value;
    }
    return fallback;
  }
}
