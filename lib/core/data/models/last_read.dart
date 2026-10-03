import '../json_utils.dart';

class LastRead {
  const LastRead({
    required this.surahNumber,
    required this.ayahNumber,
    this.source = sourceSurah,
    this.mushafPage,
    this.updatedAtMs = 0,
  });

  static const sourceSurah = 'surah';
  static const sourceMushaf = 'mushaf';

  final int surahNumber;
  final int ayahNumber;
  final String source;
  final int? mushafPage;
  final int updatedAtMs;

  bool get isMushaf => source == sourceMushaf;

  Map<String, dynamic> toJson() => {
        'surahNumber': surahNumber,
        'ayahNumber': ayahNumber,
        'source': source,
        'updatedAt': updatedAtMs,
        if (mushafPage != null) 'mushafPage': mushafPage,
      };

  factory LastRead.fromJson(Map<String, dynamic> json) {
    final page = json['mushafPage'];
    return LastRead(
      surahNumber: asInt(json['surahNumber'], fallback: 1),
      ayahNumber: asInt(json['ayahNumber'], fallback: 1),
      source: json['source'] as String? ?? sourceSurah,
      mushafPage: page == null ? null : asInt(page),
      updatedAtMs: asInt(json['updatedAt']),
    );
  }
}
