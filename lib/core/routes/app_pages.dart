import 'package:get/get.dart';

import '../../screens/bookmarks/bookmarks_screen.dart';
import '../../screens/main/main_binding.dart';
import '../../screens/main/main_navigation_screen.dart';
import '../../screens/mushaf/mushaf_binding.dart';
import '../../screens/mushaf/mushaf_screen.dart';
import '../../screens/onboarding/onboarding_binding.dart';
import '../../screens/onboarding/onboarding_screen.dart';
import '../../screens/quran/surah_detail_binding.dart';
import '../../screens/quran/surah_detail_screen.dart';
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
      page: () => const MushafScreen(),
      binding: MushafBinding(),
    ),
  ];
}
