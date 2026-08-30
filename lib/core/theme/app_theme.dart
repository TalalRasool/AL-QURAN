import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';

import '../constants/app_colors.dart';
import '../constants/app_text_styles.dart';

class AppTheme {
  AppTheme._();

  static ThemeData get light {
    return _build(
      brightness: Brightness.light,
      scaffold: const Color(0xFFF7FBF9),
      surface: const Color(0xFFFFFFFF),
      onSurface: const Color(0xFF1A1A1A),
      fill: const Color(0xFFF0F4F2),
      divider: const Color(0xFFE5E7EB),
      statusIcons: Brightness.dark,
    );
  }

  static ThemeData get dark {
    return _build(
      brightness: Brightness.dark,
      scaffold: const Color(0xFF000000),
      surface: const Color(0xFF121212),
      onSurface: const Color(0xFFF4F7F5),
      fill: const Color(0xFF1A1A1A),
      divider: const Color(0xFF2E2E2E),
      statusIcons: Brightness.light,
    );
  }

  static ThemeData _build({
    required Brightness brightness,
    required Color scaffold,
    required Color surface,
    required Color onSurface,
    required Color fill,
    required Color divider,
    required Brightness statusIcons,
  }) {
    return ThemeData(
      useMaterial3: true,
      brightness: brightness,
      scaffoldBackgroundColor: scaffold,
      primaryColor: AppColors.primary,
      colorScheme: ColorScheme(
        brightness: brightness,
        primary: AppColors.primary,
        onPrimary: AppColors.onPrimary,
        secondary: AppColors.primaryLight,
        onSecondary: AppColors.onPrimary,
        surface: surface,
        onSurface: onSurface,
        error: AppColors.error,
        onError: AppColors.white,
      ),
      appBarTheme: AppBarTheme(
        backgroundColor: Colors.transparent,
        elevation: 0,
        scrolledUnderElevation: 0,
        centerTitle: true,
        foregroundColor: onSurface,
        systemOverlayStyle: SystemUiOverlayStyle(
          statusBarColor: Colors.transparent,
          statusBarIconBrightness: statusIcons,
          statusBarBrightness:
              statusIcons == Brightness.dark ? Brightness.light : Brightness.dark,
        ),
      ),
      dividerColor: divider,
      splashFactory: InkRipple.splashFactory,
      sliderTheme: SliderThemeData(
        activeTrackColor: AppColors.primary,
        thumbColor: AppColors.primary,
      ),
      textTheme: TextTheme(
        headlineLarge: AppTextStyles.heading1.copyWith(color: onSurface),
        headlineMedium: AppTextStyles.heading2.copyWith(color: onSurface),
        titleMedium: AppTextStyles.heading3.copyWith(color: onSurface),
        bodyMedium: AppTextStyles.body.copyWith(color: onSurface),
        bodySmall: AppTextStyles.bodySmall,
        labelLarge: AppTextStyles.button,
      ),
      inputDecorationTheme: InputDecorationTheme(
        filled: true,
        fillColor: fill,
        hintStyle: AppTextStyles.bodySmall.copyWith(color: AppColors.textHint),
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(14.r),
          borderSide: BorderSide.none,
        ),
      ),
    );
  }
}
