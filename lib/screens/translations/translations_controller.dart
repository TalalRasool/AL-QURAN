import 'package:get/get.dart';

import '../../core/controllers/settings_controller.dart';
import '../../core/data/models/translation_edition.dart';
import '../../core/data/offline_translations.dart';
import '../../core/data/quran_repository.dart';
import '../../core/services/storage_service.dart';
import '../quran/surah_detail_controller.dart';

class TranslationsController extends GetxController {
  final searchQuery = ''.obs;
  final editions = <TranslationEdition>[].obs;
  final isLoading = false.obs;
  final errorMessage = RxnString();

  final QuranRepository _quran = Get.find<QuranRepository>();
  final StorageService _storage = Get.find<StorageService>();

  @override
  void onInit() {
    super.onInit();
    loadEditions();
  }

  Future<void> loadEditions() async {
    isLoading.value = true;
    errorMessage.value = null;
    try {
      final loaded = await _quran.getTranslationEditions();
      loaded.sort((a, b) {
        final language = a.languageLabel.compareTo(b.languageLabel);
        if (language != 0) return language;
        return a.authorName.compareTo(b.authorName);
      });
      editions.assignAll(loaded);
    } catch (_) {
      editions.assignAll(List.of(OfflineTranslations.editions));
    } finally {
      isLoading.value = false;
    }
  }

  List<TranslationEdition> get filteredEditions {
    final query = searchQuery.value.trim().toLowerCase();
    if (query.isEmpty) return editions;
    return editions
        .where(
          (edition) =>
              edition.authorName.toLowerCase().contains(query) ||
              edition.languageLabel.toLowerCase().contains(query) ||
              edition.identifier.toLowerCase().contains(query) ||
              edition.name.toLowerCase().contains(query),
        )
        .toList();
  }

  void onSearch(String value) => searchQuery.value = value;

  String get selectedId => OfflineTranslations.canonicalId(
        _storage.selectedTranslationId.value,
      );

  Future<void> selectTranslation(TranslationEdition edition) async {
    final canonical = OfflineTranslations.editionFor(edition.identifier);
    final changed = selectedId != canonical.identifier;
    await Get.find<SettingsController>().applyTranslation(canonical);

    if (changed) {
      await _quran.clearAyahCaches();
      if (Get.isRegistered<SurahDetailController>()) {
        await Get.find<SurahDetailController>().load();
      }
    }

    Get.back();
  }
}
