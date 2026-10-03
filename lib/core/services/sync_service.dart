import 'dart:async';

import 'package:flutter/foundation.dart';
import 'package:get/get.dart';
import 'package:supabase_flutter/supabase_flutter.dart';

import '../controllers/bookmark_controller.dart';
import '../data/json_utils.dart';
import '../data/models/app_bookmark.dart';
import '../data/models/last_read.dart';
import 'auth_service.dart';
import 'storage_service.dart';
import 'sync_merge.dart';

class SyncService extends GetxService {
  final AuthService _auth = Get.find<AuthService>();
  final StorageService _storage = Get.find<StorageService>();

  final _workers = <Worker>[];
  var _applyingRemote = false;
  var _merging = false;
  Future<void> _libraryWrite = Future<void>.value();

  Future<SyncService> init() async {
    _listenForAuthChanges();
    _listenForLocalChanges();
    if (_auth.isLoggedIn) {
      unawaited(mergeOnLogin());
    }
    return this;
  }

  bool get _canSync => _auth.isLoggedIn && _client != null;

  void _listenForAuthChanges() {
    _workers.add(
      ever(_auth.currentUser, (user) {
        if (user == null) return;
        unawaited(mergeOnLogin());
      }),
    );
  }

  void _listenForLocalChanges() {
    _workers.add(
      ever(_storage.lastRead, (_) {
        if (_applyingRemote) return;
        unawaited(pushProgressToCloud());
      }),
    );
    _workers.add(
      ever(_storage.bookmarkRevision, (_) {
        if (_applyingRemote) return;
        unawaited(pushBookmarksToCloud());
      }),
    );
    _workers.add(
      debounce(
        _storage.tasbihCount,
        (_) {
          if (_applyingRemote) return;
          unawaited(pushTasbihToCloud());
        },
        time: const Duration(milliseconds: 400),
      ),
    );
    _workers.add(
      ever(_storage.userName, (_) {
        if (_applyingRemote) return;
        unawaited(pushProfileToCloud());
      }),
    );
    _workers.add(
      ever(_storage.userCountry, (_) {
        if (_applyingRemote) return;
        unawaited(pushProfileToCloud());
      }),
    );
    _workers.add(
      ever(_storage.selectedTranslationId, (_) {
        if (_applyingRemote) return;
        unawaited(pushProfileToCloud());
      }),
    );
  }

  Future<void> mergeOnLogin() async {
    if (!_canSync || _merging) return;
    _merging = true;
    try {
      await pullCloudToLocal();
      await syncLocalToCloud();
    } catch (error) {
      debugPrint('Sync merge failed: $error');
    } finally {
      _merging = false;
    }
  }

  Future<void> syncLocalToCloud() async {
    if (!_canSync) return;
    try {
      await pushProfileToCloud();
      await pushTasbihToCloud();
      await pushProgressToCloud();
      await pushBookmarksToCloud();
    } catch (error) {
      debugPrint('Sync push failed: $error');
    }
  }

  Future<void> pushProfileToCloud() async {
    final uid = _uid;
    final client = _client;
    if (uid == null || client == null) return;

    await _guarded(
      () => client.from('profiles').upsert({
        'id': uid,
        'name': _storage.userName.value,
        'country': _storage.userCountry.value,
        'language': _storage.selectedTranslationLanguage.value,
        'translation_id': _storage.selectedTranslationId.value,
        'translation_name': _storage.selectedTranslationName.value,
        'translation_direction': _storage.selectedTranslationDirection.value,
      }, onConflict: 'id'),
    );
  }

  Future<void> pushProgressToCloud() async {
    final uid = _uid;
    final client = _client;
    if (uid == null || client == null) return;
    final lastRead = await _stampedLastRead();
    if (lastRead == null) return;

    await _writeLibrary(() => _guarded(() async {
      final updatedAt = DateTime.fromMillisecondsSinceEpoch(
        lastRead.updatedAtMs,
        isUtc: true,
      ).toIso8601String();
      await client.from('user_library').upsert({
        'user_id': uid,
        'progress': lastRead.toJson(),
        'progress_updated_at': updatedAt,
      }, onConflict: 'user_id');
      await client.from('reading_progress').upsert({
        'user_id': uid,
        'surah_number': lastRead.surahNumber,
        'ayah_number': lastRead.ayahNumber,
      }, onConflict: 'user_id');
    }));
  }

  Future<void> pushBookmarksToCloud() async {
    final uid = _uid;
    final client = _client;
    if (uid == null || client == null || !Get.isRegistered<BookmarkController>()) {
      return;
    }

    await _writeLibrary(() => _guarded(() async {
      final document = Get.find<BookmarkController>().currentSyncDocument();
      final updatedAt = document.updatedAtMs <= 0
          ? DateTime.now().toUtc().toIso8601String()
          : DateTime.fromMillisecondsSinceEpoch(
              document.updatedAtMs,
              isUtc: true,
            ).toIso8601String();
      await client.from('user_library').upsert({
        'user_id': uid,
        'bookmarks': document.items,
        'tombstones': document.tombstones,
        'bookmarks_updated_at': updatedAt,
      }, onConflict: 'user_id');
    }));
  }

  Future<void> _writeLibrary(Future<void> Function() action) {
    final run = _libraryWrite.then((_) => action());
    _libraryWrite = run.catchError((Object _) {});
    return run;
  }

  Future<void> pushTasbihToCloud() async {
    final uid = _uid;
    final client = _client;
    if (uid == null || client == null) return;

    await _guarded(
      () => client.from('tasbih_logs').upsert({
        'user_id': uid,
        'count': _storage.tasbihCount.value,
      }, onConflict: 'user_id'),
    );
  }

  Future<void> pullCloudToLocal() async {
    final uid = _uid;
    final client = _client;
    if (uid == null || client == null) return;

    _applyingRemote = true;
    try {
      await _mergeProfile(client, uid);
      await _mergeProgress(client, uid);
      await _mergeBookmarks(client, uid);
      await _mergeTasbih(client, uid);
    } catch (error) {
      debugPrint('Sync pull failed: $error');
    } finally {
      _applyingRemote = false;
    }
  }

  Future<void> _mergeProfile(SupabaseClient client, String uid) async {
    final row = await client.from('profiles').select().eq('id', uid).maybeSingle();
    if (row == null) return;
    final map = asStringKeyMap(row);

    final cloudName = '${map['name'] ?? ''}'.trim();
    final cloudCountry = '${map['country'] ?? ''}'.trim();
    if (cloudName.isNotEmpty || cloudCountry.isNotEmpty) {
      await _storage.saveProfile(
        name: cloudName.isNotEmpty ? cloudName : _storage.userName.value,
        country:
            cloudCountry.isNotEmpty ? cloudCountry : _storage.userCountry.value,
      );
    }

    final translationId = '${map['translation_id'] ?? ''}'.trim();
    if (translationId.isNotEmpty) {
      await _storage.saveTranslation(
        identifier: translationId,
        name: '${map['translation_name'] ?? _storage.selectedTranslationName.value}',
        language: '${map['language'] ?? _storage.selectedTranslationLanguage.value}',
        direction:
            '${map['translation_direction'] ?? _storage.selectedTranslationDirection.value}',
      );
    }
  }

  Future<void> _mergeProgress(SupabaseClient client, String uid) async {
    try {
      await _mergeProgressRow(client, uid);
    } catch (error) {
      debugPrint('Progress sync skipped: $error');
    }
  }

  Future<void> _mergeProgressRow(SupabaseClient client, String uid) async {
    final library = await _libraryRow(client, uid);
    var cloud = _progressFromLibrary(library);
    if (cloud == null && _storage.lastRead.value == null) {
      cloud = await _legacyProgress(client, uid);
    }
    final chosen = newerProgress(_storage.lastRead.value, cloud);
    if (chosen == null || sameProgress(_storage.lastRead.value, chosen)) return;
    await _storage.saveLastRead(
      surahNumber: chosen.surahNumber,
      ayahNumber: chosen.ayahNumber <= 0 ? 1 : chosen.ayahNumber,
      source: chosen.source,
      mushafPage: chosen.mushafPage,
      updatedAtMs: chosen.updatedAtMs <= 0 ? null : chosen.updatedAtMs,
    );
  }

  Future<void> _mergeBookmarks(SupabaseClient client, String uid) async {
    try {
      await _mergeBookmarkRows(client, uid);
    } catch (error) {
      debugPrint('Bookmark sync skipped: $error');
    }
  }

  Future<void> _mergeBookmarkRows(SupabaseClient client, String uid) async {
    if (!Get.isRegistered<BookmarkController>()) return;
    final bookmarks = Get.find<BookmarkController>();
    final local = bookmarks.currentSyncDocument();
    final library = await _libraryRow(client, uid);
    if (library == null) {
      if (local.items.isNotEmpty || local.tombstones.isNotEmpty) return;
      final imported = await _legacySurahBookmarks(client, uid);
      if (imported.isEmpty) return;
      await bookmarks.applyCloudBookmarks(
        items: imported,
        tombstones: const {},
        updatedAtMs: DateTime.now().millisecondsSinceEpoch,
      );
      return;
    }

    final cloud = _bookmarksFromLibrary(library);
    final merged = mergeBookmarkDocuments(local, cloud);
    if (!bookmarkDocumentsMatch(local, merged)) {
      await bookmarks.applyCloudBookmarks(
        items: merged.items,
        tombstones: merged.tombstones,
        updatedAtMs: merged.updatedAtMs,
      );
    }
  }

  Future<Map<String, dynamic>?> _libraryRow(
    SupabaseClient client,
    String uid,
  ) async {
    final row = await client
        .from('user_library')
        .select()
        .eq('user_id', uid)
        .maybeSingle();
    if (row == null) return null;
    return asStringKeyMap(row);
  }

  LastRead? _progressFromLibrary(Map<String, dynamic>? row) {
    if (row == null) return null;
    final raw = row['progress'];
    if (raw is! Map) return null;
    final progress = LastRead.fromJson(asStringKeyMap(raw));
    if (progress.surahNumber <= 0) return null;
    if (progress.updatedAtMs > 0) return progress;
    final columnStamp = parseSyncTime(row['progress_updated_at']);
    if (columnStamp <= 0) return progress;
    return LastRead(
      surahNumber: progress.surahNumber,
      ayahNumber: progress.ayahNumber,
      source: progress.source,
      mushafPage: progress.mushafPage,
      updatedAtMs: columnStamp,
    );
  }

  Future<LastRead?> _legacyProgress(SupabaseClient client, String uid) async {
    final row = await client
        .from('reading_progress')
        .select()
        .eq('user_id', uid)
        .maybeSingle();
    if (row == null) return null;
    final map = asStringKeyMap(row);
    final surah = asInt(map['surah_number']);
    if (surah <= 0) return null;
    final ayah = asInt(map['ayah_number']);
    return LastRead(
      surahNumber: surah,
      ayahNumber: ayah <= 0 ? 1 : ayah,
    );
  }

  BookmarkSyncDocument _bookmarksFromLibrary(Map<String, dynamic> row) {
    final items = <Map<String, dynamic>>[];
    final rawItems = row['bookmarks'];
    if (rawItems is List) {
      for (final item in rawItems) {
        if (item is Map) items.add(asStringKeyMap(item));
      }
    }
    final tombstones = <String, int>{};
    final rawTombstones = row['tombstones'];
    if (rawTombstones is Map) {
      for (final entry in rawTombstones.entries) {
        final id = '${entry.key}'.trim();
        final stamp = asInt(entry.value);
        if (id.isEmpty || stamp <= 0) continue;
        tombstones[id] = stamp;
      }
    }
    return BookmarkSyncDocument(
      items: items,
      tombstones: tombstones,
      updatedAtMs: parseSyncTime(row['bookmarks_updated_at']),
    );
  }

  Future<List<Map<String, dynamic>>> _legacySurahBookmarks(
    SupabaseClient client,
    String uid,
  ) async {
    final rows = await client
        .from('bookmarks')
        .select('surah_number')
        .eq('user_id', uid);
    final imported = <Map<String, dynamic>>[];
    for (final row in rows) {
      final number = asInt(asStringKeyMap(row)['surah_number']);
      if (number <= 0) continue;
      imported.add(
        AppBookmark.translation(surahNumber: number).toJson(),
      );
    }
    return imported;
  }

  Future<LastRead?> _stampedLastRead() async {
    final current = _storage.lastRead.value;
    if (current == null) return null;
    if (current.updatedAtMs > 0) return current;
    _applyingRemote = true;
    try {
      await _storage.saveLastRead(
        surahNumber: current.surahNumber,
        ayahNumber: current.ayahNumber,
        source: current.source,
        mushafPage: current.mushafPage,
      );
    } finally {
      _applyingRemote = false;
    }
    return _storage.lastRead.value;
  }

  Future<void> _mergeTasbih(SupabaseClient client, String uid) async {
    final row = await client
        .from('tasbih_logs')
        .select()
        .eq('user_id', uid)
        .maybeSingle();
    if (row == null) return;
    final cloudCount = asInt(asStringKeyMap(row)['count']);
    final localCount = _storage.tasbihCount.value;
    final merged = cloudCount > localCount ? cloudCount : localCount;
    await _storage.saveTasbihCount(merged);
  }

  String? get _uid => _auth.currentUser.value?.id;

  SupabaseClient? get _client {
    try {
      return Supabase.instance.client;
    } catch (_) {
      return null;
    }
  }

  Future<void> _guarded(Future<dynamic> Function() action) async {
    if (!_canSync) return;
    try {
      await action();
    } catch (error) {
      debugPrint('Sync request failed: $error');
    }
  }

  @override
  void onClose() {
    for (final worker in _workers) {
      worker.dispose();
    }
    super.onClose();
  }
}
