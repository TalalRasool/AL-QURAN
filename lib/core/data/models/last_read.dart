class LastRead {
  const LastRead({
    required this.surahNumber,
    required this.ayahNumber,
  });

  final int surahNumber;
  final int ayahNumber;

  Map<String, dynamic> toJson() => {
        'surahNumber': surahNumber,
        'ayahNumber': ayahNumber,
      };

  factory LastRead.fromJson(Map<String, dynamic> json) {
    return LastRead(
      surahNumber: json['surahNumber'] as int,
      ayahNumber: json['ayahNumber'] as int,
    );
  }
}
