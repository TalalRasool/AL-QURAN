import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:get/get.dart';

import '../../core/constants/app_assets.dart';
import '../../core/constants/app_colors.dart';
import '../../core/constants/app_text_styles.dart';
import '../../core/controllers/settings_controller.dart';
import 'audio_controller.dart';

class AudioScreen extends GetView<AudioController> {
  const AudioScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Obx(() {
      Get.find<SettingsController>().isDarkMode.value;
      return SafeArea(
        bottom: false,
        child: Padding(
          padding: EdgeInsets.symmetric(horizontal: 20.w),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              SizedBox(height: 8.h),
              Text('Audio', style: AppTextStyles.heading2),
              SizedBox(height: 4.h),
              Text(
                'Arabic recitation',
                style: AppTextStyles.bodySmall,
              ),
              SizedBox(height: 16.h),
              const Expanded(child: _ReciterList()),
            ],
          ),
        ),
      );
    });
  }
}

class _ReciterList extends GetView<AudioController> {
  const _ReciterList();

  @override
  Widget build(BuildContext context) {
    return Obx(() {
      Get.find<SettingsController>().isDarkMode.value;
      if (controller.isLoading.value) {
        return const _ReciterListSkeleton();
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
                  onPressed: controller.loadReciters,
                  child: const Text('Retry'),
                ),
              ],
            ),
          ),
        );
      }

      final reciters = controller.reciters;
      if (reciters.isEmpty) {
        return Center(
          child: Text('No reciters found', style: AppTextStyles.body),
        );
      }

      return ListView.separated(
        padding: EdgeInsets.only(bottom: 16.h),
        itemCount: reciters.length,
        separatorBuilder: (_, _) => SizedBox(height: 10.h),
        itemBuilder: (context, index) {
          final reciter = reciters[index];
          final isSelected = controller.isSelected(reciter);
          final isPlaying = controller.isPlaying(reciter);

          return GestureDetector(
            onTap: () => controller.selectReciter(reciter),
            child: Container(
              padding: EdgeInsets.symmetric(horizontal: 12.w, vertical: 10.h),
              decoration: BoxDecoration(
                color: isSelected ? AppColors.mint : AppColors.surface,
                borderRadius: BorderRadius.circular(16.r),
              ),
              child: Row(
                children: [
                  ClipOval(
                    child: Image.asset(
                      AppAssets.avatarPlaceholder,
                      width: 48.w,
                      height: 48.w,
                      fit: BoxFit.cover,
                    ),
                  ),
                  SizedBox(width: 12.w),
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          reciter.displayName,
                          style: AppTextStyles.heading3,
                          maxLines: 1,
                          overflow: TextOverflow.ellipsis,
                        ),
                        Text(reciter.subtitle, style: AppTextStyles.bodySmall),
                      ],
                    ),
                  ),
                  Icon(
                    Icons.cloud_download_outlined,
                    size: 22.sp,
                    color: AppColors.textSecondary,
                  ),
                  SizedBox(width: 10.w),
                  GestureDetector(
                    onTap: () => controller.playReciter(reciter),
                    child: Container(
                      width: 36.w,
                      height: 36.w,
                      decoration: BoxDecoration(
                        color: isPlaying ? AppColors.primary : AppColors.mint,
                        shape: BoxShape.circle,
                      ),
                      child: Icon(
                        isPlaying
                            ? Icons.pause_rounded
                            : Icons.play_arrow_rounded,
                        size: 20.sp,
                        color: isPlaying ? AppColors.white : AppColors.onMint,
                      ),
                    ),
                  ),
                ],
              ),
            ),
          );
        },
      );
    });
  }
}

class _ReciterListSkeleton extends StatelessWidget {
  const _ReciterListSkeleton();

  @override
  Widget build(BuildContext context) {
    return ListView.separated(
      physics: const NeverScrollableScrollPhysics(),
      padding: EdgeInsets.only(bottom: 16.h),
      itemCount: 6,
      separatorBuilder: (_, _) => SizedBox(height: 10.h),
      itemBuilder: (_, _) => const _ReciterSkeletonTile(),
    );
  }
}

class _ReciterSkeletonTile extends StatefulWidget {
  const _ReciterSkeletonTile();

  @override
  State<_ReciterSkeletonTile> createState() => _ReciterSkeletonTileState();
}

class _ReciterSkeletonTileState extends State<_ReciterSkeletonTile>
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
          opacity: 0.4 + (_controller.value * 0.4),
          child: child,
        );
      },
      child: Container(
        padding: EdgeInsets.symmetric(horizontal: 12.w, vertical: 10.h),
        decoration: BoxDecoration(
          color: AppColors.surface,
          borderRadius: BorderRadius.circular(16.r),
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
            ),
            SizedBox(width: 12.w),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Container(
                    height: 14.h,
                    width: 140.w,
                    decoration: BoxDecoration(
                      color: AppColors.mint,
                      borderRadius: BorderRadius.circular(8.r),
                    ),
                  ),
                  SizedBox(height: 8.h),
                  Container(
                    height: 10.h,
                    width: 90.w,
                    decoration: BoxDecoration(
                      color: AppColors.mint,
                      borderRadius: BorderRadius.circular(8.r),
                    ),
                  ),
                ],
              ),
            ),
            Container(
              width: 36.w,
              height: 36.w,
              decoration: BoxDecoration(
                color: AppColors.mint,
                shape: BoxShape.circle,
              ),
            ),
          ],
        ),
      ),
    );
  }
}
