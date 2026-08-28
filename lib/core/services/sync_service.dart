import 'dart:async';

import 'package:get/get.dart';
import 'package:supabase_flutter/supabase_flutter.dart';

import '../data/json_utils.dart';
import 'auth_service.dart';
import 'storage_service.dart';

class SyncService extends GetxService {
  final AuthService _auth = Get.find<AuthService>();
  final StorageService _storage = Get.find<StorageService>();

  final _workers = <Worker>[];
  var _applyingRemote = false;
  var _merging = false;

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
      ever(_storage.bookmarks, (_) {
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
    } catch (_) {
      // Stay on local data if the device is offline.
    } finally {
      _merging = false;
    }
  }

  Future<void> syncLocalToCloud() async {
    if (!_canSync) return;
    try {
      await Future.wait([
        pushProfileToCloud(),
        pushProgressToCloud(),
        pushBookmarksToCloud(),
        pushTasbihToCloud(),
      ]);
    } catch (_) {
      // Offline-first: local data stays; retry on next change or login.
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
    final lastRead = _storage.lastRead.value;
    if (uid == null || client == null || lastRead == null) return;

    await _guarded(
      () => client.from('reading_progress').upsert({
        'user_id': uid,
        'surah_number': lastRead.surahNumber,
        'ayah_number': lastRead.ayahNumber,
      }, onConflict: 'user_id'),
    );
  }

  Future<void> pushBookmarksToCloud() async {
    final uid = _uid;
    final client = _client;
    if (uid == null || client == null) return;

    await _guarded(() async {
      final local = _storage.bookmarks.toSet();
      final rows = await client
          .from('bookmarks')
          .select('surah_number')
          .eq('user_id', uid);
      final cloud = <int>{};
      for (final row in rows) {
        final number = asInt(asStringKeyMap(row)['surah_number']);
        if (number > 0) cloud.add(number);
      }

      final toRemove = cloud.difference(local).toList();
      final toAdd = local.difference(cloud).toList();

      if (toRemove.isNotEmpty) {
        await client
            .from('bookmarks')
            .delete()
            .eq('user_id', uid)
            .inFilter('surah_number', toRemove);
      }
      if (toAdd.isNotEmpty) {
        await client.from('bookmarks').insert(
              toAdd
                  .map(
                    (number) => {
                      'user_id': uid,
                      'surah_number': number,
                    },
                  )
                  .toList(),
            );
      }
    });
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
    } catch (_) {
      // Keep local data if the device is offline or tables are missing.
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
    if (_storage.lastRead.value != null) return;

    final row = await client
        .from('reading_progress')
        .select()
        .eq('user_id', uid)
        .maybeSingle();
    if (row == null) return;
    final map = asStringKeyMap(row);
    final surah = asInt(map['surah_number']);
    final ayah = asInt(map['ayah_number']);
    if (surah <= 0) return;
    await _storage.saveLastRead(
      surahNumber: surah,
      ayahNumber: ayah <= 0 ? 1 : ayah,
    );
  }

  Future<void> _mergeBookmarks(SupabaseClient client, String uid) async {
    final rows = await client
        .from('bookmarks')
        .select('surah_number')
        .eq('user_id', uid);
    final merged = _storage.bookmarks.toSet();
    for (final row in rows) {
      final number = asInt(asStringKeyMap(row)['surah_number']);
      if (number > 0) merged.add(number);
    }
    await _storage.replaceBookmarks(merged.toList()..sort());
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
    } catch (_) {
      // Offline-first: local data stays; cloud retry happens on next login/change.
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
