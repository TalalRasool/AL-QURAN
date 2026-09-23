import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:get/get.dart';

import '../../core/constants/app_colors.dart';
import '../../core/constants/app_text_styles.dart';
import '../../core/controllers/settings_controller.dart';
import '../../core/data/offline_translations.dart';
import '../../core/services/storage_service.dart';

class ReadingSettingsSheet extends GetView<SettingsController> {
  const ReadingSettingsSheet({super.key});

  static Future<void> open() {
    return Get.bottomSheet(
      const ReadingSettingsSheet(),
      isScrollControlled: true,
      backgroundColor: Colors.transparent,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.vertical(top: Radius.circular(24.r)),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Obx(() {
      controller.isDarkMode.value;
      return Material(
        color: AppColors.surface,
        borderRadius: BorderRadius.vertical(top: Radius.circular(24.r)),
        clipBehavior: Clip.antiAlias,
        child: SafeArea(
          top: false,
          child: Padding(
            padding: EdgeInsets.fromLTRB(20.w, 12.h, 20.w, 20.h),
            child: SingleChildScrollView(
              child: Column(
              mainAxisSize: MainAxisSize.min,
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
              Center(
                child: Container(
                  width: 40.w,
                  height: 4.h,
                  decoration: BoxDecoration(
                    color: AppColors.greyLight,
                    borderRadius: BorderRadius.circular(4.r),
                  ),
                ),
              ),
              SizedBox(height: 16.h),
              Row(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text('Reading Settings', style: AppTextStyles.heading2),
                        SizedBox(height: 6.h),
                        Text(
                          'Adjust text and appearance while you read.',
                          style: AppTextStyles.bodySmall,
                        ),
                      ],
                    ),
                  ),
                  IconButton(
                    onPressed: Get.back,
                    tooltip: 'Close',
                    icon: Icon(
                      Icons.close_rounded,
                      size: 22.sp,
                      color: AppColors.textPrimary,
                    ),
                  ),
                ],
              ),
              SizedBox(height: 20.h),
              _PreviewCard(settings: controller),
              SizedBox(height: 20.h),
              _SizeSection(
                label: 'Arabic text size',
                value: controller.arabicTextSize.value,
                min: 20,
                max: 40,
                onChanged: controller.setArabicTextSize,
              ),
              SizedBox(height: 8.h),
              _SizeSection(
                label: 'Translation text size',
                value: controller.translationTextSize.value,
                min: 12,
                max: 24,
                onChanged: controller.setTranslationTextSize,
              ),
              SizedBox(height: 16.h),
              Text('Font Style', style: AppTextStyles.heading3),
              SizedBox(height: 10.h),
              _ChoiceRow(
                options: const [
                  SettingsController.uthmaniFont,
                  SettingsController.indoPakFont,
                ],
                selected: controller.arabicFont.value,
                onSelected: controller.setArabicFont,
              ),
              SizedBox(height: 16.h),
              Text('Translation', style: AppTextStyles.heading3),
              SizedBox(height: 10.h),
              _ChoiceRow(
                options: [
                  for (final edition in controller.translationEditions)
                    edition.identifier,
                ],
                labels: {
                  for (final edition in controller.translationEditions)
                    edition.identifier: edition.languageLabel,
                },
                selected: OfflineTranslations.canonicalId(
                  Get.find<StorageService>().selectedTranslationId.value,
                ),
                onSelected: (id) => controller.applyTranslation(
                  OfflineTranslations.editionFor(id),
                ),
              ),
              SizedBox(height: 16.h),
              Text('Theme', style: AppTextStyles.heading3),
              SizedBox(height: 10.h),
              _ChoiceRow(
                options: const [
                  SettingsController.themeLight,
                  SettingsController.themeDark,
                  SettingsController.themeSystem,
                ],
                labels: const {
                  SettingsController.themeLight: 'Light',
                  SettingsController.themeDark: 'Dark',
                  SettingsController.themeSystem: 'System',
                },
                selected: controller.themeModeName.value,
                onSelected: controller.setThemeModeName,
              ),
            ],
            ),
            ),
          ),
        ),
      );
    });
  }
}

class _PreviewCard extends StatelessWidget {
  const _PreviewCard({required this.settings});

  final SettingsController settings;

  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,
      padding: EdgeInsets.all(16.w),
      decoration: BoxDecoration(
        color: AppColors.mint,
        borderRadius: BorderRadius.circular(16.r),
      ),
      child: Column(
        children: [
          Text(
            'بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ',
            textAlign: TextAlign.center,
            textDirection: TextDirection.rtl,
            style: settings.arabicStyle(
              color: AppColors.isDark ? Colors.white : AppColors.primary,
              height: 1.8,
            ),
          ),
          SizedBox(height: 8.h),
          Text(
            'In the name of God, The Most Gracious, The Dispenser of Grace.',
            textAlign: TextAlign.center,
            style: settings.translationStyle(color: AppColors.textSecondary),
          ),
        ],
      ),
    );
  }
}

class _SizeSection extends StatelessWidget {
  const _SizeSection({
    required this.label,
    required this.value,
    required this.min,
    required this.max,
    required this.onChanged,
  });

  final String label;
  final double value;
  final double min;
  final double max;
  final ValueChanged<double> onChanged;

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Row(
          children: [
            Expanded(child: Text(label, style: AppTextStyles.heading3)),
            Text(
              value.round().toString(),
              style: AppTextStyles.bodySmall.copyWith(
                color: AppColors.primaryLight,
                fontWeight: FontWeight.w600,
              ),
            ),
          ],
        ),
        SliderTheme(
          data: SliderTheme.of(context).copyWith(
            activeTrackColor: AppColors.primary,
            inactiveTrackColor: AppColors.mint,
            thumbColor: AppColors.primary,
            overlayColor: AppColors.primary.withValues(alpha: 0.12),
            trackHeight: 4.h,
          ),
          child: Slider(
            value: value.clamp(min, max),
            min: min,
            max: max,
            onChanged: onChanged,
          ),
        ),
      ],
    );
  }
}

class _ChoiceRow extends StatelessWidget {
  const _ChoiceRow({
    required this.options,
    required this.selected,
    required this.onSelected,
    this.labels,
  });

  final List<String> options;
  final String selected;
  final ValueChanged<String> onSelected;
  final Map<String, String>? labels;

  @override
  Widget build(BuildContext context) {
    if (options.length > 3) {
      return Wrap(
        spacing: 8.w,
        runSpacing: 8.h,
        children: [
          for (final option in options) _chip(option, expand: false),
        ],
      );
    }

    return Row(
      children: [
        for (var i = 0; i < options.length; i++) ...[
          if (i > 0) SizedBox(width: 8.w),
          Expanded(child: _chip(options[i], expand: true)),
        ],
      ],
    );
  }

  Widget _chip(String option, {required bool expand}) {
    final isSelected = selected == option;
    final isDark = AppColors.isDark;
    final unselectedFill =
        isDark ? const Color(0xFF2C4538) : AppColors.mint;
    final unselectedText =
        isDark ? const Color(0xFFDCE8E1) : AppColors.primary;
    return GestureDetector(
      onTap: () => onSelected(option),
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 180),
        width: expand ? double.infinity : null,
        padding: EdgeInsets.symmetric(
          vertical: 10.h,
          horizontal: expand ? 0 : 14.w,
        ),
        decoration: BoxDecoration(
          color: isSelected ? AppColors.primary : unselectedFill,
          borderRadius: BorderRadius.circular(14.r),
          border: isSelected
              ? null
              : Border.all(
                  color: isDark
                      ? const Color(0xFF5A8A70)
                      : AppColors.primary.withValues(alpha: 0.12),
                ),
        ),
        alignment: Alignment.center,
        child: Text(
          labels?[option] ?? option,
          maxLines: 1,
          overflow: TextOverflow.ellipsis,
          style: AppTextStyles.bodySmall.copyWith(
            color: isSelected ? AppColors.white : unselectedText,
            fontWeight: FontWeight.w600,
          ),
        ),
      ),
    );
  }
}
