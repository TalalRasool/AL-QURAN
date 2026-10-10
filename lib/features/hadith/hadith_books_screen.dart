import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:get/get.dart';

import '../../core/constants/app_colors.dart';
import '../../core/constants/app_text_styles.dart';
import '../../core/controllers/settings_controller.dart';
import 'data/hadith_l10n.dart';
import 'data/hadith_models.dart';
import 'hadith_books_controller.dart';
import 'hadith_script_style.dart';

class HadithBooksScreen extends GetView<HadithBooksController> {
  const HadithBooksScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Obx(() {
      Get.find<SettingsController>().isDarkMode.value;
      final lang = HadithL10n.watchLanguage();
      final isRtl = HadithL10n.isRtl(lang);
      return Directionality(
        textDirection: isRtl ? TextDirection.rtl : TextDirection.ltr,
        child: SafeArea(
          bottom: false,
          child: Padding(
            padding: EdgeInsets.symmetric(horizontal: 20.w),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                SizedBox(height: 8.h),
                Text(
                  HadithL10n.ui('hadith', lang),
                  style: hadithLanguageStyle(
                    lang,
                    fontSize: 20.sp,
                    fontWeight: FontWeight.w600,
                    color: AppColors.textPrimary,
                    height: 1.3,
                  ),
                ),
                SizedBox(height: 6.h),
                Text(
                  HadithL10n.ui('subtitle', lang),
                  style: hadithLanguageStyle(
                    lang,
                    fontSize: 12.sp,
                    color: AppColors.textSecondary,
                    height: 1.4,
                  ),
                ),
                SizedBox(height: 16.h),
                Expanded(child: _buildBody(lang)),
              ],
            ),
          ),
        ),
      );
    });
  }

  Widget _buildBody(String lang) {
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
                child: Text(
                  HadithL10n.ui('retry', lang),
                  style: hadithLanguageStyle(
                    lang,
                    fontSize: 14.sp,
                    fontWeight: FontWeight.w600,
                    color: AppColors.primary,
                  ),
                ),
              ),
            ],
          ),
        ),
      );
    }

    final books = controller.books;
    if (books.isEmpty) {
      return Center(
        child: Text(
          HadithL10n.ui('no_books', lang),
          style: hadithLanguageStyle(
            lang,
            fontSize: 14.sp,
            color: AppColors.textPrimary,
            height: 1.5,
          ),
          textAlign: TextAlign.center,
        ),
      );
    }

    return ListView.separated(
      padding: EdgeInsets.only(bottom: 16.h),
      itemCount: books.length,
      separatorBuilder: (_, _) => SizedBox(height: 12.h),
      itemBuilder: (context, index) {
        return _HadithBookCard(
          book: books[index],
          languageCode: lang,
          onTap: () => controller.openBook(books[index]),
        );
      },
    );
  }
}

class _HadithBookCard extends StatelessWidget {
  const _HadithBookCard({
    required this.book,
    required this.languageCode,
    required this.onTap,
  });

  final HadithBook book;
  final String languageCode;
  final VoidCallback onTap;

  @override
  Widget build(BuildContext context) {
    final isRtl = HadithL10n.isRtl(languageCode);
    final name = HadithL10n.bookName(
      book.id,
      fallback: book.name,
      languageCode: languageCode,
    );
    return Material(
      color: AppColors.surface,
      borderRadius: BorderRadius.circular(20.r),
      child: InkWell(
        onTap: onTap,
        borderRadius: BorderRadius.circular(20.r),
        child: Container(
          padding: EdgeInsets.all(16.w),
          decoration: BoxDecoration(
            borderRadius: BorderRadius.circular(20.r),
            border: Border.all(
              color: AppColors.primary.withValues(alpha: 0.08),
            ),
          ),
          child: Row(
            children: [
              Container(
                width: 56.w,
                height: 56.w,
                decoration: BoxDecoration(
                  color: AppColors.mint,
                  borderRadius: BorderRadius.circular(16.r),
                ),
                child: Icon(
                  Icons.menu_book_rounded,
                  color: AppColors.onMint,
                  size: 28.sp,
                ),
              ),
              SizedBox(width: 14.w),
              Expanded(
                child: Column(
                  crossAxisAlignment: isRtl
                      ? CrossAxisAlignment.end
                      : CrossAxisAlignment.start,
                  children: [
                    Text(
                      name,
                      style: hadithLanguageStyle(
                        languageCode,
                        fontSize: 16.sp,
                        fontWeight: FontWeight.w600,
                        color: AppColors.textPrimary,
                        height: 1.35,
                      ),
                      maxLines: 3,
                      overflow: TextOverflow.ellipsis,
                      textDirection:
                          isRtl ? TextDirection.rtl : TextDirection.ltr,
                    ),
                    SizedBox(height: 4.h),
                    Text(
                      HadithL10n.ui('edition_line', languageCode),
                      style: hadithLanguageStyle(
                        languageCode,
                        fontSize: 12.sp,
                        color: AppColors.textSecondary,
                        height: 1.4,
                      ),
                      maxLines: 1,
                      overflow: TextOverflow.ellipsis,
                      textDirection:
                          isRtl ? TextDirection.rtl : TextDirection.ltr,
                    ),
                  ],
                ),
              ),
              Icon(
                isRtl
                    ? Icons.chevron_left_rounded
                    : Icons.chevron_right_rounded,
                color: AppColors.textSecondary,
                size: 22.sp,
              ),
            ],
          ),
        ),
      ),
    );
  }
}
