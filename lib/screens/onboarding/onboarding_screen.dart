import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:get/get.dart';

import '../../core/constants/app_colors.dart';
import '../../core/constants/app_text_styles.dart';
import '../../core/data/models/translation_edition.dart';
import '../../core/widgets/widgets.dart';
import 'onboarding_controller.dart';

class OnboardingScreen extends GetView<OnboardingController> {
  const OnboardingScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppColors.background,
      body: Column(
        children: [
          Expanded(
            child: SingleChildScrollView(
              child: Column(
                children: [
                  const _WelcomeHeader(),
                  Transform.translate(
                    offset: Offset(0, -28.h),
                    child: Padding(
                      padding: EdgeInsets.symmetric(horizontal: 20.w),
                      child: const _ProfileCard(),
                    ),
                  ),
                ],
              ),
            ),
          ),
          SafeArea(
            top: false,
            child: Padding(
              padding: EdgeInsets.fromLTRB(20.w, 8.h, 20.w, 16.h),
              child: Obx(
                () => PrimaryButton(
                  label: 'Continue',
                  height: 56.h,
                  radius: 16.r,
                  isLoading: controller.isSaving.value,
                  onPressed: controller.continueToApp,
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}

class _WelcomeHeader extends StatelessWidget {
  const _WelcomeHeader();

  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,
      padding: EdgeInsets.fromLTRB(24.w, 0, 24.w, 56.h),
      decoration: BoxDecoration(
        gradient: const LinearGradient(
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
          colors: [AppColors.primary, AppColors.primaryLight],
        ),
        borderRadius: BorderRadius.vertical(bottom: Radius.circular(32.r)),
      ),
      child: SafeArea(
        bottom: false,
        child: Column(
          children: [
            SizedBox(height: 32.h),
            Text(
              'بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ',
              textAlign: TextAlign.center,
              textDirection: TextDirection.rtl,
              style: AppTextStyles.arabicTitle.copyWith(
                color: AppColors.white,
                fontSize: 22.sp,
              ),
            ),
            SizedBox(height: 10.h),
            Text(
              'Welcome to Al Quran',
              textAlign: TextAlign.center,
              style: AppTextStyles.heading1.copyWith(
                color: AppColors.white,
                fontSize: 28.sp,
              ),
            ),
            SizedBox(height: 8.h),
            Text(
              'A calm space to read, listen, and remember.',
              textAlign: TextAlign.center,
              style: AppTextStyles.body.copyWith(
                color: AppColors.white.withValues(alpha: 0.85),
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class _ProfileCard extends GetView<OnboardingController> {
  const _ProfileCard();

  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,
      padding: EdgeInsets.fromLTRB(20.w, 22.h, 20.w, 20.h),
      decoration: BoxDecoration(
        color: AppColors.surface,
        borderRadius: BorderRadius.circular(24.r),
        boxShadow: [
          BoxShadow(
            color: AppColors.primary.withValues(alpha: 0.08),
            blurRadius: 24.r,
            offset: Offset(0, 10.h),
          ),
        ],
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text('Tell us about you', style: AppTextStyles.heading2),
          SizedBox(height: 6.h),
          Text(
            'We’ll personalize your reading experience.',
            style: AppTextStyles.bodySmall,
          ),
          SizedBox(height: 20.h),
          Text('Name', style: AppTextStyles.heading3),
          SizedBox(height: 8.h),
          CustomTextField(
            controller: controller.nameController,
            hintText: 'Your name',
            fillColor: AppColors.searchFill,
            radius: 16.r,
            prefixIcon: Icon(
              Icons.person_outline_rounded,
              size: 22.sp,
              color: AppColors.primaryLight,
            ),
            textCapitalization: TextCapitalization.words,
            textInputAction: TextInputAction.next,
            autofillHints: const [AutofillHints.name],
          ),
          SizedBox(height: 16.h),
          Text('Country', style: AppTextStyles.heading3),
          SizedBox(height: 8.h),
          const _CountryDropdown(),
          SizedBox(height: 16.h),
          Text('Translation language', style: AppTextStyles.heading3),
          SizedBox(height: 8.h),
          const _LanguageDropdown(),
          Obx(() {
            final error = controller.errorMessage.value;
            if (error == null) return const SizedBox.shrink();
            return Padding(
              padding: EdgeInsets.only(top: 12.h),
              child: Text(
                error,
                style: AppTextStyles.bodySmall.copyWith(color: AppColors.error),
              ),
            );
          }),
        ],
      ),
    );
  }
}

class _CountryDropdown extends GetView<OnboardingController> {
  const _CountryDropdown();

  @override
  Widget build(BuildContext context) {
    return Obx(
      () => DropdownButtonFormField<String>(
        key: ValueKey(controller.selectedCountry.value),
        initialValue: controller.selectedCountry.value,
        isExpanded: true,
        dropdownColor: AppColors.surface,
        borderRadius: BorderRadius.circular(16.r),
        icon: Icon(
          Icons.keyboard_arrow_down_rounded,
          color: AppColors.primaryLight,
          size: 24.sp,
        ),
        decoration: _dropdownDecoration(
          prefixIcon: Icons.public_rounded,
        ),
        items: OnboardingController.countries
            .map(
              (country) => DropdownMenuItem(
                value: country,
                child: Text(
                  country,
                  style: AppTextStyles.body,
                  overflow: TextOverflow.ellipsis,
                ),
              ),
            )
            .toList(),
        onChanged: controller.selectCountry,
      ),
    );
  }
}

InputDecoration _dropdownDecoration({required IconData prefixIcon}) {
  return InputDecoration(
    filled: true,
    fillColor: AppColors.searchFill,
    prefixIcon: Icon(
      prefixIcon,
      size: 22.sp,
      color: AppColors.primaryLight,
    ),
    contentPadding: EdgeInsets.symmetric(
      horizontal: 12.w,
      vertical: 16.h,
    ),
    border: OutlineInputBorder(
      borderRadius: BorderRadius.circular(16.r),
      borderSide: BorderSide.none,
    ),
    enabledBorder: OutlineInputBorder(
      borderRadius: BorderRadius.circular(16.r),
      borderSide: BorderSide.none,
    ),
    focusedBorder: OutlineInputBorder(
      borderRadius: BorderRadius.circular(16.r),
      borderSide: BorderSide(color: AppColors.primary, width: 1.5.w),
    ),
  );
}

class _LanguageDropdown extends GetView<OnboardingController> {
  const _LanguageDropdown();

  @override
  Widget build(BuildContext context) {
    return Obx(() {
      if (controller.isLoadingLanguages.value && controller.languages.isEmpty) {
        return Container(
          height: 56.h,
          alignment: Alignment.center,
          decoration: BoxDecoration(
            color: AppColors.searchFill,
            borderRadius: BorderRadius.circular(16.r),
          ),
          child: SizedBox(
            width: 22.w,
            height: 22.w,
            child: const CircularProgressIndicator(
              strokeWidth: 2,
              color: AppColors.primary,
            ),
          ),
        );
      }

      return DropdownButtonFormField<TranslationEdition>(
        key: ValueKey(controller.selectedLanguage.value?.identifier),
        initialValue: controller.selectedLanguage.value,
        isExpanded: true,
        dropdownColor: AppColors.surface,
        borderRadius: BorderRadius.circular(16.r),
        icon: Icon(
          Icons.keyboard_arrow_down_rounded,
          color: AppColors.primaryLight,
          size: 24.sp,
        ),
        decoration: _dropdownDecoration(
          prefixIcon: Icons.translate_rounded,
        ),
        hint: Text('Select a language', style: AppTextStyles.body),
        items: controller.languages
            .map(
              (edition) => DropdownMenuItem(
                value: edition,
                child: Text(
                  edition.languageLabel,
                  style: AppTextStyles.body,
                  overflow: TextOverflow.ellipsis,
                ),
              ),
            )
            .toList(),
        onChanged: (edition) => controller.selectedLanguage.value = edition,
      );
    });
  }
}
