import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:flutter_svg/flutter_svg.dart';
import 'package:get/get.dart';

import '../../core/constants/app_assets.dart';
import '../../core/constants/app_colors.dart';
import '../../core/constants/app_text_styles.dart';
import '../../core/controllers/settings_controller.dart';
import '../../core/widgets/widgets.dart';
import 'home_controller.dart';

class HomeScreen extends GetView<HomeController> {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Obx(() {
      Get.find<SettingsController>().isDarkMode.value;
      return SafeArea(
        bottom: false,
        child: SingleChildScrollView(
          padding: EdgeInsets.fromLTRB(20.w, 8.h, 20.w, 24.h),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              _HomeEntrance(
                delay: Duration.zero,
                child: _HomeHeader(),
              ),
              SizedBox(height: 16.h),
              _HomeEntrance(
                delay: const Duration(milliseconds: 50),
                child: _IslamicDateCard(),
              ),
              SizedBox(height: 20.h),
              _HomeEntrance(
                delay: const Duration(milliseconds: 90),
                child: _ContinueReadingCard(),
              ),
              SizedBox(height: 24.h),
              _HomeEntrance(
                delay: const Duration(milliseconds: 180),
                child: _ShortcutsSection(),
              ),
              SizedBox(height: 24.h),
              _HomeEntrance(
                delay: const Duration(milliseconds: 270),
                child: _DailyVerseCard(),
              ),
            ],
          ),
        ),
      );
    });
  }
}

class _HomeEntrance extends StatefulWidget {
  const _HomeEntrance({
    required this.child,
    required this.delay,
  });

  final Widget child;
  final Duration delay;

  @override
  State<_HomeEntrance> createState() => _HomeEntranceState();
}

class _HomeEntranceState extends State<_HomeEntrance>
    with SingleTickerProviderStateMixin {
  late final AnimationController _controller;
  late final Animation<double> _fade;
  late final Animation<Offset> _slide;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 500),
    );
    final curve = CurvedAnimation(
      parent: _controller,
      curve: Curves.easeOutCubic,
    );
    _fade = curve;
    _slide = Tween<Offset>(
      begin: const Offset(0, 0.08),
      end: Offset.zero,
    ).animate(curve);
    Future<void>.delayed(widget.delay, () {
      if (mounted) _controller.forward();
    });
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return FadeTransition(
      opacity: _fade,
      child: SlideTransition(
        position: _slide,
        child: widget.child,
      ),
    );
  }
}

class _HomeHeader extends GetView<HomeController> {
  const _HomeHeader();

  @override
  Widget build(BuildContext context) {
    return Row(
      children: [
        SizedBox(
          width: 48.w,
          height: 48.w,
          child: ClipOval(
            child: Image.asset(
              AppAssets.avatarPlaceholder,
              fit: BoxFit.cover,
            ),
          ),
        ),
        SizedBox(width: 12.w),
        Expanded(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                'Assalamu Alaikum',
                style: AppTextStyles.bodySmall,
                maxLines: 1,
                overflow: TextOverflow.ellipsis,
              ),
              Obx(
                () => Text(
                  controller.userName,
                  style: AppTextStyles.heading2,
                  maxLines: 1,
                  overflow: TextOverflow.ellipsis,
                ),
              ),
            ],
          ),
        ),
        _HeaderIconButton(
          asset: AppAssets.notificationIcon,
          onTap: controller.onNotificationTap,
        ),
        SizedBox(width: 8.w),
        _HeaderIconButton(
          asset: AppAssets.settingsIcon,
          onTap: controller.openProfile,
        ),
      ],
    );
  }
}

class _IslamicDateCard extends GetView<HomeController> {
  const _IslamicDateCard();

  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,
      padding: EdgeInsets.fromLTRB(16.w, 16.h, 16.w, 16.h),
      decoration: BoxDecoration(
        color: AppColors.surface,
        borderRadius: BorderRadius.circular(18.r),
        border: Border.all(color: AppColors.divider),
      ),
      child: Row(
        children: [
          Container(
            width: 48.w,
            height: 48.w,
            decoration: BoxDecoration(
              color: AppColors.mint,
              shape: BoxShape.circle,
            ),
            child: Icon(
              Icons.nights_stay_rounded,
              color: AppColors.isDark ? Colors.white : AppColors.primary,
              size: 24.sp,
            ),
          ),
          SizedBox(width: 12.w),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  'Islamic Date',
                  style: AppTextStyles.bodySmall.copyWith(
                    color: AppColors.primaryLight,
                    fontWeight: FontWeight.w600,
                  ),
                ),
                SizedBox(height: 4.h),
                Text(
                  controller.hijriDateLabel,
                  style: AppTextStyles.heading3,
                  maxLines: 1,
                  overflow: TextOverflow.ellipsis,
                ),
                SizedBox(height: 2.h),
                Text(
                  controller.gregorianDateLabel,
                  style: AppTextStyles.bodySmall,
                  maxLines: 1,
                  overflow: TextOverflow.ellipsis,
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

class _HeaderIconButton extends StatelessWidget {
  const _HeaderIconButton({required this.asset, required this.onTap});

  final String asset;
  final VoidCallback onTap;

  @override
  Widget build(BuildContext context) {
    return InkWell(
      onTap: onTap,
      borderRadius: BorderRadius.circular(12.r),
      child: Container(
        width: 42.w,
        height: 42.w,
        alignment: Alignment.center,
        decoration: BoxDecoration(
          color: AppColors.surface,
          borderRadius: BorderRadius.circular(12.r),
        ),
        child: SvgPicture.asset(
          asset,
          width: 20.w,
          height: 20.w,
          colorFilter: ColorFilter.mode(
            AppColors.textPrimary,
            BlendMode.srcIn,
          ),
        ),
      ),
    );
  }
}

class _ContinueReadingCard extends GetView<HomeController> {
  const _ContinueReadingCard();

  @override
  Widget build(BuildContext context) {
    return Container(
      constraints: BoxConstraints(minHeight: 168.h),
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(20.r),
        gradient: const LinearGradient(
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
          colors: [AppColors.primary, Color(0xFF0F2E22)],
        ),
      ),
      child: ClipRRect(
        borderRadius: BorderRadius.circular(20.r),
        child: Stack(
          children: [
            Positioned(
              right: -12.w,
              bottom: -18.h,
              top: 8.h,
              child: Image.asset(
                AppAssets.quranOnRehal,
                width: 158.w,
                fit: BoxFit.contain,
              ),
            ),
            Padding(
              padding: EdgeInsets.fromLTRB(20.w, 18.h, 132.w, 16.h),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                mainAxisSize: MainAxisSize.min,
                children: [
                  Text(
                    'Continue Reading',
                    style: AppTextStyles.bodySmall.copyWith(
                      color: AppColors.white.withValues(alpha: 0.8),
                    ),
                  ),
                  SizedBox(height: 6.h),
                  Obx(
                    () => Text(
                      controller.continueSurahTitle,
                      style: AppTextStyles.heading3.copyWith(
                        color: AppColors.white,
                        fontSize: 18.sp,
                      ),
                      maxLines: 1,
                      overflow: TextOverflow.ellipsis,
                    ),
                  ),
                  Obx(
                    () => Text(
                      controller.continueAyahLabel,
                      style: AppTextStyles.bodySmall.copyWith(
                        color: AppColors.white.withValues(alpha: 0.75),
                      ),
                    ),
                  ),
                  SizedBox(height: 16.h),
                  PrimaryButton(
                    label: 'Continue',
                    width: 118.w,
                    height: 38.h,
                    radius: 20.r,
                    backgroundColor: AppColors.white,
                    foregroundColor: AppColors.primary,
                    onPressed: controller.continueReading,
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class _ShortcutsSection extends GetView<HomeController> {
  const _ShortcutsSection();

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Row(
          children: [
            Expanded(
              child: Text(
                'Shortcuts',
                style: AppTextStyles.heading3,
                maxLines: 1,
                overflow: TextOverflow.ellipsis,
              ),
            ),
            GestureDetector(
              onTap: controller.openSurahs,
              child: Text(
                'View All',
                style: AppTextStyles.bodySmall.copyWith(
                  color: AppColors.primaryLight,
                  fontWeight: FontWeight.w600,
                ),
              ),
            ),
          ],
        ),
        SizedBox(height: 14.h),
        Row(
          children: [
            _ShortcutTile(
              label: 'Surah',
              asset: AppAssets.quranIcon,
              onTap: controller.openSurahs,
            ),
            SizedBox(width: 12.w),
            _ShortcutTile(
              label: 'Juz',
              asset: AppAssets.juzIcon,
              onTap: controller.openJuz,
            ),
            SizedBox(width: 12.w),
            _ShortcutTile(
              label: 'Bookmarks',
              asset: AppAssets.bookmarkIcon,
              onTap: controller.openBookmarks,
            ),
            SizedBox(width: 12.w),
            _ShortcutTile(
              label: 'Mushaf',
              icon: Icons.menu_book_rounded,
              onTap: controller.openMushaf,
            ),
          ],
        ),
        SizedBox(height: 12.h),
        Row(
          children: [
            _ShortcutTile(
              label: 'Study',
              icon: Icons.school_rounded,
              onTap: controller.openQuranStudy,
            ),
            SizedBox(width: 12.w),
            _ShortcutTile(
              label: 'Tasbih',
              asset: AppAssets.tasbihIcon,
              onTap: controller.openTasbih,
            ),
            SizedBox(width: 12.w),
            _ShortcutTile(
              label: 'Seerah',
              icon: Icons.auto_stories_rounded,
              onTap: controller.openIslamicHistory,
            ),
            SizedBox(width: 12.w),
            _ShortcutTile(
              label: 'Hifz',
              icon: Icons.mic_rounded,
              onTap: controller.openHifzTester,
            ),
          ],
        ),
      ],
    );
  }
}

class _ShortcutTile extends StatelessWidget {
  const _ShortcutTile({
    required this.label,
    required this.onTap,
    this.asset,
    this.icon,
  });

  final String label;
  final String? asset;
  final IconData? icon;
  final VoidCallback onTap;

  @override
  Widget build(BuildContext context) {
    return Expanded(
      child: Obx(() {
        Get.find<SettingsController>().isDarkMode.value;
        final isDark = AppColors.isDark;
        final iconColor = isDark ? Colors.white : AppColors.primary;
        final labelColor = isDark ? Colors.white70 : AppColors.primary;
        final iconWell = isDark
            ? Colors.white.withValues(alpha: 0.12)
            : AppColors.surface;

        return GestureDetector(
          onTap: onTap,
          child: Container(
            padding: EdgeInsets.symmetric(vertical: 14.h),
            decoration: BoxDecoration(
              color: AppColors.mint,
              borderRadius: BorderRadius.circular(16.r),
            ),
            child: Column(
              children: [
                Container(
                  width: 40.w,
                  height: 40.w,
                  alignment: Alignment.center,
                  decoration: BoxDecoration(
                    color: iconWell,
                    shape: BoxShape.circle,
                  ),
                  child: icon != null
                      ? Icon(icon, size: 20.sp, color: iconColor)
                      : SvgPicture.asset(
                          asset!,
                          width: 20.w,
                          height: 20.w,
                          colorFilter: ColorFilter.mode(
                            iconColor,
                            BlendMode.srcIn,
                          ),
                        ),
                ),
                SizedBox(height: 8.h),
                Text(
                  label,
                  style: AppTextStyles.caption.copyWith(
                    color: labelColor,
                    fontWeight: FontWeight.w600,
                  ),
                  textAlign: TextAlign.center,
                  maxLines: 1,
                  overflow: TextOverflow.ellipsis,
                ),
              ],
            ),
          ),
        );
      }),
    );
  }
}

class _DailyVerseCard extends GetView<HomeController> {
  const _DailyVerseCard();

  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,
      padding: EdgeInsets.all(20.w),
      decoration: BoxDecoration(
        color: AppColors.surface,
        borderRadius: BorderRadius.circular(20.r),
        boxShadow: [
          BoxShadow(
            color: AppColors.primary.withValues(alpha: 0.05),
            blurRadius: 16.r,
            offset: Offset(0, 6.h),
          ),
        ],
      ),
      child: Obx(() {
        if (controller.isDailyVerseLoading.value &&
            controller.dailyVerse.value == null) {
          return const _DailyVerseLoading();
        }

        final verse = controller.dailyVerse.value;
        if (verse == null) {
          return Column(
            children: [
              Row(
                children: [
                  Expanded(
                    child: Text('Daily Verse', style: AppTextStyles.heading3),
                  ),
                ],
              ),
              SizedBox(height: 16.h),
              Text(
                'Unable to load today’s verse.',
                style: AppTextStyles.bodySmall,
                textAlign: TextAlign.center,
              ),
              TextButton(
                onPressed: controller.loadDailyVerse,
                child: const Text('Retry'),
              ),
            ],
          );
        }

        return Column(
          children: [
            Row(
              children: [
                Expanded(
                  child: Text(
                    'Daily Verse',
                    style: AppTextStyles.heading3,
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                  ),
                ),
                GestureDetector(
                  onTap: controller.shareDailyVerse,
                  child: Icon(
                    Icons.ios_share_rounded,
                    size: 18.sp,
                    color: AppColors.textSecondary,
                  ),
                ),
              ],
            ),
            SizedBox(height: 16.h),
            Obx(() {
              final settings = Get.find<SettingsController>();
              return Text(
                verse.arabic,
                style: settings.arabicStyle(height: 2.2).copyWith(
                  leadingDistribution: TextLeadingDistribution.even,
                ),
                textAlign: TextAlign.center,
                textDirection: TextDirection.rtl,
              );
            }),
            SizedBox(height: 12.h),
            Obx(() {
              final settings = Get.find<SettingsController>();
              return Text(
                verse.translation,
                style: settings.translationStyle(
                  color: AppColors.textSecondary,
                ),
                textAlign: TextAlign.center,
              );
            }),
            SizedBox(height: 14.h),
            Text(
              '(${verse.reference})',
              style: AppTextStyles.caption.copyWith(
                color: AppColors.primaryLight,
                fontWeight: FontWeight.w600,
              ),
            ),
          ],
        );
      }),
    );
  }
}

class _DailyVerseLoading extends StatelessWidget {
  const _DailyVerseLoading();

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Row(
          children: [
            Expanded(child: Text('Daily Verse', style: AppTextStyles.heading3)),
          ],
        ),
        SizedBox(height: 24.h),
        const _PulseBar(widthFactor: 0.9, height: 18),
        SizedBox(height: 10.h),
        const _PulseBar(widthFactor: 0.7, height: 18),
        SizedBox(height: 16.h),
        const _PulseBar(widthFactor: 1, height: 12),
        SizedBox(height: 8.h),
        const _PulseBar(widthFactor: 0.85, height: 12),
        SizedBox(height: 18.h),
        Center(
          child: SizedBox(
            width: 22.w,
            height: 22.w,
            child: const CircularProgressIndicator(
              strokeWidth: 2,
              color: AppColors.primary,
            ),
          ),
        ),
      ],
    );
  }
}

class _PulseBar extends StatefulWidget {
  const _PulseBar({required this.widthFactor, required this.height});

  final double widthFactor;
  final double height;

  @override
  State<_PulseBar> createState() => _PulseBarState();
}

class _PulseBarState extends State<_PulseBar>
    with SingleTickerProviderStateMixin {
  late final AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 900),
    )..repeat(reverse: true);
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return AnimatedBuilder(
      animation: _controller,
      builder: (context, child) {
        return Opacity(
          opacity: 0.35 + (_controller.value * 0.45),
          child: child,
        );
      },
      child: FractionallySizedBox(
        widthFactor: widget.widthFactor,
        alignment: Alignment.center,
        child: Container(
          height: widget.height.h,
          decoration: BoxDecoration(
            color: AppColors.mint,
            borderRadius: BorderRadius.circular(8.r),
          ),
        ),
      ),
    );
  }
}
