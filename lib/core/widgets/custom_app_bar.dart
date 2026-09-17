import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:get/get.dart';

import '../constants/app_colors.dart';
import '../constants/app_text_styles.dart';

/// Transparent app bar with a back or menu leading action and a dynamic title.
class CustomAppBar extends StatelessWidget implements PreferredSizeWidget {
  const CustomAppBar({
    super.key,
    required this.title,
    this.showBackButton = true,
    this.showMenuIcon = false,
    this.actions,
    this.onBack,
    this.onMenuTap,
    this.centerTitle = true,
    this.titleMaxLines = 1,
  });

  final String title;
  final bool showBackButton;
  final bool showMenuIcon;
  final List<Widget>? actions;
  final VoidCallback? onBack;
  final VoidCallback? onMenuTap;
  final bool centerTitle;
  final int titleMaxLines;

  double get _toolbarHeight {
    final lines = titleMaxLines < 1 ? 1 : titleMaxLines;
    return lines > 1 ? 72.h : 56.h;
  }

  @override
  Size get preferredSize => Size.fromHeight(_toolbarHeight);

  @override
  Widget build(BuildContext context) {
    return AppBar(
      backgroundColor: Colors.transparent,
      elevation: 0,
      scrolledUnderElevation: 0,
      centerTitle: centerTitle,
      automaticallyImplyLeading: false,
      toolbarHeight: _toolbarHeight,
      systemOverlayStyle: SystemUiOverlayStyle(
        statusBarColor: Colors.transparent,
        statusBarIconBrightness: Theme.of(context).brightness == Brightness.dark
            ? Brightness.light
            : Brightness.dark,
        statusBarBrightness: Theme.of(context).brightness == Brightness.dark
            ? Brightness.dark
            : Brightness.light,
      ),
      leading: _buildLeading(),
      title: Text(
        title,
        style: AppTextStyles.heading2,
        maxLines: titleMaxLines < 1 ? 1 : titleMaxLines,
        overflow: TextOverflow.ellipsis,
        textAlign: centerTitle ? TextAlign.center : TextAlign.start,
      ),
      actions: actions,
    );
  }

  Widget? _buildLeading() {
    if (showMenuIcon) {
      return IconButton(
        onPressed: onMenuTap,
        icon: Icon(
          Icons.menu_rounded,
          size: 24.sp,
          color: AppColors.textPrimary,
        ),
      );
    }

    if (showBackButton) {
      return IconButton(
        onPressed: onBack ?? () => Get.back(),
        tooltip: 'Back',
        icon: Icon(
          Icons.arrow_back_ios,
          size: 20.sp,
          color: AppColors.textPrimary,
        ),
      );
    }

    return null;
  }
}
