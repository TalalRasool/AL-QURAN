import 'package:get/get.dart';

import 'surah_detail_controller.dart';

class SurahDetailBinding extends Bindings {
  @override
  void dependencies() {
    if (Get.isRegistered<SurahDetailController>()) {
      Get.delete<SurahDetailController>(force: true);
    }
    Get.put(SurahDetailController());
  }
}
