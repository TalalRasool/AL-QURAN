/// Maps app language codes onto fawazahmed0 hadith-api editions.
///
/// Edition files are named `{prefix}-{book}.json`, using the same 3-letter
/// prefixes as the rest of the fawazahmed0 datasets (`eng-bukhari`,
/// `ben-muslim`, `fas-tirmidhi`). Hindi (`hin`) and Persian (`fas`) are not
/// published for the Sihah Sittah books; those columns stay empty and the
/// reader falls back to English.
class HadithEditions {
  HadithEditions._();

  static const specs = <HadithEditionSpec>[
    HadithEditionSpec(
      appCode: 'ar',
      editionCode: 'ara',
      label: 'Arabic',
      required: true,
    ),
    HadithEditionSpec(
      appCode: 'en',
      editionCode: 'eng',
      label: 'English',
      column: 'text_en',
      required: true,
    ),
    HadithEditionSpec(
      appCode: 'ur',
      editionCode: 'urd',
      label: 'Urdu',
      column: 'text_ur',
      required: true,
    ),
    HadithEditionSpec(
      appCode: 'hi',
      editionCode: 'hin',
      label: 'Hindi',
      column: 'text_hi',
    ),
    HadithEditionSpec(
      appCode: 'bn',
      editionCode: 'ben',
      label: 'Bengali',
      column: 'text_bn',
    ),
    HadithEditionSpec(
      appCode: 'id',
      editionCode: 'ind',
      label: 'Indonesian',
      column: 'text_id',
    ),
    HadithEditionSpec(
      appCode: 'fa',
      editionCode: 'fas',
      label: 'Persian',
      column: 'text_fa',
    ),
  ];

  static const textArColumn = 'text_ar';

  static List<HadithEditionSpec> get translations =>
      specs.where((spec) => spec.column != null).toList(growable: false);

  static String normalize(String? code) {
    final value = (code ?? '').trim().toLowerCase();
    for (final spec in translations) {
      if (spec.appCode == value) return value;
    }
    return 'en';
  }

  static String columnFor(String languageCode) {
    final code = normalize(languageCode);
    for (final spec in translations) {
      if (spec.appCode == code) return spec.column!;
    }
    return 'text_en';
  }
}

class HadithEditionSpec {
  const HadithEditionSpec({
    required this.appCode,
    required this.editionCode,
    required this.label,
    this.column,
    this.required = false,
  });

  /// App language code: `ar`, `en`, `ur`, `hi`, `bn`, `id`, or `fa`.
  final String appCode;

  /// fawazahmed0 edition prefix, e.g. `eng`, `urd`, `ben`, `ind`, `hin`, `fas`.
  final String editionCode;

  final String label;

  /// SQLite column on `ahadith`. Null for the Arabic source (`text_ar`).
  final String? column;

  /// When false, a missing edition file is safe: that language falls back
  /// to English instead of failing the build.
  final bool required;

  String fileName(String bookSlug) => '$editionCode-$bookSlug.json';
}
