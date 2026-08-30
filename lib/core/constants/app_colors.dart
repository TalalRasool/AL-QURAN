import 'package:flutter/material.dart';
import 'package:get/get.dart';

/// Brand palette extracted from the premium green Quran UI.
class AppColors {
  AppColors._();

  static bool? _forcedDark;

  static void syncDarkMode(bool isDark) => _forcedDark = isDark;

  static bool get isDark {
    if (_forcedDark != null) return _forcedDark!;
    try {
      return Get.isDarkMode;
    } catch (_) {
      return false;
    }
  }

  /// Deep forest green — hero cards, primary buttons, active nav.
  static const Color primary = Color(0xFF1B4332);

  /// Medium green — tasbih ring, compass needle, secondary accents.
  static const Color primaryLight = Color(0xFF2D6A4F);

  /// Softer mint green for chips, progress tracks, and highlights.
  static const Color primarySoft = Color(0xFF40916C);

  static const Color _lightMint = Color(0xFFE8F5E9);
  static const Color _darkMint = Color(0xFF1C1C1C);

  static Color get mint => isDark ? _darkMint : _lightMint;

  static const Color _lightBackground = Color(0xFFF7FBF9);
  static const Color _darkBackground = Color(0xFF000000);

  static Color get background => isDark ? _darkBackground : _lightBackground;

  static const Color white = Color(0xFFFFFFFF);
  static const Color black = Color(0xFF000000);

  static const Color _lightSurface = Color(0xFFFFFFFF);
  static const Color _darkSurface = Color(0xFF121212);

  static Color get surface => isDark ? _darkSurface : _lightSurface;

  /// Text and icons that sit on [mint] fills.
  static Color get onMint => isDark ? white : primary;

  /// Accent that stays readable on black dark-mode backgrounds.
  static Color get accent => isDark ? primarySoft : primary;

  static const Color _lightTextPrimary = Color(0xFF1A1A1A);
  static const Color _darkTextPrimary = Color(0xFFF4F7F5);

  static Color get textPrimary => isDark ? _darkTextPrimary : _lightTextPrimary;

  static const Color _lightTextSecondary = Color(0xFF6B7280);
  static const Color _darkTextSecondary = Color(0xFF9CA8A2);

  static Color get textSecondary =>
      isDark ? _darkTextSecondary : _lightTextSecondary;

  static const Color _lightTextHint = Color(0xFF9CA3AF);
  static const Color _darkTextHint = Color(0xFF6B7872);

  static Color get textHint => isDark ? _darkTextHint : _lightTextHint;

  static const Color onPrimary = Color(0xFFFFFFFF);

  static const Color _lightGrey = Color(0xFFE8EEEA);
  static const Color _darkGrey = Color(0xFF2A2A2A);

  static Color get greyLight => isDark ? _darkGrey : _lightGrey;

  static const Color _lightSearchFill = Color(0xFFF0F4F2);
  static const Color _darkSearchFill = Color(0xFF1A1A1A);

  static Color get searchFill => isDark ? _darkSearchFill : _lightSearchFill;

  static const Color _lightDivider = Color(0xFFE5E7EB);
  static const Color _darkDivider = Color(0xFF2E2E2E);

  static Color get divider => isDark ? _darkDivider : _lightDivider;

  static const Color error = Color(0xFFDC2626);
}
