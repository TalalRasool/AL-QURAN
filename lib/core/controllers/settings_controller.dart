import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:get/get.dart';
import 'package:get_storage/get_storage.dart';
import 'package:google_fonts/google_fonts.dart';

import '../constants/app_colors.dart';
import '../data/models/translation_edition.dart';
import '../data/offline_translations.dart';
import '../data/quran_repository.dart';
import '../services/storage_service.dart';

class SettingsController extends GetxService with WidgetsBindingObserver {
  static const arabicSizeKey = 'settings_arabic_text_size';
  static const translationSizeKey = 'settings_translation_text_size';
  static const arabicFontKey = 'settings_arabic_font';
  static const themeModeKey = 'settings_theme_mode';

  static const uthmaniFont = 'Uthmani';
  static const indoPakFont = 'IndoPak';

  static const themeLight = 'light';
  static const themeDark = 'dark';
  static const themeSystem = 'system';

  final arabicTextSize = 28.0.obs;
  final translationTextSize = 16.0.obs;
  final arabicFont = uthmaniFont.obs;
  final themeModeName = themeLight.obs;
  final isDarkMode = false.obs;

  late final GetStorage _box;

  ThemeMode get themeMode {
    switch (themeModeName.value) {
      case themeDark:
        return ThemeMode.dark;
      case themeSystem:
        return ThemeMode.system;
      default:
        return ThemeMode.light;
    }
  }

  String get themeLabel {
    switch (themeModeName.value) {
      case themeDark:
        return 'Dark';
      case themeSystem:
        return 'System';
      default:
        return 'Light';
    }
  }

  String get textSizeLabel {
    final size = arabicTextSize.value;
    if (size <= 24) return 'Small';
    if (size <= 32) return 'Medium';
    return 'Large';
  }

  Future<SettingsController> init() async {
    _box = GetStorage();
    arabicTextSize.value =
        (_box.read(arabicSizeKey) as num?)?.toDouble() ?? 28.0;
    translationTextSize.value =
        (_box.read(translationSizeKey) as num?)?.toDouble() ?? 16.0;
    arabicFont.value = _box.read(arabicFontKey) as String? ?? uthmaniFont;
    themeModeName.value = _box.read(themeModeKey) as String? ?? themeLight;
    Get.changeThemeMode(themeMode);
    _syncDarkMode();
    WidgetsBinding.instance.addObserver(this);
    return this;
  }

  @override
  void onClose() {
    WidgetsBinding.instance.removeObserver(this);
    super.onClose();
  }

  @override
  void didChangePlatformBrightness() {
    if (themeModeName.value == themeSystem) {
      _syncDarkMode();
    }
  }

  void setArabicTextSize(double value) {
    arabicTextSize.value = value;
    _box.write(arabicSizeKey, value);
  }

  void setTranslationTextSize(double value) {
    translationTextSize.value = value;
    _box.write(translationSizeKey, value);
  }

  void setArabicFont(String font) {
    arabicFont.value = font;
    _box.write(arabicFontKey, font);
  }

  void setThemeModeName(String mode) {
    themeModeName.value = mode;
    _box.write(themeModeKey, mode);
    Get.changeThemeMode(themeMode);
    _syncDarkMode();
  }

  void _syncDarkMode() {
    isDarkMode.value = switch (themeMode) {
      ThemeMode.dark => true,
      ThemeMode.light => false,
      ThemeMode.system => Get.isPlatformDarkMode,
    };
    AppColors.syncDarkMode(isDarkMode.value);
    SystemChrome.setSystemUIOverlayStyle(
      SystemUiOverlayStyle(
        statusBarColor: Colors.transparent,
        statusBarIconBrightness:
            isDarkMode.value ? Brightness.light : Brightness.dark,
        statusBarBrightness:
            isDarkMode.value ? Brightness.dark : Brightness.light,
      ),
    );
  }

  TextStyle arabicStyle({
    Color? color,
    FontWeight? fontWeight,
    double? height,
  }) {
    final size = arabicTextSize.value;
    final textColor = color ?? AppColors.textPrimary;
    if (arabicFont.value == indoPakFont) {
      return GoogleFonts.notoNastaliqUrdu(
        fontSize: size,
        color: textColor,
        height: height ?? 2.2,
        fontWeight: fontWeight ?? FontWeight.w400,
      );
    }
    return GoogleFonts.notoNaskhArabic(
      fontSize: size,
      color: textColor,
      height: height ?? 2.0,
      fontWeight: fontWeight ?? FontWeight.w400,
    );
  }

  String get translationLanguageCode {
    if (!Get.isRegistered<StorageService>()) return 'en';
    return OfflineTranslations.editionFor(
      Get.find<StorageService>().selectedTranslationId.value,
    ).language;
  }

  List<TranslationEdition> get translationEditions =>
      OfflineTranslations.editions;

  Future<void> applyTranslation(TranslationEdition edition) async {
    if (!Get.isRegistered<StorageService>()) return;
    final canonical = OfflineTranslations.editionFor(edition.identifier);
    await Get.find<StorageService>().saveTranslation(
      identifier: canonical.identifier,
      name: canonical.authorName,
      language: canonical.languageLabel,
      direction: canonical.direction,
    );
    if (Get.isRegistered<QuranRepository>()) {
      await Get.find<QuranRepository>().clearAyahCaches();
    }
  }

  TextStyle translationStyle({Color? color, double? height}) {
    final size = translationTextSize.value;
    final textColor = color ?? AppColors.textPrimary;
    final language = translationLanguageCode;
    if (language == 'ur') {
      return GoogleFonts.notoNastaliqUrdu(
        fontSize: size,
        color: textColor,
        height: height ?? 1.8,
        fontWeight: FontWeight.w400,
      );
    }
    if (language == 'hi') {
      return GoogleFonts.notoSansDevanagari(
        fontSize: size,
        color: textColor,
        height: height ?? 1.6,
        fontWeight: FontWeight.w400,
      );
    }
    if (language == 'bn') {
      return GoogleFonts.notoSansBengali(
        fontSize: size,
        color: textColor,
        height: height ?? 1.6,
        fontWeight: FontWeight.w400,
      );
    }
    return GoogleFonts.poppins(
      fontSize: size,
      color: textColor,
      height: height ?? 1.5,
      fontWeight: FontWeight.w400,
    );
  }
}
