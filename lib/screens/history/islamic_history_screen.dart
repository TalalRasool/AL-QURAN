import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:get/get.dart';

import '../../core/constants/app_colors.dart';
import '../../core/constants/app_text_styles.dart';
import '../../core/controllers/settings_controller.dart';
import '../../core/data/models/seerah.dart';
import '../../core/widgets/widgets.dart';
import 'islamic_history_controller.dart';

class IslamicHistoryScreen extends GetView<IslamicHistoryController> {
  const IslamicHistoryScreen({super.key});

  static const _tabIcons = [
    Icons.auto_stories_rounded,
    Icons.groups_rounded,
    Icons.shield_rounded,
  ];

  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 3,
      child: Obx(() {
        if (Get.isRegistered<SettingsController>()) {
          Get.find<SettingsController>().isDarkMode.value;
        }
        controller.watchLanguage();
        final isRtl = controller.isRtl;
        return Directionality(
          textDirection: isRtl ? TextDirection.rtl : TextDirection.ltr,
          child: Scaffold(
            backgroundColor: AppColors.background,
            appBar: CustomAppBar(title: controller.screenTitle),
            body: _buildBody(),
          ),
        );
      }),
    );
  }

  Widget _buildBody() {
    if (controller.isLoading.value && !controller.hasAnyChapters) {
      return const Center(
        child: CircularProgressIndicator(color: AppColors.primary),
      );
    }

    if (controller.errorMessage.value != null && !controller.hasAnyChapters) {
      return Center(
        child: Padding(
          padding: EdgeInsets.symmetric(horizontal: 24.w),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              Text(
                controller.errorMessage.value!,
                style: AppTextStyles.body,
                textAlign: TextAlign.center,
              ),
              SizedBox(height: 12.h),
              TextButton(
                onPressed: controller.load,
                child: const Text('Retry'),
              ),
            ],
          ),
        ),
      );
    }

    final labels = controller.tabLabels;
    return Column(
      children: [
        Padding(
          padding: EdgeInsets.fromLTRB(20.w, 4.h, 20.w, 8.h),
          child: _HistoryTabBar(labels: labels),
        ),
        Expanded(
          child: TabBarView(
            children: [
              for (var i = 0; i < labels.length; i++)
                _HistoryListTab(
                  chapters: List<SeerahChapter>.from(
                    controller.chaptersForTab(i),
                  ),
                  icon: _tabIcons[i],
                  emptyMessage: controller.emptyMessageForTab(i),
                ),
            ],
          ),
        ),
      ],
    );
  }
}

class _HistoryTabBar extends StatelessWidget {
  const _HistoryTabBar({required this.labels});

  final List<String> labels;

  @override
  Widget build(BuildContext context) {
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
          for (final label in labels) Tab(text: label, height: 40.h),
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
  }
}

class _HistoryListTab extends GetView<IslamicHistoryController> {
  const _HistoryListTab({
    required this.chapters,
    required this.icon,
    required this.emptyMessage,
  });

  final List<SeerahChapter> chapters;
  final IconData icon;
  final String emptyMessage;

  @override
  Widget build(BuildContext context) {
    if (chapters.isEmpty) {
      return Center(
        child: Padding(
          padding: EdgeInsets.symmetric(horizontal: 24.w),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              Text(
                emptyMessage,
                style: AppTextStyles.body,
                textAlign: TextAlign.center,
              ),
              SizedBox(height: 12.h),
              TextButton(
                onPressed: controller.load,
                child: const Text('Retry'),
              ),
            ],
          ),
        ),
      );
    }

    return ListView.separated(
      padding: EdgeInsets.fromLTRB(20.w, 8.h, 20.w, 24.h),
      itemCount: chapters.length,
      separatorBuilder: (_, _) => SizedBox(height: 12.h),
      itemBuilder: (context, index) {
        return _HistoryChapterCard(chapter: chapters[index], icon: icon);
      },
    );
  }
}

class _HistoryChapterCard extends GetView<IslamicHistoryController> {
  const _HistoryChapterCard({
    required this.chapter,
    required this.icon,
  });

  final SeerahChapter chapter;
  final IconData icon;

  @override
  Widget build(BuildContext context) {
    final settings = Get.isRegistered<SettingsController>()
        ? Get.find<SettingsController>()
        : null;
    return Obx(() {
      settings?.isDarkMode.value;
      controller.watchLanguage();
      controller.expandedIds.length;
      final lang = controller.languageCode;
      final isRtl = controller.isRtl;
      final expanded = controller.isExpanded(chapter.id);
      final title = chapter.titleFor(lang);
      final heading = chapter.headingFor(lang);
      final details = chapter.detailsFor(lang);
      final titleStyle = (lang == 'en' || lang == 'id' || settings == null)
          ? AppTextStyles.heading3
          : settings.translationStyle(color: AppColors.textPrimary);
      final bodyStyle = (lang == 'en' || lang == 'id' || settings == null)
          ? AppTextStyles.body
          : settings.translationStyle(color: AppColors.textPrimary);

      return Material(
        color: AppColors.surface,
        borderRadius: BorderRadius.circular(16.r),
        child: InkWell(
          onTap: () => controller.toggle(chapter.id),
          borderRadius: BorderRadius.circular(16.r),
          child: Padding(
            padding: EdgeInsets.fromLTRB(16.w, 14.h, 12.w, 14.h),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                Row(
                  children: [
                    Container(
                      width: 44.w,
                      height: 44.w,
                      decoration: BoxDecoration(
                        color: AppColors.mint,
                        borderRadius: BorderRadius.circular(12.r),
                      ),
                      alignment: Alignment.center,
                      child: Icon(
                        icon,
                        color: AppColors.primary,
                        size: 22.sp,
                      ),
                    ),
                    SizedBox(width: 12.w),
                    Expanded(
                      child: Column(
                        crossAxisAlignment: isRtl
                            ? CrossAxisAlignment.end
                            : CrossAxisAlignment.start,
                        children: [
                          Text(
                            title,
                            textDirection: isRtl
                                ? TextDirection.rtl
                                : TextDirection.ltr,
                            style: titleStyle,
                          ),
                          if (heading.isNotEmpty) ...[
                            SizedBox(height: 2.h),
                            Text(
                              heading,
                              textDirection: isRtl
                                  ? TextDirection.rtl
                                  : TextDirection.ltr,
                              style: AppTextStyles.bodySmall,
                            ),
                          ],
                        ],
                      ),
                    ),
                    AnimatedRotation(
                      turns: expanded ? 0.5 : 0,
                      duration: const Duration(milliseconds: 200),
                      child: Icon(
                        Icons.keyboard_arrow_down_rounded,
                        color: AppColors.textSecondary,
                        size: 26.sp,
                      ),
                    ),
                  ],
                ),
                AnimatedCrossFade(
                  firstChild: const SizedBox(width: double.infinity),
                  secondChild: Padding(
                    padding: EdgeInsets.only(top: 12.h),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.stretch,
                      children: [
                        if (details.isNotEmpty)
                          Text(
                            details,
                            textAlign: isRtl ? TextAlign.right : TextAlign.left,
                            textDirection: isRtl
                                ? TextDirection.rtl
                                : TextDirection.ltr,
                            style: bodyStyle,
                          ),
                        for (final item in chapter.items) ...[
                          SizedBox(height: 14.h),
                          _HistoryItemBlock(
                            item: item,
                            languageCode: lang,
                            isRtl: isRtl,
                            titleStyle: titleStyle,
                            bodyStyle: bodyStyle,
                          ),
                        ],
                      ],
                    ),
                  ),
                  crossFadeState: expanded
                      ? CrossFadeState.showSecond
                      : CrossFadeState.showFirst,
                  duration: const Duration(milliseconds: 220),
                  sizeCurve: Curves.easeOutCubic,
                ),
              ],
            ),
          ),
        ),
      );
    });
  }
}

class _HistoryItemBlock extends StatelessWidget {
  const _HistoryItemBlock({
    required this.item,
    required this.languageCode,
    required this.isRtl,
    required this.titleStyle,
    required this.bodyStyle,
  });

  final SeerahItem item;
  final String languageCode;
  final bool isRtl;
  final TextStyle titleStyle;
  final TextStyle bodyStyle;

  @override
  Widget build(BuildContext context) {
    final title = item.titleFor(languageCode);
    final heading = item.headingFor(languageCode);
    final details = item.detailsFor(languageCode);
    return Container(
      width: double.infinity,
      padding: EdgeInsets.all(12.w),
      decoration: BoxDecoration(
        color: AppColors.isDark ? AppColors.background : AppColors.mint,
        borderRadius: BorderRadius.circular(12.r),
      ),
      child: Column(
        crossAxisAlignment:
            isRtl ? CrossAxisAlignment.end : CrossAxisAlignment.start,
        children: [
          Text(
            title,
            textDirection: isRtl ? TextDirection.rtl : TextDirection.ltr,
            style: titleStyle,
          ),
          if (heading.isNotEmpty) ...[
            SizedBox(height: 2.h),
            Text(
              heading,
              textDirection: isRtl ? TextDirection.rtl : TextDirection.ltr,
              style: AppTextStyles.bodySmall.copyWith(
                color: AppColors.primary,
                fontWeight: FontWeight.w600,
              ),
            ),
          ],
          if (details.isNotEmpty) ...[
            SizedBox(height: 8.h),
            Text(
              details,
              textAlign: isRtl ? TextAlign.right : TextAlign.left,
              textDirection: isRtl ? TextDirection.rtl : TextDirection.ltr,
              style: bodyStyle,
            ),
          ],
        ],
      ),
    );
  }
}
