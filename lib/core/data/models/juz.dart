class Juz {
  const Juz({
    required this.number,
    required this.englishName,
    required this.arabicName,
    required this.startSurahNumber,
    required this.startAyahNumber,
  });

  final int number;
  final String englishName;
  final String arabicName;
  final int startSurahNumber;
  final int startAyahNumber;

  static const all = <Juz>[
    Juz(
      number: 1,
      englishName: 'Alif Lam Meem',
      arabicName: 'الم',
      startSurahNumber: 1,
      startAyahNumber: 1,
    ),
    Juz(
      number: 2,
      englishName: 'Sayaqool',
      arabicName: 'سَيَقُولُ',
      startSurahNumber: 2,
      startAyahNumber: 142,
    ),
    Juz(
      number: 3,
      englishName: 'Tilkal Rusul',
      arabicName: 'تِلْكَ الرُّسُلُ',
      startSurahNumber: 2,
      startAyahNumber: 253,
    ),
    Juz(
      number: 4,
      englishName: 'Lan Tanaa Lu',
      arabicName: 'لَن تَنَالُوا',
      startSurahNumber: 3,
      startAyahNumber: 93,
    ),
    Juz(
      number: 5,
      englishName: 'Wal Mohsanat',
      arabicName: 'وَالْمُحْصَنَاتُ',
      startSurahNumber: 4,
      startAyahNumber: 24,
    ),
    Juz(
      number: 6,
      englishName: 'La Yuhibbullah',
      arabicName: 'لَا يُحِبُّ اللَّهُ',
      startSurahNumber: 4,
      startAyahNumber: 148,
    ),
    Juz(
      number: 7,
      englishName: 'Wa Iza Samiu',
      arabicName: 'وَإِذَا سَمِعُوا',
      startSurahNumber: 5,
      startAyahNumber: 82,
    ),
    Juz(
      number: 8,
      englishName: 'Wa Lau Annana',
      arabicName: 'وَلَوْ أَنَّنَا',
      startSurahNumber: 6,
      startAyahNumber: 111,
    ),
    Juz(
      number: 9,
      englishName: 'Qalal Malao',
      arabicName: 'قَالَ الْمَلَأُ',
      startSurahNumber: 7,
      startAyahNumber: 88,
    ),
    Juz(
      number: 10,
      englishName: 'Wa A\'lamu',
      arabicName: 'وَاعْلَمُوا',
      startSurahNumber: 8,
      startAyahNumber: 41,
    ),
    Juz(
      number: 11,
      englishName: 'Yatazeroon',
      arabicName: 'يَعْتَذِرُونَ',
      startSurahNumber: 9,
      startAyahNumber: 93,
    ),
    Juz(
      number: 12,
      englishName: 'Wa Mamin Da\'abat',
      arabicName: 'وَمَا مِن دَابَّةٍ',
      startSurahNumber: 11,
      startAyahNumber: 6,
    ),
    Juz(
      number: 13,
      englishName: 'Wa Ma Ubrioo',
      arabicName: 'وَمَا أُبَرِّئُ',
      startSurahNumber: 12,
      startAyahNumber: 53,
    ),
    Juz(
      number: 14,
      englishName: 'Rubama',
      arabicName: 'رُبَمَا',
      startSurahNumber: 15,
      startAyahNumber: 1,
    ),
    Juz(
      number: 15,
      englishName: 'Subhanallazi',
      arabicName: 'سُبْحَانَ الَّذِي',
      startSurahNumber: 17,
      startAyahNumber: 1,
    ),
    Juz(
      number: 16,
      englishName: 'Qal Alam',
      arabicName: 'قَالَ أَلَمْ',
      startSurahNumber: 18,
      startAyahNumber: 75,
    ),
    Juz(
      number: 17,
      englishName: 'Aqtarabo',
      arabicName: 'اقْتَرَبَ',
      startSurahNumber: 21,
      startAyahNumber: 1,
    ),
    Juz(
      number: 18,
      englishName: 'Qadd Aflaha',
      arabicName: 'قَدْ أَفْلَحَ',
      startSurahNumber: 23,
      startAyahNumber: 1,
    ),
    Juz(
      number: 19,
      englishName: 'Wa Qalallazina',
      arabicName: 'وَقَالَ الَّذِينَ',
      startSurahNumber: 25,
      startAyahNumber: 21,
    ),
    Juz(
      number: 20,
      englishName: 'A\'man Khalaq',
      arabicName: 'أَمَّنْ خَلَقَ',
      startSurahNumber: 27,
      startAyahNumber: 56,
    ),
    Juz(
      number: 21,
      englishName: 'Utlu Ma Oohi',
      arabicName: 'اتْلُ مَا أُوحِيَ',
      startSurahNumber: 29,
      startAyahNumber: 46,
    ),
    Juz(
      number: 22,
      englishName: 'Wa Manyaqnut',
      arabicName: 'وَمَن يَقْنُتْ',
      startSurahNumber: 33,
      startAyahNumber: 31,
    ),
    Juz(
      number: 23,
      englishName: 'Wa Mali',
      arabicName: 'وَمَا لِيَ',
      startSurahNumber: 36,
      startAyahNumber: 28,
    ),
    Juz(
      number: 24,
      englishName: 'Faman Azlam',
      arabicName: 'فَمَنْ أَظْلَمُ',
      startSurahNumber: 39,
      startAyahNumber: 32,
    ),
    Juz(
      number: 25,
      englishName: 'Elaihi Yuraddu',
      arabicName: 'إِلَيْهِ يُرَدُّ',
      startSurahNumber: 41,
      startAyahNumber: 47,
    ),
    Juz(
      number: 26,
      englishName: 'Ha\'a Meem',
      arabicName: 'حم',
      startSurahNumber: 46,
      startAyahNumber: 1,
    ),
    Juz(
      number: 27,
      englishName: 'Qala Fama Khatbukum',
      arabicName: 'قَالَ فَمَا خَطْبُكُم',
      startSurahNumber: 51,
      startAyahNumber: 31,
    ),
    Juz(
      number: 28,
      englishName: 'Qadd Sami Allah',
      arabicName: 'قَدْ سَمِعَ اللَّهُ',
      startSurahNumber: 58,
      startAyahNumber: 1,
    ),
    Juz(
      number: 29,
      englishName: 'Tabarakallazi',
      arabicName: 'تَبَارَكَ الَّذِي',
      startSurahNumber: 67,
      startAyahNumber: 1,
    ),
    Juz(
      number: 30,
      englishName: 'Amma Yatasa\'aloon',
      arabicName: 'عَمَّ يَتَسَاءَلُونَ',
      startSurahNumber: 78,
      startAyahNumber: 1,
    ),
  ];

  Juz? get nextJuz {
    if (number >= all.length) return null;
    return all[number];
  }

  /// Inclusive start and exclusive end of this juz in surah/ayah coordinates.
  /// A null [endSurahNumber] means the juz runs through the end of the Quran.
  ({int startSurah, int startAyah, int? endSurah, int? endAyah}) get bounds {
    final next = nextJuz;
    return (
      startSurah: startSurahNumber,
      startAyah: startAyahNumber,
      endSurah: next?.startSurahNumber,
      endAyah: next?.startAyahNumber,
    );
  }
}
