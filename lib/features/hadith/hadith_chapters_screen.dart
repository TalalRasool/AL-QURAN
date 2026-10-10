import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:get/get.dart';

import '../../core/constants/app_colors.dart';
import '../../core/constants/app_text_styles.dart';
import '../../core/controllers/settings_controller.dart';
import '../../core/widgets/widgets.dart';
import 'data/hadith_l10n.dart';
import 'data/hadith_models.dart';
import 'hadith_chapters_controller.dart';
import 'hadith_script_style.dart';

class HadithChaptersScreen extends GetView<HadithChaptersController> {
  const HadithChaptersScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Obx(() {
      Get.find<SettingsController>().isDarkMode.value;
      final lang = HadithL10n.watchLanguage();
      final isRtl = HadithL10n.isRtl(lang);
      return Directionality(
        textDirection: isRtl ? TextDirection.rtl : TextDirection.ltr,
        child: Scaffold(
          backgroundColor: AppColors.background,
          appBar: CustomAppBar(
            title: controller.bookName,
            titleMaxLines: 2,
            titleStyle: hadithLanguageStyle(
              lang,
              fontSize: 20.sp,
              fontWeight: FontWeight.w600,
              color: AppColors.textPrimary,
              height: 1.3,
            ),
          ),
          body: Column(
            children: [
              if (controller.errorMessage.value == null)
                Padding(
                  padding: EdgeInsets.fromLTRB(20.w, 8.h, 20.w, 4.h),
                  child: CustomTextField(
                    hintText: HadithL10n.ui('search_chapters', lang),
                    onChanged: controller.onSearch,
                    style: hadithLanguageStyle(
                      lang,
                      fontSize: 14.sp,
                      color: AppColors.textPrimary,
                      height: 1.5,
                    ),
                  ),
                ),
              Expanded(child: _buildBody(lang, isRtl)),
            ],
          ),
        ),
      );
    });
  }

  Widget _buildBody(String lang, bool isRtl) {
    if (controller.isLoading.value && controller.chapters.isEmpty) {
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

    if (controller.chapters.isEmpty) {
      return Center(
        child: Text(
          controller.searchQuery.value.trim().isEmpty
              ? HadithL10n.ui('no_chapters', lang)
              : HadithL10n.ui('no_match_chapters', lang),
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

    final chapters = controller.chapters;
    return ListView.separated(
      padding: EdgeInsets.fromLTRB(20.w, 8.h, 20.w, 20.h),
      itemCount: chapters.length,
      separatorBuilder: (_, _) => SizedBox(height: 10.h),
      itemBuilder: (context, index) {
        final chapter = chapters[index];
        return _HadithChapterTile(
          chapter: chapter,
          languageCode: lang,
          isRtl: isRtl,
          onTap: () => controller.openChapter(chapter),
        );
      },
    );
  }
}

class _HadithChapterTile extends StatelessWidget {
  const _HadithChapterTile({
    required this.chapter,
    required this.languageCode,
    required this.isRtl,
    required this.onTap,
  });

  final HadithChapter chapter;
  final String languageCode;
  final bool isRtl;
  final VoidCallback onTap;

  @override
  Widget build(BuildContext context) {
    final name = HadithL10n.chapterName(
      chapter.name,
      languageCode: languageCode,
      number: chapter.number,
    );
    final label = HadithL10n.chapterLabel(
      chapter.number,
      languageCode: languageCode,
    );
    final number = chapter.number == 0 ? 1 : chapter.number;

    return Material(
      color: AppColors.surface,
      borderRadius: BorderRadius.circular(16.r),
      child: InkWell(
        onTap: onTap,
        borderRadius: BorderRadius.circular(16.r),
        child: Container(
          padding: EdgeInsets.symmetric(horizontal: 14.w, vertical: 12.h),
          decoration: BoxDecoration(
            borderRadius: BorderRadius.circular(16.r),
            boxShadow: [
              BoxShadow(
                color: AppColors.primary.withValues(alpha: 0.04),
                blurRadius: 12.r,
                offset: Offset(0, 4.h),
              ),
            ],
          ),
          child: Row(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Container(
                width: 44.w,
                height: 44.w,
                alignment: Alignment.center,
                decoration: BoxDecoration(
                  shape: BoxShape.circle,
                  color: AppColors.greyLight,
                ),
                child: Text(
                  '$number',
                  style: AppTextStyles.heading3.copyWith(fontSize: 14.sp),
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
                      name,
                      style: hadithLanguageStyle(
                        languageCode,
                        fontSize: 16.sp,
                        fontWeight: FontWeight.w600,
                        color: AppColors.textPrimary,
                        height: 1.35,
                      ),
                      textDirection:
                          isRtl ? TextDirection.rtl : TextDirection.ltr,
                    ),
                    SizedBox(height: 4.h),
                    Text(
                      label,
                      style: hadithLanguageStyle(
                        languageCode,
                        fontSize: 12.sp,
                        color: AppColors.textSecondary,
                        height: 1.4,
                      ),
                      textDirection:
                          isRtl ? TextDirection.rtl : TextDirection.ltr,
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
