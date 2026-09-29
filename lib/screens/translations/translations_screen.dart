import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:get/get.dart';

import '../../core/constants/app_colors.dart';
import '../../core/constants/app_text_styles.dart';
import '../../core/controllers/settings_controller.dart';
import '../../core/widgets/widgets.dart';
import 'translations_controller.dart';

class TranslationsScreen extends GetView<TranslationsController> {
  const TranslationsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Obx(() {
      Get.find<SettingsController>().isDarkMode.value;
      return Scaffold(
      backgroundColor: AppColors.background,
      appBar: const CustomAppBar(title: 'Translations'),
      body: Padding(
        padding: EdgeInsets.symmetric(horizontal: 20.w),
        child: Column(
          children: [
            CustomTextField(
              hintText: 'Search language or author',
              onChanged: controller.onSearch,
            ),
            SizedBox(height: 16.h),
            Expanded(
              child: Obx(() {
                if (controller.isLoading.value) {
                  return const Center(
                    child: CircularProgressIndicator(color: AppColors.primary),
                  );
                }

                if (controller.errorMessage.value != null) {
                  return Center(
                    child: Padding(
                      padding: EdgeInsets.symmetric(horizontal: 12.w),
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
                            onPressed: controller.loadEditions,
                            child: const Text('Retry'),
                          ),
                        ],
                      ),
                    ),
                  );
                }

                final selectedId = controller.selectedId;
                final editions = controller.filteredEditions;
                if (editions.isEmpty) {
                  return Center(
                    child: Text(
                      'No translations found',
                      style: AppTextStyles.body,
                    ),
                  );
                }

                return ListView.separated(
                  padding: EdgeInsets.only(bottom: 24.h),
                  itemCount: editions.length,
                  separatorBuilder: (_, _) => SizedBox(height: 10.h),
                  itemBuilder: (context, index) {
                    final edition = editions[index];
                    final isSelected = edition.identifier == selectedId;
                    return _TranslationTile(
                      language: edition.languageLabel,
                      author: edition.authorName,
                      isSelected: isSelected,
                      onTap: () => controller.selectTranslation(edition),
                    );
                  },
                );
              }),
            ),
          ],
        ),
      ),
      );
    });
  }
}

class _TranslationTile extends StatelessWidget {
  const _TranslationTile({
    required this.language,
    required this.author,
    required this.isSelected,
    required this.onTap,
  });

  final String language;
  final String author;
  final bool isSelected;
  final VoidCallback onTap;

  @override
  Widget build(BuildContext context) {
    return Material(
      color: isSelected ? AppColors.mint : AppColors.surface,
      borderRadius: BorderRadius.circular(16.r),
      child: InkWell(
        onTap: onTap,
        borderRadius: BorderRadius.circular(16.r),
        child: Padding(
          padding: EdgeInsets.symmetric(horizontal: 16.w, vertical: 14.h),
          child: Row(
            children: [
              Container(
                width: 44.w,
                height: 44.w,
                alignment: Alignment.center,
                decoration: BoxDecoration(
                  color: isSelected ? AppColors.surface : AppColors.mint,
                  shape: BoxShape.circle,
                ),
                child: Text(
                  language.length >= 2
                      ? language.substring(0, 2).toUpperCase()
                      : language.toUpperCase(),
                  style: AppTextStyles.caption.copyWith(
                    color: AppColors.onMint,
                    fontWeight: FontWeight.w700,
                  ),
                ),
              ),
              SizedBox(width: 12.w),
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      language,
                      style: AppTextStyles.heading3,
                      maxLines: 1,
                      overflow: TextOverflow.ellipsis,
                    ),
                    Text(
                      author,
                      style: AppTextStyles.bodySmall,
                      maxLines: 1,
                      overflow: TextOverflow.ellipsis,
                    ),
                  ],
                ),
              ),
              Icon(
                isSelected
                    ? Icons.check_circle_rounded
                    : Icons.chevron_right_rounded,
                size: 22.sp,
                color: isSelected
                    ? AppColors.accent
                    : AppColors.textSecondary,
              ),
            ],
          ),
        ),
      ),
    );
  }
}
