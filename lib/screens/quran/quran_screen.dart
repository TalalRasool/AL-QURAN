import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:flutter_svg/flutter_svg.dart';
import 'package:get/get.dart';

import '../../core/constants/app_assets.dart';
import '../../core/constants/app_colors.dart';
import '../../core/constants/app_text_styles.dart';
import '../../core/controllers/settings_controller.dart';
import '../../core/widgets/widgets.dart';
import 'quran_controller.dart';

class QuranScreen extends GetView<QuranController> {
  const QuranScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final initialTab = controller.tabIndex.value;
    return DefaultTabController(
      length: 2,
      initialIndex: initialTab < 0 || initialTab > 1 ? 0 : initialTab,
      child: _TabSync(
        child: SafeArea(
          bottom: false,
          child: Padding(
            padding: EdgeInsets.symmetric(horizontal: 20.w),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                SizedBox(height: 8.h),
                Obx(() {
                  Get.find<SettingsController>().isDarkMode.value;
                  return Text(
                    controller.isJuzTab ? 'Juz' : 'Surah',
                    style: AppTextStyles.heading2,
                  );
                }),
                SizedBox(height: 16.h),
                Obx(() {
                  Get.find<SettingsController>().isDarkMode.value;
                  return CustomTextField(
                    hintText: controller.isJuzTab
                        ? 'Search Surah or Juz'
                        : 'Search Surah',
                    prefixIcon: Padding(
                      padding: EdgeInsets.all(12.w),
                      child: SvgPicture.asset(
                        AppAssets.searchIcon,
                        width: 20.w,
                        height: 20.w,
                        colorFilter: ColorFilter.mode(
                          AppColors.textSecondary,
                          BlendMode.srcIn,
                        ),
                      ),
                    ),
                    onChanged: controller.onSearch,
                  );
                }),
                SizedBox(height: 16.h),
                const _SurahJuzTabBar(),
                SizedBox(height: 16.h),
                Expanded(child: _buildIndexBody()),
              ],
            ),
          ),
        ),
      ),
    );
  }

  Widget _buildIndexBody() {
    return Stack(
      children: [
        const TabBarView(
          children: [
            _SurahList(),
            _JuzList(),
          ],
        ),
        Obx(() {
          if (controller.isLoading.value) {
            return const ColoredBox(
              color: Colors.transparent,
              child: Center(
                child: CircularProgressIndicator(color: AppColors.primary),
              ),
            );
          }

          final error = controller.errorMessage.value;
          if (error != null) {
            return ColoredBox(
              color: AppColors.background,
              child: Center(
                child: Padding(
                  padding: EdgeInsets.symmetric(horizontal: 24.w),
                  child: Column(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Text(
                        error,
                        style: AppTextStyles.body,
                        textAlign: TextAlign.center,
                      ),
                      SizedBox(height: 12.h),
                      TextButton(
                        onPressed: controller.loadSurahs,
                        child: const Text('Retry'),
                      ),
                    ],
                  ),
                ),
              ),
            );
          }

          return const SizedBox.shrink();
        }),
      ],
    );
  }
}

class _SurahJuzTabBar extends StatelessWidget {
  const _SurahJuzTabBar();

  @override
  Widget build(BuildContext context) {
    return Obx(() {
      Get.find<SettingsController>().isDarkMode.value;
      final unselected = AppColors.isDark
          ? AppColors.textPrimary
          : AppColors.primary;
      return Container(
        height: 44.h,
        decoration: BoxDecoration(
          color: AppColors.mint,
          borderRadius: BorderRadius.circular(24.r),
        ),
        child: TabBar(
          tabs: [
            Tab(text: 'Surah', height: 40.h),
            Tab(text: 'Juz', height: 40.h),
          ],
          indicator: BoxDecoration(
            color: AppColors.primary,
            borderRadius: BorderRadius.circular(24.r),
          ),
          indicatorPadding: EdgeInsets.all(3.w),
          indicatorSize: TabBarIndicatorSize.tab,
          dividerColor: Colors.transparent,
          labelColor: AppColors.white,
          unselectedLabelColor: unselected,
          labelStyle: AppTextStyles.bodySmall.copyWith(
            fontWeight: FontWeight.w600,
          ),
          unselectedLabelStyle: AppTextStyles.bodySmall.copyWith(
            fontWeight: FontWeight.w600,
          ),
          splashBorderRadius: BorderRadius.circular(24.r),
        ),
      );
    });
  }
}

/// Keeps [DefaultTabController] in sync with [QuranController.tabIndex]
/// so Home shortcuts can still open the Juz tab.
class _TabSync extends StatefulWidget {
  const _TabSync({required this.child});

  final Widget child;

  @override
  State<_TabSync> createState() => _TabSyncState();
}

class _TabSyncState extends State<_TabSync> {
  TabController? _tabs;
  Worker? _worker;

  @override
  void initState() {
    super.initState();
    _worker = ever(Get.find<QuranController>().tabIndex, (index) {
      final tabs = _tabs;
      if (tabs != null && tabs.index != index) {
        tabs.animateTo(index);
      }
    });
  }

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    final tabs = DefaultTabController.of(context);
    if (!identical(_tabs, tabs)) {
      _tabs?.removeListener(_onTabChanged);
      _tabs = tabs;
      _tabs!.addListener(_onTabChanged);
      final wanted = Get.find<QuranController>().tabIndex.value;
      if (tabs.index != wanted) {
        tabs.index = wanted;
      }
    }
  }

  void _onTabChanged() {
    final tabs = _tabs;
    if (tabs == null || tabs.indexIsChanging) return;
    Get.find<QuranController>().onTabChanged(tabs.index);
  }

  @override
  void dispose() {
    _tabs?.removeListener(_onTabChanged);
    _worker?.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) => widget.child;
}

class _SurahList extends GetView<QuranController> {
  const _SurahList();

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        const _RevelationFilter(),
        SizedBox(height: 12.h),
        Expanded(
          child: Obx(() {
            Get.find<SettingsController>().isDarkMode.value;
            controller.searchQuery.value;
            controller.revelationFilter.value;
            final surahs = controller.filteredSurahs;
            if (surahs.isEmpty) {
              return Center(
                child: Text('No surahs found', style: AppTextStyles.body),
              );
            }

            return ListView.separated(
              padding: EdgeInsets.only(bottom: 16.h),
              itemCount: surahs.length,
              separatorBuilder: (_, _) => SizedBox(height: 10.h),
              itemBuilder: (context, index) {
                final surah = surahs[index];
                return SurahTileCard(
                  number: surah.number,
                  englishName: surah.englishName,
                  arabicName: surah.arabicName,
                  meaning: surah.meaning,
                  verseCount: surah.verseCount,
                  isActive: surah.number == controller.lastReadNumber,
                  onTap: () => controller.openSurah(surah.number),
                );
              },
            );
          }),
        ),
      ],
    );
  }
}

class _RevelationFilter extends GetView<QuranController> {
  const _RevelationFilter();

  @override
  Widget build(BuildContext context) {
    return Obx(() {
      Get.find<SettingsController>().isDarkMode.value;
      return PillTabs(
        labels: const ['All Surahs', 'Makki', 'Madani'],
        selectedIndex: controller.revelationFilter.value.index,
        onChanged: controller.onRevelationFilterChanged,
      );
    });
  }
}

class _JuzList extends GetView<QuranController> {
  const _JuzList();

  @override
  Widget build(BuildContext context) {
    return Obx(() {
      Get.find<SettingsController>().isDarkMode.value;
      controller.searchQuery.value;
      final juzList = controller.filteredJuz;
      if (juzList.isEmpty) {
        return Center(
          child: Text('No juz found', style: AppTextStyles.body),
        );
      }

      return ListView.separated(
        padding: EdgeInsets.only(bottom: 16.h),
        itemCount: juzList.length,
        separatorBuilder: (_, _) => SizedBox(height: 10.h),
        itemBuilder: (context, index) {
          final juz = juzList[index];
          return SurahTileCard(
            number: juz.number,
            englishName: juz.englishName,
            arabicName: juz.arabicName,
            meaning: 'Juz ${juz.number}',
            onTap: () => controller.openJuz(juz),
          );
        },
      );
    });
  }
}
