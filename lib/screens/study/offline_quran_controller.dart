import 'package:flutter/foundation.dart';
import 'package:get/get.dart';
import 'package:sqflite/sqflite.dart';

import '../../core/controllers/settings_controller.dart';
import '../../core/data/json_utils.dart';
import '../../core/data/juz_ranges.dart';
import '../../core/data/models/juz.dart';
import '../../core/data/models/surah.dart';
import '../../core/data/quran_repository.dart';
import '../../core/services/storage_service.dart';
import '../../services/database_helper.dart';
import 'study_models.dart';

class OfflineQuranController extends GetxController {
  static const surahTabIndex = 0;
  static const juzTabIndex = 1;

  final isReading = false.obs;
  final isLoading = false.obs;
  final errorMessage = RxnString();
  final searchQuery = ''.obs;
  final primaryTab = 0.obs;
  final selectedSurah = 0.obs;
  final selectedJuz = RxnInt();
  final languageCode = 'en'.obs;
  final ayahs = <OfflineAyah>[].obs;
  final surahs = <Surah>[].obs;
  final allJuz = <Juz>[...Juz.all].obs;

  int _loadId = 0;
  Worker? _languageWorker;

  Surah? get currentSurah {
    for (final surah in surahs) {
      if (surah.number == selectedSurah.value) return surah;
    }
    return null;
  }

  bool get isJuzTab => primaryTab.value == juzTabIndex;

  bool get isJuzReading => selectedJuz.value != null;

  bool get isRtl => OfflineLanguage.isRtl(languageCode.value);

  String get wordColumn => OfflineLanguage.wordColumn(languageCode.value);

  String get fullColumn => OfflineLanguage.fullColumn(languageCode.value);

  String get title {
    if (!isReading.value) return 'Quran Study';
    final juz = selectedJuz.value;
    if (juz != null) return 'Juz $juz';
    final name = currentSurah?.englishName;
    if (name == null || name.isEmpty) return 'Quran Study';
    return name;
  }

  @override
  void onInit() {
    super.onInit();
    allJuz.assignAll(Juz.all);
    _syncLanguage();
    if (Get.isRegistered<StorageService>()) {
      _languageWorker = ever(
        Get.find<StorageService>().selectedTranslationId,
        (_) => _syncLanguage(),
      );
    }
    _loadSurahList();
    _openFromArgs();
  }

  @override
  void onClose() {
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
    final args = Get.arguments;
    if (args is Map && '${args['tab']}' == 'juz') {
      primaryTab.value = juzTabIndex;
    }

    final juz = _juzFromArgs();
    if (juz != null) {
      loadJuz(juz);
      return;
    }
    final surah = _surahFromArgs();
    if (surah != null) loadSurah(surah);
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

  List<Surah> get filteredSurahs {
    final query = _normalizeSearch(searchQuery.value);
    if (query.isEmpty) return surahs;
    return surahs.where((surah) {
      return _matchesSearch(surah.englishName, query) ||
          _matchesSearch(surah.arabicName, query) ||
          _matchesSearch(surah.meaning, query) ||
          surah.number.toString() == query;
    }).toList();
  }

  List<Juz> get filteredJuz {
    final source = allJuz.isEmpty ? Juz.all : allJuz.toList();
    final query = _normalizeSearch(searchQuery.value);
    if (query.isEmpty) return source;
    return source.where((juz) {
      return _matchesSearch('juz ${juz.number}', query) ||
          juz.number.toString() == query ||
          _matchesSearch(juz.englishName, query) ||
          _matchesSearch(juz.arabicName, query);
    }).toList();
  }

  String surahName(int number) {
    for (final surah in surahs) {
      if (surah.number == number) return surah.englishName;
    }
    return 'Surah $number';
  }

  String _normalizeSearch(String value) {
    return value
        .replaceAll('-', ' ')
        .replaceAll(RegExp(r'\s+'), ' ')
        .trim()
        .toLowerCase();
  }

  bool _matchesSearch(String target, String normalizedQuery) {
    if (normalizedQuery.isEmpty) return true;
    final normalizedTarget = _normalizeSearch(target);
    if (normalizedTarget.contains(normalizedQuery)) return true;
    final compactQuery = normalizedQuery.replaceAll(' ', '');
    final compactTarget = normalizedTarget.replaceAll(' ', '');
    return compactQuery.isNotEmpty && compactTarget.contains(compactQuery);
  }

  void onSearch(String value) => searchQuery.value = value;

  void onPrimaryTabChanged(int index) => primaryTab.value = index;

  void closeReader() {
    _loadId++;
    isReading.value = false;
    isLoading.value = false;
    errorMessage.value = null;
    ayahs.clear();
    selectedJuz.value = null;
    selectedSurah.value = 0;
  }

  Future<void> loadSurah(int surahNumber) async {
    selectedJuz.value = null;
    selectedSurah.value = surahNumber;
    await _loadAyahs(
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
  }

  Future<void> loadJuz(int juzNumber) async {
    final range = JuzRanges.of(juzNumber);
    if (range == null || range.length != 4) return;

    final startSurah = range[0];
    final startAyah = range[1];
    final endSurah = range[2];
    final endAyah = range[3];

    selectedJuz.value = juzNumber;
    selectedSurah.value = startSurah;
    await _loadAyahs(
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
  }

  Future<void> _loadAyahs(
    Future<List<Map<String, dynamic>>> Function() query, {
    required String emptyMessage,
  }) async {
    final loadId = ++_loadId;
    isReading.value = true;
    isLoading.value = true;
    errorMessage.value = null;
    ayahs.clear();

    try {
      final ayahRows = await query();
      if (loadId != _loadId) return;

      final parsed = [
        for (final row in ayahRows) OfflineAyah.fromMap(row),
      ];
      if (parsed.isEmpty) {
        errorMessage.value = emptyMessage;
        return;
      }

      final db = await DatabaseHelper.instance.database;
      final wordsByAyah = await _wordsForAyahs(
        db,
        parsed.map((ayah) => ayah.id),
      );
      if (loadId != _loadId) return;

      ayahs.assignAll([
        for (final ayah in parsed)
          ayah.copyWith(words: wordsByAyah[ayah.id] ?? const []),
      ]);
    } catch (error) {
      if (loadId != _loadId) return;
      errorMessage.value = emptyMessage;
      debugPrint('Offline Quran load failed: $error');
    } finally {
      if (loadId == _loadId) isLoading.value = false;
    }
  }

  Future<Map<int, List<OfflineWord>>> _wordsForAyahs(
    Database db,
    Iterable<int> ayahIds,
  ) async {
    final ids = ayahIds.where((id) => id > 0).toList();
    if (ids.isEmpty) return {};

    final minId = ids.reduce((a, b) => a < b ? a : b);
    final maxId = ids.reduce((a, b) => a > b ? a : b);
    final wanted = ids.toSet();
    final rows = await db.query(
      'ayah_words',
      where: 'ayah_id >= ? AND ayah_id <= ?',
      whereArgs: [minId, maxId],
      orderBy: 'ayah_id ASC, word_position ASC',
    );

    final grouped = <int, List<OfflineWord>>{};
    for (final row in rows) {
      final word = OfflineWord.fromMap(row);
      if (!wanted.contains(word.ayahId)) continue;
      grouped.putIfAbsent(word.ayahId, () => []).add(word);
    }
    return grouped;
  }
}
