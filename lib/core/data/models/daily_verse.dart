class DailyVerse {
  const DailyVerse({
    required this.arabic,
    required this.translation,
    required this.reference,
    required this.surahNumber,
    required this.ayahNumber,
    required this.globalNumber,
  });

  final String arabic;
  final String translation;
  final String reference;
  final int surahNumber;
  final int ayahNumber;
  final int globalNumber;

  Map<String, dynamic> toJson() => {
        'arabic': arabic,
        'translation': translation,
        'reference': reference,
        'surahNumber': surahNumber,
        'ayahNumber': ayahNumber,
        'globalNumber': globalNumber,
      };

  factory DailyVerse.fromJson(Map<String, dynamic> json) {
    return DailyVerse(
      arabic: json['arabic'] as String? ?? '',
      translation: json['translation'] as String? ?? '',
      reference: json['reference'] as String? ?? '',
      surahNumber: _asInt(json['surahNumber']),
      ayahNumber: _asInt(json['ayahNumber']),
      globalNumber: _asInt(json['globalNumber']),
    );
  }

  static int _asInt(dynamic value) {
    if (value is int) return value;
    if (value is num) return value.toInt();
    return int.tryParse('$value') ?? 0;
  }
}
