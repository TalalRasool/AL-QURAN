import 'package:get/get.dart';

import 'islamic_history_controller.dart';

class IslamicHistoryBinding extends Bindings {
  @override
  void dependencies() {
    if (Get.isRegistered<IslamicHistoryController>()) {
      Get.delete<IslamicHistoryController>(force: true);
    }
    Get.put(IslamicHistoryController());
  }
}
