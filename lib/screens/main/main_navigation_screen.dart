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
        body: _PersistentTabs(index: controller.currentIndex.value),
        bottomNavigationBar: AppBottomNav(
          currentIndex: controller.currentIndex.value,
          onTap: controller.changeTab,
        ),
      );
    });
  }
}

class _PersistentTabs extends StatefulWidget {
  const _PersistentTabs({required this.index});

  final int index;

  @override
  State<_PersistentTabs> createState() => _PersistentTabsState();
}

class _PersistentTabsState extends State<_PersistentTabs> {
  final _built = <int>{0};

  @override
  Widget build(BuildContext context) {
    _built.add(widget.index);
    return IndexedStack(
      index: widget.index,
      children: [
        const HomeScreen(),
        _built.contains(1) ? const QuranScreen() : const SizedBox.shrink(),
        _built.contains(2)
            ? const HadithBooksScreen()
            : const SizedBox.shrink(),
        _built.contains(3) ? const AudioScreen() : const SizedBox.shrink(),
        _built.contains(4) ? const ProfileScreen() : const SizedBox.shrink(),
      ],
    );
  }
}
