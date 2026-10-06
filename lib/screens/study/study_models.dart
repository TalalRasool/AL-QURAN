/// Maps the app language code (`en`, `ur`, `hi`, `bn`, `id`, `fa`) onto the
/// SQLite columns in `ayahs` (`*_full`) and `ayah_words`.
class OfflineLanguage {
  OfflineLanguage._();

  static const wordColumns = <String, String>{
    'en': 'english',
    'ur': 'urdu',
    'hi': 'hindi',
    'bn': 'bengali',
    'id': 'indonesian',
    'fa': 'persian',
  };

  static const fullColumns = <String, String>{
    'en': 'english_full',
    'ur': 'urdu_full',
    'hi': 'hindi_full',
    'bn': 'bengali_full',
    'id': 'indonesian_full',
    'fa': 'persian_full',
  };

  static const ayahKeyColumns = <String>[
    'id',
    'surah_number',
    'ayah_number',
    'arabic',
  ];

  static const _ayahLabels = <String, String>{
    'en': 'Ayah',
    'ur': 'آیہ',
    'hi': 'आयत',
    'bn': 'আয়াত',
    'id': 'Ayat',
    'fa': 'آیه',
  };

  static const _rtlCodes = {'ur', 'fa', 'ar'};

  static String normalize(String? code) {
    final value = (code ?? '').trim().toLowerCase();
    return wordColumns.containsKey(value) ? value : 'en';
  }

  static String wordColumn(String languageCode) =>
      wordColumns[normalize(languageCode)]!;

  static String fullColumn(String languageCode) =>
      fullColumns[normalize(languageCode)]!;

  /// Columns read from `ayahs`, including every bundled translation.
  static List<String> get ayahSelectColumns => [
        ...ayahKeyColumns,
        ...fullColumns.values,
      ];

  static String get ayahSelectSql => ayahSelectColumns.join(', ');

  /// Columns read from `ayah_words`, including every bundled gloss.
  static List<String> get wordSelectColumns => [
        'ayah_id',
        'word_position',
        'arabic',
        ...wordColumns.values,
      ];

  static bool isRtl(String languageCode) =>
      _rtlCodes.contains(languageCode.trim().toLowerCase());

  static String ayahLabel(String languageCode) =>
      _ayahLabels[normalize(languageCode)] ?? 'Ayah';
}

class OfflineWord {
  const OfflineWord({
    required this.ayahId,
    required this.position,
    required this.arabic,
    required this.translations,
  });

  factory OfflineWord.fromMap(Map<String, dynamic> map) {
    return OfflineWord(
      ayahId: _asInt(map['ayah_id']),
      position: _asInt(map['word_position']),
      arabic: '${map['arabic'] ?? ''}'.trim(),
      translations: {
        for (final entry in OfflineLanguage.wordColumns.entries)
          entry.key: '${map[entry.value] ?? ''}'.trim(),
      },
    );
  }

  final int ayahId;
  final int position;
  final String arabic;
  final Map<String, String> translations;

  String textFor(String languageCode) {
    final code = OfflineLanguage.normalize(languageCode);
    final direct = translations[code];
    if (direct != null && direct.isNotEmpty) return direct;
    return translations['en'] ?? '';
  }
}

class OfflineAyah {
  const OfflineAyah({
    required this.id,
    required this.surahNumber,
    required this.ayahNumber,
    required this.arabic,
    required this.fullTranslations,
    required this.words,
  });

  factory OfflineAyah.fromMap(
    Map<String, dynamic> map, {
    List<OfflineWord> words = const [],
  }) {
    return OfflineAyah(
      id: _asInt(map['id']),
      surahNumber: _asInt(map['surah_number']),
      ayahNumber: _asInt(map['ayah_number']),
      arabic: '${map['arabic'] ?? ''}'.trim(),
      fullTranslations: {
        for (final entry in OfflineLanguage.fullColumns.entries)
          entry.key: '${map[entry.value] ?? ''}'.trim(),
      },
      words: words,
    );
  }

  final int id;
  final int surahNumber;
  final int ayahNumber;
  final String arabic;
  final Map<String, String> fullTranslations;
  final List<OfflineWord> words;

  String fullTextFor(String languageCode) {
    final code = OfflineLanguage.normalize(languageCode);
    final direct = fullTranslations[code];
    if (direct != null && direct.isNotEmpty) return direct;
    return fullTranslations['en'] ?? '';
  }

  OfflineAyah copyWith({List<OfflineWord>? words}) {
    return OfflineAyah(
      id: id,
      surahNumber: surahNumber,
      ayahNumber: ayahNumber,
      arabic: arabic,
      fullTranslations: fullTranslations,
      words: words ?? this.words,
    );
  }
}

int _asInt(dynamic value) {
  if (value is int) return value;
  if (value is num) return value.toInt();
  return int.tryParse('$value') ?? 0;
}
