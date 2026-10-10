import 'package:get/get.dart';

import 'worship_controller.dart';

class WorshipBinding extends Bindings {
  @override
  void dependencies() {
    if (!Get.isRegistered<WorshipController>()) {
      Get.put(WorshipController());
    }
  }
}
