import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:get/get.dart';

import '../../core/constants/app_colors.dart';
import '../../core/constants/app_text_styles.dart';
import '../../core/controllers/bookmark_controller.dart';
import '../../core/controllers/settings_controller.dart';
import '../../core/widgets/widgets.dart';
import 'surah_detail_controller.dart';

class SurahDetailScreen extends GetView<SurahDetailController> {
  const SurahDetailScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Obx(() {
      Get.find<SettingsController>().isDarkMode.value;
      return Scaffold(
        backgroundColor: AppColors.background,
        appBar: CustomAppBar(
          title: controller.title,
          actions: [
            HifzModeButton(
              isActive: controller.isHifzMode.value,
              onPressed: controller.toggleHifzMode,
            ),
            Obx(() {
              final bookmarks = Get.find<BookmarkController>();
              bookmarks.items.length;
              final number = controller.surah.value?.number ?? 0;
              return BookmarkIconButton(
                isBookmarked: number > 0 &&
                    bookmarks.isTranslationBookmarked(number),
                onPressed: controller.toggleBookmark,
              );
            }),
          ],
        ),
        body: _buildBody(),
      );
    });
  }

  Widget _buildBody() {
    if (controller.isLoading.value) {
      return const Center(
        child: CircularProgressIndicator(color: AppColors.primary),
      );
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
                onPressed: controller.load,
                child: const Text('Retry'),
              ),
            ],
          ),
        ),
      );
    }

    return Stack(
      children: [
        ListView.builder(
          padding: EdgeInsets.fromLTRB(20.w, 8.h, 20.w, 120.h),
          itemCount: controller.ayahs.length,
          itemBuilder: (context, index) {
            final ayah = controller.ayahs[index];
            final showHeader = controller.isJuzMode &&
                ayah.surahNumber > 0 &&
                (index == 0 ||
                    controller.ayahs[index - 1].surahNumber !=
                        ayah.surahNumber);
            return Column(
              children: [
                if (index == 0 && controller.showBismillah) ...[
                  const _BismillahHeader(),
                  SizedBox(height: 16.h),
                ],
                if (showHeader)
                  Padding(
                    padding: EdgeInsets.only(
                      top: index == 0 && !controller.showBismillah ? 0 : 8.h,
                      bottom: 12.h,
                    ),
                    child: _SurahSectionHeader(
                      title: ayah.surahEnglishName.isEmpty
                          ? 'Surah ${ayah.surahNumber}'
                          : ayah.surahEnglishName,
                    ),
                  ),
                _AyahCard(
                  ayahId: controller.hifzIdFor(ayah),
                  number: ayah.number,
                  arabic: ayah.arabic,
                  translation: ayah.translation,
                  isHighlighted: controller.isHighlighted(ayah),
                  isRtl: controller.isRtlTranslation,
                ),
              ],
            );
          },
        ),
        const Positioned(
          left: 0,
          right: 0,
          bottom: 0,
          child: _FloatingPlayer(),
        ),
      ],
    );
  }
}

class _SurahSectionHeader extends StatelessWidget {
  const _SurahSectionHeader({required this.title});

  final String title;

  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,
      padding: EdgeInsets.symmetric(vertical: 10.h, horizontal: 14.w),
      decoration: BoxDecoration(
        color: AppColors.mint,
        borderRadius: BorderRadius.circular(12.r),
      ),
      child: Text(
        title,
        style: AppTextStyles.heading3.copyWith(color: AppColors.onMint),
        textAlign: TextAlign.center,
      ),
    );
  }
}

class _BismillahHeader extends StatelessWidget {
  const _BismillahHeader();

  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,
      padding: EdgeInsets.symmetric(vertical: 20.h, horizontal: 16.w),
      decoration: BoxDecoration(
        color: AppColors.mint,
        borderRadius: BorderRadius.circular(16.r),
      ),
      child: Obx(() {
        final settings = Get.find<SettingsController>();
        return Text(
          'بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ',
          textAlign: TextAlign.center,
          textDirection: TextDirection.rtl,
          style: settings.arabicStyle(
            color: AppColors.onMint,
            fontWeight: FontWeight.w700,
          ),
        );
      }),
    );
  }
}

class _AyahCard extends GetView<SurahDetailController> {
  const _AyahCard({
    required this.ayahId,
    required this.number,
    required this.arabic,
    required this.translation,
    required this.isHighlighted,
    required this.isRtl,
  });

  final int ayahId;
  final int number;
  final String arabic;
  final String translation;
  final bool isHighlighted;
  final bool isRtl;

  @override
  Widget build(BuildContext context) {
    return Obx(() {
      final settings = Get.find<SettingsController>();
      final hifz = controller.isHifzMode.value;
      final revealed = controller.isAyahRevealed(ayahId);

      return Padding(
        padding: EdgeInsets.only(bottom: 12.h),
        child: Material(
          color: isHighlighted || (hifz && revealed)
              ? AppColors.mint
              : AppColors.surface,
          borderRadius: BorderRadius.circular(16.r),
          child: InkWell(
            onTap: hifz ? () => controller.toggleAyahReveal(ayahId) : null,
            borderRadius: BorderRadius.circular(16.r),
            child: AnimatedContainer(
              duration: const Duration(milliseconds: 280),
              curve: Curves.easeOut,
              padding: EdgeInsets.all(16.w),
              decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(16.r),
                border: hifz && revealed
                    ? Border.all(
                        color: AppColors.primary.withValues(alpha: 0.4),
                        width: 1.2,
                      )
                    : Border.all(color: Colors.transparent, width: 1.2),
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: [
                  Align(
                    alignment: Alignment.centerLeft,
                    child: Container(
                      width: 28.w,
                      height: 28.w,
                      alignment: Alignment.center,
                      decoration: const BoxDecoration(
                        color: AppColors.primary,
                        shape: BoxShape.circle,
                      ),
                      child: FittedBox(
                        child: Padding(
                          padding: EdgeInsets.all(4.w),
                          child: Text(
                            '$number',
                            style: AppTextStyles.caption.copyWith(
                              color: AppColors.white,
                              fontWeight: FontWeight.w600,
                            ),
                          ),
                        ),
                      ),
                    ),
                  ),
                  SizedBox(height: 10.h),
                  HifzAyahText(
                    text: arabic,
                    style: settings.arabicStyle(),
                    isHifzMode: hifz,
                    isRevealed: revealed,
                    showHighlight: false,
                    tappable: false,
                    onReveal: () => controller.toggleAyahReveal(ayahId),
                  ),
                  if (!hifz) ...[
                    SizedBox(height: 10.h),
                    Text(
                      translation,
                      textAlign: isRtl ? TextAlign.right : TextAlign.left,
                      textDirection:
                          isRtl ? TextDirection.rtl : TextDirection.ltr,
                      style: settings.translationStyle(
                        color: AppColors.textSecondary,
                      ),
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

class _FloatingPlayer extends GetView<SurahDetailController> {
  const _FloatingPlayer();

  @override
  Widget build(BuildContext context) {
    return SafeArea(
      top: false,
      child: Padding(
        padding: EdgeInsets.fromLTRB(16.w, 0, 16.w, 12.h),
        child: Container(
          padding: EdgeInsets.symmetric(horizontal: 16.w, vertical: 12.h),
          decoration: BoxDecoration(
            color: AppColors.primary,
            borderRadius: BorderRadius.circular(20.r),
            boxShadow: [
              BoxShadow(
                color: AppColors.primary.withValues(alpha: 0.25),
                blurRadius: 16.r,
                offset: Offset(0, 6.h),
              ),
            ],
          ),
          child: Obx(
            () => Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                Row(
                  children: [
                    Expanded(
                      child: Text(
                        controller.reciterName,
                        style: AppTextStyles.bodySmall.copyWith(
                          color: AppColors.white,
                          fontWeight: FontWeight.w600,
                        ),
                        maxLines: 1,
                        overflow: TextOverflow.ellipsis,
                      ),
                    ),
                    GestureDetector(
                      onTap: controller.skipBack,
                      child: Icon(
                        Icons.skip_previous_rounded,
                        color: AppColors.white,
                        size: 28.sp,
                      ),
                    ),
                    SizedBox(width: 8.w),
                    GestureDetector(
                      onTap: controller.togglePlay,
                      child: Container(
                        width: 40.w,
                        height: 40.w,
                        decoration: const BoxDecoration(
                          color: AppColors.white,
                          shape: BoxShape.circle,
                        ),
                        child: controller.isAudioLoading
                            ? Padding(
                                padding: EdgeInsets.all(10.w),
                                child: CircularProgressIndicator(
                                  strokeWidth: 2.w,
                                  color: AppColors.primary,
                                ),
                              )
                            : Icon(
                                controller.isPlayingThisSurah
                                    ? Icons.pause_rounded
                                    : Icons.play_arrow_rounded,
                                color: AppColors.primary,
                                size: 24.sp,
                              ),
                      ),
                    ),
                    SizedBox(width: 8.w),
                    GestureDetector(
                      onTap: controller.skipForward,
                      child: Icon(
                        Icons.skip_next_rounded,
                        color: AppColors.white,
                        size: 28.sp,
                      ),
                    ),
                  ],
                ),
                SizedBox(height: 4.h),
                SliderTheme(
                  data: SliderThemeData(
                    trackHeight: 4.h,
                    thumbShape: RoundSliderThumbShape(enabledThumbRadius: 6.r),
                    overlayShape: RoundSliderOverlayShape(overlayRadius: 12.r),
                    activeTrackColor: AppColors.white,
                    inactiveTrackColor: AppColors.white.withValues(alpha: 0.2),
                    thumbColor: AppColors.white,
                  ),
                  child: Slider(
                    value: controller.progress,
                    onChanged: controller.seekToProgress,
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
