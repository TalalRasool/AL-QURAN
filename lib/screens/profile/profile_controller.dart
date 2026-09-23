import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:get/get.dart';

import '../../core/constants/app_colors.dart';
import '../../core/constants/app_text_styles.dart';
import '../../core/routes/app_routes.dart';
import '../../core/services/auth_service.dart';
import '../../core/services/storage_service.dart';
import '../../core/controllers/prayer_notification_controller.dart';
import 'auth_bottom_sheet.dart';
import 'reading_settings_sheet.dart';

class ProfileController extends GetxController {
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

  final StorageService _storage = Get.find<StorageService>();
  final AuthService _auth = Get.find<AuthService>();

  final editFormKey = GlobalKey<FormState>();
  final nameController = TextEditingController();
  final selectedCountry = defaultCountry.obs;
  final isSavingProfile = false.obs;
  final editErrorMessage = RxnString();

  RxBool get notificationsEnabled => _storage.notificationsEnabled;

  String get userName {
    final name = _storage.userName.value.trim();
    return name.isEmpty ? 'Reader' : name;
  }

  String get userCountry {
    final country = _storage.userCountry.value.trim();
    return country.isEmpty ? 'Not set' : country;
  }

  String get translationLabel => _storage.selectedTranslationLanguage.value;

  bool get isLoggedIn => _auth.isLoggedIn;

  String get accountEmail => _auth.email ?? '';

  List<String> get countryOptions {
    final current = selectedCountry.value.trim();
    final options = List<String>.from(countries);
    if (current.isNotEmpty && !options.contains(current)) {
      options.insert(0, current);
    }
    return options;
  }

  @override
  void onClose() {
    nameController.dispose();
    super.onClose();
  }

  void toggleNotifications(bool value) =>
      _storage.saveNotificationsEnabled(value);

  Future<void> togglePrayerNotifications(bool value) async {
    final prayer = Get.find<PrayerNotificationController>();
    if (prayer.isBusy.value) return;
    if (value) {
      await prayer.requestLocationAndEnableNotifications();
    } else {
      await prayer.disableNotifications();
    }
  }

  void openTranslations() => Get.toNamed(AppRoutes.translations);

  void openReadingSettings() => ReadingSettingsSheet.open();

  void openEditProfile() {
    final storedName = _storage.userName.value.trim();
    nameController.text = storedName.isEmpty ? '' : storedName;
    final storedCountry = _storage.userCountry.value.trim();
    selectedCountry.value = storedCountry.isEmpty
        ? defaultCountry
        : storedCountry;
    editErrorMessage.value = null;
    isSavingProfile.value = false;
    Get.toNamed(AppRoutes.editProfile);
  }

  void selectCountry(String? country) {
    if (country == null || country.trim().isEmpty) return;
    selectedCountry.value = country.trim();
  }

  Future<void> saveProfile() async {
    final name = nameController.text.trim();
    final country = selectedCountry.value.trim();

    if (editFormKey.currentState != null &&
        !editFormKey.currentState!.validate()) {
      return;
    }
    if (name.isEmpty) {
      editErrorMessage.value = 'Please enter your name.';
      return;
    }
    if (country.isEmpty) {
      editErrorMessage.value = 'Please choose your country.';
      return;
    }

    isSavingProfile.value = true;
    editErrorMessage.value = null;
    try {
      await _storage.saveProfile(name: name, country: country);

      if (_auth.isLoggedIn) {
        try {
          await _auth.updateProfile(name: name, country: country);
        } catch (_) {
          Get.snackbar(
            'Profile saved',
            'Saved on this device. Account sync will retry when you are online.',
            snackPosition: SnackPosition.BOTTOM,
          );
          Get.back();
          return;
        }
      }

      Get.back();
      Get.snackbar(
        'Profile saved',
        'Your profile was updated.',
        snackPosition: SnackPosition.BOTTOM,
        backgroundColor: AppColors.primary,
        colorText: AppColors.white,
        titleText: Text(
          'Profile saved',
          style: AppTextStyles.heading3.copyWith(color: AppColors.white),
        ),
        messageText: Text(
          'Your profile was updated.',
          style: AppTextStyles.bodySmall.copyWith(color: AppColors.white),
        ),
      );
    } catch (_) {
      editErrorMessage.value = 'Unable to save your profile. Please try again.';
    } finally {
      isSavingProfile.value = false;
    }
  }

  void openAuthSheet() {
    Get.bottomSheet(
      const AuthBottomSheet(),
      backgroundColor: Get.theme.colorScheme.surface,
      isScrollControlled: true,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.vertical(top: Radius.circular(24.r)),
      ),
    );
  }

  Future<void> signOut() async {
    try {
      await _auth.signOut();
    } catch (_) {
      Get.snackbar(
        'Sign out',
        'Unable to sign out right now.',
        snackPosition: SnackPosition.BOTTOM,
      );
    }
  }
}
