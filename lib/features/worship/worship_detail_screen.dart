import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:get/get.dart';

import '../../core/constants/app_colors.dart';
import '../../core/constants/app_text_styles.dart';
import '../../core/widgets/custom_app_bar.dart';
import 'worship_controller.dart';
import 'worship_guide_model.dart';
import 'worship_l10n.dart';

class WorshipDetailScreen extends GetView<WorshipController> {
  const WorshipDetailScreen({super.key});

  String get _categoryId {
    final args = Get.arguments;
    if (args is String) return args;
    if (args is Map && args['category'] is String) {
      return args['category'] as String;
    }
    return '';
  }

  @override
  Widget build(BuildContext context) {
    return Obx(() {
      controller.watchAppearance();
      final lang = controller.languageCode;
      final direction = WorshipL10n.direction(lang);
      final title = controller.categoryLabel(_categoryId);

      return Directionality(
        textDirection: direction,
        child: Scaffold(
          backgroundColor: AppColors.background,
          appBar: CustomAppBar(
            title: title,
            titleStyle: controller.readingStyle(
              fontSize: 20.sp,
              fontWeight: FontWeight.w600,
            ),
          ),
          body: _buildBody(lang, direction),
        ),
      );
    });
  }

  Widget _buildBody(String lang, TextDirection direction) {
    if (controller.isLoading.value && controller.guides.isEmpty) {
      return const Center(
        child: CircularProgressIndicator(color: AppColors.primary),
      );
    }

    if (controller.errorMessage.value != null && controller.guides.isEmpty) {
      return Center(
        child: Padding(
          padding: EdgeInsets.symmetric(horizontal: 24.w),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              Text(
                controller.errorMessage.value!,
                style: controller.readingStyle(),
                textAlign: TextAlign.center,
              ),
              SizedBox(height: 12.h),
              TextButton(
                onPressed: controller.loadWorshipData,
                child: Text(
                  WorshipL10n.text(WorshipL10n.retry, lang),
                  style: controller.readingStyle(),
                ),
              ),
            ],
          ),
        ),
      );
    }

    final items = controller.guidesForCategory(_categoryId);
    if (items.isEmpty) {
      return Center(
        child: Padding(
          padding: EdgeInsets.symmetric(horizontal: 24.w),
          child: Text(
            WorshipL10n.text(WorshipL10n.emptyCategory, lang),
            style: controller.readingStyle(),
            textAlign: TextAlign.center,
          ),
        ),
      );
    }

    return RefreshIndicator(
      color: AppColors.primary,
      onRefresh: controller.loadWorshipData,
      child: ListView.separated(
        physics: const AlwaysScrollableScrollPhysics(),
        padding: EdgeInsets.fromLTRB(20.w, 8.h, 20.w, 32.h),
        itemCount: items.length + 1,
        separatorBuilder: (_, index) {
          final beforeDisclaimer = index == items.length - 1;
          return SizedBox(height: beforeDisclaimer ? 18.h : 14.h);
        },
        itemBuilder: (context, index) {
          if (index == items.length) {
            return Text(
              WorshipL10n.text(WorshipL10n.disclaimer, lang),
              style: controller.readingStyle(
                color: AppColors.textSecondary,
                fontSize: 12.sp,
              ),
            );
          }
          return _GuideArticle(
            guide: items[index],
            languageCode: lang,
            direction: direction,
          );
        },
      ),
    );
  }
}

class _GuideArticle extends GetView<WorshipController> {
  const _GuideArticle({
    required this.guide,
    required this.languageCode,
    required this.direction,
  });

  final WorshipGuideItem guide;
  final String languageCode;
  final TextDirection direction;

  @override
  Widget build(BuildContext context) {
    final title = guide.titleFor(languageCode);
    final summary = guide.summaryFor(languageCode);
    final steps = guide.stepsFor(languageCode);
    final problems = guide.problemsFor(languageCode);

    return Container(
      width: double.infinity,
      padding: EdgeInsets.fromLTRB(18.w, 18.h, 18.w, 18.h),
      decoration: BoxDecoration(
        color: AppColors.surface,
        borderRadius: BorderRadius.circular(20.r),
        border: Border.all(color: AppColors.divider),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          if (title.isNotEmpty)
            Text(
              title,
              textDirection: direction,
              style: controller.readingStyle(
                fontSize: 18.sp,
                fontWeight: FontWeight.w700,
              ),
            ),
          if (summary.isNotEmpty) ...[
            SizedBox(height: 12.h),
            _SectionLabel(WorshipL10n.text(WorshipL10n.summary, languageCode)),
            SizedBox(height: 6.h),
            Text(
              summary,
              textDirection: direction,
              style: controller.readingStyle(),
            ),
          ],
          if (steps.isNotEmpty) ...[
            SizedBox(height: 16.h),
            _SectionLabel(WorshipL10n.text(WorshipL10n.steps, languageCode)),
            SizedBox(height: 8.h),
            for (var i = 0; i < steps.length; i++) ...[
              if (i > 0) SizedBox(height: 10.h),
              _NumberedLine(
                number: '${i + 1}',
                text: steps[i],
                direction: direction,
              ),
            ],
          ],
          if (problems.isNotEmpty) ...[
            SizedBox(height: 16.h),
            _SectionLabel(WorshipL10n.text(WorshipL10n.problems, languageCode)),
            SizedBox(height: 8.h),
            for (var i = 0; i < problems.length; i++) ...[
              if (i > 0) SizedBox(height: 8.h),
              _NoteLine(text: problems[i], direction: direction),
            ],
          ],
          if (guide.references.isNotEmpty) ...[
            SizedBox(height: 16.h),
            _SectionLabel(
              WorshipL10n.text(WorshipL10n.references, languageCode),
            ),
            SizedBox(height: 8.h),
            for (final citation in guide.references) ...[
              Padding(
                padding: EdgeInsets.only(bottom: 4.h),
                child: Text(
                  citation,
                  textDirection: TextDirection.ltr,
                  style: AppTextStyles.bodySmall.copyWith(
                    color: AppColors.textSecondary,
                  ),
                ),
              ),
            ],
          ],
        ],
      ),
    );
  }
}

class _SectionLabel extends GetView<WorshipController> {
  const _SectionLabel(this.label);

  final String label;

  @override
  Widget build(BuildContext context) {
    return Text(
      label,
      style: controller.readingStyle(
        fontWeight: FontWeight.w600,
        color: AppColors.primaryLight,
        fontSize: 13.sp,
      ),
    );
  }
}

class _NumberedLine extends GetView<WorshipController> {
  const _NumberedLine({
    required this.number,
    required this.text,
    required this.direction,
  });

  final String number;
  final String text;
  final TextDirection direction;

  @override
  Widget build(BuildContext context) {
    return Row(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Container(
          width: 24.w,
          height: 24.w,
          alignment: Alignment.center,
          decoration: BoxDecoration(
            color: AppColors.mint,
            shape: BoxShape.circle,
          ),
          child: Text(
            number,
            style: AppTextStyles.caption.copyWith(
              color: AppColors.onMint,
              fontWeight: FontWeight.w700,
            ),
          ),
        ),
        SizedBox(width: 10.w),
        Expanded(
          child: Padding(
            padding: EdgeInsets.only(top: 2.h),
            child: Text(
              text,
              textDirection: direction,
              style: controller.readingStyle(),
            ),
          ),
        ),
      ],
    );
  }
}

class _NoteLine extends GetView<WorshipController> {
  const _NoteLine({required this.text, required this.direction});

  final String text;
  final TextDirection direction;

  @override
  Widget build(BuildContext context) {
    return Row(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Padding(
          padding: EdgeInsets.only(top: 3.h),
          child: Icon(
            Icons.info_outline_rounded,
            size: 16.sp,
            color: AppColors.primarySoft,
          ),
        ),
        SizedBox(width: 8.w),
        Expanded(
          child: Text(
            text,
            textDirection: direction,
            style: controller.readingStyle(color: AppColors.textSecondary),
          ),
        ),
      ],
    );
  }
}
