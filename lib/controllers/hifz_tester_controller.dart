import 'dart:async';
import 'dart:convert';
import 'dart:io';
import 'package:flutter/foundation.dart';
import 'package:get/get.dart';
import 'package:http/http.dart' as http;
import 'package:path/path.dart' as p;
import 'package:path_provider/path_provider.dart';
import 'package:permission_handler/permission_handler.dart';
import 'package:record/record.dart';
import '../core/data/models/surah.dart';
import '../core/data/quran_repository.dart';
class RecitationWord {
  const RecitationWord({required this.text, required this.status});
  factory RecitationWord.fromJson(Map<String, dynamic> json) {
    return RecitationWord(
      text: '${json['text'] ?? json['word'] ?? ''}',
      status: '${json['status'] ?? ''}'.toLowerCase(),
    );
  }
  final String text;
  final String status;
  bool get isCorrect => status == 'correct';
}
class HifzTesterController extends GetxController {
  static const _requestTimeout = Duration(seconds: 150);
  final isRecording = false.obs;
  final isLoading = false.obs;
  final recordedFilePath = ''.obs;
  final wordResults = <RecitationWord>[].obs;
  final accuracy = 0.obs;
  final hasResult = false.obs;
  final selectedSurah = 1.obs;
  final surahs = <Surah>[].obs;
  final String apiUrl =
      'https://talalrasool--hifz-ai-backend-fastapi-app.modal.run/analyze_recitation';
  final AudioRecorder _recorder = AudioRecorder();
  @override
  void onInit() {
    super.onInit();
    _loadSurahs();
  }
  @override
  void onClose() {
    _recorder.dispose();
    super.onClose();
  }
  Surah? get currentSurah {
    for (final surah in surahs) {
      if (surah.number == selectedSurah.value) return surah;
    }
    return null;
  }
  /// Verse count of the selected surah, or 0 while the list is still loading.
  int get ayahCount => currentSurah?.verseCount ?? 0;
  String get selectionLabel {
    final name = currentSurah?.englishName;
    if (name == null || name.isEmpty) return 'Surah ${selectedSurah.value}';
    return '${selectedSurah.value}. $name';
  }
  int get correctWordCount =>
      wordResults.where((word) => word.isCorrect).length;
  Future<void> _loadSurahs() async {
    if (!Get.isRegistered<QuranRepository>()) return;
    try {
      surahs.assignAll(await Get.find<QuranRepository>().getAllSurahs());
    } catch (error) {
      debugPrint('Failed to load surah list: $error');
    }
  }
  void onSurahChanged(int? surahNumber) {
    if (surahNumber == null || surahNumber == selectedSurah.value) return;
    selectedSurah.value = surahNumber;
    _clearResults();
  }
  void _clearResults() {
    wordResults.clear();
    accuracy.value = 0;
    hasResult.value = false;
  }
  Future<void> startRecording() async {
    if (isRecording.value || isLoading.value) return;
    try {
      final status = await Permission.microphone.request();
      if (!status.isGranted) {
        Get.snackbar(
          'Microphone needed',
          'Allow microphone access to record your recitation.',
          snackPosition: SnackPosition.BOTTOM,
        );
        return;
      }
      final wavSupported = await _recorder.isEncoderSupported(AudioEncoder.wav);
      if (!wavSupported) {
        throw Exception('WAV encoder is not supported on this device.');
      }
      final tempDir = await getTemporaryDirectory();
      final filePath = p.join(tempDir.path, 'hifz_record.wav');
      await _recorder.start(
        const RecordConfig(
          encoder: AudioEncoder.wav,
          sampleRate: 16000,
          numChannels: 1,
        ),
        path: filePath,
      );
      recordedFilePath.value = filePath;
      _clearResults();
      isRecording.value = true;
    } catch (error) {
      isRecording.value = false;
      Get.snackbar(
        'Recording Error',
        error.toString(),
        snackPosition: SnackPosition.BOTTOM,
      );
    }
  }
  Future<void> stopRecording() async {
    if (!isRecording.value) return;

    try {
      final path = await _recorder.stop();
      if (path != null && path.isNotEmpty) {
        recordedFilePath.value = path;
      }
      isRecording.value = false;
      debugPrint('Hifz recording saved: ${recordedFilePath.value}');
      final audioFile = File(recordedFilePath.value);
      if (!await audioFile.exists()) {
        Get.snackbar(
          'Error',
          'Audio file was not created!',
          snackPosition: SnackPosition.BOTTOM,
        );
        return;
      }
      isLoading.value = true;
      try {
        // The endpoint scores a whole surah, so it takes surah + audio only.
        final request = http.MultipartRequest('POST', Uri.parse(apiUrl))
          ..fields['surah'] = selectedSurah.value.toString()
          ..files.add(
            await http.MultipartFile.fromPath('audio', audioFile.path),
          );
        final streamed = await request.send().timeout(_requestTimeout);
        final body =
            await streamed.stream.bytesToString().timeout(_requestTimeout);
        debugPrint('Response from backend: ${streamed.statusCode} $body');
        if (streamed.statusCode == 200) {
          _applyAnalysis(body);
        } else {
          Get.snackbar(
            'Analysis failed',
            'Server responded ${streamed.statusCode}: $body',
            snackPosition: SnackPosition.BOTTOM,
          );
        }
      } on TimeoutException {
        Get.snackbar(
          'Server is waking up',
          'The Cloud AI took too long to respond. Please try once more.',
          snackPosition: SnackPosition.BOTTOM,
        );
      } catch (error) {
        Get.snackbar(
          'Network Error',
          error.toString(),
          snackPosition: SnackPosition.BOTTOM,
        );
      } finally {
        isLoading.value = false;
      }
    } catch (error) {
      isRecording.value = false;
      isLoading.value = false;
      Get.snackbar(
        'Recording Error',
        error.toString(),
        snackPosition: SnackPosition.BOTTOM,
      );
    }
  }
  /// Reads the analyzer response for the whole surah:
  /// `{"surah": 2, "accuracy": 85,
  ///   "words": [{"text": "ءَامَنَ", "status": "correct"}]}`
  void _applyAnalysis(String body) {
    try {
      final decoded = jsonDecode(body);
      if (decoded is! Map) {
        throw const FormatException('Expected a JSON object');
      }
      final rawWords = decoded['words'];
      wordResults.assignAll(
        rawWords is! List
            ? const <RecitationWord>[]
            : rawWords
                .whereType<Map>()
                .map(
                  (word) =>
                      RecitationWord.fromJson(word.cast<String, dynamic>()),
                )
                .where((word) => word.text.isNotEmpty),
      );
      final rawAccuracy = decoded['accuracy'];
      final parsed = rawAccuracy is num
          ? rawAccuracy.round()
          : int.tryParse('$rawAccuracy') ?? 0;
      accuracy.value = parsed.clamp(0, 100);
      hasResult.value = true;
    } catch (error) {
      debugPrint('Failed to parse analysis JSON: $error');
      Get.snackbar(
        'Unexpected response',
        'The Cloud AI reply could not be read.',
        snackPosition: SnackPosition.BOTTOM,
      );
    }
  }
  Future<void> toggleRecording() async {
    if (isLoading.value) return;
    if (isRecording.value) {
      await stopRecording();
    } else {
      await startRecording();
    }
  }
}
