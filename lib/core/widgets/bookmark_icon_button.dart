import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:get/get.dart';

import '../constants/app_colors.dart';
import '../constants/app_text_styles.dart';

class BookmarkIconButton extends StatelessWidget {
  const BookmarkIconButton({
    super.key,
    required this.isBookmarked,
    required this.onPressed,
  });

  final bool isBookmarked;
  final VoidCallback onPressed;

  @override
  Widget build(BuildContext context) {
    return IconButton(
      onPressed: onPressed,
      tooltip: isBookmarked ? 'Remove bookmark' : 'Add bookmark',
      icon: Icon(
        isBookmarked ? Icons.bookmark : Icons.bookmark_border,
        color: isBookmarked ? AppColors.primary : Colors.grey,
        size: 24.sp,
      ),
    );
  }
}

void showBookmarkSnackbar({required bool added}) {
  Get.snackbar(
    'Success',
    added ? 'Added to Bookmarks!' : 'Removed from Bookmarks',
    snackPosition: SnackPosition.BOTTOM,
    duration: const Duration(seconds: 2),
    backgroundColor: AppColors.primary,
    colorText: AppColors.white,
    margin: EdgeInsets.fromLTRB(16.w, 0, 16.w, 16.h),
    borderRadius: 12.r,
    titleText: Text(
      'Success',
      style: AppTextStyles.heading3.copyWith(color: AppColors.white),
    ),
    messageText: Text(
      added ? 'Added to Bookmarks!' : 'Removed from Bookmarks',
      style: AppTextStyles.bodySmall.copyWith(color: AppColors.white),
    ),
  );
}
