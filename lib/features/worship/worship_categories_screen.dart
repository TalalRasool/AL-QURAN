import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:get/get.dart';

import '../../core/constants/app_colors.dart';
import '../../core/routes/app_routes.dart';
import '../../core/widgets/custom_app_bar.dart';
import 'worship_controller.dart';
import 'worship_guide_model.dart';
import 'worship_l10n.dart';

class WorshipCategoriesScreen extends GetView<WorshipController> {
  const WorshipCategoriesScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Obx(() {
      controller.watchAppearance();
      final lang = controller.languageCode;
      final direction = WorshipL10n.direction(lang);
      return Directionality(
        textDirection: direction,
        child: Scaffold(
          backgroundColor: AppColors.background,
          appBar: CustomAppBar(
            title: WorshipL10n.text(WorshipL10n.homeTitle, lang),
            titleStyle: controller.readingStyle(
              fontSize: 20.sp,
              fontWeight: FontWeight.w600,
            ),
          ),
          body: _buildBody(lang),
        ),
      );
    });
  }

  Widget _buildBody(String lang) {
    if (controller.isLoading.value && controller.guides.isEmpty) {
      return const Center(
        child: CircularProgressIndicator(color: AppColors.primary),
      );
    }

    if (controller.errorMessage.value != null && controller.guides.isEmpty) {
      return _MessageState(
        message: controller.errorMessage.value!,
        actionLabel: WorshipL10n.text(WorshipL10n.retry, lang),
        style: controller.readingStyle(),
        onAction: controller.loadWorshipData,
      );
    }

    final groups = controller.guidesByCategory;
    final categories = controller.categories
        .where((category) => (groups[category.id] ?? const []).isNotEmpty)
        .toList(growable: false);

    return RefreshIndicator(
      color: AppColors.primary,
      onRefresh: controller.loadWorshipData,
      child: CustomScrollView(
        physics: const AlwaysScrollableScrollPhysics(),
        slivers: [
          SliverToBoxAdapter(
            child: Padding(
              padding: EdgeInsets.fromLTRB(20.w, 4.h, 20.w, 16.h),
              child: Text(
                WorshipL10n.text(WorshipL10n.intro, lang),
                style: controller.readingStyle(color: AppColors.textSecondary),
              ),
            ),
          ),
          SliverPadding(
            padding: EdgeInsets.fromLTRB(20.w, 0, 20.w, 28.h),
            sliver: SliverGrid(
              gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
                crossAxisCount: 2,
                mainAxisSpacing: 14.h,
                crossAxisSpacing: 14.w,
                childAspectRatio: 0.92,
              ),
              delegate: SliverChildBuilderDelegate((context, index) {
                final category = categories[index];
                final count = groups[category.id]?.length ?? 0;
                return _CategoryCard(
                  category: category,
                  languageCode: lang,
                  count: count,
                  onTap: () => Get.toNamed(
                    AppRoutes.worshipDetail,
                    arguments: category.id,
                  ),
                );
              }, childCount: categories.length),
            ),
          ),
        ],
      ),
    );
  }
}

class _CategoryCard extends GetView<WorshipController> {
  const _CategoryCard({
    required this.category,
    required this.languageCode,
    required this.count,
    required this.onTap,
  });

  final WorshipCategory category;
  final String languageCode;
  final int count;
  final VoidCallback onTap;

  @override
  Widget build(BuildContext context) {
    final icon = _iconFor(category.id);
    final accent = _accentFor(category.id);
    final name = WorshipL10n.categoryName(
      category.id,
      languageCode,
      fallback: category.englishLabel,
    );

    return DecoratedBox(
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(20.r),
        boxShadow: [
          BoxShadow(
            color: AppColors.primary.withValues(alpha: 0.05),
            blurRadius: 16.r,
            offset: Offset(0, 6.h),
          ),
        ],
      ),
      child: Material(
        color: AppColors.surface,
        borderRadius: BorderRadius.circular(20.r),
        child: InkWell(
          onTap: onTap,
          borderRadius: BorderRadius.circular(20.r),
          child: Ink(
            decoration: BoxDecoration(
              borderRadius: BorderRadius.circular(20.r),
              border: Border.all(color: AppColors.divider),
            ),
            child: Padding(
              padding: EdgeInsets.fromLTRB(16.w, 16.h, 16.w, 14.h),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Container(
                    width: 52.w,
                    height: 52.w,
                    alignment: Alignment.center,
                    decoration: BoxDecoration(
                      color: accent.withValues(alpha: 0.12),
                      borderRadius: BorderRadius.circular(16.r),
                    ),
                    child: Icon(icon, color: accent, size: 26.sp),
                  ),
                  const Spacer(),
                  Text(
                    name,
                    style: controller.readingStyle(
                      fontWeight: FontWeight.w600,
                      fontSize: 16.sp,
                    ),
                    maxLines: 2,
                    overflow: TextOverflow.ellipsis,
                  ),
                  SizedBox(height: 4.h),
                  Text(
                    WorshipL10n.topicCount(languageCode, count),
                    style: controller.readingStyle(
                      color: AppColors.textSecondary,
                      fontSize: 12.sp,
                    ),
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                  ),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }

  IconData _iconFor(String id) {
    return switch (id) {
      'salah' => Icons.mosque_rounded,
      'purification' => Icons.water_drop_rounded,
      'hajj' => Icons.account_balance_rounded,
      'umrah' => Icons.explore_rounded,
      'zakat' => Icons.volunteer_activism_rounded,
      'fasting' => Icons.nights_stay_rounded,
      'funeral' => Icons.groups_rounded,
      'adhkar' => Icons.auto_stories_rounded,
      _ => Icons.menu_book_rounded,
    };
  }

  Color _accentFor(String id) {
    return switch (id) {
      'salah' => AppColors.primary,
      'purification' => const Color(0xFF1D6A8A),
      'hajj' => const Color(0xFF8A5A2B),
      'umrah' => const Color(0xFF2D6A4F),
      'zakat' => const Color(0xFF0F6E56),
      'fasting' => const Color(0xFF3D4F8A),
      'funeral' => const Color(0xFF5C4B6A),
      'adhkar' => AppColors.primaryLight,
      _ => AppColors.primary,
    };
  }
}

class _MessageState extends StatelessWidget {
  const _MessageState({
    required this.message,
    required this.actionLabel,
    required this.style,
    required this.onAction,
  });

  final String message;
  final String actionLabel;
  final TextStyle style;
  final VoidCallback onAction;

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Padding(
        padding: EdgeInsets.symmetric(horizontal: 24.w),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Text(message, style: style, textAlign: TextAlign.center),
            SizedBox(height: 12.h),
            TextButton(
              onPressed: onAction,
              child: Text(actionLabel, style: style),
            ),
          ],
        ),
      ),
    );
  }
}
