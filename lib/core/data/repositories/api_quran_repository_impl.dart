import 'dart:convert';
import 'dart:math';

import 'package:flutter/services.dart';
import 'package:get/get.dart';
import 'package:get_storage/get_storage.dart';
import 'package:http/http.dart' as http;

import '../../constants/app_assets.dart';
import '../../services/storage_service.dart';
import '../json_utils.dart';
import '../models/ayah.dart';
import '../models/daily_verse.dart';
import '../models/reciter.dart';
import '../models/surah.dart';
import '../models/translation_edition.dart';
import '../offline_translations.dart';
import '../quran_repository.dart';

class ApiQuranRepositoryImpl implements QuranRepository {
  ApiQuranRepositoryImpl({
    http.Client? client,
    GetStorage? box,
    AssetBundle? bundle,
  })  : _client = client ?? http.Client(),
        _box = box ?? GetStorage(),
        _bundle = bundle ?? rootBundle;

  static const _baseUrl = 'https://api.alquran.cloud/v1';
  static const _recitersCacheKey = 'cached_reciters';
  static const _dailyVerseCacheKey = 'cached_daily_verse';
  static const _timeout = Duration(seconds: 15);

  final http.Client _client;
  final GetStorage _box;
  final AssetBundle _bundle;

  List<Map<String, dynamic>>? _arabicSurahs;
  final _translationSurahs = <String, List<Map<String, dynamic>>>{};

  String get _selectedTranslationId {
    if (Get.isRegistered<StorageService>()) {
      return OfflineTranslations.canonicalId(
        Get.find<StorageService>().selectedTranslationId.value,
      );
    }
    return OfflineTranslations.english.identifier;
  }

  @override
  Future<List<Surah>> getAllSurahs() async {
    final surahs = await _loadArabicSurahs();
    return surahs.map(Surah.fromJson).toList();
  }

  @override
  Future<Surah> getSurahByNumber(int number) async {
    final surahs = await getAllSurahs();
    if (surahs.isEmpty) {
      throw StateError('No surahs available');
    }
    return surahs.firstWhere(
      (surah) => surah.number == number,
      orElse: () => surahs.first,
    );
  }

  @override
  Future<List<Ayah>> getAyahs(int surahNumber) async {
    final arabicSurahs = await _loadArabicSurahs();
    final translationSurahs = await _loadTranslationSurahs();
    final arabic = _surahByNumber(arabicSurahs, surahNumber);
    final translated = _surahByNumber(translationSurahs, surahNumber);
    if (arabic == null) return [];

    final englishName = arabic['englishName'] as String? ?? '';
    final translationAyahs = _ayahMaps(translated);
    final byNumberInSurah = <int, Map<String, dynamic>>{
      for (final ayah in translationAyahs)
        asInt(ayah['numberInSurah']): ayah,
    };

    return _ayahMaps(arabic).map((ayah) {
      final numberInSurah = asInt(ayah['numberInSurah']);
      return Ayah(
        number: numberInSurah,
        arabic: ayah['text'] as String? ?? '',
        translation: _translationText(byNumberInSurah[numberInSurah]),
        surahNumber: surahNumber,
        surahEnglishName: englishName,
      );
    }).toList();
  }

  @override
  Future<List<Ayah>> getJuzAyahs(int juzNumber) async {
    final arabicSurahs = await _loadArabicSurahs();
    final translationSurahs = await _loadTranslationSurahs();
    final translationByGlobal = <int, String>{};
    for (final surah in translationSurahs) {
      for (final ayah in _ayahMaps(surah)) {
        translationByGlobal[asInt(ayah['number'])] = _translationText(ayah);
      }
    }

    final ayahs = <Ayah>[];
    for (final surah in arabicSurahs) {
      final surahNumber = asInt(surah['number']);
      final englishName = surah['englishName'] as String? ?? '';
      for (final ayah in _ayahMaps(surah)) {
        if (asInt(ayah['juz']) != juzNumber) continue;
        final globalNumber = asInt(ayah['number']);
        ayahs.add(
          Ayah(
            number: asInt(ayah['numberInSurah']),
            arabic: ayah['text'] as String? ?? '',
            translation: translationByGlobal[globalNumber] ?? '',
            surahNumber: surahNumber,
            surahEnglishName: englishName,
          ),
        );
      }
    }
    return ayahs;
  }

  @override
  Future<List<List<Ayah>>> getMushafPages() async {
    final arabicSurahs = await _loadArabicSurahs();
    final pages = List<List<Ayah>>.generate(604, (_) => <Ayah>[]);
    for (final surah in arabicSurahs) {
      final surahNumber = asInt(surah['number']);
      final englishName = surah['englishName'] as String? ?? '';
      for (final ayah in _ayahMaps(surah)) {
        final page = asInt(ayah['page']);
        if (page < 1 || page > 604) continue;
        pages[page - 1].add(
          Ayah(
            number: asInt(ayah['numberInSurah']),
            arabic: ayah['text'] as String? ?? '',
            translation: '',
            surahNumber: surahNumber,
            surahEnglishName: englishName,
          ),
        );
      }
    }
    return pages;
  }

  @override
  Future<DailyVerse> getDailyVerse() async {
    final translationId = _selectedTranslationId;
    final today = _todayKey();
    final cached = _readDailyVerseCache();
    if (cached != null &&
        cached.date == today &&
        cached.translationId == translationId &&
        cached.verse.arabic.isNotEmpty) {
      return cached.verse;
    }

    final arabicSurahs = await _loadArabicSurahs();
    final totalAyahs = _countAyahs(arabicSurahs);
    if (totalAyahs <= 0) {
      throw StateError('Bundled Quran data is missing');
    }

    final cachedNumber = cached?.verse.globalNumber ?? 0;
    final globalNumber = (cached != null &&
            cached.date == today &&
            cachedNumber >= 1 &&
            cachedNumber <= totalAyahs)
        ? cachedNumber
        : Random().nextInt(totalAyahs) + 1;

    final verse = await _verseAtGlobalNumber(globalNumber);
    await _writeDailyVerseCache(
      date: today,
      translationId: translationId,
      verse: verse,
    );
    return verse;
  }

  @override
  Future<List<Reciter>> getReciters() async {
    final cached = _readJsonCache(_recitersCacheKey);
    if (cached != null) {
      final parsed = _parseReciters(cached);
      if (parsed.isNotEmpty) return parsed;
    }

    try {
      final data = await _getApiData(
        '$_baseUrl/edition?format=audio&language=ar',
      );
      await _writeJsonCache(_recitersCacheKey, data);
      return _parseReciters(data);
    } catch (_) {
      final fallback = _parseReciters(_readJsonCache(_recitersCacheKey));
      if (fallback.isNotEmpty) return fallback;
      rethrow;
    }
  }

  @override
  Future<List<TranslationEdition>> getTranslationEditions() async {
    return List<TranslationEdition>.from(OfflineTranslations.editions);
  }

  @override
  Future<void> clearAyahCaches() async {
    _translationSurahs.clear();
    await _box.remove(_dailyVerseCacheKey);
  }

  Future<DailyVerse> _verseAtGlobalNumber(int globalNumber) async {
    final arabicSurahs = await _loadArabicSurahs();
    final translationSurahs = await _loadTranslationSurahs();
    final translationByGlobal = <int, String>{};
    for (final surah in translationSurahs) {
      for (final ayah in _ayahMaps(surah)) {
        translationByGlobal[asInt(ayah['number'])] = _translationText(ayah);
      }
    }

    for (final surah in arabicSurahs) {
      final surahNumber = asInt(surah['number']);
      final englishName = surah['englishName'] as String? ?? 'Surah';
      for (final ayah in _ayahMaps(surah)) {
        if (asInt(ayah['number']) != globalNumber) continue;
        final ayahNumber = asInt(ayah['numberInSurah']);
        return DailyVerse(
          arabic: ayah['text'] as String? ?? '',
          translation: translationByGlobal[globalNumber] ?? '',
          reference: '$englishName $surahNumber:$ayahNumber',
          surahNumber: surahNumber,
          ayahNumber: ayahNumber,
          globalNumber: globalNumber,
        );
      }
    }

    throw StateError('Ayah $globalNumber was not found in bundled data');
  }

  Future<List<Map<String, dynamic>>> _loadTranslationSurahs() async {
    final translationId = _selectedTranslationId;
    final cached = _translationSurahs[translationId];
    if (cached != null) return cached;

    final asset = OfflineTranslations.assetFor(translationId);
    if (asset == AppAssets.quranArabicJson) {
      throw StateError('Translation mapping resolved to Arabic text');
    }

    final surahs = await _loadSurahsFromAsset(
      asset,
      expectTranslation: true,
      expectedLanguage: OfflineTranslations.editionFor(translationId).language,
    );
    _translationSurahs[translationId] = surahs;
    return surahs;
  }

  Future<List<Map<String, dynamic>>> _loadArabicSurahs() async {
    return _arabicSurahs ??= await _loadSurahsFromAsset(
      AppAssets.quranArabicJson,
      expectTranslation: false,
      expectedLanguage: 'ar',
    );
  }

  Future<List<Map<String, dynamic>>> _loadSurahsFromAsset(
    String asset, {
    required bool expectTranslation,
    required String expectedLanguage,
  }) async {
    final raw = await _bundle.loadString(asset);
    final decoded = jsonDecode(raw);
    final root = asStringKeyMap(decoded);
    final data = asStringKeyMap(root['data']);
    _assertEdition(
      data,
      asset: asset,
      expectTranslation: expectTranslation,
      expectedLanguage: expectedLanguage,
    );
    final surahs = data['surahs'];
    if (surahs is! List) return [];
    return surahs.map(asStringKeyMap).toList();
  }

  void _assertEdition(
    Map<String, dynamic> data, {
    required String asset,
    required bool expectTranslation,
    required String expectedLanguage,
  }) {
    final edition = asStringKeyMap(data['edition']);
    if (edition.isEmpty) return;

    final language = '${edition['language'] ?? ''}'.toLowerCase();
    final type = '${edition['type'] ?? ''}'.toLowerCase();
    final identifier = '${edition['identifier'] ?? ''}';

    if (expectTranslation && (type == 'quran' || language == 'ar')) {
      throw StateError(
        'Asset $asset is Arabic Quran text ($identifier), not a translation. '
        'Run: dart run scripts/download_quran.dart',
      );
    }
    if (language.isNotEmpty && language != expectedLanguage) {
      throw StateError(
        'Asset $asset language is $language, expected $expectedLanguage.',
      );
    }
  }

  String _translationText(Map<String, dynamic>? ayah) {
    final text = (ayah?['text'] as String? ?? '').trim();
    return text;
  }

  Map<String, dynamic>? _surahByNumber(
    List<Map<String, dynamic>> surahs,
    int number,
  ) {
    for (final surah in surahs) {
      if (asInt(surah['number']) == number) return surah;
    }
    return null;
  }

  List<Map<String, dynamic>> _ayahMaps(Map<String, dynamic>? surah) {
    final ayahs = surah?['ayahs'];
    if (ayahs is! List) return [];
    return ayahs.map(asStringKeyMap).toList();
  }

  int _countAyahs(List<Map<String, dynamic>> surahs) {
    var count = 0;
    for (final surah in surahs) {
      count += _ayahMaps(surah).length;
    }
    return count;
  }

  Future<dynamic> _getApiData(String url) async {
    final response = await _client.get(Uri.parse(url)).timeout(_timeout);
    if (response.statusCode != 200) {
      throw Exception('AlQuran.cloud returned ${response.statusCode}');
    }

    final body = jsonDecode(response.body);
    final map = asStringKeyMap(body);
    if (asInt(map['code']) != 200) {
      throw Exception(map['status']?.toString() ?? 'AlQuran.cloud error');
    }
    return map['data'];
  }

  Future<void> _writeJsonCache(String key, dynamic data) {
    return _box.write(key, jsonEncode(data));
  }

  dynamic _readJsonCache(String key) {
    final raw = _box.read(key);
    if (raw is! String || raw.isEmpty) return null;
    try {
      return jsonDecode(raw);
    } catch (_) {
      return null;
    }
  }

  List<Reciter> _parseReciters(dynamic data) {
    if (data is! List) return [];
    return data
        .map(Reciter.fromDynamic)
        .where((reciter) => reciter.identifier.isNotEmpty)
        .toList();
  }

  String _todayKey() {
    final now = DateTime.now();
    final month = now.month.toString().padLeft(2, '0');
    final day = now.day.toString().padLeft(2, '0');
    return '${now.year}-$month-$day';
  }

  _DailyVerseCache? _readDailyVerseCache() {
    final raw = _readJsonCache(_dailyVerseCacheKey);
    if (raw is! Map) return null;
    final map = asStringKeyMap(raw);
    final verseRaw = map['verse'];
    if (verseRaw is! Map) return null;
    return _DailyVerseCache(
      date: map['date'] as String? ?? '',
      translationId: map['translationId'] as String? ?? '',
      verse: DailyVerse.fromJson(asStringKeyMap(verseRaw)),
    );
  }

  Future<void> _writeDailyVerseCache({
    required String date,
    required String translationId,
    required DailyVerse verse,
  }) {
    return _writeJsonCache(_dailyVerseCacheKey, {
      'date': date,
      'translationId': translationId,
      'verse': verse.toJson(),
    });
  }
}

class _DailyVerseCache {
  const _DailyVerseCache({
    required this.date,
    required this.translationId,
    required this.verse,
  });

  final String date;
  final String translationId;
  final DailyVerse verse;
}
