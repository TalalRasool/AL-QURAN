import 'models/ayah.dart';
import 'models/surah.dart';

class MockReciter {
  const MockReciter({
    required this.name,
    required this.subtitle,
  });

  final String name;
  final String subtitle;
}

class MockDua {
  const MockDua({
    required this.title,
    required this.arabic,
    required this.translation,
  });

  final String title;
  final String arabic;
  final String translation;
}

/// Static UI data only — no API or database.
class MockData {
  MockData._();

  static const List<Surah> surahs = [
    Surah(
      number: 1,
      englishName: 'Al-Fatihah',
      arabicName: 'الفاتحة',
      meaning: 'The Opening',
      verseCount: 7,
      revelation: RevelationType.meccan,
    ),
    Surah(
      number: 2,
      englishName: 'Al-Baqarah',
      arabicName: 'البقرة',
      meaning: 'The Cow',
      verseCount: 286,
      revelation: RevelationType.medinan,
    ),
    Surah(
      number: 3,
      englishName: 'Aal-E-Imran',
      arabicName: 'آل عمران',
      meaning: 'The Family of Imran',
      verseCount: 200,
      revelation: RevelationType.medinan,
    ),
    Surah(
      number: 4,
      englishName: 'An-Nisa',
      arabicName: 'النساء',
      meaning: 'The Women',
      verseCount: 176,
      revelation: RevelationType.medinan,
    ),
    Surah(
      number: 5,
      englishName: 'Al-Maidah',
      arabicName: 'المائدة',
      meaning: 'The Table Spread',
      verseCount: 120,
      revelation: RevelationType.medinan,
    ),
    Surah(
      number: 6,
      englishName: 'Al-Anam',
      arabicName: 'الأنعام',
      meaning: 'The Cattle',
      verseCount: 165,
      revelation: RevelationType.meccan,
    ),
    Surah(
      number: 7,
      englishName: 'Al-Araf',
      arabicName: 'الأعراف',
      meaning: 'The Heights',
      verseCount: 206,
      revelation: RevelationType.meccan,
    ),
    Surah(
      number: 12,
      englishName: 'Yusuf',
      arabicName: 'يوسف',
      meaning: 'Joseph',
      verseCount: 111,
      revelation: RevelationType.meccan,
    ),
    Surah(
      number: 18,
      englishName: 'Al-Kahf',
      arabicName: 'الكهف',
      meaning: 'The Cave',
      verseCount: 110,
      revelation: RevelationType.meccan,
    ),
    Surah(
      number: 19,
      englishName: 'Maryam',
      arabicName: 'مريم',
      meaning: 'Mary',
      verseCount: 98,
      revelation: RevelationType.meccan,
    ),
    Surah(
      number: 36,
      englishName: 'Ya-Sin',
      arabicName: 'يس',
      meaning: 'Ya Sin',
      verseCount: 83,
      revelation: RevelationType.meccan,
    ),
    Surah(
      number: 55,
      englishName: 'Ar-Rahman',
      arabicName: 'الرحمن',
      meaning: 'The Most Merciful',
      verseCount: 78,
      revelation: RevelationType.medinan,
    ),
    Surah(
      number: 67,
      englishName: 'Al-Mulk',
      arabicName: 'الملك',
      meaning: 'The Sovereignty',
      verseCount: 30,
      revelation: RevelationType.meccan,
    ),
    Surah(
      number: 112,
      englishName: 'Al-Ikhlas',
      arabicName: 'الإخلاص',
      meaning: 'The Sincerity',
      verseCount: 4,
      revelation: RevelationType.meccan,
    ),
    Surah(
      number: 113,
      englishName: 'Al-Falaq',
      arabicName: 'الفلق',
      meaning: 'The Daybreak',
      verseCount: 5,
      revelation: RevelationType.meccan,
    ),
    Surah(
      number: 114,
      englishName: 'An-Nas',
      arabicName: 'الناس',
      meaning: 'Mankind',
      verseCount: 6,
      revelation: RevelationType.meccan,
    ),
  ];

  static Surah surahByNumber(int number) {
    return surahs.firstWhere(
      (surah) => surah.number == number,
      orElse: () => surahs.first,
    );
  }

  static const List<Ayah> fatihahAyahs = [
    Ayah(
      number: 1,
      arabic: 'بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ',
      translation: 'In the name of Allah, the Entirely Merciful, the Especially Merciful.',
    ),
    Ayah(
      number: 2,
      arabic: 'الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ',
      translation: 'All praise is due to Allah, Lord of the worlds.',
    ),
    Ayah(
      number: 3,
      arabic: 'الرَّحْمَٰنِ الرَّحِيمِ',
      translation: 'The Entirely Merciful, the Especially Merciful.',
    ),
    Ayah(
      number: 4,
      arabic: 'مَالِكِ يَوْمِ الدِّينِ',
      translation: 'Sovereign of the Day of Recompense.',
    ),
    Ayah(
      number: 5,
      arabic: 'إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ',
      translation: 'It is You we worship and You we ask for help.',
    ),
    Ayah(
      number: 6,
      arabic: 'اهْدِنَا الصِّرَاطَ الْمُسْتَقِيمَ',
      translation: 'Guide us to the straight path.',
    ),
    Ayah(
      number: 7,
      arabic: 'صِرَاطَ الَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ الْمَغْضُوبِ عَلَيْهِمْ وَلَا الضَّالِّينَ',
      translation:
          'The path of those upon whom You have bestowed favor, not of those who have evoked [Your] anger or of those who are astray.',
    ),
  ];

  static const List<Ayah> baqarahAyahs = [
    Ayah(
      number: 1,
      arabic: 'الم',
      translation: 'Alif, Lam, Meem.',
    ),
    Ayah(
      number: 2,
      arabic: 'ذَٰلِكَ الْكِتَابُ لَا رَيْبَ ۛ فِيهِ ۛ هُدًى لِّلْمُتَّقِينَ',
      translation: 'This is the Book about which there is no doubt, a guidance for those conscious of Allah.',
    ),
    Ayah(
      number: 3,
      arabic: 'الَّذِينَ يُؤْمِنُونَ بِالْغَيْبِ وَيُقِيمُونَ الصَّلَاةَ وَمِمَّا رَزَقْنَاهُمْ يُنفِقُونَ',
      translation:
          'Who believe in the unseen, establish prayer, and spend out of what We have provided for them.',
    ),
    Ayah(
      number: 255,
      arabic:
          'اللَّهُ لَا إِلَٰهَ إِلَّا هُوَ الْحَيُّ الْقَيُّومُ ۚ لَا تَأْخُذُهُ سِنَةٌ وَلَا نَوْمٌ',
      translation:
          'Allah — there is no deity except Him, the Ever-Living, the Sustainer of existence. Neither drowsiness overtakes Him nor sleep.',
    ),
  ];

  static const List<Ayah> ikhlasAyahs = [
    Ayah(
      number: 1,
      arabic: 'قُلْ هُوَ اللَّهُ أَحَدٌ',
      translation: 'Say, “He is Allah, [who is] One.”',
    ),
    Ayah(
      number: 2,
      arabic: 'اللَّهُ الصَّمَدُ',
      translation: 'Allah, the Eternal Refuge.',
    ),
    Ayah(
      number: 3,
      arabic: 'لَمْ يَلِدْ وَلَمْ يُولَدْ',
      translation: 'He neither begets nor is born.',
    ),
    Ayah(
      number: 4,
      arabic: 'وَلَمْ يَكُن لَّهُ كُفُوًا أَحَدٌ',
      translation: 'Nor is there to Him any equivalent.',
    ),
  ];

  static List<Ayah> ayahsFor(int surahNumber) {
    return switch (surahNumber) {
      1 => fatihahAyahs,
      2 => baqarahAyahs,
      112 => ikhlasAyahs,
      _ => fatihahAyahs,
    };
  }

  static const List<MockReciter> reciters = [
    MockReciter(name: 'Mishary Rashid Alafasy', subtitle: 'Full Quran'),
    MockReciter(name: 'Abdul Rahman Al-Sudais', subtitle: 'Full Quran'),
    MockReciter(name: 'Maher Al-Muaiqly', subtitle: 'Full Quran'),
    MockReciter(name: 'Saad Al-Ghamdi', subtitle: 'Full Quran'),
    MockReciter(name: 'Ahmed Al-Ajmi', subtitle: 'Full Quran'),
    MockReciter(name: 'Yasser Al-Dosari', subtitle: 'Full Quran'),
  ];

  static const List<MockDua> duas = [
    MockDua(
      title: 'For Forgiveness',
      arabic: 'رَبَّنَا اغْفِرْ لِي وَلِوَالِدَيَّ',
      translation: 'Our Lord, forgive me and my parents.',
    ),
    MockDua(
      title: 'For Guidance',
      arabic: 'رَبَّنَا آتِنَا فِي الدُّنْيَا حَسَنَةً',
      translation: 'Our Lord, give us good in this world.',
    ),
    MockDua(
      title: 'For Protection',
      arabic: 'حَسْبُنَا اللَّهُ وَنِعْمَ الْوَكِيلُ',
      translation: 'Allah is sufficient for us, and He is the best Disposer of affairs.',
    ),
  ];
}
