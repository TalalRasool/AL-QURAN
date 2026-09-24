import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:get/get.dart';
import 'package:google_fonts/google_fonts.dart';

import '../../core/constants/app_colors.dart';
import '../../core/constants/app_text_styles.dart';
import '../../core/controllers/settings_controller.dart';
import '../../core/widgets/widgets.dart';
import '../study/study_models.dart';
import 'quran_reading_controller.dart';

/// Reading Mode: Arabic + full ayah translation only (no word-by-word).
class QuranReadingScreen extends GetView<QuranReadingController> {
  const QuranReadingScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Obx(() {
      final settings = Get.find<SettingsController>();
      settings.isDarkMode.value;
      settings.arabicTextSize.value;
      settings.translationTextSize.value;
      controller.languageCode.value;
      return Scaffold(
        backgroundColor: AppColors.background,
        appBar: CustomAppBar(title: controller.title),
        body: _ReadingBody(
          settings: settings,
          language: controller.languageCode.value,
          isRtl: controller.isRtl,
        ),
      );
    });
  }
}

class _ReadingBody extends GetView<QuranReadingController> {
  const _ReadingBody({
    required this.settings,
    required this.language,
    required this.isRtl,
  });

  final SettingsController settings;
  final String language;
  final bool isRtl;

  @override
  Widget build(BuildContext context) {
    return Obx(() {
      if (controller.isLoading.value && controller.ayahs.isEmpty) {
        return const Center(
          child: CircularProgressIndicator(color: AppColors.primary),
        );
      }

      if (controller.errorMessage.value != null && controller.ayahs.isEmpty) {
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
                  onPressed: () {
                    final juz = controller.selectedJuz.value;
                    if (juz != null) {
                      controller.loadJuz(juz);
                    } else {
                      controller.loadSurah(controller.selectedSurah.value);
                    }
                  },
                  child: const Text('Retry'),
                ),
              ],
            ),
          ),
        );
      }

      return Directionality(
        textDirection: isRtl ? TextDirection.rtl : TextDirection.ltr,
        child: ListView.builder(
          padding: EdgeInsets.fromLTRB(16.w, 8.h, 16.w, 28.h),
          itemCount: controller.ayahs.length,
          itemBuilder: (context, index) {
            final ayah = controller.ayahs[index];
            final showSurahHeader = controller.isJuzReading &&
                (index == 0 ||
                    ayah.surahNumber !=
                        controller.ayahs[index - 1].surahNumber);
            return Column(
              children: [
                if (showSurahHeader)
                  Padding(
                    padding: EdgeInsets.fromLTRB(4.w, 4.h, 4.w, 12.h),
                    child: Text(
                      '${ayah.surahNumber}. ${controller.surahName(ayah.surahNumber)}',
                      textAlign: TextAlign.center,
                      style: AppTextStyles.heading3.copyWith(
                        color: AppColors.primary,
                      ),
                    ),
                  ),
                _ReadingAyahCard(
                  ayah: ayah,
                  language: language,
                  isRtl: isRtl,
                  settings: settings,
                ),
              ],
            );
          },
        ),
      );
    });
  }
}

class _ReadingAyahCard extends StatelessWidget {
  const _ReadingAyahCard({
    required this.ayah,
    required this.language,
    required this.isRtl,
    required this.settings,
  });

  final OfflineAyah ayah;
  final String language;
  final bool isRtl;
  final SettingsController settings;

  @override
  Widget build(BuildContext context) {
    final arabicStyle = settings.arabicStyle(height: 1.9);
    final fullStyle = settings.translationStyle(height: 2.0);
    final translation = ayah.fullTextFor(language);
    final badgeAlignment =
        isRtl ? Alignment.centerRight : Alignment.centerLeft;

    return Container(
      width: double.infinity,
      margin: EdgeInsets.only(bottom: 14.h),
      padding: EdgeInsets.fromLTRB(16.w, 16.h, 16.w, 16.h),
      decoration: BoxDecoration(
        color: AppColors.surface,
        borderRadius: BorderRadius.circular(18.r),
        border: Border.all(color: AppColors.divider),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          Align(
            alignment: badgeAlignment,
            child: Container(
              padding: EdgeInsets.symmetric(horizontal: 10.w, vertical: 4.h),
              decoration: BoxDecoration(
                color: AppColors.mint,
                borderRadius: BorderRadius.circular(20.r),
              ),
              child: Text(
                '${OfflineLanguage.ayahLabel(language)} ${ayah.ayahNumber}',
                textDirection: isRtl ? TextDirection.rtl : TextDirection.ltr,
                style: _badgeStyle(language),
              ),
            ),
          ),
          SizedBox(height: 14.h),
          Text(
            ayah.arabic,
            textDirection: TextDirection.rtl,
            textAlign: TextAlign.right,
            style: arabicStyle,
          ),
          if (translation.isNotEmpty) ...[
            SizedBox(height: 16.h),
            Divider(color: AppColors.divider, height: 1.h),
            SizedBox(height: 14.h),
            Text(
              translation,
              textDirection: isRtl ? TextDirection.rtl : TextDirection.ltr,
              textAlign: isRtl ? TextAlign.right : TextAlign.left,
              style: fullStyle,
            ),
          ],
        ],
      ),
    );
  }

  TextStyle _badgeStyle(String languageCode) {
    final color = AppColors.onMint;
    switch (OfflineLanguage.normalize(languageCode)) {
      case 'ur':
        return GoogleFonts.notoNastaliqUrdu(
          fontSize: 12.sp,
          color: color,
          fontWeight: FontWeight.w600,
        );
      case 'hi':
        return GoogleFonts.notoSansDevanagari(
          fontSize: 12.sp,
          color: color,
          fontWeight: FontWeight.w600,
        );
      case 'bn':
        return GoogleFonts.notoSansBengali(
          fontSize: 12.sp,
          color: color,
          fontWeight: FontWeight.w600,
        );
      default:
        return AppTextStyles.bodySmall.copyWith(
          color: color,
          fontWeight: FontWeight.w600,
        );
    }
  }
}
