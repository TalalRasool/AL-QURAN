import 'package:get/get.dart';

import 'translations_controller.dart';

class TranslationsBinding extends Bindings {
  @override
  void dependencies() {
    Get.lazyPut<TranslationsController>(
      TranslationsController.new,
      fenix: true,
    );
  }
}
