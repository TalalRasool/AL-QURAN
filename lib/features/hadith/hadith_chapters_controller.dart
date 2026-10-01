import 'dart:async';

import 'package:get/get.dart';

import '../../core/data/json_utils.dart';
import '../../core/routes/app_routes.dart';
import '../../core/services/storage_service.dart';
import 'data/hadith_db_helper.dart';
import 'data/hadith_l10n.dart';
import 'data/hadith_models.dart';

class HadithChaptersController extends GetxController {
  final chapters = <HadithChapter>[].obs;
  final searchQuery = ''.obs;
  final isLoading = false.obs;
  final errorMessage = RxnString();
  final englishBookName = ''.obs;

  final HadithDbHelper _db = Get.find<HadithDbHelper>();
  final _allChapters = <HadithChapter>[];
  Timer? _searchDebounce;
  Worker? _languageWorker;
  int _requestId = 0;

  int get bookId {
    final args = Get.arguments;
    if (args is Map) return asInt(args['bookId'], fallback: 1);
    if (args is int) return args;
    return 1;
  }

  String get bookName =>
      HadithL10n.bookName(bookId, fallback: englishBookName.value);

  @override
  void onInit() {
    super.onInit();
    final args = Get.arguments;
    if (args is Map) {
      final name = '${args['bookName'] ?? ''}'.trim();
      if (name.isNotEmpty) englishBookName.value = name;
    }
    if (Get.isRegistered<StorageService>()) {
      _languageWorker = ever(
        Get.find<StorageService>().selectedTranslationId,
        (_) => _applyFilter(),
      );
    }
    load();
  }

  @override
  void onClose() {
    _searchDebounce?.cancel();
    _languageWorker?.dispose();
    super.onClose();
  }

  Future<void> load({bool showSpinner = true}) async {
    if (showSpinner && chapters.isEmpty) isLoading.value = true;
    errorMessage.value = null;
    final requestId = ++_requestId;
    try {
      final rows = await _db.getChapters(bookId);
      if (requestId != _requestId) return;
      _allChapters
        ..clear()
        ..addAll(rows);
      _applyFilter();
    } catch (_) {
      if (requestId != _requestId) return;
      errorMessage.value = _db.initError ?? 'Unable to load chapters.';
    } finally {
      if (requestId == _requestId) isLoading.value = false;
    }
  }

  void onSearch(String value) {
    searchQuery.value = value;
    _searchDebounce?.cancel();
    _searchDebounce = Timer(const Duration(milliseconds: 220), _applyFilter);
  }

  void _applyFilter() {
    final query = searchQuery.value;
    chapters.assignAll(
      _allChapters.where(
        (chapter) => HadithL10n.matchesQuery(
          query: query,
          englishName: chapter.name,
          number: chapter.number,
        ),
      ),
    );
  }

  void openChapter(HadithChapter chapter) {
    Get.toNamed(
      AppRoutes.hadithRead,
      arguments: {
        'bookId': chapter.bookId,
        'bookName': englishBookName.value,
        'chapterId': chapter.id,
        'chapterName': chapter.name,
      },
    );
  }
}
