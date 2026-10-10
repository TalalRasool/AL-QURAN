import 'hadith_editions.dart';

class HadithBook {
  const HadithBook({required this.id, required this.name});

  final int id;
  final String name;

  factory HadithBook.fromMap(Map<String, Object?> map) {
    return HadithBook(
      id: (map['id'] as num?)?.toInt() ?? 0,
      name: '${map['name'] ?? ''}',
    );
  }
}

class HadithChapter {
  const HadithChapter({
    required this.id,
    required this.bookId,
    required this.number,
    required this.name,
  });

  final int id;
  final int bookId;
  final int number;
  final String name;

  factory HadithChapter.fromMap(Map<String, Object?> map) {
    final id = (map['id'] as num?)?.toInt() ?? 0;
    return HadithChapter(
      id: id,
      bookId: (map['book_id'] as num?)?.toInt() ?? 0,
      number: (map['number'] as num?)?.toInt() ?? id,
      name: '${map['name'] ?? ''}',
    );
  }
}

class Hadith {
  const Hadith({
    required this.id,
    required this.bookId,
    required this.chapterId,
    required this.hadithNumber,
    required this.textAr,
    required this.translations,
  });

  final int id;
  final int bookId;
  final int chapterId;
  final num hadithNumber;
  final String textAr;

  /// Translation text keyed by app language code (`en`, `ur`, `hi`, `bn`, `id`, `fa`).
  final Map<String, String> translations;

  String get textEn => translations['en'] ?? '';

  String get textUr => translations['ur'] ?? '';

  String get numberLabel {
    if (hadithNumber is int || hadithNumber == hadithNumber.roundToDouble()) {
      return '${hadithNumber.toInt()}';
    }
    return hadithNumber.toString();
  }

  /// Language whose text will be shown. Empty translations fall back to English.
  String resolvedLanguage(String languageCode) {
    final code = HadithEditions.normalize(languageCode);
    if (_filled(code)) return code;
    if (code != 'en' && _filled('en')) return 'en';
    return code;
  }

  /// Arabic is read separately from [textAr]. This is the selected translation,
  /// or English when that edition has no text for this hadith.
  String textFor(String languageCode) {
    final code = resolvedLanguage(languageCode);
    return (translations[code] ?? '').trim();
  }

  bool _filled(String code) => (translations[code] ?? '').trim().isNotEmpty;

  factory Hadith.fromMap(Map<String, Object?> map) {
    return Hadith(
      id: (map['id'] as num?)?.toInt() ?? 0,
      bookId: (map['book_id'] as num?)?.toInt() ?? 0,
      chapterId: (map['chapter_id'] as num?)?.toInt() ?? 0,
      hadithNumber: (map['hadith_number'] as num?) ?? 0,
      textAr: '${map[HadithEditions.textArColumn] ?? ''}',
      translations: {
        for (final spec in HadithEditions.translations)
          spec.appCode: '${map[spec.column] ?? ''}',
      },
    );
  }
}
