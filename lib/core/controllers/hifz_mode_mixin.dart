import 'package:get/get.dart';

mixin HifzModeMixin on GetxController {
  final isHifzMode = false.obs;
  final revealedAyahs = <int>{}.obs;

  static int ayahId(int surahNumber, int ayahNumber) =>
      surahNumber * 10000 + ayahNumber;

  void toggleHifzMode() {
    isHifzMode.toggle();
    resetRevealedAyahs();
  }

  void toggleAyahReveal(int ayahNumber) {
    if (!isHifzMode.value) return;
    if (revealedAyahs.contains(ayahNumber)) {
      revealedAyahs.remove(ayahNumber);
    } else {
      revealedAyahs.add(ayahNumber);
    }
    revealedAyahs.refresh();
  }

  void resetRevealedAyahs() {
    revealedAyahs.clear();
  }

  bool isAyahRevealed(int ayahNumber) => revealedAyahs.contains(ayahNumber);
}
