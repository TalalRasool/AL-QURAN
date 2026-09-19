import 'dart:convert';

import 'package:flutter/services.dart';
import 'package:get/get.dart';

import '../../core/constants/app_assets.dart';
import '../../core/controllers/settings_controller.dart';
import '../../core/data/models/seerah.dart';
import '../../core/services/storage_service.dart';

class IslamicHistoryController extends GetxController {
  static const screenTitles = {
    'en': 'Islamic History',
    'ur': 'اسلامی تاریخ',
    'hi': 'इस्लामी इतिहास',
    'bn': 'ইসলামি ইতিহাস',
    'id': 'Sejarah Islam',
  };

  static const tabLabelsByLang = {
    'en': ['Seerah', 'Sahaba', 'Ghazawat'],
    'ur': ['سیرت', 'صحابہ', 'غزوات'],
    'hi': ['सीरत', 'सहाबा', 'ग़ज़वात'],
    'bn': ['সিরাত', 'সাহাবা', 'গাজওয়া'],
    'id': ['Sirah', 'Sahabat', 'Ghazwah'],
  };

  static const _emptyByTab = {
    0: {
      'en': 'No Seerah chapters were found.',
      'ur': 'سیرت کے ابواب نہیں ملے۔',
      'hi': 'सीरत के अध्याय नहीं मिले।',
      'bn': 'সিরাত অধ্যায় পাওয়া যায়নি।',
      'id': 'Bab sirah tidak ditemukan.',
    },
    1: {
      'en': 'No Sahaba entries were found.',
      'ur': 'صحابہ کی معلومات نہیں ملیں۔',
      'hi': 'सहाबा की जानकारी नहीं मिली।',
      'bn': 'সাহাবা তথ্য পাওয়া যায়নি।',
      'id': 'Data sahabat tidak ditemukan.',
    },
    2: {
      'en': 'No Ghazawat entries were found.',
      'ur': 'غزوات کی معلومات نہیں ملیں۔',
      'hi': 'ग़ज़वात की जानकारी नहीं मिली।',
      'bn': 'গাজওয়া তথ্য পাওয়া যায়নি।',
      'id': 'Data ghazwah tidak ditemukan.',
    },
  };

  final seerahChapters = <SeerahChapter>[].obs;
  final sahabaChapters = <SeerahChapter>[].obs;
  final ghazawatChapters = <SeerahChapter>[].obs;
  final expandedIds = <String>{}.obs;
  final isLoading = false.obs;
  final errorMessage = RxnString();

  bool get hasAnyChapters =>
      seerahChapters.isNotEmpty ||
      sahabaChapters.isNotEmpty ||
      ghazawatChapters.isNotEmpty;

  String get languageCode {
    if (!Get.isRegistered<SettingsController>()) return 'en';
    return Get.find<SettingsController>().translationLanguageCode;
  }

  bool get isRtl => languageCode == 'ur';

  String get screenTitle {
    final title = screenTitles[languageCode];
    if (title != null && title.isNotEmpty) return title;
    return screenTitles['en']!;
  }

  List<String> get tabLabels {
    final labels = tabLabelsByLang[languageCode] ?? tabLabelsByLang['en']!;
    if (labels.length >= 3) return labels.sublist(0, 3);
    return [
      ...labels,
      ...tabLabelsByLang['en']!.skip(labels.length),
    ].take(3).toList(growable: false);
  }

  List<SeerahChapter> chaptersForTab(int tab) {
    return switch (tab) {
      1 => sahabaChapters,
      2 => ghazawatChapters,
      _ => seerahChapters,
    };
  }

  String emptyMessageForTab(int tab) {
    final map = _emptyByTab[tab] ?? _emptyByTab[0]!;
    return map[languageCode] ?? map['en']!;
  }

  @override
  void onInit() {
    super.onInit();
    load();
  }

  Future<void> load() async {
    isLoading.value = true;
    errorMessage.value = null;
    try {
      final results = await Future.wait([
        _loadChapters(AppAssets.seerahJson, 'seerah'),
        _loadChapters(AppAssets.sahabaJson, 'sahaba'),
        _loadChapters(AppAssets.ghazawatJson, 'ghazawat'),
      ]);
      seerahChapters.assignAll(results[0]);
      sahabaChapters.assignAll(results[1]);
      ghazawatChapters.assignAll(results[2]);
      if (!hasAnyChapters) {
        errorMessage.value = 'Unable to load Islamic History.';
      }
    } catch (_) {
      errorMessage.value = 'Unable to load Islamic History.';
    } finally {
      isLoading.value = false;
    }
  }

  Future<List<SeerahChapter>> _loadChapters(
    String asset,
    String keyPrefix,
  ) async {
    try {
      final raw = jsonDecode(await rootBundle.loadString(asset));
      return SeerahChapter.listFrom(raw, keyPrefix: keyPrefix);
    } catch (_) {
      return const [];
    }
  }

  bool isExpanded(String id) => expandedIds.contains(id);

  void toggle(String id) {
    if (expandedIds.contains(id)) {
      expandedIds.remove(id);
    } else {
      expandedIds.add(id);
    }
    expandedIds.refresh();
  }

  /// Touch reactive language so Obx rebuilds when translation changes.
  void watchLanguage() {
    if (Get.isRegistered<StorageService>()) {
      Get.find<StorageService>().selectedTranslationId.value;
    }
  }
}
