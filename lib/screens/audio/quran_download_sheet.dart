import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:get/get.dart';

import '../../core/constants/app_colors.dart';
import '../../core/constants/app_text_styles.dart';
import '../../core/controllers/quran_audio_controller.dart';

class QuranDownloadSheet extends GetView<QuranAudioController> {
  const QuranDownloadSheet({super.key});

  @override
  Widget build(BuildContext context) {
    return SafeArea(
      top: false,
      child: Padding(
        padding: EdgeInsets.fromLTRB(12.w, 0, 12.w, 12.h),
        child: Obx(() {
          final phase = controller.downloadPhase.value;
          final knownTotal = controller.totalBytes.value > 0;
          final progress = knownTotal
              ? (controller.downloadPercent.value / 100).clamp(0.0, 1.0)
              : null;

          return Material(
            color: AppColors.surface,
            borderRadius: BorderRadius.circular(24.r),
            child: Padding(
              padding: EdgeInsets.fromLTRB(20.w, 12.h, 20.w, 20.h),
              child: Column(
                mainAxisSize: MainAxisSize.min,
                children: [
                  Container(
                    width: 40.w,
                    height: 4.h,
                    decoration: BoxDecoration(
                      color: AppColors.greyLight,
                      borderRadius: BorderRadius.circular(4.r),
                    ),
                  ),
                  SizedBox(height: 16.h),
                  Text(
                    controller.downloadSurahTitle.value,
                    style: AppTextStyles.heading3,
                    textAlign: TextAlign.center,
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                  ),
                  SizedBox(height: 4.h),
                  Text(
                    controller.downloadReciterName.value,
                    style: AppTextStyles.bodySmall,
                    textAlign: TextAlign.center,
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                  ),
                  SizedBox(height: 18.h),
                  ClipRRect(
                    borderRadius: BorderRadius.circular(8.r),
                    child: LinearProgressIndicator(
                      value: phase == QuranDownloadPhase.saved ? 1 : progress,
                      minHeight: 8.h,
                      backgroundColor: AppColors.greyLight,
                      color: AppColors.primary,
                    ),
                  ),
                  SizedBox(height: 12.h),
                  Row(
                    children: [
                      Text(
                        controller.percentLabel,
                        style: AppTextStyles.heading3.copyWith(
                          color: AppColors.primary,
                        ),
                      ),
                      const Spacer(),
                      Text(
                        controller.sizeLabel,
                        style: AppTextStyles.bodySmall.copyWith(
                          fontWeight: FontWeight.w600,
                        ),
                      ),
                    ],
                  ),
                  if (phase == QuranDownloadPhase.failed &&
                      controller.downloadError.value != null) ...[
                    SizedBox(height: 10.h),
                    Text(
                      controller.downloadError.value!,
                      style: AppTextStyles.bodySmall,
                      textAlign: TextAlign.center,
                    ),
                  ],
                  if (phase == QuranDownloadPhase.saved) ...[
                    SizedBox(height: 8.h),
                    Text(
                      'Saved on this device',
                      style: AppTextStyles.bodySmall.copyWith(
                        color: AppColors.primary,
                        fontWeight: FontWeight.w600,
                      ),
                    ),
                  ],
                  if (phase == QuranDownloadPhase.cancelled) ...[
                    SizedBox(height: 8.h),
                    Text(
                      'Download cancelled',
                      style: AppTextStyles.bodySmall,
                    ),
                  ],
                  SizedBox(height: 16.h),
                  _SheetActions(phase: phase),
                ],
              ),
            ),
          );
        }),
      ),
    );
  }
}

class _SheetActions extends GetView<QuranAudioController> {
  const _SheetActions({required this.phase});

  final QuranDownloadPhase phase;

  @override
  Widget build(BuildContext context) {
    switch (phase) {
      case QuranDownloadPhase.downloading:
        return _SheetButton(
          label: 'Cancel',
          filled: false,
          onPressed: controller.cancelDownload,
        );
      case QuranDownloadPhase.saved:
        return _SheetButton(
          label: 'Play',
          filled: true,
          onPressed: () {
            Get.back();
            controller.playOrToggle(
              surahNumber: controller.downloadSurahNumber.value,
              surahName: controller.downloadSurahTitle.value,
            );
          },
        );
      case QuranDownloadPhase.failed:
      case QuranDownloadPhase.cancelled:
        return _SheetButton(
          label: 'Try again',
          filled: true,
          onPressed: () => controller.downloadSurah(
            surahNumber: controller.downloadSurahNumber.value,
            surahName: controller.downloadSurahTitle.value,
          ),
        );
      case QuranDownloadPhase.idle:
        return const SizedBox.shrink();
    }
  }
}

class _SheetButton extends StatelessWidget {
  const _SheetButton({
    required this.label,
    required this.filled,
    required this.onPressed,
  });

  final String label;
  final bool filled;
  final VoidCallback onPressed;

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      width: double.infinity,
      height: 48.h,
      child: filled
          ? FilledButton(
              onPressed: onPressed,
              style: FilledButton.styleFrom(
                backgroundColor: AppColors.primary,
                foregroundColor: AppColors.white,
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(14.r),
                ),
              ),
              child: Text(
                label,
                style: AppTextStyles.button.copyWith(
                  color: filled ? AppColors.white : AppColors.accent,
                ),
              ),
            )
          : OutlinedButton(
              onPressed: onPressed,
              style: OutlinedButton.styleFrom(
                foregroundColor: AppColors.accent,
                side: BorderSide(color: AppColors.accent),
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(14.r),
                ),
              ),
              child: Text(
                label,
                style: AppTextStyles.button.copyWith(color: AppColors.accent),
              ),
            ),
    );
  }
}
