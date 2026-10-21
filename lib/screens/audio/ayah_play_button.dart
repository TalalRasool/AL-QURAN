import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:get/get.dart';

import '../../core/constants/app_colors.dart';
import '../../core/controllers/quran_audio_controller.dart';

/// Play or pause one ayah with the selected reciter.
class AyahPlayButton extends StatelessWidget {
  const AyahPlayButton({
    super.key,
    required this.surahNumber,
    required this.ayahNumber,
    required this.surahName,
  });

  final int surahNumber;
  final int ayahNumber;
  final String surahName;

  @override
  Widget build(BuildContext context) {
    if (surahNumber < 1 || ayahNumber < 1) return const SizedBox.shrink();
    if (!Get.isRegistered<QuranAudioController>()) {
      return const SizedBox.shrink();
    }
    final audio = Get.find<QuranAudioController>();
    return Obx(() {
      final playing = audio.isAyahPlaying(surahNumber, ayahNumber);
      final loading = audio.isAyahLoading(surahNumber, ayahNumber);
      return SizedBox(
        width: 36.w,
        height: 36.w,
        child: IconButton(
          padding: EdgeInsets.zero,
          tooltip: playing ? 'Pause ayah' : 'Play ayah',
          onPressed: loading
              ? null
              : () => audio.playOrToggleAyah(
                  surahNumber: surahNumber,
                  ayahNumber: ayahNumber,
                  surahName: surahName,
                ),
          icon: loading
              ? SizedBox(
                  width: 18.w,
                  height: 18.w,
                  child: CircularProgressIndicator(
                    strokeWidth: 2,
                    color: AppColors.primary,
                  ),
                )
              : Icon(
                  playing ? Icons.pause_rounded : Icons.play_arrow_rounded,
                  color: AppColors.primary,
                  size: 26.sp,
                ),
        ),
      );
    });
  }
}
