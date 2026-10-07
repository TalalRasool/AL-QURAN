import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:get/get.dart';

import '../../core/constants/app_colors.dart';
import '../../core/constants/app_text_styles.dart';
import '../../core/controllers/quran_audio_controller.dart';
import '../../core/services/storage_service.dart';

/// Play and download actions for the surah or juz being read.
class QuranAudioActions extends StatefulWidget {
  const QuranAudioActions({
    super.key,
    required this.surahNumber,
    required this.surahName,
  });

  final int surahNumber;
  final String surahName;

  @override
  State<QuranAudioActions> createState() => _QuranAudioActionsState();
}

class _QuranAudioActionsState extends State<QuranAudioActions> {
  Worker? _reciterWorker;

  QuranAudioController get _audio => Get.find<QuranAudioController>();

  @override
  void initState() {
    super.initState();
    _refresh();
    if (Get.isRegistered<StorageService>()) {
      _reciterWorker = ever(
        Get.find<StorageService>().selectedReciterId,
        (_) => _refresh(),
      );
    }
  }

  @override
  void didUpdateWidget(QuranAudioActions oldWidget) {
    super.didUpdateWidget(oldWidget);
    if (oldWidget.surahNumber != widget.surahNumber) _refresh();
  }

  @override
  void dispose() {
    _reciterWorker?.dispose();
    super.dispose();
  }

  void _refresh() {
    _audio.refreshDownloaded(widget.surahNumber);
  }

  @override
  Widget build(BuildContext context) {
    if (widget.surahNumber < 1) return const SizedBox.shrink();
    return Obx(() {
      final playingThis = _audio.isCurrentTrack(widget.surahNumber) &&
          _audio.isPlaying;
      final downloaded = _audio.isDownloaded(widget.surahNumber);
      final downloading = _audio.isDownloadingSurah(widget.surahNumber);
      return Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          IconButton(
            tooltip: playingThis ? 'Pause recitation' : 'Play recitation',
            onPressed: () => _audio.playOrToggle(
              surahNumber: widget.surahNumber,
              surahName: widget.surahName,
            ),
            icon: Icon(
              playingThis ? Icons.pause_rounded : Icons.play_arrow_rounded,
              color: AppColors.textPrimary,
              size: 26.sp,
            ),
          ),
          IconButton(
            tooltip: downloaded ? 'Saved recitation' : 'Download recitation',
            onPressed: () => _audio.downloadSurah(
              surahNumber: widget.surahNumber,
              surahName: widget.surahName,
            ),
            icon: downloading
                ? SizedBox(
                    width: 26.w,
                    height: 26.w,
                    child: Stack(
                      alignment: Alignment.center,
                      children: [
                        CircularProgressIndicator(
                          strokeWidth: 2.2.w,
                          color: AppColors.primary,
                          value: _audio.totalBytes.value <= 0
                              ? null
                              : (_audio.downloadPercent.value / 100)
                                  .clamp(0.0, 1.0),
                        ),
                        Text(
                          '${_audio.downloadPercent.value.round()}',
                          style: AppTextStyles.caption.copyWith(
                            fontSize: 8.sp,
                            color: AppColors.primary,
                            fontWeight: FontWeight.w700,
                          ),
                        ),
                      ],
                    ),
                  )
                : Icon(
                    downloaded
                        ? Icons.download_done_rounded
                        : Icons.download_rounded,
                    color: downloaded
                        ? AppColors.primary
                        : AppColors.textPrimary,
                    size: 24.sp,
                  ),
          ),
        ],
      );
    });
  }
}
