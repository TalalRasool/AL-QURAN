import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:get/get.dart';
import 'package:google_fonts/google_fonts.dart';

import '../../core/constants/app_colors.dart';
import '../../core/constants/app_text_styles.dart';
import '../../core/controllers/settings_controller.dart';
import '../../core/widgets/widgets.dart';
import 'offline_quran_controller.dart';
import 'study_models.dart';

class QuranStudyScreen extends GetView<OfflineQuranController> {
  const QuranStudyScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Obx(() {
      final settings = Get.find<SettingsController>();
      settings.isDarkMode.value;
      settings.arabicTextSize.value;
      settings.translationTextSize.value;
      final reading = controller.isReading.value;
      return PopScope(
        canPop: !reading,
        onPopInvokedWithResult: (didPop, _) {
          if (!didPop) controller.closeReader();
        },
        child: Scaffold(
          backgroundColor: AppColors.background,
          appBar: CustomAppBar(
            title: controller.title,
            onBack: reading ? controller.closeReader : null,
          ),
          body: reading ? _ReaderBody(
                    settings: settings,
                    language: controller.languageCode.value,
                    isRtl: controller.isRtl,
                  )
              : const _IndexBody(),
        ),
      );
    });
  }
}

class _IndexBody extends GetView<OfflineQuranController> {
  const _IndexBody();

  @override
  Widget build(BuildContext context) {
    return Obx(() {
      Get.find<SettingsController>().isDarkMode.value;
      return Column(
        children: [
          Padding(
            padding: EdgeInsets.fromLTRB(20.w, 0, 20.w, 0),
            child: Column(
              children: [
                CustomTextField(
                  hintText: controller.isJuzTab
                      ? 'Search Surah or Juz'
                      : 'Search Surah',
                  onChanged: controller.onSearch,
                ),
                SizedBox(height: 14.h),
                PillTabs(
                  labels: const ['Surah', 'Juz'],
                  selectedIndex: controller.primaryTab.value,
                  onChanged: controller.onPrimaryTabChanged,
                ),
              ],
            ),
          ),
          SizedBox(height: 12.h),
          Expanded(
            child: controller.isJuzTab
                ? const _JuzIndexList()
                : const _SurahIndexList(),
          ),
        ],
      );
    });
  }
}

class _SurahIndexList extends GetView<OfflineQuranController> {
  const _SurahIndexList();

  @override
  Widget build(BuildContext context) {
    return Obx(() {
      Get.find<SettingsController>().isDarkMode.value;
      controller.searchQuery.value;
      final surahs = controller.filteredSurahs;
      if (surahs.isEmpty) {
        return Center(
          child: Text('No surahs found', style: AppTextStyles.body),
        );
      }

      return ListView.separated(
        padding: EdgeInsets.fromLTRB(20.w, 0, 20.w, 24.h),
        itemCount: surahs.length,
        separatorBuilder: (_, _) => SizedBox(height: 10.h),
        itemBuilder: (context, index) {
          final surah = surahs[index];
          return SurahTileCard(
            number: surah.number,
            englishName: surah.englishName,
            arabicName: surah.arabicName,
            meaning: surah.meaning,
            verseCount: surah.verseCount,
            onTap: () => controller.loadSurah(surah.number),
          );
        },
      );
    });
  }
}

class _JuzIndexList extends GetView<OfflineQuranController> {
  const _JuzIndexList();

  @override
  Widget build(BuildContext context) {
    return Obx(() {
      Get.find<SettingsController>().isDarkMode.value;
      controller.searchQuery.value;
      final juzList = controller.filteredJuz;
      if (juzList.isEmpty) {
        return Center(
          child: Text('No juz found', style: AppTextStyles.body),
        );
      }

      return ListView.separated(
        padding: EdgeInsets.fromLTRB(20.w, 0, 20.w, 24.h),
        itemCount: juzList.length,
        separatorBuilder: (_, _) => SizedBox(height: 10.h),
        itemBuilder: (context, index) {
          final juz = juzList[index];
          return SurahTileCard(
            number: juz.number,
            englishName: juz.englishName,
            arabicName: juz.arabicName,
            meaning: 'Juz ${juz.number}',
            onTap: () => controller.loadJuz(juz.number),
          );
        },
      );
    });
  }
}

class _ReaderBody extends GetView<OfflineQuranController> {
  const _ReaderBody({
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
                _SurahHeader(
                  number: ayah.surahNumber,
                  name: controller.surahName(ayah.surahNumber),
                ),
              _AyahCard(
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

class _SurahHeader extends StatelessWidget {
  const _SurahHeader({required this.number, required this.name});

  final int number;
  final String name;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: EdgeInsets.fromLTRB(4.w, 4.h, 4.w, 12.h),
      child: Text(
        '$number. $name',
        textAlign: TextAlign.center,
        style: AppTextStyles.heading3.copyWith(color: AppColors.primary),
      ),
    );
  }
}

class _AyahCard extends StatelessWidget {
  const _AyahCard({
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
    final arabicStyle = settings.arabicStyle(height: 1.7).copyWith(
          fontSize: 26.sp,
          fontWeight: FontWeight.w600,
        );
    final wordStyle = settings
        .translationStyle(color: AppColors.primarySoft, height: 1.7)
        .copyWith(fontSize: 12.sp);
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
          Wrap(
            textDirection: TextDirection.rtl,
            alignment: WrapAlignment.start,
            spacing: 10.w,
            runSpacing: 12.h,
            children: [
              for (final word in ayah.words)
                _WordCell(
                  arabic: word.arabic,
                  translation: word.textFor(language),
                  arabicStyle: arabicStyle,
                  translationStyle: wordStyle,
                  isRtl: isRtl,
                ),
            ],
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

class _WordCell extends StatelessWidget {
  const _WordCell({
    required this.arabic,
    required this.translation,
    required this.arabicStyle,
    required this.translationStyle,
    required this.isRtl,
  });

  final String arabic;
  final String translation;
  final TextStyle arabicStyle;
  final TextStyle translationStyle;
  final bool isRtl;

  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisSize: MainAxisSize.min,
      children: [
        Text(
          arabic,
          textDirection: TextDirection.rtl,
          textAlign: TextAlign.center,
          style: arabicStyle,
        ),
        SizedBox(height: 4.h),
        Text(
          translation,
          textDirection: isRtl ? TextDirection.rtl : TextDirection.ltr,
          textAlign: TextAlign.center,
          style: translationStyle,
        ),
      ],
    );
  }
}
