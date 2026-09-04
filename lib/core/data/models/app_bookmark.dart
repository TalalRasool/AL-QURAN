import '../json_utils.dart';

enum BookmarkType {
  translation,
  mushaf,
  hadith,
  dua;

  String get label {
    switch (this) {
      case BookmarkType.translation:
        return 'Quran';
      case BookmarkType.mushaf:
        return 'Mushaf';
      case BookmarkType.hadith:
        return 'Hadiths';
      case BookmarkType.dua:
        return 'Duas';
    }
  }

  static BookmarkType fromValue(String? raw) {
    return BookmarkType.values.firstWhere(
      (value) => value.name == raw,
      orElse: () => BookmarkType.translation,
    );
  }
}

class AppBookmark {
  const AppBookmark({
    required this.id,
    required this.type,
    required this.title,
    this.subtitle = '',
    this.payload = const {},
    required this.createdAt,
  });

  final String id;
  final BookmarkType type;
  final String title;
  final String subtitle;
  final Map<String, dynamic> payload;
  final int createdAt;

  static String translationId(int surahNumber) => 'translation:$surahNumber';

  static String mushafId(int page) => 'mushaf:$page';

  static String hadithId(int hadithId) => 'hadith:$hadithId';

  static String duaId(String duaId) => 'dua:$duaId';

  factory AppBookmark.translation({
    required int surahNumber,
    String englishName = '',
    String arabicName = '',
    int verseCount = 0,
  }) {
    final name = englishName.trim().isEmpty ? 'Surah $surahNumber' : englishName;
    return AppBookmark(
      id: translationId(surahNumber),
      type: BookmarkType.translation,
      title: name,
      subtitle: [
        if (arabicName.trim().isNotEmpty) arabicName.trim(),
        if (verseCount > 0) '$verseCount ayahs',
      ].join(' · '),
      payload: {
        'surahNumber': surahNumber,
        'englishName': name,
        'arabicName': arabicName,
        'verseCount': verseCount,
      },
      createdAt: DateTime.now().millisecondsSinceEpoch,
    );
  }

  factory AppBookmark.mushaf({
    required int page,
    int? surahNumber,
    int? ayahNumber,
    String surahName = '',
  }) {
    return AppBookmark(
      id: mushafId(page),
      type: BookmarkType.mushaf,
      title: 'Page $page',
      subtitle: [
        if (surahName.trim().isNotEmpty) surahName.trim(),
        if (surahNumber != null && ayahNumber != null)
          '$surahNumber:$ayahNumber',
      ].join(' · '),
      payload: {
        'page': page,
        'surahNumber': ?surahNumber,
        'ayahNumber': ?ayahNumber,
        if (surahName.trim().isNotEmpty) 'surahName': surahName.trim(),
      },
      createdAt: DateTime.now().millisecondsSinceEpoch,
    );
  }

  factory AppBookmark.hadith({
    required int hadithId,
    required int bookId,
    required int chapterId,
    required num hadithNumber,
    String bookName = '',
    String chapterName = '',
  }) {
    final numberLabel = hadithNumber is int ||
            hadithNumber == hadithNumber.roundToDouble()
        ? '${hadithNumber.toInt()}'
        : '$hadithNumber';
    final book = bookName.trim();
    return AppBookmark(
      id: AppBookmark.hadithId(hadithId),
      type: BookmarkType.hadith,
      title: book.isEmpty ? 'Hadith $numberLabel' : book,
      subtitle: [
        'Hadith $numberLabel',
        if (chapterName.trim().isNotEmpty) chapterName.trim(),
      ].join(' · '),
      payload: {
        'hadithId': hadithId,
        'bookId': bookId,
        'chapterId': chapterId,
        'hadithNumber': hadithNumber,
        'bookName': book,
        'chapterName': chapterName.trim(),
      },
      createdAt: DateTime.now().millisecondsSinceEpoch,
    );
  }

  factory AppBookmark.dua({
    required String duaId,
    required String title,
  }) {
    return AppBookmark(
      id: AppBookmark.duaId(duaId),
      type: BookmarkType.dua,
      title: title.trim().isEmpty ? 'Dua' : title.trim(),
      subtitle: 'Dua',
      payload: {'duaId': duaId},
      createdAt: DateTime.now().millisecondsSinceEpoch,
    );
  }

  AppBookmark copyWith({
    String? title,
    String? subtitle,
    Map<String, dynamic>? payload,
  }) {
    return AppBookmark(
      id: id,
      type: type,
      title: title ?? this.title,
      subtitle: subtitle ?? this.subtitle,
      payload: payload ?? this.payload,
      createdAt: createdAt,
    );
  }

  Map<String, dynamic> toJson() => {
        'id': id,
        'type': type.name,
        'title': title,
        'subtitle': subtitle,
        'payload': payload,
        'createdAt': createdAt,
      };

  factory AppBookmark.fromJson(Map<String, dynamic> json) {
    return AppBookmark(
      id: '${json['id'] ?? ''}',
      type: BookmarkType.fromValue('${json['type'] ?? ''}'),
      title: '${json['title'] ?? ''}',
      subtitle: '${json['subtitle'] ?? ''}',
      payload: asStringKeyMap(json['payload']),
      createdAt: asInt(json['createdAt']),
    );
  }
}
