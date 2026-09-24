import 'package:get/get.dart';

import '../../core/data/models/juz.dart';
import '../../core/data/models/surah.dart';
import '../../core/data/quran_repository.dart';
import '../../core/routes/app_routes.dart';
import '../../core/services/storage_service.dart';

enum SurahRevelationFilter { all, makki, madani }

class QuranController extends GetxController {
  static const surahTabIndex = 0;
  static const juzTabIndex = 1;

  final searchQuery = ''.obs;
  final tabIndex = 0.obs;
  final revelationFilter = SurahRevelationFilter.all.obs;
  final allSurahs = <Surah>[].obs;
  final allJuz = <Juz>[].obs;
  final isLoading = false.obs;
  final errorMessage = RxnString();

  final QuranRepository _quran = Get.find<QuranRepository>();
  final StorageService _storage = Get.find<StorageService>();

  int get lastReadNumber {
    final last = _storage.lastRead.value;
    if (last == null || last.isMushaf) return -1;
    return last.surahNumber;
  }

  bool get isJuzTab => tabIndex.value == juzTabIndex;

  @override
  void onInit() {
    super.onInit();
    allJuz.assignAll(Juz.all);
    loadSurahs();
  }

  Future<void> loadSurahs() async {
    isLoading.value = true;
    errorMessage.value = null;
    try {
      allSurahs.assignAll(await _quran.getAllSurahs());
    } catch (_) {
      errorMessage.value =
          'Unable to load surahs from the offline Quran data.';
    } finally {
      isLoading.value = false;
    }
  }

  List<Surah> get filteredSurahs {
    final query = _normalizeSearch(searchQuery.value);
    final filter = revelationFilter.value;
    return allSurahs.where((surah) {
      final matchesFilter = switch (filter) {
        SurahRevelationFilter.all => true,
        SurahRevelationFilter.makki => surah.isMeccan,
        SurahRevelationFilter.madani => !surah.isMeccan,
      };
      if (!matchesFilter) return false;
      if (query.isEmpty) return true;
      return _matchesSearch(surah.englishName, query) ||
          _matchesSearch(surah.arabicName, query) ||
          _matchesSearch(surah.meaning, query) ||
          surah.number.toString() == query;
    }).toList();
  }

  List<Juz> get filteredJuz {
    final query = _normalizeSearch(searchQuery.value);
    if (query.isEmpty) return allJuz;
    return allJuz.where((juz) {
      return _matchesSearch('juz ${juz.number}', query) ||
          juz.number.toString() == query ||
          _matchesSearch(juz.englishName, query) ||
          _matchesSearch(juz.arabicName, query) ||
          _matchesSearch(startSurahName(juz), query);
    }).toList();
  }

  String _normalizeSearch(String value) {
    return value
        .replaceAll('-', ' ')
        .replaceAll(RegExp(r'\s+'), ' ')
        .trim()
        .toLowerCase();
  }

  bool _matchesSearch(String target, String normalizedQuery) {
    if (normalizedQuery.isEmpty) return true;
    final normalizedTarget = _normalizeSearch(target);
    if (normalizedTarget.contains(normalizedQuery)) return true;
    final compactQuery = normalizedQuery.replaceAll(' ', '');
    final compactTarget = normalizedTarget.replaceAll(' ', '');
    return compactQuery.isNotEmpty && compactTarget.contains(compactQuery);
  }

  String startSurahName(Juz juz) {
    for (final surah in allSurahs) {
      if (surah.number == juz.startSurahNumber) return surah.englishName;
    }
    return 'Surah ${juz.startSurahNumber}';
  }

  void openSurah(int number) {
    Get.toNamed(AppRoutes.quranReading, arguments: {'surah': number});
  }

  void openJuz(Juz juz) {
    Get.toNamed(AppRoutes.quranReading, arguments: {'juz': juz.number});
  }

  void onSearch(String value) => searchQuery.value = value;

  void onTabChanged(int index) => tabIndex.value = index;

  void onRevelationFilterChanged(int index) {
    revelationFilter.value = SurahRevelationFilter
        .values[index.clamp(0, SurahRevelationFilter.values.length - 1)];
  }

  void showSurahTab() => tabIndex.value = surahTabIndex;

  void showJuzTab() => tabIndex.value = juzTabIndex;
}
