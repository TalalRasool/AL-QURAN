import 'dart:convert';

import 'package:flutter/services.dart';
import 'package:flutter/widgets.dart';
import 'package:get/get.dart';
import 'package:scrollable_positioned_list/scrollable_positioned_list.dart';

import '../../core/constants/app_assets.dart';
import '../../core/controllers/bookmark_controller.dart';
import '../../core/data/models/app_bookmark.dart';
import '../../core/data/models/azkar_dua.dart';
import '../../core/services/storage_service.dart';

class TasbihController extends GetxController {
  static const int maxCount = StorageService.tasbihMaxCount;

  final tabIndex = 0.obs;
  final count = 0.obs;
  final target = maxCount;
  final dhikr = 'SubhanAllah';
  final dhikrTranslation = 'Glory be to Allah';
  final azkar = <AzkarItem>[].obs;
  final duas = <DuaItem>[].obs;
  final isContentLoading = false.obs;
  final contentError = RxnString();
  final highlightDuaId = ''.obs;
  final duaRevealIndex = 0.obs;
  final duaScrollController = ItemScrollController();

  final StorageService _storage = Get.find<StorageService>();
  Worker? _countWorker;

  double get progress =>
      target == 0 ? 0 : (count.value / target).clamp(0, 1);

  BookmarkController get _bookmarks => Get.find<BookmarkController>();

  @override
  void onInit() {
    super.onInit();
    count.value = _storage.getTasbihCount().clamp(0, maxCount);
    _countWorker = ever(_storage.tasbihCount, (value) {
      count.value = value.clamp(0, maxCount);
    });
    applyRouteArgs(Get.arguments);
    loadContent();
  }

  @override
  void onClose() {
    _countWorker?.dispose();
    super.onClose();
  }

  void applyRouteArgs(dynamic args) {
    if (args is! Map) return;
    final tab = args['tab'];
    if (tab is int) tabIndex.value = tab.clamp(0, 2);
    final duaId = '${args['duaId'] ?? ''}'.trim();
    if (duaId.isNotEmpty) {
      highlightDuaId.value = duaId;
      tabIndex.value = 1;
    }
  }

  void onTabChanged(int index) {
    tabIndex.value = index;
    if (index == 1) _scrollToHighlightedDua();
  }

  void increment() {
    if (count.value >= maxCount) return;
    count.value++;
    _persist();
  }

  void decrement() {
    if (count.value <= 0) return;
    count.value--;
    _persist();
  }

  void reset() {
    count.value = 0;
    _persist();
  }

  Future<void> loadContent() async {
    isContentLoading.value = true;
    contentError.value = null;
    try {
      final azkarRaw = jsonDecode(
        await rootBundle.loadString(AppAssets.azkarJson),
      );
      final duasRaw = jsonDecode(
        await rootBundle.loadString(AppAssets.duasJson),
      );
      azkar.assignAll(
        (azkarRaw as List)
            .whereType<Map>()
            .map((item) => AzkarItem.fromJson(Map<String, dynamic>.from(item))),
      );
      duas.assignAll(
        (duasRaw as List)
            .whereType<Map>()
            .map((item) => DuaItem.fromJson(Map<String, dynamic>.from(item))),
      );
    } catch (_) {
      contentError.value = 'Unable to load Azkar and Duas.';
    } finally {
      isContentLoading.value = false;
    }
    _scrollToHighlightedDua();
  }

  bool isDuaBookmarked(String id) => _bookmarks.isDuaBookmarked(id);

  Future<void> toggleDuaBookmark(DuaItem dua, String languageCode) {
    return _bookmarks.toggle(
      AppBookmark.dua(
        duaId: dua.id,
        title: dua.titleFor(languageCode),
      ),
    );
  }

  void _scrollToHighlightedDua() {
    final id = highlightDuaId.value;
    if (id.isEmpty || duas.isEmpty) return;
    final index = duas.indexWhere((dua) => dua.id == id);
    if (index < 0) return;
    duaRevealIndex.value = index;
    WidgetsBinding.instance.addPostFrameCallback((_) {
      if (!duaScrollController.isAttached) return;
      duaScrollController.jumpTo(index: index, alignment: 0.08);
    });
  }

  void _persist() {
    _storage.saveTasbihCount(count.value);
  }
}
