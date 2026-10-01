import 'package:get/get.dart';

import 'hadith_chapters_controller.dart';
import 'hadith_read_controller.dart';

class HadithChaptersBinding extends Bindings {
  @override
  void dependencies() {
    if (Get.isRegistered<HadithChaptersController>()) {
      Get.delete<HadithChaptersController>(force: true);
    }
    Get.put(HadithChaptersController());
  }
}

class HadithReadBinding extends Bindings {
  @override
  void dependencies() {
    if (Get.isRegistered<HadithReadController>()) {
      Get.delete<HadithReadController>(force: true);
    }
    Get.put(HadithReadController());
  }
}
