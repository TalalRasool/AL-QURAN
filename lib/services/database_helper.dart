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

  Database? _db;
  static bool _ffiReady = false;
  String? initError;

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
    _db = await _open();
    return _db!;
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
    if (await databaseExists(path)) {
      final file = File(path);
      if (file.existsSync() && file.lengthSync() > 0) return;
    }

    if (_db != null && _db!.isOpen) {
      await _db!.close();
      _db = null;
    }

    final data = await rootBundle.load(assetPath);
    final bytes = data.buffer.asUint8List(
      data.offsetInBytes,
      data.lengthInBytes,
    );
    await File(path).writeAsBytes(bytes, flush: true);
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
