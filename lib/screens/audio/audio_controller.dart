import 'package:get/get.dart';

import '../../core/data/models/reciter.dart';
import '../../core/data/quran_repository.dart';
import '../../core/services/audio_service.dart';
import '../../core/services/storage_service.dart';

class AudioController extends GetxController {
  final reciters = <Reciter>[].obs;
  final isLoading = false.obs;
  final errorMessage = RxnString();

  final QuranRepository _quran = Get.find<QuranRepository>();
  final StorageService _storage = Get.find<StorageService>();
  final AudioService _audio = Get.find<AudioService>();

  @override
  void onInit() {
    super.onInit();
    loadReciters();
  }

  Future<void> loadReciters() async {
    isLoading.value = true;
    errorMessage.value = null;
    try {
      reciters.assignAll(await _quran.getReciters());
    } catch (_) {
      errorMessage.value =
          'Unable to load reciters. Check your connection and try again.';
    } finally {
      isLoading.value = false;
    }
  }

  bool isSelected(Reciter reciter) =>
      _storage.selectedReciterId.value == reciter.identifier;

  bool isPlaying(Reciter reciter) =>
      _audio.isPlaying.value &&
      _audio.currentReciterId.value == reciter.identifier;

  Future<void> selectReciter(Reciter reciter) {
    return _storage.saveReciter(
      identifier: reciter.identifier,
      name: reciter.displayName,
    );
  }

  Future<void> playReciter(Reciter reciter) async {
    await selectReciter(reciter);
    final surahNumber = _storage.lastRead.value?.surahNumber ?? 1;
    try {
      await _audio.togglePlay(
        surahNumber: surahNumber,
        reciterIdentifier: reciter.identifier,
        reciterName: reciter.displayName,
      );
    } catch (_) {
      Get.snackbar('Audio', 'Unable to play this reciter right now.');
    }
  }
}
