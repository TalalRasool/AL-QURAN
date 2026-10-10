import 'package:flutter/material.dart';
import 'package:get/get.dart';

import '../../core/controllers/settings_controller.dart';

/// Readable typeface for a Hadith label in the selected app language.
TextStyle hadithLanguageStyle(
  String languageCode, {
  double? fontSize,
  FontWeight? fontWeight,
  Color? color,
  double? height,
}) {
  final style = Get.find<SettingsController>().translationStyle(
    languageCode: languageCode,
    color: color,
    height: height,
  );
  if (fontSize == null && fontWeight == null) return style;
  return style.copyWith(fontSize: fontSize, fontWeight: fontWeight);
}
