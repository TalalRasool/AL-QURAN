import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:google_fonts/google_fonts.dart';

import 'app_colors.dart';

/// Shared typography. Getters are used so `.sp` is evaluated after
/// [ScreenUtilInit], not at class-load time.
class AppTextStyles {
  AppTextStyles._();

  // ── English (Poppins) ──────────────────────────────────────────────

  static TextStyle get heading1 => GoogleFonts.poppins(
        fontSize: 24.sp,
        fontWeight: FontWeight.w700,
        color: AppColors.textPrimary,
        height: 1.3,
      );

  static TextStyle get heading2 => GoogleFonts.poppins(
        fontSize: 20.sp,
        fontWeight: FontWeight.w600,
        color: AppColors.textPrimary,
        height: 1.3,
      );

  static TextStyle get heading3 => GoogleFonts.poppins(
        fontSize: 16.sp,
        fontWeight: FontWeight.w600,
        color: AppColors.textPrimary,
        height: 1.35,
      );

  static TextStyle get subtitle => GoogleFonts.poppins(
        fontSize: 14.sp,
        fontWeight: FontWeight.w500,
        color: AppColors.textSecondary,
        height: 1.4,
      );

  static TextStyle get body => GoogleFonts.poppins(
        fontSize: 14.sp,
        fontWeight: FontWeight.w400,
        color: AppColors.textPrimary,
        height: 1.5,
      );

  static TextStyle get bodySmall => GoogleFonts.poppins(
        fontSize: 12.sp,
        fontWeight: FontWeight.w400,
        color: AppColors.textSecondary,
        height: 1.4,
      );

  static TextStyle get caption => GoogleFonts.poppins(
        fontSize: 11.sp,
        fontWeight: FontWeight.w400,
        color: AppColors.textSecondary,
        height: 1.3,
      );

  static TextStyle get button => GoogleFonts.poppins(
        fontSize: 15.sp,
        fontWeight: FontWeight.w600,
        color: AppColors.onPrimary,
        height: 1.2,
      );

  // ── Arabic (Naskh / Amiri) ─────────────────────────────────────────

  /// Surah names and display Arabic.
  static TextStyle get arabicTitle => GoogleFonts.amiri(
        fontSize: 22.sp,
        fontWeight: FontWeight.w700,
        color: AppColors.textPrimary,
        height: 1.8,
      );

  /// Ayah body text — swap in an Uthmani font asset later if needed.
  static TextStyle get arabicBody => GoogleFonts.notoNaskhArabic(
        fontSize: 20.sp,
        fontWeight: FontWeight.w400,
        color: AppColors.textPrimary,
        height: 2.0,
      );
}
