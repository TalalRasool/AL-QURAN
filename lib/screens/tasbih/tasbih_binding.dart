import 'package:get/get.dart';

import 'tasbih_controller.dart';

class TasbihBinding extends Bindings {
  @override
  void dependencies() {
    if (Get.isRegistered<TasbihController>()) {
      Get.delete<TasbihController>(force: true);
    }
    Get.put(TasbihController());
  }
}
