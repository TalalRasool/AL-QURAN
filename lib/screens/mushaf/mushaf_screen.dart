import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:get/get.dart';

import '../../core/constants/app_colors.dart';
import '../../core/constants/app_text_styles.dart';
import '../../core/controllers/bookmark_controller.dart';
import '../../core/controllers/settings_controller.dart';
import '../../core/data/models/ayah.dart';
import '../../core/data/models/juz.dart';
import '../../core/widgets/widgets.dart';
import 'mushaf_controller.dart';

class MushafScreen extends GetView<MushafController> {
  const MushafScreen({super.key, this.initialPage});

  final int? initialPage;

  @override
  Widget build(BuildContext context) {
    return Obx(() {
      Get.find<SettingsController>().isDarkMode.value;
      controller.isLoading.value;
      controller.errorMessage.value;
      controller.isHifzMode.value;
      controller.pages.length;
      return Scaffold(
        backgroundColor: AppColors.background,
        appBar: PreferredSize(
          preferredSize: Size.fromHeight(56.h),
          child: Obx(() {
            Get.find<SettingsController>().isDarkMode.value;
            controller.currentPage.value;
            controller.isHifzMode.value;
            return CustomAppBar(
              title: controller.title,
              actions: [
                HifzModeButton(
                  isActive: controller.isHifzMode.value,
                  onPressed: controller.toggleHifzMode,
                ),
                Obx(() {
                  final bookmarks = Get.find<BookmarkController>();
                  bookmarks.items.length;
                  return BookmarkIconButton(
                    isBookmarked: bookmarks.isMushafBookmarked(
                      controller.currentPage.value,
                    ),
                    onPressed: controller.toggleBookmark,
                  );
                }),
                IconButton(
                  tooltip: 'Index',
                  onPressed: _openIndex,
                  icon: Icon(
                    Icons.list_rounded,
                    size: 24.sp,
                    color: AppColors.textPrimary,
                  ),
                ),
              ],
            );
          }),
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

    return PageView.builder(
      controller: controller.pageController,
      reverse: true,
      itemCount: MushafController.pageCount,
      onPageChanged: controller.onPageChanged,
      itemBuilder: (context, index) {
        return _MushafPage(ayahs: controller.ayahsForIndex(index));
      },
    );
  }

  void _openIndex() {
    Get.bottomSheet(
      Material(
        color: AppColors.surface,
        borderRadius: BorderRadius.vertical(top: Radius.circular(20.r)),
        clipBehavior: Clip.antiAlias,
        child: DefaultTabController(
          length: 2,
          child: SizedBox(
            height: Get.height * 0.78,
            child: Column(
              children: [
                SizedBox(height: 10.h),
                Container(
                  width: 40.w,
                  height: 4.h,
                  decoration: BoxDecoration(
                    color: AppColors.greyLight,
                    borderRadius: BorderRadius.circular(4.r),
                  ),
                ),
                SizedBox(height: 8.h),
                Text('Index', style: AppTextStyles.heading2),
                TabBar(
                  labelColor: AppColors.isDark
                      ? AppColors.white
                      : AppColors.primary,
                  unselectedLabelColor: AppColors.textSecondary,
                  indicatorColor: AppColors.isDark
                      ? AppColors.white
                      : AppColors.primary,
                  labelStyle: AppTextStyles.bodySmall.copyWith(
                    fontWeight: FontWeight.w700,
                  ),
                  tabs: const [
                    Tab(text: 'Surahs'),
                    Tab(text: 'Juz'),
                  ],
                ),
                Expanded(
                  child: TabBarView(
                    children: [
                      _SurahIndexList(controller: controller),
                      _JuzIndexList(controller: controller),
                    ],
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
      isScrollControlled: true,
      backgroundColor: Colors.transparent,
    );
  }
}

class _SurahIndexList extends StatelessWidget {
  const _SurahIndexList({required this.controller});

  final MushafController controller;

  @override
  Widget build(BuildContext context) {
    return Obx(() {
      final items = controller.surahs;
      if (items.isEmpty) {
        return Center(
          child: Text('No surahs found', style: AppTextStyles.body),
        );
      }

      return ListView.separated(
        padding: EdgeInsets.fromLTRB(16.w, 12.h, 16.w, 24.h),
        itemCount: items.length,
        separatorBuilder: (_, _) => SizedBox(height: 10.h),
        itemBuilder: (context, index) {
          final surah = items[index];
          return SurahTileCard(
            number: surah.number,
            englishName: surah.englishName,
            arabicName: surah.arabicName,
            meaning: surah.meaning,
            verseCount: surah.verseCount,
            onTap: () => controller.jumpToSurah(surah.number),
          );
        },
      );
    });
  }
}

class _JuzIndexList extends StatelessWidget {
  const _JuzIndexList({required this.controller});

  final MushafController controller;

  @override
  Widget build(BuildContext context) {
    return ListView.separated(
      padding: EdgeInsets.fromLTRB(16.w, 12.h, 16.w, 24.h),
      itemCount: Juz.all.length,
      separatorBuilder: (_, _) => SizedBox(height: 10.h),
      itemBuilder: (context, index) {
        final juz = Juz.all[index];
        return SurahTileCard(
          number: juz.number,
          englishName: juz.englishName,
          arabicName: juz.arabicName,
          meaning: 'Juz ${juz.number}',
          onTap: () => controller.jumpToJuz(juz.number),
        );
      },
    );
  }
}

class _MushafPage extends StatelessWidget {
  const _MushafPage({required this.ayahs});

  final List<Ayah> ayahs;

  @override
  Widget build(BuildContext context) {
    final settings = Get.find<SettingsController>();
    if (ayahs.isEmpty) {
      return Center(
        child: Text('No ayahs on this page.', style: AppTextStyles.bodySmall),
      );
    }

    return Obx(() {
      settings.arabicTextSize.value;
      settings.arabicFont.value;
      final hifz = Get.find<MushafController>().isHifzMode.value;
      return SingleChildScrollView(
        padding: EdgeInsets.fromLTRB(20.w, 12.h, 20.w, 28.h),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            for (final section in _sections)
              ...[
                _SurahBanner(title: section.title),
                if (hifz)
                  _HifzSection(ayahs: section.ayahs)
                else
                  Text.rich(
                    TextSpan(
                      children: [
                        for (final ayah in section.ayahs) ...[
                          TextSpan(
                            text: ayah.arabic,
                            style: settings.arabicStyle(height: 2.2),
                          ),
                          TextSpan(
                            text: ' \uFD3F${ayah.number}\uFD3E ',
                            style: settings.arabicStyle(
                              color: AppColors.primaryLight,
                              fontWeight: FontWeight.w700,
                              height: 2.2,
                            ),
                          ),
                        ],
                      ],
                    ),
                    textAlign: TextAlign.justify,
                    textDirection: TextDirection.rtl,
                  ),
                SizedBox(height: 8.h),
              ],
          ],
        ),
      );
    });
  }

  List<_MushafSection> get _sections {
    final sections = <_MushafSection>[];
    for (final ayah in ayahs) {
      final title = ayah.surahEnglishName.isEmpty
          ? 'Surah ${ayah.surahNumber}'
          : ayah.surahEnglishName;
      if (sections.isEmpty || sections.last.surahNumber != ayah.surahNumber) {
        sections.add(
          _MushafSection(
            surahNumber: ayah.surahNumber,
            title: title,
            ayahs: [ayah],
          ),
        );
      } else {
        sections.last.ayahs.add(ayah);
      }
    }
    return sections;
  }
}

class _HifzSection extends GetView<MushafController> {
  const _HifzSection({required this.ayahs});

  final List<Ayah> ayahs;

  @override
  Widget build(BuildContext context) {
    final settings = Get.find<SettingsController>();
    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        for (final ayah in ayahs) ...[
          Obx(() {
            final id = controller.hifzIdFor(ayah);
            final revealed = controller.isAyahRevealed(id);
            return Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                HifzAyahText(
                  text: ayah.arabic,
                  style: settings.arabicStyle(height: 2.2),
                  isHifzMode: true,
                  isRevealed: revealed,
                  onReveal: () => controller.toggleAyahReveal(id),
                ),
                Align(
                  alignment: Alignment.centerRight,
                  child: Text(
                    '\uFD3F${ayah.number}\uFD3E',
                    textDirection: TextDirection.rtl,
                    style: settings.arabicStyle(
                      color: AppColors.primaryLight,
                      fontWeight: FontWeight.w700,
                      height: 2.2,
                    ),
                  ),
                ),
                SizedBox(height: 6.h),
              ],
            );
          }),
        ],
      ],
    );
  }
}

class _MushafSection {
  _MushafSection({
    required this.surahNumber,
    required this.title,
    required this.ayahs,
  });

  final int surahNumber;
  final String title;
  final List<Ayah> ayahs;
}

class _SurahBanner extends StatelessWidget {
  const _SurahBanner({required this.title});

  final String title;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: EdgeInsets.symmetric(vertical: 12.h),
      child: SizedBox(
        width: double.infinity,
        child: Container(
          padding: EdgeInsets.symmetric(vertical: 8.h, horizontal: 12.w),
          decoration: BoxDecoration(
            color: AppColors.mint,
            borderRadius: BorderRadius.circular(12.r),
          ),
          alignment: Alignment.center,
          child: Text(
            title,
            textAlign: TextAlign.center,
            style: AppTextStyles.heading3.copyWith(color: AppColors.onMint),
          ),
        ),
      ),
    );
  }
}
