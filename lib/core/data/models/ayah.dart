import '../json_utils.dart';

class Ayah {
  const Ayah({
    required this.number,
    required this.arabic,
    required this.translation,
    this.surahNumber = 0,
    this.surahEnglishName = '',
  });

  final int number;
  final String arabic;
  final String translation;
  final int surahNumber;
  final String surahEnglishName;

  factory Ayah.fromEditions({
    required Map<String, dynamic> arabicJson,
    required Map<String, dynamic> translationJson,
  }) {
    final surah = asStringKeyMap(arabicJson['surah']);
    return Ayah(
      number: asInt(arabicJson['numberInSurah']),
      arabic: arabicJson['text'] as String? ?? '',
      translation: translationJson['text'] as String? ?? '',
      surahNumber: asInt(surah['number']),
      surahEnglishName: surah['englishName'] as String? ?? '',
    );
  }
}
