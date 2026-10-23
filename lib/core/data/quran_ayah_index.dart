/// Maps a surah and ayah to the absolute ayah number used by recitation APIs.
class QuranAyahIndex {
  QuranAyahIndex._();

  static const ayahCounts = <int>[
    7, 286, 200, 176, 120, 165, 206, 75, 129, 109, // 1-10
    123, 111, 43, 52, 99, 128, 111, 110, 98, 135, // 11-20
    112, 78, 118, 64, 77, 227, 93, 88, 69, 60, // 21-30
    34, 30, 73, 54, 45, 83, 182, 88, 75, 85, // 31-40
    54, 53, 89, 59, 37, 35, 38, 29, 18, 45, // 41-50
    60, 49, 62, 55, 78, 96, 29, 22, 24, 13, // 51-60
    14, 11, 11, 18, 12, 12, 30, 52, 52, 44, // 61-70
    28, 28, 20, 56, 40, 31, 50, 40, 46, 42, // 71-80
    29, 19, 36, 25, 22, 17, 19, 26, 30, 20, // 81-90
    15, 21, 11, 8, 8, 19, 5, 8, 8, 11, // 91-100
    11, 8, 3, 9, 5, 4, 7, 3, 6, 3, // 101-110
    5, 4, 5, 6, // 111-114
  ];

  static int globalNumber(int surahNumber, int ayahNumber) {
    if (surahNumber < 1 || surahNumber > ayahCounts.length) return 0;
    final count = ayahCounts[surahNumber - 1];
    if (ayahNumber < 1 || ayahNumber > count) return 0;
    var total = ayahNumber;
    for (var index = 0; index < surahNumber - 1; index++) {
      total += ayahCounts[index];
    }
    return total;
  }
}
