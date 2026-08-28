import '../json_utils.dart';

enum RevelationType { meccan, medinan }

class Surah {
  const Surah({
    required this.number,
    required this.englishName,
    required this.arabicName,
    required this.meaning,
    required this.verseCount,
    required this.revelation,
  });

  final int number;
  final String englishName;
  final String arabicName;
  final String meaning;
  final int verseCount;
  final RevelationType revelation;

  bool get isMeccan => revelation == RevelationType.meccan;

  factory Surah.fromJson(Map<String, dynamic> json) {
    return Surah(
      number: asInt(json['number']),
      englishName: json['englishName'] as String? ?? '',
      arabicName: json['name'] as String? ?? '',
      meaning: json['englishNameTranslation'] as String? ?? '',
      verseCount: _verseCount(json),
      revelation: RevelationTypeParser.fromApi(
        json['revelationType'] as String?,
      ),
    );
  }

  static int _verseCount(Map<String, dynamic> json) {
    final counted = asInt(json['numberOfAyahs']);
    if (counted > 0) return counted;
    final ayahs = json['ayahs'];
    return ayahs is List ? ayahs.length : 0;
  }
}

extension RevelationTypeParser on RevelationType {
  static RevelationType fromApi(String? value) {
    switch (value?.toLowerCase()) {
      case 'medinan':
        return RevelationType.medinan;
      default:
        return RevelationType.meccan;
    }
  }
}
