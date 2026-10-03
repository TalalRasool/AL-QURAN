import 'dart:async';

import 'package:flutter/foundation.dart';
import 'package:get/get.dart';
import 'package:scrollable_positioned_list/scrollable_positioned_list.dart';

import '../../core/controllers/settings_controller.dart';
import '../../core/data/json_utils.dart';
import '../../core/data/juz_ranges.dart';
import '../../core/data/models/surah.dart';
import '../../core/data/quran_repository.dart';
import '../../core/services/storage_service.dart';
import '../../services/database_helper.dart';
import '../study/study_models.dart';
import 'reading_position.dart';

/// Reading Mode: Arabic ayah + full translation from `ayahs` only.
/// Does not load `ayah_words` (no word-by-word).
class QuranReadingController extends GetxController {
  final isLoading = false.obs;
  final errorMessage = RxnString();
  final selectedSurah = 0.obs;
  final selectedJuz = RxnInt();
  final languageCode = 'en'.obs;
  final ayahs = <OfflineAyah>[].obs;
  final surahs = <Surah>[].obs;
  final revealIndexValue = 0.obs;
  final highlightedIndex = 0.obs;

  final itemScrollController = ItemScrollController();
  final itemPositionsListener = ItemPositionsListener.create();

  int _loadId = 0;
  int _armedIndex = -1;
  Worker? _languageWorker;
  Timer? _saveTimer;

  Surah? get currentSurah {
    for (final surah in surahs) {
      if (surah.number == selectedSurah.value) return surah;
    }
    return null;
  }

  bool get isJuzReading => selectedJuz.value != null;

  bool get isRtl => OfflineLanguage.isRtl(languageCode.value);

  String get title {
    final juz = selectedJuz.value;
    if (juz != null) return 'Juz $juz';
    final name = currentSurah?.englishName;
    if (name == null || name.isEmpty) return 'Reading';
    return name;
  }

  @override
  void onInit() {
    super.onInit();
    _syncLanguage();
    if (Get.isRegistered<StorageService>()) {
      _languageWorker = ever(
        Get.find<StorageService>().selectedTranslationId,
        (_) => _syncLanguage(),
      );
    }
    itemPositionsListener.itemPositions.addListener(_onItemPositions);
    _loadSurahList();
    _openFromArgs();
  }

  @override
  void onClose() {
    itemPositionsListener.itemPositions.removeListener(_onItemPositions);
    _saveTimer?.cancel();
    _languageWorker?.dispose();
    super.onClose();
  }

  void _syncLanguage() {
    final code = Get.isRegistered<SettingsController>()
        ? Get.find<SettingsController>().translationLanguageCode
        : 'en';
    languageCode.value = OfflineLanguage.normalize(code);
  }

  void _openFromArgs() {
    final juz = _juzFromArgs();
    if (juz != null) {
      loadJuz(juz, useRouteAyah: true);
      return;
    }
    final surah = _surahFromArgs() ?? 1;
    loadSurah(surah, useRouteAyah: true);
  }

  int? _ayahFromArgs() {
    final args = Get.arguments;
    if (args is! Map || !args.containsKey('ayah')) return null;
    final ayah = asInt(args['ayah']);
    if (ayah < 1) return null;
    return ayah;
  }

  int? _surahFromArgs() {
    final args = Get.arguments;
    if (args is int && args >= 1 && args <= 114) return args;
    if (args is Map) {
      final number = asInt(args['surah']);
      if (number >= 1 && number <= 114) return number;
    }
    return null;
  }

  int? _juzFromArgs() {
    final args = Get.arguments;
    if (args is Map) {
      final number = asInt(args['juz']);
      if (number >= 1 && number <= 30) return number;
    }
    return null;
  }

  Future<void> _loadSurahList() async {
    if (!Get.isRegistered<QuranRepository>()) return;
    try {
      surahs.assignAll(await Get.find<QuranRepository>().getAllSurahs());
    } catch (error) {
      debugPrint('Failed to load surah list: $error');
    }
  }

  String surahName(int number) {
    for (final surah in surahs) {
      if (surah.number == number) return surah.englishName;
    }
    return 'Surah $number';
  }

  Future<void> loadSurah(
    int surahNumber, {
    bool useRouteAyah = false,
  }) async {
    selectedJuz.value = null;
    selectedSurah.value = surahNumber;
    final parsed = await _loadAyahs(
      () async {
        final db = await DatabaseHelper.instance.database;
        return db.query(
          'ayahs',
          where: 'surah_number = ?',
          whereArgs: [surahNumber],
          orderBy: 'ayah_number ASC',
        );
      },
      emptyMessage: 'Could not load this surah from the offline database.',
    );
    if (parsed == null || parsed.isEmpty || isClosed) return;
    await _revealParsed(
      parsed,
      preferredSurah: surahNumber,
      preferredAyah: useRouteAyah ? _ayahFromArgs() : null,
    );
  }

  Future<void> loadJuz(
    int juzNumber, {
    bool useRouteAyah = false,
  }) async {
    final range = JuzRanges.of(juzNumber);
    if (range == null || range.length != 4) return;

    final startSurah = range[0];
    final startAyah = range[1];
    final endSurah = range[2];
    final endAyah = range[3];

    selectedJuz.value = juzNumber;
    selectedSurah.value = startSurah;
    final parsed = await _loadAyahs(
      () async {
        final db = await DatabaseHelper.instance.database;
        return db.rawQuery(
          '''
          SELECT * FROM ayahs
          WHERE (surah_number * 1000 + ayah_number)
            BETWEEN ? AND ?
          ORDER BY surah_number ASC, ayah_number ASC
          ''',
          [
            startSurah * 1000 + startAyah,
            endSurah * 1000 + endAyah,
          ],
        );
      },
      emptyMessage: 'Could not load this juz from the offline database.',
    );
    if (parsed == null || parsed.isEmpty || isClosed) return;
    await _revealParsed(
      parsed,
      preferredSurah: useRouteAyah ? _surahFromArgs() : null,
      preferredAyah: useRouteAyah ? _ayahFromArgs() : null,
    );
  }

  Future<void> _revealParsed(
    List<OfflineAyah> parsed, {
    int? preferredSurah,
    int? preferredAyah,
  }) async {
    final saved = Get.isRegistered<StorageService>()
        ? Get.find<StorageService>().lastRead.value
        : null;
    final index = revealIndex(
      [
        for (final ayah in parsed)
          (surahNumber: ayah.surahNumber, ayahNumber: ayah.ayahNumber),
      ],
      preferredSurah: preferredSurah,
      preferredAyah: preferredAyah,
      saved: saved,
    );
    final ayah = parsed[index];
    _armedIndex = index;
    revealIndexValue.value = index;
    highlightedIndex.value = index;
    await _saveLastRead(
      surahNumber: ayah.surahNumber,
      ayahNumber: ayah.ayahNumber,
    );
    if (!isClosed) isLoading.value = false;
  }

  void _onItemPositions() {
    if (isClosed || ayahs.isEmpty) return;
    final positions = itemPositionsListener.itemPositions.value;
    ItemPosition? top;
    for (final position in positions) {
      if (position.itemTrailingEdge <= 0.02) continue;
      if (top == null || position.itemLeadingEdge < top.itemLeadingEdge) {
        top = position;
      }
    }
    if (top == null || top.index < 0 || top.index >= ayahs.length) return;
    if (_armedIndex >= 0 && top.index != _armedIndex) return;
    _armedIndex = -1;
    if (highlightedIndex.value == top.index) return;
    highlightedIndex.value = top.index;
    final ayah = ayahs[top.index];
    _saveTimer?.cancel();
    _saveTimer = Timer(const Duration(milliseconds: 400), () {
      if (isClosed) return;
      _saveLastRead(
        surahNumber: ayah.surahNumber,
        ayahNumber: ayah.ayahNumber,
      );
    });
  }

  Future<void> _saveLastRead({
    required int surahNumber,
    required int ayahNumber,
  }) async {
    if (!Get.isRegistered<StorageService>()) return;
    try {
      await Get.find<StorageService>().saveLastRead(
        surahNumber: surahNumber,
        ayahNumber: ayahNumber,
      );
    } catch (_) {}
  }

  Future<List<OfflineAyah>?> _loadAyahs(
    Future<List<Map<String, dynamic>>> Function() query, {
    required String emptyMessage,
  }) async {
    final loadId = ++_loadId;
    isLoading.value = true;
    errorMessage.value = null;
    ayahs.clear();

    try {
      final ayahRows = await query();
      if (loadId != _loadId || isClosed) return null;

      final parsed = [
        for (final row in ayahRows) OfflineAyah.fromMap(row),
      ];
      if (parsed.isEmpty) {
        errorMessage.value = emptyMessage;
        isLoading.value = false;
        return [];
      }
      ayahs.assignAll(parsed);
      return parsed;
    } catch (error) {
      if (loadId != _loadId || isClosed) return null;
      errorMessage.value = emptyMessage;
      isLoading.value = false;
      debugPrint('Quran reading load failed: $error');
      return [];
    }
  }
}
