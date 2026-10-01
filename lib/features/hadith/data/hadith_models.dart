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
    required this.textEn,
    required this.textUr,
  });

  final int id;
  final int bookId;
  final int chapterId;
  final num hadithNumber;
  final String textAr;
  final String textEn;
  final String textUr;

  String get numberLabel {
    if (hadithNumber is int || hadithNumber == hadithNumber.roundToDouble()) {
      return '${hadithNumber.toInt()}';
    }
    return hadithNumber.toString();
  }

  factory Hadith.fromMap(Map<String, Object?> map) {
    return Hadith(
      id: (map['id'] as num?)?.toInt() ?? 0,
      bookId: (map['book_id'] as num?)?.toInt() ?? 0,
      chapterId: (map['chapter_id'] as num?)?.toInt() ?? 0,
      hadithNumber: (map['hadith_number'] as num?) ?? 0,
      textAr: '${map['text_ar'] ?? ''}',
      textEn: '${map['text_en'] ?? ''}',
      textUr: '${map['text_ur'] ?? ''}',
    );
  }
}
