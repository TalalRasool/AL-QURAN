import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:get/get.dart';
import 'package:scrollable_positioned_list/scrollable_positioned_list.dart';

import '../../core/constants/app_colors.dart';
import '../../core/constants/app_text_styles.dart';
import '../../core/controllers/bookmark_controller.dart';
import '../../core/controllers/quran_audio_controller.dart';
import '../../core/controllers/settings_controller.dart';
import '../../core/widgets/widgets.dart';
import '../audio/quran_audio_actions.dart';
import '../audio/quran_bottom_player.dart';
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
            QuranAudioActions(
              surahNumber: controller.playbackSurahNumber,
              surahName: controller.playbackSurahName,
            ),
          ],
        ),
        body: Stack(
          children: [
            _buildBody(context),
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

  Widget _buildBody(BuildContext context) {
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
        ScrollablePositionedList.builder(
          initialScrollIndex: controller.ayahs.isEmpty
              ? 0
              : controller.revealIndexValue.value.clamp(
                  0,
                  controller.ayahs.length - 1,
                ),
          itemScrollController: controller.itemScrollController,
          itemPositionsListener: controller.itemPositionsListener,
          padding: EdgeInsets.fromLTRB(
            20.w,
            8.h,
            20.w,
            quranListBottomPadding(
              context,
              Get.find<QuranAudioController>().showPlayer,
            ),
          ),
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
