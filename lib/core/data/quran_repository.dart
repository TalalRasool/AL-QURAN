import 'models/ayah.dart';
import 'models/daily_verse.dart';
import 'models/reciter.dart';
import 'models/surah.dart';
import 'models/translation_edition.dart';

abstract class QuranRepository {
  Future<List<Surah>> getAllSurahs();

  Future<Surah> getSurahByNumber(int number);

  Future<List<Ayah>> getAyahs(int surahNumber);

  Future<List<Ayah>> getJuzAyahs(int juzNumber);

  Future<List<List<Ayah>>> getMushafPages();

  Future<DailyVerse> getDailyVerse();

  Future<List<Reciter>> getReciters();

  Future<List<TranslationEdition>> getTranslationEditions();

  Future<void> clearAyahCaches();
}

