import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:flutter_svg/flutter_svg.dart';
import 'package:get/get.dart';

import '../../core/constants/app_assets.dart';
import '../../core/constants/app_colors.dart';
import '../../core/constants/app_text_styles.dart';
import '../../core/controllers/bookmark_controller.dart';
import '../../core/controllers/settings_controller.dart';
import '../../core/data/json_utils.dart';
import '../../core/data/models/app_bookmark.dart';
import '../../core/widgets/widgets.dart';
import '../../features/hadith/data/hadith_l10n.dart';

class BookmarksScreen extends StatefulWidget {
  const BookmarksScreen({super.key});

  @override
  State<BookmarksScreen> createState() => _BookmarksScreenState();
}

class _BookmarksScreenState extends State<BookmarksScreen> {
  final _tabIndex = 0.obs;

  static const _tabs = [
    BookmarkType.translation,
    BookmarkType.mushaf,
    BookmarkType.hadith,
    BookmarkType.dua,
  ];

  @override
  Widget build(BuildContext context) {
    final bookmarks = Get.find<BookmarkController>();

    return Obx(() {
      Get.find<SettingsController>().isDarkMode.value;
      HadithL10n.watchLanguage();
      bookmarks.items.length;
      final type = _tabs[_tabIndex.value.clamp(0, _tabs.length - 1)];
      final items = bookmarks.ofType(type);

      return Scaffold(
        backgroundColor: AppColors.background,
        appBar: const CustomAppBar(title: 'Bookmarks'),
        body: Padding(
          padding: EdgeInsets.symmetric(horizontal: 20.w),
          child: Column(
            children: [
              PillTabs(
                labels: const ['Quran', 'Mushaf', 'Hadiths', 'Duas'],
                selectedIndex: _tabIndex.value,
                onChanged: (index) => _tabIndex.value = index,
              ),
              SizedBox(height: 12.h),
              Expanded(
                child: items.isEmpty
                    ? _EmptyBookmarks(type: type)
                    : ListView.separated(
                        padding: EdgeInsets.only(bottom: 20.h),
                        itemCount: items.length,
                        separatorBuilder: (_, _) => SizedBox(height: 10.h),
                        itemBuilder: (context, index) {
                          final item = items[index];
                          if (item.type == BookmarkType.translation) {
                            return SurahTileCard(
                              number: asInt(item.payload['surahNumber']),
                              englishName: item.title,
                              arabicName:
                                  '${item.payload['arabicName'] ?? ''}',
                              verseCount: asInt(item.payload['verseCount']) > 0
                                  ? asInt(item.payload['verseCount'])
                                  : null,
                              onTap: () => bookmarks.open(item),
                            );
                          }
                          if (item.type == BookmarkType.hadith) {
                            return _BookmarkTile(
                              item: item,
                              title: _hadithTitle(item),
                              subtitle: _hadithSubtitle(item),
                              onTap: () => bookmarks.open(item),
                              onRemove: () => bookmarks.remove(item.id),
                            );
                          }
                          return _BookmarkTile(
                            item: item,
                            title: item.title,
                            subtitle: item.subtitle,
                            onTap: () => bookmarks.open(item),
                            onRemove: () => bookmarks.remove(item.id),
                          );
                        },
                      ),
              ),
            ],
          ),
        ),
      );
    });
  }

  String _hadithTitle(AppBookmark item) {
    final bookId = asInt(item.payload['bookId']);
    final english = '${item.payload['bookName'] ?? item.title}'.trim();
    return HadithL10n.bookName(bookId, fallback: english);
  }

  String _hadithSubtitle(AppBookmark item) {
    final number = '${item.payload['hadithNumber'] ?? ''}'.trim();
    final englishChapter = '${item.payload['chapterName'] ?? ''}'.trim();
    final numberLabel = number.isEmpty
        ? HadithL10n.ui('hadith')
        : HadithL10n.hadithNumberLabel(number);
    if (englishChapter.isEmpty) return numberLabel;
    return '$numberLabel · ${HadithL10n.chapterName(englishChapter)}';
  }
}

class _BookmarkTile extends StatelessWidget {
  const _BookmarkTile({
    required this.item,
    required this.title,
    required this.subtitle,
    required this.onTap,
    required this.onRemove,
  });

  final AppBookmark item;
  final String title;
  final String subtitle;
  final VoidCallback onTap;
  final VoidCallback onRemove;

  @override
  Widget build(BuildContext context) {
    final isRtl = item.type == BookmarkType.hadith && HadithL10n.isRtl();
    return Material(
      color: AppColors.surface,
      borderRadius: BorderRadius.circular(16.r),
      child: InkWell(
        onTap: onTap,
        borderRadius: BorderRadius.circular(16.r),
        child: Padding(
          padding: EdgeInsets.fromLTRB(14.w, 12.h, 4.w, 12.h),
          child: Row(
            children: [
              Container(
                width: 44.w,
                height: 44.w,
                decoration: BoxDecoration(
                  color: AppColors.mint,
                  borderRadius: BorderRadius.circular(12.r),
                ),
                alignment: Alignment.center,
                child: Icon(
                  _iconFor(item.type),
                  color: AppColors.primary,
                  size: 22.sp,
                ),
              ),
              SizedBox(width: 12.w),
              Expanded(
                child: Column(
                  crossAxisAlignment: isRtl
                      ? CrossAxisAlignment.end
                      : CrossAxisAlignment.start,
                  children: [
                    Text(
                      title,
                      style: AppTextStyles.heading3,
                      maxLines: item.type == BookmarkType.hadith ? 3 : 1,
                      overflow: TextOverflow.ellipsis,
                      textDirection:
                          isRtl ? TextDirection.rtl : TextDirection.ltr,
                    ),
                    if (subtitle.trim().isNotEmpty) ...[
                      SizedBox(height: 2.h),
                      Text(
                        subtitle,
                        style: AppTextStyles.bodySmall,
                        maxLines: item.type == BookmarkType.hadith ? 4 : 2,
                        overflow: TextOverflow.ellipsis,
                        textDirection:
                            isRtl ? TextDirection.rtl : TextDirection.ltr,
                      ),
                    ],
                  ],
                ),
              ),
              IconButton(
                tooltip: 'Remove bookmark',
                onPressed: onRemove,
                icon: Icon(
                  Icons.bookmark,
                  color: AppColors.primary,
                  size: 22.sp,
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  IconData _iconFor(BookmarkType type) {
    switch (type) {
      case BookmarkType.translation:
        return Icons.menu_book_outlined;
      case BookmarkType.mushaf:
        return Icons.auto_stories_outlined;
      case BookmarkType.hadith:
        return Icons.menu_book;
      case BookmarkType.dua:
        return Icons.favorite_outline;
    }
  }
}

class _EmptyBookmarks extends StatelessWidget {
  const _EmptyBookmarks({required this.type});

  final BookmarkType type;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: EdgeInsets.symmetric(horizontal: 12.w),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Container(
            width: 72.w,
            height: 72.w,
            decoration: BoxDecoration(
              color: AppColors.mint,
              shape: BoxShape.circle,
            ),
            padding: EdgeInsets.all(20.w),
            child: SvgPicture.asset(
              AppAssets.bookmarkIcon,
              colorFilter: ColorFilter.mode(
                AppColors.onMint,
                BlendMode.srcIn,
              ),
            ),
          ),
          SizedBox(height: 16.h),
          Text(
            'No ${type.label} yet',
            style: AppTextStyles.heading3,
            textAlign: TextAlign.center,
          ),
          SizedBox(height: 8.h),
          Text(
            _message,
            style: AppTextStyles.bodySmall,
            textAlign: TextAlign.center,
          ),
        ],
      ),
    );
  }

  String get _message {
    switch (type) {
      case BookmarkType.translation:
        return 'Tap the bookmark icon while reading a Surah to save it here.';
      case BookmarkType.mushaf:
        return 'Tap the bookmark icon on a Mushaf page to save it here.';
      case BookmarkType.hadith:
        return 'Tap the bookmark icon on a Hadith to save it here.';
      case BookmarkType.dua:
        return 'Tap the bookmark icon on a Dua to save it here.';
    }
  }
}
