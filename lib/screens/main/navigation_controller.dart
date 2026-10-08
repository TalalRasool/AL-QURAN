import 'package:get/get.dart';

class NavigationController extends GetxController {
  static const hadithTabIndex = 2;
  static const audioTabIndex = 3;
  static const profileTabIndex = 4;

  final currentIndex = 0.obs;

  void changeTab(int index) {
    currentIndex.value = index;
  }
}
