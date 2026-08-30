import 'dart:ui';

import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';

import '../constants/app_colors.dart';

/// Blurs Arabic text in Hifz mode until the user taps to reveal it.
class HifzAyahText extends StatelessWidget {
  const HifzAyahText({
    super.key,
    required this.text,
    required this.style,
    required this.isHifzMode,
    required this.isRevealed,
    required this.onReveal,
    this.textAlign = TextAlign.right,
    this.textDirection = TextDirection.rtl,
    this.showHighlight = true,
    this.tappable = true,
  });

  final String text;
  final TextStyle style;
  final bool isHifzMode;
  final bool isRevealed;
  final VoidCallback onReveal;
  final TextAlign textAlign;
  final TextDirection textDirection;
  final bool showHighlight;
  final bool tappable;

  @override
  Widget build(BuildContext context) {
    final ayahText = Text(
      text,
      textAlign: textAlign,
      textDirection: textDirection,
      style: style,
    );

    if (!isHifzMode) return ayahText;

    Widget content = AnimatedContainer(
      duration: const Duration(milliseconds: 280),
      curve: Curves.easeOut,
      padding: showHighlight
          ? EdgeInsets.symmetric(horizontal: 8.w, vertical: 6.h)
          : EdgeInsets.zero,
      decoration: BoxDecoration(
        color: showHighlight && isRevealed
            ? AppColors.mint
            : Colors.transparent,
        borderRadius: BorderRadius.circular(12.r),
        border: showHighlight && isRevealed
            ? Border.all(
                color: AppColors.primary.withValues(alpha: 0.4),
                width: 1.2,
              )
            : Border.all(color: Colors.transparent, width: 1.2),
      ),
      child: TweenAnimationBuilder<double>(
        duration: const Duration(milliseconds: 280),
        curve: Curves.easeOut,
        tween: Tween<double>(end: isRevealed ? 0 : 5),
        builder: (context, sigma, child) {
          final blurred = sigma > 0.05;
          Widget painted = child!;
          if (blurred) {
            painted = ClipRect(
              child: ImageFiltered(
                imageFilter: ImageFilter.blur(sigmaX: sigma, sigmaY: sigma),
                child: Opacity(opacity: 0.45, child: child),
              ),
            );
          }
          return painted;
        },
        child: ayahText,
      ),
    );

    if (!tappable) return content;

    return GestureDetector(
      onTap: onReveal,
      behavior: HitTestBehavior.opaque,
      child: content,
    );
  }
}

class HifzModeButton extends StatelessWidget {
  const HifzModeButton({
    super.key,
    required this.isActive,
    required this.onPressed,
  });

  final bool isActive;
  final VoidCallback onPressed;

  @override
  Widget build(BuildContext context) {
    return IconButton(
      tooltip: isActive ? 'Exit Hifz Mode' : 'Hifz Mode',
      onPressed: onPressed,
      icon: Icon(
        isActive ? Icons.visibility_off_outlined : Icons.visibility_outlined,
        size: 22.sp,
        color: isActive ? AppColors.accent : AppColors.textPrimary,
      ),
    );
  }
}
