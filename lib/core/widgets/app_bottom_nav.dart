import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:flutter_svg/flutter_svg.dart';

import '../constants/app_assets.dart';
import '../constants/app_colors.dart';
import '../constants/app_text_styles.dart';

class AppBottomNav extends StatelessWidget {
  const AppBottomNav({
    super.key,
    required this.currentIndex,
    required this.onTap,
  });

  final int currentIndex;
  final ValueChanged<int> onTap;

  @override
  Widget build(BuildContext context) {
    final items = <_NavItem>[
      const _NavItem(label: 'Home', asset: AppAssets.homeIcon),
      const _NavItem(label: 'Quran', asset: AppAssets.quranIcon),
      const _NavItem(label: 'Hadith', icon: Icons.menu_book_rounded),
      const _NavItem(label: 'Audio', asset: AppAssets.audioIcon),
      const _NavItem(label: 'Profile', asset: AppAssets.profileIcon),
    ];

    return Container(
      decoration: BoxDecoration(
        color: AppColors.surface,
        boxShadow: [
          BoxShadow(
            color: AppColors.primary.withValues(alpha: 0.06),
            blurRadius: 16.r,
            offset: Offset(0, -4.h),
          ),
        ],
      ),
      child: SafeArea(
        top: false,
        child: Padding(
          padding: EdgeInsets.symmetric(horizontal: 4.w, vertical: 8.h),
          child: Row(
            children: List.generate(items.length, (index) {
              final item = items[index];
              final isActive = index == currentIndex;
              final color = isActive
                  ? (AppColors.isDark ? AppColors.white : AppColors.primary)
                  : AppColors.textSecondary;

              return Expanded(
                child: InkWell(
                  onTap: () => onTap(index),
                  borderRadius: BorderRadius.circular(12.r),
                  child: Padding(
                    padding: EdgeInsets.symmetric(vertical: 6.h),
                    child: Column(
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        if (item.icon != null)
                          Icon(item.icon, size: 22.sp, color: color)
                        else
                          SvgPicture.asset(
                            item.asset!,
                            width: 22.w,
                            height: 22.w,
                            colorFilter: ColorFilter.mode(
                              color,
                              BlendMode.srcIn,
                            ),
                          ),
                        SizedBox(height: 4.h),
                        Text(
                          item.label,
                          maxLines: 1,
                          overflow: TextOverflow.ellipsis,
                          style: AppTextStyles.caption.copyWith(
                            color: color,
                            fontSize: 10.sp,
                            fontWeight:
                                isActive ? FontWeight.w600 : FontWeight.w400,
                          ),
                        ),
                      ],
                    ),
                  ),
                ),
              );
            }),
          ),
        ),
      ),
    );
  }
}

class _NavItem {
  const _NavItem({required this.label, this.asset, this.icon});

  final String label;
  final String? asset;
  final IconData? icon;
}
