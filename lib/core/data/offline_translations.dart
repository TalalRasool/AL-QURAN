import '../constants/app_assets.dart';
import 'models/translation_edition.dart';

/// Bundled offline translation editions and the JSON asset each one reads.
class OfflineTranslations {
  OfflineTranslations._();

  static const english = TranslationEdition(
    identifier: 'en.asad',
    language: 'en',
    name: 'Muhammad Asad',
    englishName: 'Asad',
  );

  static const urdu = TranslationEdition(
    identifier: 'ur.jalandhry',
    language: 'ur',
    name: 'Fateh Muhammad Jalandhry',
    englishName: 'Fateh Muhammad Jalandhry',
    direction: 'rtl',
  );

  static const hindi = TranslationEdition(
    identifier: 'hi.hindi',
    language: 'hi',
    name: 'Suhel Farooq Khan and Saifur Rahman Nadwi',
    englishName: 'Farooq Khan & Nadwi',
  );

  static const indonesian = TranslationEdition(
    identifier: 'id.indonesian',
    language: 'id',
    name: 'Bahasa Indonesia',
    englishName: 'Indonesian',
  );

  static const bengali = TranslationEdition(
    identifier: 'bn.bengali',
    language: 'bn',
    name: 'Muhiuddin Khan',
    englishName: 'Muhiuddin Khan',
  );

  static const editions = <TranslationEdition>[
    english,
    urdu,
    hindi,
    indonesian,
    bengali,
  ];

  static const _aliases = <String, String>{
    'ur.jalandhari': 'ur.jalandhry',
    'ur.jalandhry': 'ur.jalandhry',
    'en.asad': 'en.asad',
    'hi.hindi': 'hi.hindi',
    'id.indonesian': 'id.indonesian',
    'bn.bengali': 'bn.bengali',
  };

  static const _assets = <String, String>{
    'en.asad': AppAssets.quranEnglishJson,
    'ur.jalandhry': AppAssets.quranUrduJson,
    'hi.hindi': AppAssets.quranHindiJson,
    'id.indonesian': AppAssets.quranIndonesianJson,
    'bn.bengali': AppAssets.quranBengaliJson,
  };

  static String canonicalId(String identifier) {
    return _aliases[identifier.toLowerCase()] ?? english.identifier;
  }

  static String assetFor(String identifier) {
    return _assets[canonicalId(identifier)] ?? AppAssets.quranEnglishJson;
  }

  static TranslationEdition editionFor(String identifier) {
    final id = canonicalId(identifier);
    return editions.firstWhere(
      (edition) => edition.identifier == id,
      orElse: () => english,
    );
  }
}
