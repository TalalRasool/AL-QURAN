import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:get/get.dart';

import '../controllers/hifz_tester_controller.dart';
import '../core/constants/app_colors.dart';
import '../core/constants/app_text_styles.dart';
import '../core/controllers/settings_controller.dart';
import '../core/widgets/widgets.dart';

class HifzTesterScreen extends GetView<HifzTesterController> {
  const HifzTesterScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppColors.background,
      appBar: const CustomAppBar(title: 'Hifz Tester'),
      body: SafeArea(
        child: Padding(
          padding: EdgeInsets.fromLTRB(20.w, 12.h, 20.w, 24.h),
          child: Column(
            children: [
              const _SurahSelector(),
              SizedBox(height: 12.h),
              const Expanded(child: _AnalysisResults()),
              SizedBox(height: 12.h),
              Obx(() {
                final recording = controller.isRecording.value;
                final loading = controller.isLoading.value;
                return Column(
                  children: [
                    if (loading) ...[
                      Text(
                        'Analyzing recitation on Cloud AI...',
                        textAlign: TextAlign.center,
                        style: AppTextStyles.heading3.copyWith(
                          color: AppColors.primary,
                        ),
                      ),
                      SizedBox(height: 16.h),
                    ] else if (recording) ...[
                      Text(
                        'Recording...',
                        style: AppTextStyles.heading3.copyWith(
                          color: const Color(0xFFC62828),
                        ),
                      ),
                      SizedBox(height: 16.h),
                    ],
                    if (loading)
                      SizedBox(
                        width: 88.w,
                        height: 88.w,
                        child: Center(
                          child: SizedBox(
                            width: 44.w,
                            height: 44.w,
                            child: CircularProgressIndicator(
                              color: AppColors.primary,
                              strokeWidth: 3.5.w,
                            ),
                          ),
                        ),
                      )
                    else
                      _RecordButton(
                        isRecording: recording,
                        onTap: controller.toggleRecording,
                      ),
                    SizedBox(height: 12.h),
                    Text(
                      loading
                          ? 'Please wait — the first request may take up to '
                              '15 seconds while the GPU server wakes up'
                          : recording
                          ? 'Tap to stop'
                          : 'Tap the microphone to recite',
                      style: AppTextStyles.bodySmall,
                      textAlign: TextAlign.center,
                    ),
                  ],
                );
              }),
            ],
          ),
        ),
      ),
    );
  }
}

class _AnalysisResults extends GetView<HifzTesterController> {
  const _AnalysisResults();

  static const _correct = Color(0xFF15803D);
  static const _wrong = Color(0xFFDC2626);

  @override
  Widget build(BuildContext context) {
    return Obx(() {
      if (!controller.hasResult.value) return const _IdlePrompt();

      final settings = Get.isRegistered<SettingsController>()
          ? Get.find<SettingsController>()
          : null;
      final baseStyle =
          (settings?.arabicStyle(height: 1.9) ?? AppTextStyles.arabicBody)
              .copyWith(fontSize: 30.sp, fontWeight: FontWeight.w600);
      final words = controller.wordResults;

      return Container(
        width: double.infinity,
        padding: EdgeInsets.fromLTRB(16.w, 20.h, 16.w, 16.h),
        decoration: BoxDecoration(
          color: AppColors.surface,
          borderRadius: BorderRadius.circular(20.r),
          border: Border.all(color: AppColors.divider),
        ),
        child: Column(
          children: [
            _AccuracyBadge(accuracy: controller.accuracy.value),
            SizedBox(height: 14.h),
            if (words.isNotEmpty) ...[
              Text(
                '${controller.correctWordCount} of ${words.length} words matched',
                style: AppTextStyles.bodySmall.copyWith(
                  color: AppColors.textSecondary,
                ),
              ),
              SizedBox(height: 16.h),
              Divider(color: AppColors.divider, height: 1.h),
              // A full surah can run to hundreds of words, so the highlighted
              // text scrolls on its own while the score stays pinned above.
              Expanded(
                child: SingleChildScrollView(
                  padding: EdgeInsets.symmetric(vertical: 16.h),
                  child: Wrap(
                    textDirection: TextDirection.rtl,
                    alignment: WrapAlignment.center,
                    runAlignment: WrapAlignment.center,
                    spacing: 8.w,
                    runSpacing: 10.h,
                    children: [
                      for (final word in words)
                        _WordChip(word: word, baseStyle: baseStyle),
                    ],
                  ),
                ),
              ),
              Divider(color: AppColors.divider, height: 1.h),
              SizedBox(height: 14.h),
              const _Legend(correct: _correct, wrong: _wrong),
            ] else
              Padding(
                padding: EdgeInsets.only(top: 4.h),
                child: Text(
                  'No words were recognised in this recitation. '
                  'Try reciting a little louder.',
                  textAlign: TextAlign.center,
                  style: AppTextStyles.bodySmall.copyWith(
                    color: AppColors.textSecondary,
                  ),
                ),
              ),
          ],
        ),
      );
    });
  }
}

/// Shown before the first analysis, in place of the results card.
class _IdlePrompt extends GetView<HifzTesterController> {
  const _IdlePrompt();

  @override
  Widget build(BuildContext context) {
    return Center(
      child: SingleChildScrollView(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Icon(
              Icons.auto_awesome_rounded,
              size: 44.sp,
              color: AppColors.primary.withValues(alpha: 0.55),
            ),
            SizedBox(height: 14.h),
            Obx(() {
              final count = controller.ayahCount;
              return Text(
                count > 0
                    ? 'Recite all $count ayahs of ${controller.selectionLabel}'
                    : 'Recite ${controller.selectionLabel}',
                textAlign: TextAlign.center,
                style: AppTextStyles.subtitle.copyWith(
                  color: AppColors.textPrimary,
                ),
              );
            }),
            SizedBox(height: 8.h),
            Padding(
              padding: EdgeInsets.symmetric(horizontal: 24.w),
              child: Text(
                'The Cloud AI listens to the whole surah and highlights '
                'every word you recite.',
                textAlign: TextAlign.center,
                style: AppTextStyles.bodySmall.copyWith(
                  color: AppColors.textSecondary,
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class _AccuracyBadge extends StatelessWidget {
  const _AccuracyBadge({required this.accuracy});

  final int accuracy;

  Color get _ringColor {
    if (accuracy >= 80) return const Color(0xFF15803D);
    if (accuracy >= 50) return const Color(0xFFD97706);
    return const Color(0xFFDC2626);
  }

  String get _verdict {
    if (accuracy >= 90) return 'Excellent — Masha Allah';
    if (accuracy >= 80) return 'Strong recitation';
    if (accuracy >= 50) return 'Keep revising';
    return 'Needs more revision';
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        SizedBox(
          width: 116.w,
          height: 116.w,
          child: Stack(
            alignment: Alignment.center,
            children: [
              SizedBox.expand(
                child: CircularProgressIndicator(
                  value: accuracy / 100,
                  strokeWidth: 9.w,
                  strokeCap: StrokeCap.round,
                  backgroundColor: AppColors.greyLight,
                  valueColor: AlwaysStoppedAnimation(_ringColor),
                ),
              ),
              Column(
                mainAxisSize: MainAxisSize.min,
                children: [
                  Text(
                    '$accuracy%',
                    style: AppTextStyles.heading2.copyWith(
                      color: _ringColor,
                      fontWeight: FontWeight.w700,
                    ),
                  ),
                  Text(
                    'accuracy',
                    style: AppTextStyles.caption.copyWith(
                      color: AppColors.textSecondary,
                    ),
                  ),
                ],
              ),
            ],
          ),
        ),
        SizedBox(height: 12.h),
        Text(
          _verdict,
          style: AppTextStyles.subtitle.copyWith(color: AppColors.textPrimary),
        ),
      ],
    );
  }
}

class _WordChip extends StatelessWidget {
  const _WordChip({required this.word, required this.baseStyle});

  final RecitationWord word;
  final TextStyle baseStyle;

  @override
  Widget build(BuildContext context) {
    final color = word.isCorrect
        ? _AnalysisResults._correct
        : _AnalysisResults._wrong;

    return Container(
      padding: EdgeInsets.symmetric(horizontal: 10.w, vertical: 4.h),
      decoration: BoxDecoration(
        color: color.withValues(alpha: 0.08),
        borderRadius: BorderRadius.circular(10.r),
      ),
      child: Text(
        word.text,
        textDirection: TextDirection.rtl,
        style: baseStyle.copyWith(color: color),
      ),
    );
  }
}

class _Legend extends StatelessWidget {
  const _Legend({required this.correct, required this.wrong});

  final Color correct;
  final Color wrong;

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        _LegendDot(color: correct, label: 'Correct'),
        SizedBox(width: 18.w),
        _LegendDot(color: wrong, label: 'Needs review'),
      ],
    );
  }
}

class _LegendDot extends StatelessWidget {
  const _LegendDot({required this.color, required this.label});

  final Color color;
  final String label;

  @override
  Widget build(BuildContext context) {
    return Row(
      children: [
        Container(
          width: 10.w,
          height: 10.w,
          decoration: BoxDecoration(color: color, shape: BoxShape.circle),
        ),
        SizedBox(width: 6.w),
        Text(
          label,
          style: AppTextStyles.caption.copyWith(color: AppColors.textSecondary),
        ),
      ],
    );
  }
}

class _SurahSelector extends GetView<HifzTesterController> {
  const _SurahSelector();

  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,
      padding: EdgeInsets.fromLTRB(16.w, 14.h, 16.w, 16.h),
      decoration: BoxDecoration(
        color: AppColors.surface,
        borderRadius: BorderRadius.circular(16.r),
      ),
      child: Obx(() {
        // The dropdown stays locked while recording or analysing so the audio
        // always matches the surah sent to the backend.
        final locked =
            controller.isRecording.value || controller.isLoading.value;
        final surahs = controller.surahs;
        final ayahCount = controller.ayahCount;

        return Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                Expanded(
                  child: Text(
                    'Choose a surah to recite',
                    style: AppTextStyles.bodySmall.copyWith(
                      color: AppColors.textSecondary,
                      fontWeight: FontWeight.w600,
                    ),
                  ),
                ),
                if (ayahCount > 0)
                  Text(
                    '$ayahCount ayahs',
                    style: AppTextStyles.caption.copyWith(
                      color: AppColors.primary,
                      fontWeight: FontWeight.w600,
                    ),
                  ),
              ],
            ),
            SizedBox(height: 10.h),
            _DropdownField<int>(
              label: 'Surah',
              value: controller.selectedSurah.value,
              onChanged: locked ? null : controller.onSurahChanged,
              items: [
                if (surahs.isEmpty)
                  for (var number = 1; number <= 114; number++)
                    DropdownMenuItem(
                      value: number,
                      child: Text(
                        'Surah $number',
                        overflow: TextOverflow.ellipsis,
                        style: AppTextStyles.body,
                      ),
                    )
                else
                  for (final surah in surahs)
                    DropdownMenuItem(
                      value: surah.number,
                      child: Text(
                        '${surah.number}. ${surah.englishName}',
                        overflow: TextOverflow.ellipsis,
                        style: AppTextStyles.body,
                      ),
                    ),
              ],
            ),
          ],
        );
      }),
    );
  }
}

class _DropdownField<T> extends StatelessWidget {
  const _DropdownField({
    required this.label,
    required this.value,
    required this.items,
    required this.onChanged,
  });

  final String label;
  final T value;
  final List<DropdownMenuItem<T>> items;
  final ValueChanged<T?>? onChanged;

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          label,
          style: AppTextStyles.bodySmall.copyWith(color: AppColors.textHint),
        ),
        SizedBox(height: 6.h),
        Container(
          padding: EdgeInsets.symmetric(horizontal: 12.w),
          decoration: BoxDecoration(
            color: AppColors.searchFill,
            borderRadius: BorderRadius.circular(12.r),
            border: Border.all(color: AppColors.divider),
          ),
          child: DropdownButtonHideUnderline(
            child: DropdownButton<T>(
              value: value,
              items: items,
              onChanged: onChanged,
              isExpanded: true,
              borderRadius: BorderRadius.circular(12.r),
              menuMaxHeight: 360.h,
              icon: Icon(
                Icons.keyboard_arrow_down_rounded,
                color: AppColors.textSecondary,
                size: 22.sp,
              ),
              dropdownColor: AppColors.surface,
              style: AppTextStyles.body,
            ),
          ),
        ),
      ],
    );
  }
}

class _RecordButton extends StatefulWidget {
  const _RecordButton({
    required this.isRecording,
    required this.onTap,
  });

  final bool isRecording;
  final VoidCallback onTap;

  @override
  State<_RecordButton> createState() => _RecordButtonState();
}

class _RecordButtonState extends State<_RecordButton>
    with SingleTickerProviderStateMixin {
  late final AnimationController _pulse;

  @override
  void initState() {
    super.initState();
    _pulse = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 900),
    );
    if (widget.isRecording) _pulse.repeat(reverse: true);
  }

  @override
  void didUpdateWidget(covariant _RecordButton oldWidget) {
    super.didUpdateWidget(oldWidget);
    if (widget.isRecording && !_pulse.isAnimating) {
      _pulse.repeat(reverse: true);
    } else if (!widget.isRecording && _pulse.isAnimating) {
      _pulse
        ..stop()
        ..value = 0;
    }
  }

  @override
  void dispose() {
    _pulse.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final recording = widget.isRecording;
    final color = recording ? const Color(0xFFC62828) : AppColors.primary;

    return AnimatedBuilder(
      animation: _pulse,
      builder: (context, child) {
        final scale = recording ? 1 + (_pulse.value * 0.08) : 1.0;
        return Transform.scale(scale: scale, child: child);
      },
      child: Material(
        color: color,
        shape: const CircleBorder(),
        elevation: 4,
        child: InkWell(
          customBorder: const CircleBorder(),
          onTap: widget.onTap,
          child: SizedBox(
            width: 88.w,
            height: 88.w,
            child: Icon(
              recording ? Icons.stop_rounded : Icons.mic_rounded,
              color: AppColors.white,
              size: 40.sp,
            ),
          ),
        ),
      ),
    );
  }
}
