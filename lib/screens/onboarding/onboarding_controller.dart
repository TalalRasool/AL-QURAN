import 'package:flutter/widgets.dart';
import 'package:get/get.dart';

import '../../core/data/models/translation_edition.dart';
import '../../core/data/offline_translations.dart';
import '../../core/data/quran_repository.dart';
import '../../core/routes/app_routes.dart';
import '../../core/services/storage_service.dart';

class OnboardingController extends GetxController {
  static const defaultCountry = 'Pakistan';
  static const countries = [
    'Afghanistan',
    'Bangladesh',
    'Canada',
    'Egypt',
    'India',
    'Indonesia',
    'Iran',
    'Iraq',
    'Malaysia',
    'Morocco',
    'Nigeria',
    'Pakistan',
    'Qatar',
    'Saudi Arabia',
    'South Africa',
    'Turkey',
    'United Arab Emirates',
    'United Kingdom',
    'United States',
    'Yemen',
  ];

  final nameController = TextEditingController();
  final selectedCountry = defaultCountry.obs;

  final languages = <TranslationEdition>[].obs;
  final selectedLanguage = Rxn<TranslationEdition>();
  final isLoadingLanguages = false.obs;
  final isSaving = false.obs;
  final errorMessage = RxnString();

  final QuranRepository _quran = Get.find<QuranRepository>();
  final StorageService _storage = Get.find<StorageService>();

  @override
  void onInit() {
    super.onInit();
    loadLanguages();
  }

  @override
  void onClose() {
    nameController.dispose();
    super.onClose();
  }

  Future<void> loadLanguages() async {
    isLoadingLanguages.value = true;
    errorMessage.value = null;
    try {
      final editions = await _quran.getTranslationEditions();
      if (isClosed) return;
      languages.assignAll(_uniqueLanguages(editions));
    } catch (_) {
      if (isClosed) return;
      languages.assignAll(OfflineTranslations.editions);
    } finally {
      if (!isClosed) {
        if (languages.isEmpty) {
          languages.assignAll(OfflineTranslations.editions);
        }
        if (languages.isNotEmpty) {
          selectedLanguage.value = languages.firstWhere(
            (edition) =>
                edition.identifier == StorageService.defaultTranslationId,
            orElse: () => languages.first,
          );
        }
        isLoadingLanguages.value = false;
      }
    }
  }

  Future<void> continueToApp() async {
    final name = nameController.text.trim();
    final country = selectedCountry.value.trim();
    final language = selectedLanguage.value;

    if (name.isEmpty) {
      errorMessage.value = 'Please enter your name.';
      return;
    }
    if (country.isEmpty) {
      errorMessage.value = 'Please choose your country.';
      return;
    }
    if (language == null) {
      errorMessage.value = 'Please choose a translation language.';
      return;
    }

    isSaving.value = true;
    errorMessage.value = null;
    try {
      await _storage.saveProfile(name: name, country: country);
      await _storage.saveTranslation(
        identifier: language.identifier,
        name: language.authorName,
        language: language.languageLabel,
        direction: language.direction,
      );
      await _storage.completeOnboarding();
      Get.offAllNamed(AppRoutes.home);
    } catch (_) {
      if (isClosed) return;
      errorMessage.value = 'Unable to save your details. Please try again.';
    } finally {
      if (!isClosed) isSaving.value = false;
    }
  }

  List<TranslationEdition> _uniqueLanguages(List<TranslationEdition> editions) {
    final byLanguage = <String, TranslationEdition>{};
    for (final edition in editions) {
      if (edition.language.isEmpty) continue;
      final existing = byLanguage[edition.language];
      if (existing == null ||
          edition.identifier == StorageService.defaultTranslationId) {
        byLanguage[edition.language] = edition;
      }
    }

    final unique = byLanguage.values.toList()
      ..sort((a, b) => a.languageLabel.compareTo(b.languageLabel));
    return unique;
  }

  void selectCountry(String? country) {
    if (country == null || country.isEmpty) return;
    selectedCountry.value = country;
  }
}
