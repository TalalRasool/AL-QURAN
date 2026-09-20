import 'package:flutter/material.dart';
import 'package:get/get.dart';

import '../../core/constants/app_colors.dart';
import '../../core/controllers/settings_controller.dart';
import '../../core/widgets/widgets.dart';
import '../audio/audio_screen.dart';
import '../home/home_screen.dart';
import '../profile/profile_screen.dart';
import '../quran/quran_screen.dart';
import '../../features/hadith/hadith_books_screen.dart';
import 'navigation_controller.dart';

class MainNavigationScreen extends GetView<NavigationController> {
  const MainNavigationScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Obx(() {
      Get.find<SettingsController>().isDarkMode.value;
      return Scaffold(
        backgroundColor: AppColors.background,
        body: IndexedStack(
          index: controller.currentIndex.value,
          children: [
            HomeScreen(),
            QuranScreen(),
            HadithBooksScreen(),
            AudioScreen(),
            ProfileScreen(),
          ],
        ),
        bottomNavigationBar: AppBottomNav(
          currentIndex: controller.currentIndex.value,
          onTap: controller.changeTab,
        ),
      );
    });
  }
}
