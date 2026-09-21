import 'package:flutter/widgets.dart';
import 'package:get/get.dart';

import '../../core/controllers/bookmark_controller.dart';
import '../../core/controllers/hifz_mode_mixin.dart';
import '../../core/data/json_utils.dart';
import '../../core/data/models/app_bookmark.dart';
import '../../core/data/models/ayah.dart';
import '../../core/data/models/juz.dart';
import '../../core/data/models/surah.dart';
import '../../core/data/quran_repository.dart';
import '../../core/services/storage_service.dart';

class MushafController extends GetxController with HifzModeMixin {
  MushafController({int? initialPage}) : requestedPage = initialPage;

  static const pageCount = 604;

  final int? requestedPage;
  final isLoading = false.obs;
  final errorMessage = RxnString();
  final currentPage = 1.obs;
  final pages = <List<Ayah>>[].obs;
  final surahs = <Surah>[].obs;

  final surahStartPages = <int, int>{};
  final juzStartPages = <int, int>{};

  final QuranRepository _quran = Get.find<QuranRepository>();
  final StorageService _storage = Get.find<StorageService>();
  late final PageController pageController;

  BookmarkController get _bookmarks => Get.find<BookmarkController>();

  static int? resolveInitialPage(dynamic args) {
    int? raw;
    if (args is int) {
      raw = args;
    } else if (args is Map) {
      final map = asStringKeyMap(args);
      if (map.containsKey('initialPage')) {
        raw = asInt(map['initialPage']);
      } else if (map.containsKey('page')) {
        raw = asInt(map['page']);
      }
    }
    if (raw == null || raw < 1) return null;
    return raw.clamp(1, pageCount);
  }

  @override
  void onInit() {
    super.onInit();
    final page = (requestedPage ??
            resolveInitialPage(Get.arguments) ??
            _storage.lastMushafPage)
        .clamp(1, pageCount);
    currentPage.value = page;
    pageController = PageController(initialPage: page - 1);
    load();
  }

  @override
  void onClose() {
    pageController.dispose();
    super.onClose();
  }

  String get title => 'Page ${currentPage.value}';

  List<Ayah> ayahsForIndex(int index) {
    if (index < 0 || index >= pages.length) return const [];
    return pages[index];
  }

  int hifzIdFor(Ayah ayah) =>
      HifzModeMixin.ayahId(ayah.surahNumber, ayah.number);

  void onPageChanged(int index) {
    currentPage.value = index + 1;
    persistLastRead();
  }

  void jumpToPageNumber(int page) {
    final index = page.clamp(1, pageCount) - 1;
    currentPage.value = index + 1;
    persistLastRead();
    if (pageController.hasClients) {
      pageController.jumpToPage(index);
    }
  }

  void jumpToSurah(int surahNumber) {
    final page = surahStartPages[surahNumber];
    if (page == null) return;
    Get.back();
    jumpToPageNumber(page);
  }

  void jumpToJuz(int juzNumber) {
    final page = juzStartPages[juzNumber];
    if (page == null) return;
    Get.back();
    jumpToPageNumber(page);
  }

  Future<void> toggleBookmark() {
    final page = currentPage.value;
    final ayahs = ayahsForIndex(page - 1);
    final first = ayahs.isEmpty ? null : ayahs.first;
    final surahName = first == null
        ? ''
        : surahs
            .where((surah) => surah.number == first.surahNumber)
            .map((surah) => surah.englishName)
            .firstWhere((name) => name.isNotEmpty, orElse: () => first.surahEnglishName);
    return _bookmarks.toggle(
      AppBookmark.mushaf(
        page: page,
        surahNumber: first?.surahNumber,
        ayahNumber: first?.number,
        surahName: surahName,
      ),
    );
  }

  Future<void> load() async {
    isLoading.value = true;
    errorMessage.value = null;
    try {
      final loadedPages = await _quran.getMushafPages();
      final loadedSurahs = await _quran.getAllSurahs();
      if (isClosed) return;
      pages.assignAll(loadedPages);
      surahs.assignAll(loadedSurahs);
      _buildStartPages();
      persistLastRead();
    } catch (_) {
      if (isClosed) return;
      errorMessage.value = 'Unable to load Mushaf pages.';
    } finally {
      if (!isClosed) isLoading.value = false;
    }
  }

  void persistLastRead() {
    final ayahs = ayahsForIndex(currentPage.value - 1);
    final first = ayahs.isEmpty ? null : ayahs.first;
    _storage.saveMushafLastPage(
      page: currentPage.value,
      surahNumber: first?.surahNumber ?? 1,
      ayahNumber: first?.number ?? 1,
    );
  }

  void _buildStartPages() {
    surahStartPages.clear();
    juzStartPages.clear();

    for (var i = 0; i < pages.length; i++) {
      final pageNumber = i + 1;
      for (final ayah in pages[i]) {
        surahStartPages.putIfAbsent(ayah.surahNumber, () => pageNumber);
      }
    }

    for (final juz in Juz.all) {
      juzStartPages[juz.number] = _pageForAyah(
        juz.startSurahNumber,
        juz.startAyahNumber,
      );
    }
  }

  int _pageForAyah(int surahNumber, int ayahNumber) {
    for (var i = 0; i < pages.length; i++) {
      final found = pages[i].any(
        (ayah) =>
            ayah.surahNumber == surahNumber && ayah.number == ayahNumber,
      );
      if (found) return i + 1;
    }
    return surahStartPages[surahNumber] ?? 1;
  }
}
