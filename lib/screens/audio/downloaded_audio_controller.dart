import 'package:get/get.dart';

import '../../core/controllers/quran_audio_controller.dart';
import '../../core/data/quran_repository.dart';
import '../../core/services/quran_audio_store.dart';

class DownloadedAudioItem {
  const DownloadedAudioItem({
    required this.file,
    required this.surahNumber,
    required this.surahName,
    required this.reciterId,
    required this.bytes,
  });

  final LocalSurahAudio file;
  final int surahNumber;
  final String surahName;
  final String reciterId;
  final int bytes;

  String get sizeLabel =>
      '${QuranAudioStore.megabytes(bytes).toStringAsFixed(1)} MB';
}

class DownloadedAudioController extends GetxController {
  final items = <DownloadedAudioItem>[].obs;
  final isLoading = false.obs;

  QuranAudioController get _player => Get.find<QuranAudioController>();

  @override
  void onInit() {
    super.onInit();
    load();
  }

  Future<void> load() async {
    isLoading.value = true;
    try {
      final files = await QuranAudioStore.listSurahFiles();
      final names = await _surahNames();
      items.assignAll([
        for (final file in files)
          DownloadedAudioItem(
            file: file,
            surahNumber: file.surahNumber,
            surahName: names[file.surahNumber] ?? 'Surah ${file.surahNumber}',
            reciterId: file.reciterId,
            bytes: file.bytes,
          ),
      ]);
    } catch (_) {
      items.clear();
    } finally {
      isLoading.value = false;
    }
  }

  Future<void> play(DownloadedAudioItem item) {
    return _player.playDownloadedSurah(
      file: item.file.file,
      surahNumber: item.surahNumber,
      reciterId: item.reciterId,
      surahName: item.surahName,
      reciterName: _reciterLabel(item.reciterId),
    );
  }

  Future<void> delete(DownloadedAudioItem item) async {
    await _player.deleteDownloadedSurah(
      file: item.file.file,
      surahNumber: item.surahNumber,
      reciterId: item.reciterId,
    );
    items.remove(item);
  }

  Future<Map<int, String>> _surahNames() async {
    if (!Get.isRegistered<QuranRepository>()) return const {};
    try {
      final surahs = await Get.find<QuranRepository>().getAllSurahs();
      return {
        for (final surah in surahs)
          if (surah.englishName.isNotEmpty) surah.number: surah.englishName,
      };
    } catch (_) {
      return const {};
    }
  }

  String _reciterLabel(String reciterId) {
    return reciterId.replaceAll('.', ' ').replaceAll('_', ' ');
  }
}
