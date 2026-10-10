import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:get/get.dart';

import '../../core/constants/app_colors.dart';
import '../../core/constants/app_text_styles.dart';
import '../../core/controllers/settings_controller.dart';
import '../../core/controllers/bookmark_controller.dart';
import '../../core/widgets/widgets.dart';
import 'data/hadith_l10n.dart';
import 'data/hadith_models.dart';
import 'hadith_read_controller.dart';
import 'hadith_script_style.dart';

class HadithReadScreen extends GetView<HadithReadController> {
  const HadithReadScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Obx(() {
      Get.find<SettingsController>().isDarkMode.value;
      Get.find<SettingsController>().arabicTextSize.value;
      Get.find<SettingsController>().translationTextSize.value;
      controller.activeTranslationKey;
      final lang = HadithL10n.watchLanguage();
      final isRtl = HadithL10n.isRtl(lang);
      final titleStyle = hadithLanguageStyle(
        lang,
        fontSize: 20.sp,
        fontWeight: FontWeight.w600,
        color: AppColors.textPrimary,
        height: 1.3,
      );
      return Directionality(
        textDirection: isRtl ? TextDirection.rtl : TextDirection.ltr,
        child: Scaffold(
          backgroundColor: AppColors.background,
          appBar: CustomAppBar(
            title: controller.bookName,
            titleMaxLines: 2,
            titleStyle: titleStyle,
          ),
          body: Column(
            children: [
              if (controller.errorMessage.value == null) ...[
                Padding(
                  padding: EdgeInsets.fromLTRB(20.w, 10.h, 20.w, 0),
                  child: Align(
                    alignment:
                        isRtl ? Alignment.centerRight : Alignment.centerLeft,
                    child: Text(
                      controller.chapterName,
                      style: hadithLanguageStyle(
                        lang,
                        fontSize: 16.sp,
                        fontWeight: FontWeight.w600,
                        color: AppColors.textPrimary,
                        height: 1.35,
                      ),
                      textAlign: isRtl ? TextAlign.right : TextAlign.left,
                      textDirection:
                          isRtl ? TextDirection.rtl : TextDirection.ltr,
                    ),
                  ),
                ),
                Padding(
                  padding: EdgeInsets.fromLTRB(20.w, 8.h, 20.w, 4.h),
                  child: CustomTextField(
                    hintText: HadithL10n.ui('search_ahadith', lang),
                    onChanged: controller.onSearch,
                    style: hadithLanguageStyle(
                      lang,
                      fontSize: 14.sp,
                      color: AppColors.textPrimary,
                      height: 1.5,
                    ),
                  ),
                ),
              ],
              Expanded(child: _buildBody(lang)),
            ],
          ),
        ),
      );
    });
  }

  Widget _buildBody(String lang) {
    if (controller.isLoading.value && controller.ahadith.isEmpty) {
      return const Center(
        child: CircularProgressIndicator(color: AppColors.primary),
      );
    }

    if (controller.errorMessage.value != null) {
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
                child: Text(
                  HadithL10n.ui('retry', lang),
                  style: hadithLanguageStyle(
                    lang,
                    fontSize: 14.sp,
                    fontWeight: FontWeight.w600,
                    color: AppColors.primary,
                  ),
                ),
              ),
            ],
          ),
        ),
      );
    }

    if (controller.ahadith.isEmpty) {
      return Center(
        child: Text(
          controller.searchQuery.value.trim().isEmpty
              ? HadithL10n.ui('no_ahadith', lang)
              : HadithL10n.ui('no_match_ahadith', lang),
          style: hadithLanguageStyle(
            lang,
            fontSize: 14.sp,
            color: AppColors.textPrimary,
            height: 1.5,
          ),
          textAlign: TextAlign.center,
        ),
      );
    }

    final items = controller.ahadith;
    final extra = controller.isLoadingMore.value ? 1 : 0;
    return ListView.separated(
      controller: controller.scrollController,
      padding: EdgeInsets.fromLTRB(20.w, 8.h, 20.w, 24.h),
      itemCount: items.length + extra,
      separatorBuilder: (_, _) => SizedBox(height: 12.h),
      itemBuilder: (context, index) {
        if (index >= items.length) {
          return Padding(
            padding: EdgeInsets.symmetric(vertical: 12.h),
            child: const Center(
              child: CircularProgressIndicator(color: AppColors.primary),
            ),
          );
        }
        return _HadithCard(hadith: items[index], languageCode: lang);
      },
    );
  }
}

class _HadithCard extends GetView<HadithReadController> {
  const _HadithCard({required this.hadith, required this.languageCode});

  final Hadith hadith;
  final String languageCode;

  @override
  Widget build(BuildContext context) {
    final settings = Get.find<SettingsController>();
    final translation = controller.translationOf(hadith);
    final translationLanguage = controller.translationLanguageOf(hadith);
    final isRtl = controller.translationIsRtl(hadith);
    final arabicColor =
        AppColors.isDark ? const Color(0xFF81C784) : const Color(0xFF1B5E20);
    final translationColor =
        AppColors.isDark ? Colors.grey[400] : Colors.grey[800];

    return Container(
      padding: EdgeInsets.fromLTRB(16.w, 8.h, 8.w, 16.h),
      decoration: BoxDecoration(
        color: AppColors.surface,
        borderRadius: BorderRadius.circular(16.r),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          Row(
            children: [
              Container(
                padding: EdgeInsets.symmetric(horizontal: 12.w, vertical: 5.h),
                decoration: BoxDecoration(
                  color: AppColors.primary,
                  borderRadius: BorderRadius.circular(20.r),
                ),
                child: Text(
                  HadithL10n.hadithNumberLabel(
                    hadith.numberLabel,
                    languageCode: languageCode,
                  ),
                  style: hadithLanguageStyle(
                    languageCode,
                    fontSize: 11.sp,
                    fontWeight: FontWeight.w700,
                    color: AppColors.white,
                    height: 1.3,
                  ),
                ),
              ),
              const Spacer(),
              Obx(() {
                controller.bookmarks.length;
                return BookmarkIconButton(
                  isBookmarked: Get.find<BookmarkController>().isHadithBookmarked(
                    hadith.id,
                  ),
                  onPressed: () => controller.toggleBookmark(hadith),
                );
              }),
            ],
          ),
          Padding(
            padding: EdgeInsetsDirectional.only(end: 8.w),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                if (hadith.textAr.trim().isNotEmpty) ...[
                  SizedBox(height: 8.h),
                  Text(
                    hadith.textAr,
                    textAlign: TextAlign.right,
                    textDirection: TextDirection.rtl,
                    style: settings.arabicStyle(color: arabicColor),
                  ),
                ],
                if (translation.trim().isNotEmpty) ...[
                  SizedBox(height: 12.h),
                  Text(
                    translation,
                    textAlign: isRtl ? TextAlign.right : TextAlign.left,
                    textDirection:
                        isRtl ? TextDirection.rtl : TextDirection.ltr,
                    style: settings.translationStyle(
                      color: translationColor,
                      languageCode: translationLanguage,
                    ),
                  ),
                ],
              ],
            ),
          ),
        ],
      ),
    );
  }
}
