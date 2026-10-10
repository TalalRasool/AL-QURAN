import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:get/get.dart';

import '../../core/constants/app_assets.dart';
import '../../core/constants/app_text_styles.dart';
import '../../core/controllers/settings_controller.dart';
import '../../core/data/json_utils.dart';
import '../../core/services/storage_service.dart';
import 'worship_guide_model.dart';
import 'worship_l10n.dart';

class WorshipController extends GetxController {
  final categories = <WorshipCategory>[].obs;
  final guides = <WorshipGuideItem>[].obs;
  final isLoading = false.obs;
  final errorMessage = RxnString();

  String get languageCode {
    if (!Get.isRegistered<SettingsController>()) return 'en';
    return WorshipL10n.code(
      Get.find<SettingsController>().translationLanguageCode,
    );
  }

  bool get isRtl => WorshipL10n.isRtl(languageCode);

  /// Touch language, theme, and type size so [Obx] rebuilds with them.
  void watchAppearance() {
    if (Get.isRegistered<StorageService>()) {
      Get.find<StorageService>().selectedTranslationId.value;
    }
    if (!Get.isRegistered<SettingsController>()) return;
    final settings = Get.find<SettingsController>();
    settings.isDarkMode.value;
    settings.translationTextSize.value;
  }

  /// Namaz, Hajj, Zakat, and the other topics, each with its own articles.
  Map<String, List<WorshipGuideItem>> get guidesByCategory {
    final grouped = <String, List<WorshipGuideItem>>{};
    for (final item in guides) {
      grouped.putIfAbsent(item.category, () => []).add(item);
    }
    return grouped;
  }

  List<WorshipGuideItem> guidesForCategory(String categoryId) =>
      guidesByCategory[categoryId] ?? const [];

  WorshipCategory? categoryById(String categoryId) {
    for (final category in categories) {
      if (category.id == categoryId) return category;
    }
    return null;
  }

  String categoryLabel(String categoryId) {
    final category = categoryById(categoryId);
    return WorshipL10n.categoryName(
      categoryId,
      languageCode,
      fallback: category?.englishLabel,
    );
  }

  TextStyle readingStyle({
    double? fontSize,
    FontWeight? fontWeight,
    Color? color,
    double? height,
    String? languageCode,
  }) {
    final code = languageCode ?? this.languageCode;
    if (!Get.isRegistered<SettingsController>()) {
      return AppTextStyles.body.copyWith(
        fontSize: fontSize,
        fontWeight: fontWeight,
        color: color,
        height: height,
      );
    }
    final style = Get.find<SettingsController>().translationStyle(
      languageCode: code,
      color: color,
      height: height,
    );
    if (fontSize == null && fontWeight == null) return style;
    return style.copyWith(fontSize: fontSize, fontWeight: fontWeight);
  }

  @override
  void onInit() {
    super.onInit();
    loadWorshipData();
  }

  Future<void> loadWorshipData() async {
    isLoading.value = true;
    errorMessage.value = null;
    try {
      final raw = await rootBundle.loadString(AppAssets.worshipGuideJson);
      final decoded = jsonDecode(raw);
      if (decoded is! Map) {
        throw const FormatException('Worship guide JSON is not an object');
      }
      final dataset = WorshipDataset.fromJson(asStringKeyMap(decoded));
      categories.assignAll(dataset.categories);
      guides.assignAll(dataset.guides);
      if (guides.isEmpty) {
        errorMessage.value = WorshipL10n.text(
          WorshipL10n.loadError,
          languageCode,
        );
      }
    } catch (_) {
      categories.clear();
      guides.clear();
      errorMessage.value = WorshipL10n.text(
        WorshipL10n.loadError,
        languageCode,
      );
    } finally {
      isLoading.value = false;
    }
  }
}
