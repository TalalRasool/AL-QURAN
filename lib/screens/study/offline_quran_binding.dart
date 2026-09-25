import 'package:get/get.dart';

import 'offline_quran_controller.dart';

class OfflineQuranBinding extends Bindings {
  @override
  void dependencies() {
    if (Get.isRegistered<OfflineQuranController>()) {
      Get.delete<OfflineQuranController>(force: true);
    }
    Get.put(OfflineQuranController());
  }
}
