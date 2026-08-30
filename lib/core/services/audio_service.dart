import 'dart:async';

import 'package:get/get.dart';
import 'package:just_audio/just_audio.dart';

class AudioService extends GetxService {
  static const _cdnBase =
      'https://cdn.islamic.network/quran/audio-surah/128';

  AudioPlayer? _player;
  final _subscriptions = <StreamSubscription<dynamic>>[];

  final isPlaying = false.obs;
  final isLoading = false.obs;
  final currentPosition = Duration.zero.obs;
  final totalDuration = Duration.zero.obs;
  final bufferedPosition = Duration.zero.obs;
  final currentSurahNumber = 0.obs;
  final currentReciterId = ''.obs;
  final currentReciterName = ''.obs;

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
        isPlaying.value = state.playing;
        if (state.processingState == ProcessingState.completed) {
          isPlaying.value = false;
          currentPosition.value = Duration.zero;
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
    return '$_cdnBase/$reciterIdentifier/$surahNumber.mp3';
  }

  Future<void> playSurah(int surahNumber, String reciterIdentifier, {String? reciterName}) async {
    isLoading.value = true;
    currentSurahNumber.value = surahNumber;
    currentReciterId.value = reciterIdentifier;
    if (reciterName != null && reciterName.isNotEmpty) {
      currentReciterName.value = reciterName;
    }

    try {
      final url = audioUrl(surahNumber, reciterIdentifier);
      await _audio.stop();
      await _audio.setUrl(url);
      await _audio.play();
    } catch (_) {
      isPlaying.value = false;
      rethrow;
    } finally {
      isLoading.value = false;
    }
  }

  Future<void> pause() async {
    try {
      await _audio.pause();
    } catch (_) {}
  }

  Future<void> resume() => _audio.play();

  Future<void> stop() => _audio.stop();

  Future<void> seek(Duration position) => _audio.seek(position);

  Future<void> togglePlay({
    required int surahNumber,
    required String reciterIdentifier,
    String? reciterName,
  }) async {
    final isSameTrack = currentSurahNumber.value == surahNumber &&
        currentReciterId.value == reciterIdentifier &&
        totalDuration.value > Duration.zero;

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
