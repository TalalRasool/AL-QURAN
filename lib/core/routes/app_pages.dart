import 'package:get/get.dart';

import '../../features/hadith/hadith_binding.dart';
import '../../features/hadith/hadith_chapters_screen.dart';
import '../../features/hadith/hadith_read_screen.dart';
import '../../screens/bookmarks/bookmarks_screen.dart';
import '../../screens/hifz_tester_binding.dart';
import '../../screens/hifz_tester_screen.dart';
import '../../screens/history/islamic_history_binding.dart';
import '../../screens/history/islamic_history_screen.dart';
import '../../screens/main/main_binding.dart';
import '../../screens/main/main_navigation_screen.dart';
import '../../screens/mushaf/mushaf_binding.dart';
import '../../screens/mushaf/mushaf_controller.dart';
import '../../screens/mushaf/mushaf_screen.dart';
import '../../screens/onboarding/onboarding_binding.dart';
import '../../screens/onboarding/onboarding_screen.dart';
import '../../screens/profile/edit_profile_screen.dart';
import '../../screens/profile/profile_controller.dart';
import '../../screens/quran/quran_reading_binding.dart';
import '../../screens/quran/quran_reading_screen.dart';
import '../../screens/quran/surah_detail_binding.dart';
import '../../screens/quran/surah_detail_screen.dart';
import '../../screens/study/offline_quran_binding.dart';
import '../../screens/study/offline_quran_screen.dart';
import '../../screens/tasbih/tasbih_binding.dart';
import '../../screens/tasbih/tasbih_screen.dart';
import '../../screens/translations/translations_binding.dart';
import '../../screens/translations/translations_screen.dart';
import 'app_routes.dart';

class AppPages {
  AppPages._();

  static final pages = <GetPage<dynamic>>[
    GetPage(
      name: AppRoutes.onboarding,
      page: () => const OnboardingScreen(),
      binding: OnboardingBinding(),
    ),
    GetPage(
      name: AppRoutes.home,
      page: () => const MainNavigationScreen(),
      binding: MainBinding(),
    ),
    GetPage(
      name: AppRoutes.surahDetail,
      page: () => const SurahDetailScreen(),
      binding: SurahDetailBinding(),
    ),
    GetPage(
      name: AppRoutes.tasbih,
      page: () => const TasbihScreen(),
      binding: TasbihBinding(),
    ),
    GetPage(
      name: AppRoutes.translations,
      page: () => const TranslationsScreen(),
      binding: TranslationsBinding(),
    ),
    GetPage(
      name: AppRoutes.bookmarks,
      page: () => const BookmarksScreen(),
    ),
    GetPage(
      name: AppRoutes.mushaf,
      page: () => MushafScreen(
        initialPage: MushafController.resolveInitialPage(Get.arguments),
      ),
      binding: MushafBinding(),
    ),
    GetPage(
      name: AppRoutes.hadithChapters,
      page: () => const HadithChaptersScreen(),
      binding: HadithChaptersBinding(),
    ),
    GetPage(
      name: AppRoutes.hadithRead,
      page: () => const HadithReadScreen(),
      binding: HadithReadBinding(),
    ),
    GetPage(
      name: AppRoutes.islamicHistory,
      page: () => const IslamicHistoryScreen(),
      binding: IslamicHistoryBinding(),
    ),
    GetPage(
      name: AppRoutes.hifzTester,
      page: () => const HifzTesterScreen(),
      binding: HifzTesterBinding(),
    ),
    GetPage(
      name: AppRoutes.quranStudy,
      page: () => const QuranStudyScreen(),
      binding: OfflineQuranBinding(),
    ),
    GetPage(
      name: AppRoutes.quranReading,
      page: () => const QuranReadingScreen(),
      binding: QuranReadingBinding(),
    ),
    GetPage(
      name: AppRoutes.editProfile,
      page: () => const EditProfileScreen(),
      binding: BindingsBuilder(() {
        if (!Get.isRegistered<ProfileController>()) {
          Get.put(ProfileController());
        }
      }),
    ),
  ];
}
