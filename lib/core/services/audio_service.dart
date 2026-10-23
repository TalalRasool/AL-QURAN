import 'dart:async';
import 'dart:io';

import 'package:flutter/foundation.dart';
import 'package:get/get.dart';
import 'package:just_audio/just_audio.dart';
import 'package:just_audio_background/just_audio_background.dart';
import 'package:permission_handler/permission_handler.dart';

import 'quran_audio_store.dart';

class AudioService extends GetxService {
  static const _surahCdnBase =
      'https://cdn.islamic.network/quran/audio-surah/128';
  static const _ayahCdnBase = 'https://cdn.islamic.network/quran/audio/128';

  AudioPlayer? _player;
  final _subscriptions = <StreamSubscription<dynamic>>[];

  final isPlaying = false.obs;
  final isLoading = false.obs;
  final hasActiveAudio = false.obs;
  final currentPosition = Duration.zero.obs;
  final totalDuration = Duration.zero.obs;
  final bufferedPosition = Duration.zero.obs;
  final currentSurahNumber = 0.obs;
  final currentAyahNumber = 0.obs;
  final currentSurahName = ''.obs;
  final currentReciterId = ''.obs;
  final currentReciterName = ''.obs;
  final processing = ProcessingState.idle.obs;

  AudioPlayer get _audio {
    final existing = _player;
    if (existing != null) return existing;
    final created = AudioPlayer();
    _player = created;
    _bind(created);
    return created;
  }

  Future<AudioService> init() async {
    try {
      _audio;
    } catch (_) {
      // Player plugins are unavailable in some test environments.
    }
    return this;
  }

  void _bind(AudioPlayer player) {
    _subscriptions.add(
      player.playerStateStream.listen((state) {
        processing.value = state.processingState;
        isPlaying.value = state.playing;
        if (state.processingState == ProcessingState.completed) {
          isPlaying.value = false;
        }
      }),
    );
    _subscriptions.add(
      player.positionStream.listen((position) {
        currentPosition.value = position;
      }),
    );
    _subscriptions.add(
      player.durationStream.listen((duration) {
        totalDuration.value = duration ?? Duration.zero;
      }),
    );
    _subscriptions.add(
      player.bufferedPositionStream.listen((position) {
        bufferedPosition.value = position;
      }),
    );
  }

  double get progress {
    final total = totalDuration.value.inMilliseconds;
    if (total <= 0) return 0;
    return (currentPosition.value.inMilliseconds / total).clamp(0.0, 1.0);
  }

  String audioUrl(int surahNumber, String reciterIdentifier) {
    return '$_surahCdnBase/$reciterIdentifier/$surahNumber.mp3';
  }

  String ayahAudioUrl(int globalAyahNumber, String reciterIdentifier) {
    return '$_ayahCdnBase/$reciterIdentifier/$globalAyahNumber.mp3';
  }

  Future<void> playSurah(
    int surahNumber,
    String reciterIdentifier, {
    String? reciterName,
    String? surahName,
  }) async {
    isLoading.value = true;
    currentSurahNumber.value = surahNumber;
    currentAyahNumber.value = 0;
    currentReciterId.value = reciterIdentifier;
    if (reciterName != null && reciterName.isNotEmpty) {
      currentReciterName.value = reciterName;
    }
    final title = (surahName == null || surahName.trim().isEmpty)
        ? 'Surah $surahNumber'
        : surahName.trim();
    currentSurahName.value = title;

    try {
      await _requestNotificationPermission();
      final local = await QuranAudioStore.surahFile(
        reciterIdentifier,
        surahNumber,
      );
      final artist = currentReciterName.value.trim().isEmpty
          ? 'Qari'
          : currentReciterName.value.trim();
      final tag = MediaItem(
        id: '$reciterIdentifier:$surahNumber',
        album: 'Al Quran',
        title: title,
        artist: artist,
        artUri: await QuranAudioStore.artworkUri(),
      );
      await _audio.stop();
      final onlineUrl = audioUrl(surahNumber, reciterIdentifier);
      if (await File(local.path).exists()) {
        try {
          await _audio.setFilePath(local.path, tag: tag);
        } catch (_) {
          await _audio.setUrl(onlineUrl, tag: tag);
        }
      } else {
        await _audio.setUrl(onlineUrl, tag: tag);
      }
      hasActiveAudio.value = true;
      await _audio.play();
    } catch (_) {
      isPlaying.value = false;
      rethrow;
    } finally {
      isLoading.value = false;
    }
  }

  Future<void> _requestNotificationPermission() async {
    try {
      if (kIsWeb || !Platform.isAndroid) return;
      final status = await Permission.notification.status;
      if (status.isGranted || status.isLimited || status.isPermanentlyDenied) {
        return;
      }
      await Permission.notification.request();
    } catch (_) {}
  }

  Future<void> pause() async {
    try {
      await _audio.pause();
    } catch (_) {}
  }

  Future<void> resume() async {
    if (_audio.processingState == ProcessingState.completed) {
      await _audio.seek(Duration.zero);
    }
    await _audio.play();
  }

  Future<void> stop({bool clearSession = true}) async {
    try {
      await _audio.stop();
    } catch (_) {}
    if (clearSession) {
      hasActiveAudio.value = false;
      currentPosition.value = Duration.zero;
    }
  }

  Future<void> seek(Duration position) => _audio.seek(position);

  Future<void> seekBy(Duration offset) async {
    var target = currentPosition.value + offset;
    if (target < Duration.zero) target = Duration.zero;
    final total = totalDuration.value;
    if (total > Duration.zero && target > total) target = total;
    await seek(target);
  }

  Future<void> seekToFraction(double value) async {
    final total = totalDuration.value.inMilliseconds;
    if (total <= 0) return;
    final fraction = value.clamp(0.0, 1.0);
    await seek(Duration(milliseconds: (fraction * total).round()));
  }

  Future<void> playAyah({
    required int surahNumber,
    required int ayahNumber,
    required int globalAyahNumber,
    required String reciterIdentifier,
    String? reciterName,
    String? surahName,
  }) async {
    isLoading.value = true;
    currentSurahNumber.value = surahNumber;
    currentAyahNumber.value = ayahNumber;
    currentReciterId.value = reciterIdentifier;
    if (reciterName != null && reciterName.isNotEmpty) {
      currentReciterName.value = reciterName;
    }
    final surahTitle = (surahName == null || surahName.trim().isEmpty)
        ? 'Surah $surahNumber'
        : surahName.trim();
    currentSurahName.value = '$surahTitle · Ayah $ayahNumber';

    try {
      await _requestNotificationPermission();
      final local = await QuranAudioStore.ayahFile(
        reciterIdentifier,
        globalAyahNumber,
      );
      final artist = currentReciterName.value.trim().isEmpty
          ? 'Qari'
          : currentReciterName.value.trim();
      final tag = MediaItem(
        id: '$reciterIdentifier:$surahNumber:$ayahNumber',
        album: 'Al Quran',
        title: currentSurahName.value,
        artist: artist,
        artUri: await QuranAudioStore.artworkUri(),
      );
      final onlineUrl = ayahAudioUrl(globalAyahNumber, reciterIdentifier);
      await _audio.stop();
      if (await File(local.path).exists()) {
        try {
          await _audio.setFilePath(local.path, tag: tag);
        } catch (_) {
          await _audio.setUrl(onlineUrl, tag: tag);
        }
      } else {
        await _audio.setUrl(onlineUrl, tag: tag);
      }
      hasActiveAudio.value = true;
      await _audio.play();
    } catch (_) {
      isPlaying.value = false;
      rethrow;
    } finally {
      isLoading.value = false;
    }
  }

  Future<void> playLocalSurahFile({
    required File file,
    required int surahNumber,
    required String reciterIdentifier,
    String? reciterName,
    String? surahName,
  }) async {
    isLoading.value = true;
    currentSurahNumber.value = surahNumber;
    currentAyahNumber.value = 0;
    currentReciterId.value = reciterIdentifier;
    if (reciterName != null && reciterName.isNotEmpty) {
      currentReciterName.value = reciterName;
    }
    final title = (surahName == null || surahName.trim().isEmpty)
        ? 'Surah $surahNumber'
        : surahName.trim();
    currentSurahName.value = title;
    try {
      await _requestNotificationPermission();
      final artist = currentReciterName.value.trim().isEmpty
          ? 'Qari'
          : currentReciterName.value.trim();
      await _audio.stop();
      await _audio.setFilePath(
        file.path,
        tag: MediaItem(
          id: '$reciterIdentifier:$surahNumber',
          album: 'Al Quran',
          title: title,
          artist: artist,
          artUri: await QuranAudioStore.artworkUri(),
        ),
      );
      hasActiveAudio.value = true;
      await _audio.play();
    } catch (_) {
      isPlaying.value = false;
      rethrow;
    } finally {
      isLoading.value = false;
    }
  }

  Future<void> toggleAyah({
    required int surahNumber,
    required int ayahNumber,
    required int globalAyahNumber,
    required String reciterIdentifier,
    String? reciterName,
    String? surahName,
  }) async {
    final isSameAyah =
        currentSurahNumber.value == surahNumber &&
        currentAyahNumber.value == ayahNumber &&
        currentReciterId.value == reciterIdentifier &&
        hasActiveAudio.value;
    if (isSameAyah && isPlaying.value) {
      await pause();
      return;
    }
    if (isSameAyah && !isPlaying.value) {
      await resume();
      return;
    }
    await playAyah(
      surahNumber: surahNumber,
      ayahNumber: ayahNumber,
      globalAyahNumber: globalAyahNumber,
      reciterIdentifier: reciterIdentifier,
      reciterName: reciterName,
      surahName: surahName,
    );
  }

  Future<void> togglePlay({
    required int surahNumber,
    required String reciterIdentifier,
    String? reciterName,
    String? surahName,
  }) async {
    final isSameTrack =
        currentSurahNumber.value == surahNumber &&
        currentAyahNumber.value == 0 &&
        currentReciterId.value == reciterIdentifier &&
        hasActiveAudio.value;

    if (isSameTrack && isPlaying.value) {
      await pause();
      return;
    }
    if (isSameTrack && !isPlaying.value) {
      await resume();
      return;
    }
    await playSurah(
      surahNumber,
      reciterIdentifier,
      reciterName: reciterName,
      surahName: surahName,
    );
  }

  @override
  void onClose() {
    for (final subscription in _subscriptions) {
      subscription.cancel();
    }
    _subscriptions.clear();
    _player?.dispose();
    super.onClose();
  }
}
