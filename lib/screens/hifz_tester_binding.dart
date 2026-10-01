import 'package:get/get.dart';

import '../controllers/hifz_tester_controller.dart';

class HifzTesterBinding extends Bindings {
  @override
  void dependencies() {
    if (Get.isRegistered<HifzTesterController>()) {
      Get.delete<HifzTesterController>(force: true);
    }
    Get.put(HifzTesterController());
  }
}
