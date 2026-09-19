import 'package:get/get.dart';
import 'package:hijri/hijri_calendar.dart';

import '../../core/data/models/daily_verse.dart';
import '../../core/data/models/surah.dart';
import '../../core/data/quran_repository.dart';
import '../../core/routes/app_routes.dart';
import '../../core/services/storage_service.dart';
import '../main/navigation_controller.dart';
import '../quran/quran_controller.dart';

class HomeController extends GetxController {
  final QuranRepository _quran = Get.find<QuranRepository>();
  final StorageService _storage = Get.find<StorageService>();
  final lastReadSurah = Rxn<Surah>();
  final dailyVerse = Rxn<DailyVerse>();
  final isDailyVerseLoading = false.obs;
  final _workers = <Worker>[];

  NavigationController get _nav => Get.find<NavigationController>();

  String get userName {
    final name = _storage.userName.value.trim();
    return name.isEmpty ? 'Reader' : name;
  }

  String get gregorianDateLabel {
    const weekdays = [
      'Monday',
      'Tuesday',
      'Wednesday',
      'Thursday',
      'Friday',
      'Saturday',
      'Sunday',
    ];
    const months = [
      'January',
      'February',
      'March',
      'April',
      'May',
      'June',
      'July',
      'August',
      'September',
      'October',
      'November',
      'December',
    ];
    final now = DateTime.now();
    return '${weekdays[now.weekday - 1]}, ${now.day} ${months[now.month - 1]} ${now.year}';
  }

  String get hijriDateLabel {
    final hijri = HijriCalendar.fromDate(DateTime.now());
    return '${hijri.hDay} ${hijri.getLongMonthName()} ${hijri.hYear} AH';
  }

  @override
  void onInit() {
    super.onInit();
    loadLastRead();
    loadDailyVerse();
    _workers.add(ever(_storage.lastRead, (_) => loadLastRead()));
    _workers.add(ever(_storage.selectedTranslationId, (_) => loadDailyVerse()));
  }

  @override
  void onClose() {
    for (final worker in _workers) {
      worker.dispose();
    }
    super.onClose();
  }

  Future<void> loadLastRead() async {
    try {
      final number = _storage.lastRead.value?.surahNumber ?? 1;
      final surah = await _quran.getSurahByNumber(number);
      if (isClosed) return;
      lastReadSurah.value = surah;
    } catch (_) {
      if (isClosed) return;
      lastReadSurah.value = null;
    }
  }

  Future<void> loadDailyVerse() async {
    isDailyVerseLoading.value = dailyVerse.value == null;
    try {
      final verse = await _quran.getDailyVerse();
      if (isClosed) return;
      dailyVerse.value = verse;
    } catch (_) {
      if (isClosed) return;
    } finally {
      if (!isClosed) {
        isDailyVerseLoading.value = false;
      }
    }
  }

  bool get isMushafLastRead => _storage.lastRead.value?.isMushaf ?? false;

  String get continueSurahTitle {
    if (isMushafLastRead) {
      final page = _storage.lastRead.value?.mushafPage ?? _storage.lastMushafPage;
      return 'Mushaf - Page $page';
    }
    final name = lastReadSurah.value?.englishName;
    if (name == null || name.isEmpty) return 'Surah Al-Fatihah';
    return 'Surah $name';
  }

  String get continueAyahLabel {
    if (isMushafLastRead) {
      final name = lastReadSurah.value?.englishName;
      if (name == null || name.isEmpty) return 'Mushaf Mode';
      return name;
    }
    final ayah = _storage.lastRead.value?.ayahNumber ?? 1;
    return 'Ayah $ayah';
  }

  void continueReading() {
    final last = _storage.lastRead.value;
    if (last != null && last.isMushaf) {
      Get.toNamed(
        AppRoutes.mushaf,
        arguments: {
          'initialPage': last.mushafPage ?? _storage.lastMushafPage,
        },
      );
      return;
    }
    final number =
        lastReadSurah.value?.number ?? last?.surahNumber ?? 1;
    Get.toNamed(
      AppRoutes.quranReading,
      arguments: {
        'surah': number,
        'ayah': last?.ayahNumber ?? 1,
      },
    );
  }

  void openSurahs() {
    Get.find<QuranController>().showSurahTab();
    _nav.changeTab(1);
  }

  void openJuz() {
    Get.find<QuranController>().showJuzTab();
    _nav.changeTab(1);
  }

  void openBookmarks() => Get.toNamed(AppRoutes.bookmarks);

  void openMushaf() => Get.toNamed(
        AppRoutes.mushaf,
        arguments: {'initialPage': _storage.lastMushafPage},
      );

  void openTasbih() => Get.toNamed(AppRoutes.tasbih);

  void openIslamicHistory() => Get.toNamed(AppRoutes.islamicHistory);

  void openHifzTester() => Get.toNamed(AppRoutes.hifzTester);

  void openQuranStudy() => Get.toNamed(AppRoutes.quranStudy);

  void openLastRead() => continueReading();

  void openProfile() => _nav.changeTab(NavigationController.profileTabIndex);

  void onNotificationTap() {
    Get.snackbar(
      'Notifications',
      'You are all caught up.',
      snackPosition: SnackPosition.TOP,
    );
  }

  void shareDailyVerse() {
    final verse = dailyVerse.value;
    if (verse == null) return;
    Get.snackbar(
      'Daily Verse',
      '${verse.translation}\n(${verse.reference})',
      snackPosition: SnackPosition.BOTTOM,
    );
  }
}
