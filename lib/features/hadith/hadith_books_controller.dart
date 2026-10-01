import 'package:get/get.dart';

import '../../core/routes/app_routes.dart';
import '../../core/services/storage_service.dart';
import 'data/hadith_db_helper.dart';
import 'data/hadith_models.dart';

class HadithBooksController extends GetxController {
  final books = <HadithBook>[].obs;
  final isLoading = false.obs;
  final errorMessage = RxnString();

  final HadithDbHelper _db = Get.find<HadithDbHelper>();
  Worker? _languageWorker;

  @override
  void onInit() {
    super.onInit();
    if (Get.isRegistered<StorageService>()) {
      _languageWorker = ever(
        Get.find<StorageService>().selectedTranslationId,
        (_) {
          books.refresh();
          errorMessage.refresh();
        },
      );
    }
    load();
  }

  @override
  void onClose() {
    _languageWorker?.dispose();
    super.onClose();
  }

  Future<void> load() async {
    isLoading.value = true;
    errorMessage.value = null;
    try {
      books.assignAll(await _db.getBooks());
      if (books.isEmpty && _db.initError != null) {
        errorMessage.value = _db.initError;
      }
    } catch (_) {
      errorMessage.value = _db.initError ?? 'Unable to load Hadith books.';
    } finally {
      isLoading.value = false;
    }
  }

  void openBook(HadithBook book) {
    Get.toNamed(
      AppRoutes.hadithChapters,
      arguments: {'bookId': book.id, 'bookName': book.name},
    );
  }
}
