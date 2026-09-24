import 'package:get/get.dart';

import 'quran_reading_controller.dart';

class QuranReadingBinding extends Bindings {
  @override
  void dependencies() {
    if (Get.isRegistered<QuranReadingController>()) {
      Get.delete<QuranReadingController>(force: true);
    }
    Get.put(QuranReadingController());
  }
}
