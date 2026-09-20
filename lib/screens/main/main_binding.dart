import 'package:get/get.dart';

import '../../features/hadith/hadith_books_controller.dart';
import '../audio/audio_controller.dart';
import '../home/home_controller.dart';
import '../profile/profile_controller.dart';
import '../quran/quran_controller.dart';
import 'navigation_controller.dart';

class MainBinding extends Bindings {
  @override
  void dependencies() {
    Get.put(NavigationController());
    Get.lazyPut<HomeController>(HomeController.new, fenix: true);
    Get.lazyPut<QuranController>(QuranController.new, fenix: true);
    Get.lazyPut<HadithBooksController>(HadithBooksController.new, fenix: true);
    Get.lazyPut<AudioController>(AudioController.new, fenix: true);
    Get.lazyPut<ProfileController>(ProfileController.new, fenix: true);
  }
}
