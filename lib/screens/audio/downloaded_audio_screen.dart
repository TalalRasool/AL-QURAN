import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:get/get.dart';
import 'package:google_fonts/google_fonts.dart';

import '../../core/constants/app_colors.dart';
import '../../core/constants/app_text_styles.dart';
import '../../core/controllers/quran_audio_controller.dart';
import '../../core/controllers/settings_controller.dart';
import '../../core/widgets/custom_app_bar.dart';
import '../audio/quran_bottom_player.dart';
import 'downloaded_audio_controller.dart';

class DownloadedAudioScreen extends GetView<DownloadedAudioController> {
  const DownloadedAudioScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Obx(() {
      if (Get.isRegistered<SettingsController>()) {
        Get.find<SettingsController>().isDarkMode.value;
      }
      return Scaffold(
        backgroundColor: AppColors.background,
        appBar: CustomAppBar(
          title: 'Downloaded Audios',
          titleStyle: AppTextStyles.heading2,
        ),
        body: Stack(
          children: [
            Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                Padding(
                  padding: EdgeInsets.fromLTRB(20.w, 4.h, 20.w, 12.h),
                  child: Text(
                    'میری ڈاؤن لوڈز',
                    textDirection: TextDirection.rtl,
                    style: GoogleFonts.notoNastaliqUrdu(
                      fontSize: 16.sp,
                      color: AppColors.textSecondary,
                      height: 1.8,
                    ),
                  ),
                ),
                Expanded(child: _buildList()),
              ],
            ),
            const Positioned(
              left: 0,
              right: 0,
              bottom: 0,
              child: QuranBottomPlayer(),
            ),
          ],
        ),
      );
    });
  }

  Widget _buildList() {
    if (controller.isLoading.value && controller.items.isEmpty) {
      return const Center(
        child: CircularProgressIndicator(color: AppColors.primary),
      );
    }

    if (controller.items.isEmpty) {
      return Center(
        child: Padding(
          padding: EdgeInsets.symmetric(horizontal: 24.w),
          child: Text(
            'No surah audio has been downloaded yet.',
            style: AppTextStyles.body,
            textAlign: TextAlign.center,
          ),
        ),
      );
    }

    final playerOpen =
        Get.isRegistered<QuranAudioController>() &&
        Get.find<QuranAudioController>().showPlayer;
    return RefreshIndicator(
      color: AppColors.primary,
      onRefresh: controller.load,
      child: ListView.separated(
        physics: const AlwaysScrollableScrollPhysics(),
        padding: EdgeInsets.fromLTRB(20.w, 0, 20.w, playerOpen ? 96.h : 24.h),
        itemCount: controller.items.length,
        separatorBuilder: (_, _) => SizedBox(height: 10.h),
        itemBuilder: (context, index) {
          return _DownloadTile(item: controller.items[index]);
        },
      ),
    );
  }
}

class _DownloadTile extends GetView<DownloadedAudioController> {
  const _DownloadTile({required this.item});

  final DownloadedAudioItem item;

  @override
  Widget build(BuildContext context) {
    return Obx(() {
      final audio = Get.find<QuranAudioController>();
      final playing = audio.isPlayingDownloaded(
        surahNumber: item.surahNumber,
        reciterId: item.reciterId,
      );
      return Container(
        padding: EdgeInsets.fromLTRB(14.w, 12.h, 8.w, 12.h),
        decoration: BoxDecoration(
          color: AppColors.surface,
          borderRadius: BorderRadius.circular(16.r),
          border: Border.all(color: AppColors.divider),
        ),
        child: Row(
          children: [
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    item.surahName,
                    style: AppTextStyles.heading3,
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                  ),
                  SizedBox(height: 4.h),
                  Text(item.sizeLabel, style: AppTextStyles.bodySmall),
                ],
              ),
            ),
            IconButton(
              tooltip: playing ? 'Pause' : 'Play',
              onPressed: () => controller.play(item),
              icon: Icon(
                playing ? Icons.pause_rounded : Icons.play_arrow_rounded,
                color: AppColors.primary,
              ),
            ),
            IconButton(
              tooltip: 'Delete',
              onPressed: () => _confirmDelete(context),
              icon: Icon(Icons.delete_outline_rounded, color: AppColors.error),
            ),
          ],
        ),
      );
    });
  }

  Future<void> _confirmDelete(BuildContext context) async {
    final confirmed = await showDialog<bool>(
      context: context,
      builder: (context) {
        return AlertDialog(
          title: const Text('Delete download'),
          content: Text('Remove ${item.surahName} from this device?'),
          actions: [
            TextButton(
              onPressed: () => Navigator.of(context).pop(false),
              child: const Text('Cancel'),
            ),
            TextButton(
              onPressed: () => Navigator.of(context).pop(true),
              child: const Text('Delete'),
            ),
          ],
        );
      },
    );
    if (confirmed == true) await controller.delete(item);
  }
}

class DownloadedAudioBinding extends Bindings {
  @override
  void dependencies() {
    if (Get.isRegistered<DownloadedAudioController>()) {
      Get.delete<DownloadedAudioController>(force: true);
    }
    Get.put(DownloadedAudioController());
  }
}
