import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:get/get.dart';

import '../../core/constants/app_colors.dart';
import '../../core/constants/app_text_styles.dart';
import '../../core/controllers/quran_audio_controller.dart';

/// Space the ayah list needs so the sticky player does not cover the text.
double quranListBottomPadding(BuildContext context, bool playerVisible) {
  final safeBottom = MediaQuery.paddingOf(context).bottom;
  return safeBottom + (playerVisible ? 210.h : 28.h);
}

String formatAudioClock(Duration duration) {
  final totalSeconds = duration.inSeconds.abs();
  final hours = totalSeconds ~/ 3600;
  final minutes = (totalSeconds % 3600) ~/ 60;
  final seconds = totalSeconds % 60;
  final mm = minutes.toString().padLeft(2, '0');
  final ss = seconds.toString().padLeft(2, '0');
  if (hours > 0) return '$hours:$mm:$ss';
  return '$mm:$ss';
}

/// Sticky player shown only while a recitation is playing or paused.
class QuranBottomPlayer extends StatefulWidget {
  const QuranBottomPlayer({super.key});

  @override
  State<QuranBottomPlayer> createState() => _QuranBottomPlayerState();
}

class _QuranBottomPlayerState extends State<QuranBottomPlayer> {
  double? _dragFraction;

  @override
  Widget build(BuildContext context) {
    final audio = Get.find<QuranAudioController>();
    return Obx(() {
      if (!audio.showPlayer) return const SizedBox.shrink();
      final progress = _dragFraction ?? audio.progress;
      return SafeArea(
        top: false,
        child: Padding(
          padding: EdgeInsets.fromLTRB(16.w, 0, 16.w, 12.h),
          child: Directionality(
            textDirection: TextDirection.ltr,
            child: Container(
              padding: EdgeInsets.fromLTRB(16.w, 12.h, 16.w, 6.h),
              decoration: BoxDecoration(
                color: AppColors.primary,
                borderRadius: BorderRadius.circular(22.r),
                boxShadow: [
                  BoxShadow(
                    color: AppColors.primary.withValues(alpha: 0.28),
                    blurRadius: 18.r,
                    offset: Offset(0, 8.h),
                  ),
                ],
              ),
              child: Column(
                mainAxisSize: MainAxisSize.min,
                children: [
                  Text(
                    audio.nowPlayingTitle,
                    style: AppTextStyles.body.copyWith(
                      color: AppColors.white,
                      fontWeight: FontWeight.w600,
                    ),
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                    textAlign: TextAlign.center,
                  ),
                  Text(
                    audio.nowPlayingArtist,
                    style: AppTextStyles.caption.copyWith(
                      color: AppColors.white.withValues(alpha: 0.75),
                    ),
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                    textAlign: TextAlign.center,
                  ),
                  SizedBox(height: 4.h),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      IconButton(
                        tooltip: 'Rewind 10 seconds',
                        onPressed: audio.rewind,
                        icon: Icon(
                          Icons.replay_10_rounded,
                          color: AppColors.white,
                          size: 30.sp,
                        ),
                      ),
                      SizedBox(width: 8.w),
                      _PlayButton(audio: audio),
                      SizedBox(width: 8.w),
                      IconButton(
                        tooltip: 'Forward 10 seconds',
                        onPressed: audio.forward,
                        icon: Icon(
                          Icons.forward_10_rounded,
                          color: AppColors.white,
                          size: 30.sp,
                        ),
                      ),
                    ],
                  ),
                  SliderTheme(
                    data: SliderThemeData(
                      trackHeight: 4.h,
                      thumbShape: RoundSliderThumbShape(
                        enabledThumbRadius: 7.r,
                      ),
                      overlayShape: RoundSliderOverlayShape(
                        overlayRadius: 14.r,
                      ),
                      activeTrackColor: AppColors.white,
                      inactiveTrackColor: AppColors.white.withValues(alpha: 0.25),
                      thumbColor: AppColors.white,
                    ),
                    child: Slider(
                      value: progress.clamp(0.0, 1.0),
                      onChangeStart: (value) {
                        setState(() => _dragFraction = value);
                      },
                      onChanged: (value) {
                        setState(() => _dragFraction = value);
                      },
                      onChangeEnd: (value) async {
                        await audio.seekToFraction(value);
                        if (mounted) setState(() => _dragFraction = null);
                      },
                    ),
                  ),
                  Padding(
                    padding: EdgeInsets.fromLTRB(12.w, 0, 12.w, 8.h),
                    child: Row(
                      children: [
                        Text(
                          formatAudioClock(audio.position),
                          style: AppTextStyles.caption.copyWith(
                            color: AppColors.white.withValues(alpha: 0.85),
                          ),
                        ),
                        const Spacer(),
                        Text(
                          formatAudioClock(audio.duration),
                          style: AppTextStyles.caption.copyWith(
                            color: AppColors.white.withValues(alpha: 0.85),
                          ),
                        ),
                      ],
                    ),
                  ),
                ],
              ),
            ),
          ),
        ),
      );
    });
  }
}

class _PlayButton extends StatelessWidget {
  const _PlayButton({required this.audio});

  final QuranAudioController audio;

  @override
  Widget build(BuildContext context) {
    return Obx(() {
      final loading = audio.isBuffering;
      final playing = audio.isPlaying;
      return Material(
        color: AppColors.white,
        shape: const CircleBorder(),
        child: InkWell(
          customBorder: const CircleBorder(),
          onTap: loading ? null : audio.toggleCurrent,
          child: SizedBox(
            width: 52.w,
            height: 52.w,
            child: loading
                ? Padding(
                    padding: EdgeInsets.all(14.w),
                    child: CircularProgressIndicator(
                      strokeWidth: 2.4.w,
                      color: AppColors.primary,
                    ),
                  )
                : Icon(
                    playing ? Icons.pause_rounded : Icons.play_arrow_rounded,
                    color: AppColors.primary,
                    size: 32.sp,
                  ),
          ),
        ),
      );
    });
  }
}
