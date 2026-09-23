import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:get/get.dart';

import '../../core/constants/app_colors.dart';
import '../../core/constants/app_text_styles.dart';
import '../../core/controllers/settings_controller.dart';
import '../../core/widgets/widgets.dart';
import 'profile_controller.dart';

class EditProfileScreen extends GetView<ProfileController> {
  const EditProfileScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Obx(() {
      Get.find<SettingsController>().isDarkMode.value;
      return Scaffold(
        backgroundColor: AppColors.background,
        appBar: const CustomAppBar(title: 'Edit Profile'),
        body: SafeArea(
          child: Form(
            key: controller.editFormKey,
            child: ListView(
              padding: EdgeInsets.fromLTRB(20.w, 8.h, 20.w, 24.h),
              children: [
                Text(
                  'Personal information',
                  style: AppTextStyles.heading2,
                ),
                SizedBox(height: 6.h),
                Text(
                  'Update your name and country. These details appear on your profile.',
                  style: AppTextStyles.bodySmall,
                ),
                SizedBox(height: 20.h),
                Text('Name', style: AppTextStyles.heading3),
                SizedBox(height: 8.h),
                TextFormField(
                  controller: controller.nameController,
                  textCapitalization: TextCapitalization.words,
                  textInputAction: TextInputAction.next,
                  autofillHints: const [AutofillHints.name],
                  style: AppTextStyles.body,
                  cursorColor: AppColors.primary,
                  validator: (value) {
                    if (value == null || value.trim().isEmpty) {
                      return 'Please enter your name.';
                    }
                    return null;
                  },
                  decoration: _fieldDecoration(
                    hintText: 'Your name',
                    prefixIcon: Icons.person_outline_rounded,
                  ),
                ),
                SizedBox(height: 16.h),
                Text('Country', style: AppTextStyles.heading3),
                SizedBox(height: 8.h),
                Obx(
                  () => DropdownButtonFormField<String>(
                    key: ValueKey(controller.selectedCountry.value),
                    initialValue: controller.countryOptions.contains(
                          controller.selectedCountry.value,
                        )
                        ? controller.selectedCountry.value
                        : controller.countryOptions.first,
                    isExpanded: true,
                    dropdownColor: AppColors.surface,
                    borderRadius: BorderRadius.circular(16.r),
                    icon: Icon(
                      Icons.keyboard_arrow_down_rounded,
                      color: AppColors.primaryLight,
                      size: 24.sp,
                    ),
                    decoration: _fieldDecoration(
                      hintText: 'Country',
                      prefixIcon: Icons.public_rounded,
                    ),
                    items: controller.countryOptions
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
                    validator: (value) {
                      if (value == null || value.trim().isEmpty) {
                        return 'Please choose your country.';
                      }
                      return null;
                    },
                  ),
                ),
                if (controller.accountEmail.isNotEmpty) ...[
                  SizedBox(height: 16.h),
                  Text('Email', style: AppTextStyles.heading3),
                  SizedBox(height: 8.h),
                  TextFormField(
                    initialValue: controller.accountEmail,
                    readOnly: true,
                    enableInteractiveSelection: true,
                    style: AppTextStyles.body,
                    decoration: _fieldDecoration(
                      hintText: 'Email',
                      prefixIcon: Icons.mail_outline_rounded,
                    ),
                  ),
                ],
                Obx(() {
                  final error = controller.editErrorMessage.value;
                  if (error == null) return const SizedBox.shrink();
                  return Padding(
                    padding: EdgeInsets.only(top: 12.h),
                    child: Text(
                      error,
                      style: AppTextStyles.bodySmall.copyWith(
                        color: AppColors.error,
                      ),
                    ),
                  );
                }),
                SizedBox(height: 24.h),
                Obx(
                  () => PrimaryButton(
                    label: 'Save',
                    isLoading: controller.isSavingProfile.value,
                    onPressed: controller.saveProfile,
                  ),
                ),
              ],
            ),
          ),
        ),
      );
    });
  }

  InputDecoration _fieldDecoration({
    required String hintText,
    required IconData prefixIcon,
  }) {
    return InputDecoration(
      filled: true,
      fillColor: AppColors.searchFill,
      hintText: hintText,
      hintStyle: AppTextStyles.body.copyWith(color: AppColors.textHint),
      prefixIcon: Icon(
        prefixIcon,
        size: 22.sp,
        color: AppColors.primaryLight,
      ),
      contentPadding: EdgeInsets.symmetric(
        horizontal: 16.w,
        vertical: 14.h,
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
      errorBorder: OutlineInputBorder(
        borderRadius: BorderRadius.circular(16.r),
        borderSide: BorderSide(color: AppColors.error, width: 1.w),
      ),
      focusedErrorBorder: OutlineInputBorder(
        borderRadius: BorderRadius.circular(16.r),
        borderSide: BorderSide(color: AppColors.error, width: 1.5.w),
      ),
    );
  }
}
