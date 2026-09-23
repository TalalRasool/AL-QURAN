import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:get/get.dart';

import '../../core/constants/app_colors.dart';
import '../../core/constants/app_text_styles.dart';
import '../../core/routes/app_routes.dart';
import '../../core/widgets/widgets.dart';
import '../../core/controllers/prayer_notification_controller.dart';
import '../../core/controllers/settings_controller.dart';
import 'profile_controller.dart';

class ProfileScreen extends GetView<ProfileController> {
  const ProfileScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Obx(() {
      Get.find<SettingsController>().isDarkMode.value;
      return Column(
        children: [
          const _ProfileHeader(),
          Expanded(
            child: ListView(
              padding: EdgeInsets.fromLTRB(20.w, 20.h, 20.w, 24.h),
              children: [
                _SettingsTile(
                  icon: Icons.menu_book_rounded,
                  title: 'Reading Settings',
                  onTap: controller.openReadingSettings,
                ),
                Obx(
                  () => _SettingsTile(
                    icon: Icons.translate_rounded,
                    title: 'Translations',
                    value: controller.translationLabel,
                    onTap: controller.openTranslations,
                  ),
                ),
                Obx(
                  () => _SettingsTile(
                    icon: Icons.font_download_outlined,
                    title: 'Font Style',
                    value: Get.find<SettingsController>().arabicFont.value,
                    onTap: controller.openReadingSettings,
                  ),
                ),
                Obx(
                  () => _SettingsTile(
                    icon: Icons.format_size_rounded,
                    title: 'Text Size',
                    value: Get.find<SettingsController>().textSizeLabel,
                    onTap: controller.openReadingSettings,
                  ),
                ),
                Obx(
                  () => _SettingsTile(
                    icon: Icons.palette_outlined,
                    title: 'Theme',
                    value: Get.find<SettingsController>().themeLabel,
                    onTap: controller.openReadingSettings,
                  ),
                ),
                Obx(
                  () => _SettingsTile(
                    icon: Icons.notifications_none_rounded,
                    title: 'Notifications',
                    trailing: Switch.adaptive(
                      value: controller.notificationsEnabled.value,
                      activeThumbColor: AppColors.primary,
                      onChanged: controller.toggleNotifications,
                    ),
                  ),
                ),
                Obx(() {
                  final prayer = Get.find<PrayerNotificationController>();
                  final busy = prayer.isBusy.value;
                  return _SettingsTile(
                    icon: Icons.mosque_outlined,
                    title: 'Prayer Notifications',
                    trailing: Switch.adaptive(
                      value: prayer.isEnabled.value,
                      activeThumbColor: AppColors.primary,
                      onChanged: busy
                          ? null
                          : controller.togglePrayerNotifications,
                    ),
                  );
                }),
                _SettingsTile(
                  icon: Icons.fingerprint_rounded,
                  title: 'Tasbih Counter',
                  onTap: () => Get.toNamed(AppRoutes.tasbih),
                ),
                _SettingsTile(
                  icon: Icons.auto_stories_outlined,
                  title: 'Islamic History & Seerah',
                  onTap: () => Get.toNamed(AppRoutes.islamicHistory),
                ),
                _SettingsTile(
                  icon: Icons.mic_none_rounded,
                  title: 'Hifz Tester',
                  onTap: () => Get.toNamed(AppRoutes.hifzTester),
                ),
                _SettingsTile(
                  icon: Icons.bookmark_border_rounded,
                  title: 'Bookmarks',
                  onTap: () => Get.toNamed(AppRoutes.bookmarks),
                ),
                SizedBox(height: 8.h),
                Text('Data Backup', style: AppTextStyles.heading3),
                SizedBox(height: 10.h),
                const _DataBackupCard(),
              ],
            ),
          ),
        ],
      );
    });
  }
}

class _ProfileHeader extends GetView<ProfileController> {
  const _ProfileHeader();

  @override
  Widget build(BuildContext context) {
    return ClipPath(
      clipper: _CurveClipper(),
      child: Container(
        width: double.infinity,
        height: 250.h,
        color: AppColors.primary,
        child: SafeArea(
          bottom: false,
          child: Padding(
            padding: EdgeInsets.fromLTRB(20.w, 12.h, 20.w, 36.h),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.center,
              children: [
                SizedBox(
                  height: 40.h,
                  child: Stack(
                    alignment: Alignment.center,
                    children: [
                      Text(
                        'Profile',
                        textAlign: TextAlign.center,
                        style: AppTextStyles.heading3.copyWith(
                          color: AppColors.white,
                        ),
                      ),
                      Align(
                        alignment: Alignment.centerRight,
                        child: IconButton(
                          tooltip: 'Edit Profile',
                          onPressed: controller.openEditProfile,
                          padding: EdgeInsets.zero,
                          constraints: BoxConstraints(
                            minWidth: 40.w,
                            minHeight: 40.h,
                          ),
                          visualDensity: VisualDensity.compact,
                          icon: Icon(
                            Icons.edit_outlined,
                            color: AppColors.white,
                            size: 22.sp,
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
                SizedBox(height: 16.h),
                Center(
                  child: Container(
                    width: 84.w,
                    height: 84.w,
                    decoration: BoxDecoration(
                      shape: BoxShape.circle,
                      color: AppColors.white.withValues(alpha: 0.16),
                      border: Border.all(
                        color: AppColors.white,
                        width: 3.w,
                      ),
                    ),
                    child: Icon(
                      Icons.person_rounded,
                      color: AppColors.white,
                      size: 42.sp,
                    ),
                  ),
                ),
                SizedBox(height: 10.h),
                Obx(
                  () => Text(
                    controller.userName,
                    textAlign: TextAlign.center,
                    style: AppTextStyles.heading2.copyWith(
                      color: AppColors.white,
                    ),
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                  ),
                ),
                Obx(
                  () => Text(
                    controller.userCountry,
                    textAlign: TextAlign.center,
                    style: AppTextStyles.bodySmall.copyWith(
                      color: AppColors.white.withValues(alpha: 0.8),
                    ),
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

class _DataBackupCard extends GetView<ProfileController> {
  const _DataBackupCard();

  @override
  Widget build(BuildContext context) {
    return Obx(() {
      final loggedIn = controller.isLoggedIn;
      return Container(
        width: double.infinity,
        padding: EdgeInsets.all(16.w),
        decoration: BoxDecoration(
          color: AppColors.surface,
          borderRadius: BorderRadius.circular(16.r),
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                Container(
                  width: 40.w,
                  height: 40.w,
                  decoration: BoxDecoration(
                    color: AppColors.mint,
                    shape: BoxShape.circle,
                  ),
                  child: Icon(
                    Icons.cloud_outlined,
                    color: AppColors.primary,
                    size: 20.sp,
                  ),
                ),
                SizedBox(width: 12.w),
                Expanded(
                  child: Text(
                    loggedIn ? 'Synced to your account' : 'Optional cloud sync',
                    style: AppTextStyles.heading3,
                  ),
                ),
              ],
            ),
            SizedBox(height: 8.h),
            Text(
              loggedIn
                  ? controller.accountEmail
                  : 'Sign in to back up bookmarks and reading progress.',
              style: AppTextStyles.bodySmall,
            ),
            SizedBox(height: 14.h),
            if (loggedIn)
              PrimaryButton(
                label: 'Sign Out',
                onPressed: controller.signOut,
              )
            else
              PrimaryButton(
                label: 'Sign In / Sign Up',
                onPressed: controller.openAuthSheet,
              ),
          ],
        ),
      );
    });
  }
}

class _CurveClipper extends CustomClipper<Path> {
  @override
  Path getClip(Size size) {
    final path = Path()
      ..lineTo(0, size.height - 28)
      ..quadraticBezierTo(
        size.width / 2,
        size.height,
        size.width,
        size.height - 28,
      )
      ..lineTo(size.width, 0)
      ..close();
    return path;
  }

  @override
  bool shouldReclip(covariant CustomClipper<Path> oldClipper) => false;
}

class _SettingsTile extends StatelessWidget {
  const _SettingsTile({
    required this.icon,
    required this.title,
    this.value,
    this.trailing,
    this.onTap,
  });

  final IconData icon;
  final String title;
  final String? value;
  final Widget? trailing;
  final VoidCallback? onTap;

  @override
  Widget build(BuildContext context) {
    return Obx(() {
      Get.find<SettingsController>().isDarkMode.value;
      final iconColor = AppColors.isDark ? Colors.white : AppColors.primary;
      return Padding(
        padding: EdgeInsets.only(bottom: 10.h),
        child: Material(
          color: AppColors.surface,
          borderRadius: BorderRadius.circular(16.r),
          child: InkWell(
            onTap: onTap,
            borderRadius: BorderRadius.circular(16.r),
            child: Padding(
              padding: EdgeInsets.symmetric(horizontal: 14.w, vertical: 14.h),
              child: Row(
                children: [
                  Container(
                    width: 40.w,
                    height: 40.w,
                    decoration: BoxDecoration(
                      color: AppColors.mint,
                      shape: BoxShape.circle,
                    ),
                    child: Icon(icon, color: iconColor, size: 20.sp),
                  ),
                  SizedBox(width: 12.w),
                  Expanded(
                    child: Text(
                      title,
                      style: AppTextStyles.heading3,
                      maxLines: 1,
                      overflow: TextOverflow.ellipsis,
                    ),
                  ),
                  if (trailing != null)
                    trailing!
                  else ...[
                    if (value != null)
                      Flexible(
                        child: Text(
                          value!,
                          style: AppTextStyles.bodySmall.copyWith(
                            color: AppColors.isDark
                                ? AppColors.textSecondary
                                : AppColors.primaryLight,
                            fontWeight: FontWeight.w600,
                          ),
                          maxLines: 1,
                          overflow: TextOverflow.ellipsis,
                          textAlign: TextAlign.end,
                        ),
                      ),
                    Icon(
                      Icons.chevron_right_rounded,
                      size: 22.sp,
                      color: AppColors.textSecondary,
                    ),
                  ],
                ],
              ),
            ),
          ),
        ),
      );
    });
  }
}
