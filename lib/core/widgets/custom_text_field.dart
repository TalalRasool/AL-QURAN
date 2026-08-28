import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';

import '../constants/app_colors.dart';
import '../constants/app_text_styles.dart';

/// Lightly rounded search field matching the Surah list screen.
class CustomTextField extends StatelessWidget {
  const CustomTextField({
    super.key,
    this.controller,
    this.hintText = 'Search',
    this.prefixIcon,
    this.suffixIcon,
    this.onChanged,
    this.onSubmitted,
    this.keyboardType,
    this.textInputAction = TextInputAction.search,
    this.obscureText = false,
    this.showPrefixIcon = true,
    this.textCapitalization = TextCapitalization.none,
    this.autofillHints,
    this.fillColor,
    this.radius,
  });

  final TextEditingController? controller;
  final String hintText;
  final Widget? prefixIcon;
  final Widget? suffixIcon;
  final ValueChanged<String>? onChanged;
  final ValueChanged<String>? onSubmitted;
  final TextInputType? keyboardType;
  final TextInputAction textInputAction;
  final bool obscureText;
  final bool showPrefixIcon;
  final TextCapitalization textCapitalization;
  final Iterable<String>? autofillHints;
  final Color? fillColor;
  final double? radius;

  @override
  Widget build(BuildContext context) {
    return TextField(
      controller: controller,
      onChanged: onChanged,
      onSubmitted: onSubmitted,
      keyboardType: keyboardType,
      textInputAction: textInputAction,
      obscureText: obscureText,
      textCapitalization: textCapitalization,
      autofillHints: autofillHints,
      style: AppTextStyles.body,
      cursorColor: AppColors.primary,
      decoration: InputDecoration(
        filled: true,
        fillColor: fillColor ?? AppColors.searchFill,
        hintText: hintText,
        hintStyle: AppTextStyles.body.copyWith(color: AppColors.textHint),
        prefixIcon: showPrefixIcon
            ? prefixIcon ??
                Icon(
                  Icons.search_rounded,
                  size: 22.sp,
                  color: AppColors.textSecondary,
                )
            : prefixIcon,
        suffixIcon: suffixIcon,
        contentPadding: EdgeInsets.symmetric(
          horizontal: 16.w,
          vertical: 14.h,
        ),
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(radius ?? 14.r),
          borderSide: BorderSide.none,
        ),
        enabledBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(radius ?? 14.r),
          borderSide: BorderSide.none,
        ),
        focusedBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(radius ?? 14.r),
          borderSide: BorderSide(color: AppColors.primary, width: 1.w),
        ),
      ),
    );
  }
}
