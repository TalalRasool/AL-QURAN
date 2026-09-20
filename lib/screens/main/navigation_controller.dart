import 'package:get/get.dart';

import '../../core/services/audio_service.dart';

class NavigationController extends GetxController {
  static const hadithTabIndex = 2;
  static const audioTabIndex = 3;
  static const profileTabIndex = 4;

  final currentIndex = 0.obs;

  void changeTab(int index) {
    if (index != audioTabIndex) {
      _pauseAudio();
    }
    currentIndex.value = index;
  }

  void _pauseAudio() {
    if (!Get.isRegistered<AudioService>()) return;
    final audio = Get.find<AudioService>();
    if (audio.isPlaying.value || audio.isLoading.value) {
      audio.pause();
    }
  }
}
