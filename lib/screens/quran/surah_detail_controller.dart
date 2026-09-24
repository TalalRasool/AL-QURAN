import 'package:get/get.dart';

import '../../core/controllers/bookmark_controller.dart';
import '../../core/controllers/hifz_mode_mixin.dart';
import '../../core/data/models/app_bookmark.dart';
import '../../core/data/models/ayah.dart';
import '../../core/data/models/surah.dart';
import '../../core/data/quran_repository.dart';
import '../../core/services/audio_service.dart';
import '../../core/services/storage_service.dart';

class SurahDetailController extends GetxController with HifzModeMixin {
  final isLoading = false.obs;
  final errorMessage = RxnString();
  final surah = Rxn<Surah>();
  final ayahs = <Ayah>[].obs;
  final highlightedAyah = 1.obs;
  final highlightedSurah = 0.obs;
  final juzNumber = RxnInt();

  final QuranRepository _quran = Get.find<QuranRepository>();
  final StorageService _storage = Get.find<StorageService>();
  final AudioService _audio = Get.find<AudioService>();
  Worker? _translationWorker;

  @override
  void onInit() {
    super.onInit();
    juzNumber.value = _juzFromArgs;
    _translationWorker = ever(_storage.selectedTranslationId, (_) => load());
    load();
  }

  @override
  void onClose() {
    _translationWorker?.dispose();
    super.onClose();
  }

  bool get isJuzMode => juzNumber.value != null;

  bool get showBismillah {
    if (isJuzMode) return false;
    final number = surah.value?.number ?? 0;
    return number != 1 && number != 9;
  }

  String get title {
    if (isJuzMode) return 'Juz ${juzNumber.value}';
    return surah.value?.englishName ?? 'Surah';
  }

  int? get _surahNumberOrNull {
    final args = Get.arguments;
    if (args is int && args >= 1 && args <= 114) return args;
    return null;
  }

  int? get _juzFromArgs {
    final args = Get.arguments;
    if (args is Map && args['juz'] is int) {
      final value = args['juz'] as int;
      if (value >= 1 && value <= 30) return value;
    }
    return null;
  }

  Future<void> load() async {
    isLoading.value = true;
    errorMessage.value = null;
    try {
      if (isJuzMode) {
        await _loadJuz(juzNumber.value!);
      } else {
        final number = _surahNumberOrNull;
        if (number == null) {
          errorMessage.value = 'This surah could not be found.';
          return;
        }
        await _loadSurah(number);
      }
    } catch (_) {
      errorMessage.value = isJuzMode
          ? 'Unable to load this juz from the offline Quran data.'
          : 'Unable to load this surah from the offline Quran data.';
    } finally {
      isLoading.value = false;
    }
  }

  Future<void> _loadSurah(int number) async {
    final loadedSurah = await _quran.getSurahByNumber(number);
    final loadedAyahs = await _quran.getAyahs(loadedSurah.number);
    surah.value = loadedSurah;
    ayahs.assignAll(loadedAyahs);

    highlightedSurah.value = loadedSurah.number;
    highlightedAyah.value =
        loadedAyahs.isNotEmpty ? loadedAyahs.first.number : 1;
    final saved = _storage.lastRead.value;
    if (saved != null && saved.surahNumber == loadedSurah.number) {
      highlightedAyah.value = saved.ayahNumber;
    }

    await _storage.saveLastRead(
      surahNumber: loadedSurah.number,
      ayahNumber: highlightedAyah.value,
    );
  }

  Future<void> _loadJuz(int number) async {
    final loadedAyahs = await _quran.getJuzAyahs(number);
    if (loadedAyahs.isEmpty) {
      throw StateError('Juz $number has no ayahs');
    }
    ayahs.assignAll(loadedAyahs);

    final first = loadedAyahs.first;
    final startSurah = first.surahNumber > 0 ? first.surahNumber : 1;
    surah.value = await _quran.getSurahByNumber(startSurah);
    highlightedSurah.value = startSurah;
    highlightedAyah.value = first.number;
    await _storage.saveLastRead(
      surahNumber: startSurah,
      ayahNumber: first.number,
    );
  }

  bool get isRtlTranslation =>
      _storage.selectedTranslationDirection.value.toLowerCase() == 'rtl';

  String get reciterName {
    if (_audio.currentReciterName.value.isNotEmpty) {
      return _audio.currentReciterName.value;
    }
    return _storage.selectedReciterName.value;
  }

  bool get isAudioLoading => _audio.isLoading.value;

  double get progress => _audio.progress;

  bool get isPlayingThisSurah {
    final number = surah.value?.number;
    return number != null &&
        _audio.isPlaying.value &&
        _audio.currentSurahNumber.value == number;
  }

  bool isHighlighted(Ayah ayah) {
    if (isJuzMode) {
      return ayah.surahNumber == highlightedSurah.value &&
          ayah.number == highlightedAyah.value;
    }
    return ayah.number == highlightedAyah.value;
  }

  int hifzIdFor(Ayah ayah) {
    final surahNumber = ayah.surahNumber > 0
        ? ayah.surahNumber
        : (surah.value?.number ?? 0);
    return HifzModeMixin.ayahId(surahNumber, ayah.number);
  }

  Future<void> togglePlay() async {
    final number = surah.value?.number;
    if (number == null) return;
    try {
      await _audio.togglePlay(
        surahNumber: number,
        reciterIdentifier: _storage.selectedReciterId.value,
        reciterName: _storage.selectedReciterName.value,
      );
    } catch (_) {
      Get.snackbar('Audio', 'Unable to play this surah right now.');
    }
  }

  Future<void> seekToProgress(double value) async {
    final total = _audio.totalDuration.value.inMilliseconds;
    if (total <= 0) return;
    await _audio.seek(Duration(milliseconds: (value * total).round()));
  }

  Future<void> skipBack() => _audio.seek(Duration.zero);

  Future<void> skipForward() async {
    final next = _audio.currentPosition.value + const Duration(seconds: 10);
    final total = _audio.totalDuration.value;
    await _audio.seek(next > total ? total : next);
  }

  Future<void> toggleBookmark() async {
    final current = surah.value;
    if (current == null) return;
    await Get.find<BookmarkController>().toggle(
      AppBookmark.translation(
        surahNumber: current.number,
        englishName: current.englishName,
        arabicName: current.arabicName,
        verseCount: current.verseCount,
      ),
    );
  }
}
