import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:get/get.dart';
import 'package:scrollable_positioned_list/scrollable_positioned_list.dart';

import '../../core/constants/app_colors.dart';
import '../../core/constants/app_text_styles.dart';
import '../../core/controllers/bookmark_controller.dart';
import '../../core/controllers/settings_controller.dart';
import '../../core/data/models/azkar_dua.dart';
import '../../core/services/storage_service.dart';
import '../../core/widgets/widgets.dart';
import 'tasbih_controller.dart';

class TasbihScreen extends GetView<TasbihController> {
  const TasbihScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Obx(() {
      Get.find<SettingsController>().isDarkMode.value;
      return Scaffold(
        backgroundColor: AppColors.background,
        appBar: const CustomAppBar(title: 'Tasbih'),
        body: Padding(
          padding: EdgeInsets.symmetric(horizontal: 20.w),
          child: Column(
            children: [
              Obx(
                () => PillTabs(
                  labels: const ['Counter', 'Duas', 'Zikr o Azkar'],
                  selectedIndex: controller.tabIndex.value,
                  onChanged: controller.onTabChanged,
                ),
              ),
              SizedBox(height: 12.h),
              Expanded(
                child: Obx(() {
                  return switch (controller.tabIndex.value) {
                    1 => const _DuasTab(),
                    2 => const _AzkarTab(),
                    _ => const _CounterTab(),
                  };
                }),
              ),
            ],
          ),
        ),
      );
    });
  }
}

class _CounterTab extends GetView<TasbihController> {
  const _CounterTab();

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        const Spacer(),
        Obx(
          () => SizedBox(
            width: 240.w,
            height: 240.w,
            child: Stack(
              alignment: Alignment.center,
              children: [
                SizedBox(
                  width: 240.w,
                  height: 240.w,
                  child: CircularProgressIndicator(
                    value: controller.progress,
                    strokeWidth: 14.w,
                    backgroundColor: AppColors.mint,
                    color: AppColors.primary,
                    strokeCap: StrokeCap.round,
                  ),
                ),
                Padding(
                  padding: EdgeInsets.symmetric(horizontal: 28.w),
                  child: Column(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      FittedBox(
                        fit: BoxFit.scaleDown,
                        child: Text(
                          '${controller.count.value}',
                          style: AppTextStyles.heading1.copyWith(
                            fontSize: 56.sp,
                            color: AppColors.accent,
                          ),
                        ),
                      ),
                      Text(
                        '/ ${controller.target}',
                        style: AppTextStyles.heading3.copyWith(
                          color: AppColors.textSecondary,
                        ),
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),
        ),
        SizedBox(height: 24.h),
        Text(controller.dhikr, style: AppTextStyles.heading2),
        Text(controller.dhikrTranslation, style: AppTextStyles.bodySmall),
        const Spacer(),
        Row(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [
            _RoundIconButton(
              icon: Icons.remove_rounded,
              onTap: controller.decrement,
            ),
            GestureDetector(
              onTap: controller.increment,
              child: Container(
                width: 84.w,
                height: 84.w,
                decoration: BoxDecoration(
                  color: AppColors.primary,
                  shape: BoxShape.circle,
                  boxShadow: [
                    BoxShadow(
                      color: AppColors.primary.withValues(alpha: 0.3),
                      blurRadius: 16.r,
                      offset: Offset(0, 8.h),
                    ),
                  ],
                ),
                child: Icon(Icons.add_rounded, color: AppColors.white, size: 40.sp),
              ),
            ),
            _RoundIconButton(
              icon: Icons.restart_alt_rounded,
              onTap: controller.reset,
            ),
          ],
        ),
        SizedBox(height: 32.h),
      ],
    );
  }
}

class _RoundIconButton extends StatelessWidget {
  const _RoundIconButton({required this.icon, required this.onTap});

  final IconData icon;
  final VoidCallback onTap;

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: onTap,
      child: Container(
        width: 48.w,
        height: 48.w,
        decoration: BoxDecoration(
          color: AppColors.mint,
          shape: BoxShape.circle,
        ),
        child: Icon(icon, color: AppColors.primary, size: 22.sp),
      ),
    );
  }
}

class _DuasTab extends GetView<TasbihController> {
  const _DuasTab();

  @override
  Widget build(BuildContext context) {
    return Obx(() {
      if (controller.isContentLoading.value && controller.duas.isEmpty) {
        return const Center(
          child: CircularProgressIndicator(color: AppColors.primary),
        );
      }
      if (controller.contentError.value != null && controller.duas.isEmpty) {
        return Center(
          child: TextButton(
            onPressed: controller.loadContent,
            child: const Text('Retry'),
          ),
        );
      }
      if (controller.duas.isEmpty) {
        return Center(
          child: Text('No duas found.', style: AppTextStyles.body),
        );
      }

      final initialIndex = controller.duaRevealIndex.value.clamp(
        0,
        controller.duas.length - 1,
      );
      return ScrollablePositionedList.separated(
        initialScrollIndex: initialIndex,
        itemScrollController: controller.duaScrollController,
        padding: EdgeInsets.only(bottom: 20.h),
        itemCount: controller.duas.length,
        separatorBuilder: (_, _) => SizedBox(height: 12.h),
        itemBuilder: (context, index) {
          return _DuaCard(dua: controller.duas[index]);
        },
      );
    });
  }
}

class _DuaCard extends GetView<TasbihController> {
  const _DuaCard({required this.dua});

  final DuaItem dua;

  @override
  Widget build(BuildContext context) {
    final settings = Get.find<SettingsController>();
    return Obx(() {
      settings.isDarkMode.value;
      Get.find<StorageService>().selectedTranslationId.value;
      Get.find<BookmarkController>().items.length;
      controller.highlightDuaId.value;
      final lang = settings.translationLanguageCode;
      final highlighted = controller.highlightDuaId.value == dua.id;
      final title = dua.titleFor(lang);
      final translation = dua.translationFor(lang);
      final isRtl = lang == 'ur';
      return Container(
        width: double.infinity,
        padding: EdgeInsets.fromLTRB(16.w, 12.h, 8.w, 16.h),
        decoration: BoxDecoration(
          color: AppColors.surface,
          borderRadius: BorderRadius.circular(16.r),
          border: highlighted
              ? Border.all(color: AppColors.primary, width: 1.5)
              : null,
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Expanded(
                  child: Padding(
                    padding: EdgeInsets.only(top: 8.h),
                    child: Text(
                      title,
                      textDirection:
                          isRtl ? TextDirection.rtl : TextDirection.ltr,
                      style: (lang == 'en' || lang == 'id')
                          ? AppTextStyles.heading3
                          : settings.translationStyle(
                              color: AppColors.textPrimary,
                            ),
                    ),
                  ),
                ),
                BookmarkIconButton(
                  isBookmarked: controller.isDuaBookmarked(dua.id),
                  onPressed: () => controller.toggleDuaBookmark(dua, lang),
                ),
              ],
            ),
            Padding(
              padding: EdgeInsets.only(right: 8.w),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: [
                  SizedBox(height: 8.h),
                  Text(
                    dua.arabicText,
                    textAlign: TextAlign.right,
                    textDirection: TextDirection.rtl,
                    style: AppTextStyles.arabicTitle.copyWith(
                      color: AppColors.isDark
                          ? const Color(0xFF81C784)
                          : const Color(0xFF1B5E20),
                    ),
                  ),
                  SizedBox(height: 8.h),
                  Text(
                    translation,
                    textAlign: isRtl ? TextAlign.right : TextAlign.left,
                    textDirection:
                        isRtl ? TextDirection.rtl : TextDirection.ltr,
                    style: settings.translationStyle(
                      color: AppColors.isDark
                          ? Colors.grey[400]
                          : Colors.grey[800],
                    ),
                  ),
                ],
              ),
            ),
          ],
        ),
      );
    });
  }
}

class _AzkarTab extends GetView<TasbihController> {
  const _AzkarTab();

  @override
  Widget build(BuildContext context) {
    return Obx(() {
      if (controller.isContentLoading.value && controller.azkar.isEmpty) {
        return const Center(
          child: CircularProgressIndicator(color: AppColors.primary),
        );
      }
      if (controller.contentError.value != null && controller.azkar.isEmpty) {
        return Center(
          child: TextButton(
            onPressed: controller.loadContent,
            child: const Text('Retry'),
          ),
        );
      }
      if (controller.azkar.isEmpty) {
        return Center(
          child: Text('No azkar found.', style: AppTextStyles.body),
        );
      }

      return ListView.separated(
        padding: EdgeInsets.only(bottom: 20.h),
        itemCount: controller.azkar.length,
        separatorBuilder: (_, _) => SizedBox(height: 10.h),
        itemBuilder: (context, index) {
          final item = controller.azkar[index];
          return Container(
            width: double.infinity,
            padding: EdgeInsets.all(16.w),
            decoration: BoxDecoration(
              color: AppColors.surface,
              borderRadius: BorderRadius.circular(16.r),
            ),
            child: Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Container(
                  width: 32.w,
                  height: 32.w,
                  alignment: Alignment.center,
                  decoration: const BoxDecoration(
                    color: AppColors.primary,
                    shape: BoxShape.circle,
                  ),
                  child: Text(
                    '${index + 1}',
                    style: AppTextStyles.caption.copyWith(
                      color: AppColors.white,
                      fontWeight: FontWeight.w700,
                    ),
                  ),
                ),
                SizedBox(width: 12.w),
                Expanded(
                  child: Text(
                    item.arabic,
                    textAlign: TextAlign.right,
                    textDirection: TextDirection.rtl,
                    style: AppTextStyles.arabicTitle.copyWith(
                      color: AppColors.isDark
                          ? const Color(0xFF81C784)
                          : const Color(0xFF1B5E20),
                    ),
                  ),
                ),
              ],
            ),
          );
        },
      );
    });
  }
}
