import 'dart:io';

import 'package:dio/dio.dart';
import 'package:flutter/material.dart';
import 'package:flutter/scheduler.dart';
import 'package:get/get.dart';
import 'package:just_audio/just_audio.dart';

import '../../screens/audio/quran_download_sheet.dart';
import '../services/audio_service.dart';
import '../services/quran_audio_store.dart';
import '../services/storage_service.dart';

enum QuranDownloadPhase { idle, downloading, saved, failed, cancelled }

/// Downloads surah recitations and drives the sticky player.
class QuranAudioController extends GetxController {
  final AudioService _audio = Get.find<AudioService>();
  final StorageService _storage = Get.find<StorageService>();
  final Dio _dio = Dio(
    BaseOptions(
      connectTimeout: const Duration(seconds: 30),
      receiveTimeout: const Duration(minutes: 30),
    ),
  );

  final isDownloading = false.obs;
  final downloadPhase = QuranDownloadPhase.idle.obs;
  final downloadPercent = 0.0.obs;
  final receivedBytes = 0.obs;
  final totalBytes = 0.obs;
  final downloadSurahNumber = 0.obs;
  final downloadSurahTitle = ''.obs;
  final downloadReciterName = ''.obs;
  final downloadError = RxnString();
  final downloadRevision = 0.obs;

  final _downloaded = <String>{};
  CancelToken? _cancelToken;
  int _job = 0;
  String _activeReciterId = '';
  int _activeSurahNumber = 0;

  bool get showPlayer => _audio.hasActiveAudio.value;

  bool get isPlaying => _audio.isPlaying.value;

  bool get isBuffering => _audio.isLoading.value;

  double get progress => _audio.progress;

  String get nowPlayingTitle {
    final name = _audio.currentSurahName.value.trim();
    return name.isEmpty ? 'Surah' : name;
  }

  String get nowPlayingArtist {
    final name = _audio.currentReciterName.value.trim();
    return name.isEmpty ? 'Qari' : name;
  }

  Duration get position => _audio.currentPosition.value;

  Duration get duration => _audio.totalDuration.value;

  String get percentLabel {
    if (downloadPhase.value == QuranDownloadPhase.saved) return '100%';
    if (totalBytes.value <= 0) return '0%';
    return QuranAudioStore.percentLabel(downloadPercent.value);
  }

  String get sizeLabel => QuranAudioStore.sizeLabelFromBytes(
        receivedBytes.value,
        totalBytes.value,
      );

  bool isCurrentTrack(int surahNumber) {
    if (surahNumber < 1 || !_audio.hasActiveAudio.value) return false;
    return _audio.currentSurahNumber.value == surahNumber &&
        _audio.currentReciterId.value == _storage.selectedReciterId.value;
  }

  bool isDownloaded(int surahNumber) {
    downloadRevision.value;
    if (surahNumber < 1) return false;
    return _downloaded.contains(_key(_storage.selectedReciterId.value, surahNumber));
  }

  bool isDownloadingSurah(int surahNumber) {
    return isDownloading.value &&
        _activeSurahNumber == surahNumber &&
        _activeReciterId == _storage.selectedReciterId.value;
  }

  Future<void> refreshDownloaded(int surahNumber) async {
    if (surahNumber < 1) return;
    final reciterId = _storage.selectedReciterId.value;
    final file = await QuranAudioStore.surahFile(reciterId, surahNumber);
    _markDownloaded(reciterId, surahNumber, await QuranAudioStore.isComplete(file));
  }

  Future<void> playOrToggle({
    required int surahNumber,
    required String surahName,
  }) async {
    if (surahNumber < 1) return;
    try {
      await _audio.togglePlay(
        surahNumber: surahNumber,
        reciterIdentifier: _storage.selectedReciterId.value,
        reciterName: _storage.selectedReciterName.value,
        surahName: surahName,
      );
    } catch (_) {
      Get.snackbar('Audio', 'Unable to play this surah right now.');
    }
  }

  Future<void> toggleCurrent() async {
    if (!_audio.hasActiveAudio.value) return;
    try {
      if (_audio.processing.value == ProcessingState.completed) {
        await _audio.seek(Duration.zero);
        await _audio.resume();
        return;
      }
      if (_audio.isPlaying.value) {
        await _audio.pause();
      } else {
        await _audio.resume();
      }
    } catch (_) {
      Get.snackbar('Audio', 'Unable to control playback right now.');
    }
  }

  Future<void> rewind() => _audio.seekBy(const Duration(seconds: -10));

  Future<void> forward() => _audio.seekBy(const Duration(seconds: 10));

  Future<void> seekToFraction(double value) => _audio.seekToFraction(value);

  Future<void> downloadSurah({
    required int surahNumber,
    required String surahName,
  }) async {
    if (surahNumber < 1 || surahNumber > 114) return;
    final reciterId = _storage.selectedReciterId.value;
    final reciterName = _storage.selectedReciterName.value;
    downloadSurahNumber.value = surahNumber;
    downloadSurahTitle.value = surahName.trim().isEmpty
        ? 'Surah $surahNumber'
        : surahName.trim();
    downloadReciterName.value = reciterName;
    downloadError.value = null;

    final sameActiveJob = isDownloading.value &&
        _activeReciterId == reciterId &&
        _activeSurahNumber == surahNumber;
    if (sameActiveJob) {
      _presentSheet();
      return;
    }

    final existing = await QuranAudioStore.surahFile(reciterId, surahNumber);
    if (await QuranAudioStore.isComplete(existing)) {
      await _showSaved(existing, reciterId, surahNumber);
      _presentSheet();
      return;
    }

    downloadPhase.value = QuranDownloadPhase.downloading;
    downloadPercent.value = 0;
    receivedBytes.value = 0;
    totalBytes.value = 0;
    _presentSheet();
    await _runDownload(
      surahNumber: surahNumber,
      reciterId: reciterId,
    );
  }

  Future<void> cancelDownload() async {
    _cancelToken?.cancel('cancelled');
  }

  Future<void> _runDownload({
    required int surahNumber,
    required String reciterId,
  }) async {
    final job = ++_job;
    _cancelToken?.cancel('replaced');
    final token = CancelToken();
    _cancelToken = token;
    _activeReciterId = reciterId;
    _activeSurahNumber = surahNumber;

    final destination = await QuranAudioStore.surahFile(reciterId, surahNumber);
    if (await QuranAudioStore.isComplete(destination)) {
      if (job != _job) return;
      await _showSaved(destination, reciterId, surahNumber);
      return;
    }

    isDownloading.value = true;
    downloadPhase.value = QuranDownloadPhase.downloading;
    downloadPercent.value = 0;
    receivedBytes.value = 0;
    totalBytes.value = 0;

    final partial = File('${destination.path}.part');
    try {
      await destination.parent.create(recursive: true);
      if (await partial.exists()) await partial.delete();

      await _dio.download(
        _audio.audioUrl(surahNumber, reciterId),
        partial.path,
        cancelToken: token,
        onReceiveProgress: (received, total) {
          if (job != _job) return;
          receivedBytes.value = received;
          totalBytes.value = total < 0 ? 0 : total;
          downloadPercent.value = QuranAudioStore.percent(
            received,
            totalBytes.value,
          );
        },
      );

      if (job != _job || token.isCancelled) return;
      if (await destination.exists()) await destination.delete();
      await partial.rename(destination.path);
      await _showSaved(destination, reciterId, surahNumber);
    } on DioException catch (error) {
      if (job != _job) return;
      await _deleteIfExists(partial);
      if (CancelToken.isCancel(error)) {
        isDownloading.value = false;
        downloadPhase.value = QuranDownloadPhase.cancelled;
        downloadError.value = null;
        return;
      }
      _fail(job, 'The download stopped. Check your connection and try again.');
    } catch (_) {
      if (job != _job) return;
      await _deleteIfExists(partial);
      _fail(job, 'The download stopped. Check your connection and try again.');
    } finally {
      if (job == _job) isDownloading.value = false;
    }
  }

  Future<void> _showSaved(File file, String reciterId, int surahNumber) async {
    final length = await file.length();
    receivedBytes.value = length;
    totalBytes.value = length;
    downloadPercent.value = 100;
    downloadPhase.value = QuranDownloadPhase.saved;
    isDownloading.value = false;
    _markDownloaded(reciterId, surahNumber, true);
  }

  void _fail(int job, String message) {
    if (job != _job) return;
    isDownloading.value = false;
    downloadPhase.value = QuranDownloadPhase.failed;
    downloadError.value = message;
  }

  void _markDownloaded(String reciterId, int surahNumber, bool downloaded) {
    final key = _key(reciterId, surahNumber);
    if (downloaded) {
      _downloaded.add(key);
    } else {
      _downloaded.remove(key);
    }
    downloadRevision.value++;
  }

  void _presentSheet() {
    if (Get.isBottomSheetOpen ?? false) return;
    SchedulerBinding.instance.addPostFrameCallback((_) {
      if (isClosed || (Get.isBottomSheetOpen ?? false)) return;
      Get.bottomSheet(
        const QuranDownloadSheet(),
        isScrollControlled: true,
        backgroundColor: const Color(0x00000000),
      );
    });
  }

  String _key(String reciterId, int surahNumber) => '$reciterId:$surahNumber';

  Future<void> _deleteIfExists(File file) async {
    if (await file.exists()) await file.delete();
  }

  @override
  void onClose() {
    _job++;
    _cancelToken?.cancel('closed');
    _dio.close(force: true);
    super.onClose();
  }
}
