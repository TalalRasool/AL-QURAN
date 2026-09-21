import 'package:get/get.dart';

import 'mushaf_controller.dart';

class MushafBinding extends Bindings {
  @override
  void dependencies() {
    if (Get.isRegistered<MushafController>()) {
      Get.delete<MushafController>(force: true);
    }
    Get.put(
      MushafController(
        initialPage: MushafController.resolveInitialPage(Get.arguments),
      ),
    );
  }
}
