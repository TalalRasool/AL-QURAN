import 'dart:io';

import 'package:flutter/services.dart';
import 'package:path/path.dart' as p;
import 'package:sqflite/sqflite.dart';
import 'package:sqflite_common_ffi/sqflite_ffi.dart' as ffi;

/// Copies [quran_5_languages_wbw_full.db] from assets on first launch, then
/// opens a read-only SQLite connection.
class DatabaseHelper {
  DatabaseHelper._();

  static final DatabaseHelper instance = DatabaseHelper._();

  static const assetPath = 'assets/databases/quran_5_languages_wbw_full.db';
  static const fileName = 'quran_5_languages_wbw_full.db';

  /// Bump this whenever `quran_5_languages_wbw_full.db` in assets must replace
  /// the copy already stored on the device.
  /// 2: Persian full-ayah (`persian_full`) and word (`persian`) columns.
  static const schemaVersion = 2;

  Database? _db;
  Future<Database>? _opening;
  static bool _ffiReady = false;
  String? initError;

  static bool needsAssetCopy({
    required bool databaseFileExists,
    required bool versionMarkerExists,
  }) {
    return !(databaseFileExists && versionMarkerExists);
  }

  Future<DatabaseHelper> init() async {
    try {
      await database;
      initError = null;
    } catch (_) {
      initError =
          'Quran database could not be opened. Fully rebuild the app and try again.';
    }
    return this;
  }

  Future<Database> get database async {
    final existing = _db;
    if (existing != null && existing.isOpen) return existing;
    final inFlight = _opening;
    if (inFlight != null) return inFlight;
    final opening = _open();
    _opening = opening;
    try {
      final opened = await opening;
      _db = opened;
      return opened;
    } finally {
      if (identical(_opening, opening)) _opening = null;
    }
  }

  Future<Database> _open() async {
    _ensureFfi();
    final databasesPath = await getDatabasesPath();
    await Directory(databasesPath).create(recursive: true);
    final path = p.join(databasesPath, fileName);
    await _copyFromAssetsIfNeeded(path);
    return openDatabase(path, readOnly: true, singleInstance: false);
  }

  Future<void> _copyFromAssetsIfNeeded(String path) async {
    final file = File(path);
    final marker = File('$path.v$schemaVersion');
    final fileReady = file.existsSync() && file.lengthSync() > 0;
    if (!needsAssetCopy(
      databaseFileExists: fileReady,
      versionMarkerExists: marker.existsSync(),
    )) {
      return;
    }

    if (_db != null && _db!.isOpen) {
      await _db!.close();
      _db = null;
    }
    if (file.existsSync()) {
      await file.delete();
    }
    await _deleteStaleMarkers(file.parent);

    final data = await rootBundle.load(assetPath);
    final bytes = data.buffer.asUint8List(
      data.offsetInBytes,
      data.lengthInBytes,
    );
    await file.writeAsBytes(bytes, flush: true);
    await marker.writeAsString('$schemaVersion', flush: true);
  }

  Future<void> _deleteStaleMarkers(Directory directory) async {
    if (!directory.existsSync()) return;
    await for (final entity in directory.list()) {
      if (entity is! File) continue;
      final name = p.basename(entity.path);
      if (name.startsWith('$fileName.v') &&
          name != '$fileName.v$schemaVersion') {
        await entity.delete();
      }
    }
  }

  static void _ensureFfi() {
    if (_ffiReady) return;
    if (Platform.isWindows || Platform.isLinux || Platform.isMacOS) {
      ffi.sqfliteFfiInit();
      databaseFactory = ffi.databaseFactoryFfi;
    }
    _ffiReady = true;
  }
}
