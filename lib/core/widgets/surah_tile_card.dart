import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';

import '../constants/app_colors.dart';
import '../constants/app_text_styles.dart';

/// Surah list row: numbered circle, English name, trailing Arabic name.
class SurahTileCard extends StatelessWidget {
  const SurahTileCard({
    super.key,
    required this.number,
    required this.englishName,
    required this.arabicName,
    this.meaning,
    this.verseCount,
    this.isActive = false,
    this.onTap,
  });

  final int number;
  final String englishName;
  final String arabicName;
  final String? meaning;
  final int? verseCount;
  final bool isActive;
  final VoidCallback? onTap;

  @override
  Widget build(BuildContext context) {
    return Material(
      color: AppColors.surface,
      borderRadius: BorderRadius.circular(16.r),
      child: InkWell(
        onTap: onTap,
        borderRadius: BorderRadius.circular(16.r),
        child: Container(
          padding: EdgeInsets.symmetric(horizontal: 14.w, vertical: 12.h),
          decoration: BoxDecoration(
            borderRadius: BorderRadius.circular(16.r),
            boxShadow: [
              BoxShadow(
                color: AppColors.primary.withValues(alpha: 0.04),
                blurRadius: 12.r,
                offset: Offset(0, 4.h),
              ),
            ],
          ),
          child: Row(
            children: [
              _NumberCircle(number: number, isActive: isActive),
              SizedBox(width: 12.w),
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      englishName,
                      style: AppTextStyles.heading3,
                      maxLines: 1,
                      overflow: TextOverflow.ellipsis,
                    ),
                    if (_subtitle != null) ...[
                      SizedBox(height: 2.h),
                      Text(
                        _subtitle!,
                        style: AppTextStyles.bodySmall,
                        maxLines: 1,
                        overflow: TextOverflow.ellipsis,
                      ),
                    ],
                  ],
                ),
              ),
              SizedBox(width: 8.w),
              Flexible(
                child: Text(
                  arabicName,
                  style: AppTextStyles.arabicTitle,
                  textDirection: TextDirection.rtl,
                  maxLines: 1,
                  overflow: TextOverflow.ellipsis,
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  String? get _subtitle {
    final parts = <String>[
      if (meaning != null && meaning!.isNotEmpty) meaning!,
      if (verseCount != null) '$verseCount Verses',
    ];
    if (parts.isEmpty) return null;
    return parts.join('  •  ');
  }
}

class _NumberCircle extends StatelessWidget {
  const _NumberCircle({required this.number, required this.isActive});

  final int number;
  final bool isActive;

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 44.w,
      height: 44.w,
      alignment: Alignment.center,
      decoration: BoxDecoration(
        shape: BoxShape.circle,
        color: isActive ? AppColors.primary : AppColors.greyLight,
      ),
      child: Text(
        '$number',
        style: AppTextStyles.heading3.copyWith(
          color: isActive ? AppColors.onPrimary : AppColors.textPrimary,
          fontSize: 14.sp,
        ),
        maxLines: 1,
        overflow: TextOverflow.ellipsis,
      ),
    );
  }
}
