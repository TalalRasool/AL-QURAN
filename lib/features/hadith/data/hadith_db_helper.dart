import 'dart:io';

import 'package:flutter/services.dart';
import 'package:path/path.dart' as p;
import 'package:sqflite_common_ffi/sqflite_ffi.dart';

import 'hadith_editions.dart';
import 'hadith_models.dart';

class HadithDbHelper {
  HadithDbHelper._();

  static final HadithDbHelper instance = HadithDbHelper._();

  static const assetPath = 'assets/databases/hadith.db';
  static const fileName = 'hadith.db';

  /// Bump this whenever `hadith.db` in assets must replace the device copy.
  static const schemaVersion = 4;
  static const pageSize = 40;

  Database? _db;
  static bool _ffiReady = false;

  /// Set when copy/open fails so the Hadith UI can show a real error.
  String? initError;

  Future<HadithDbHelper> init() async {
    try {
      await database;
      initError = null;
    } catch (_) {
      initError =
          'Hadith database could not be opened. Fully rebuild the app and try again.';
    }
    return this;
  }

  Future<Database> get database async {
    final existing = _db;
    if (existing != null && existing.isOpen) return existing;
    _db = await _open();
    return _db!;
  }

  Future<List<HadithBook>> getBooks() async {
    final rows = await (await database).query('books', orderBy: 'id ASC');
    return rows.map(HadithBook.fromMap).toList();
  }

  Future<List<HadithChapter>> getChapters(
    int bookId, {
    String query = '',
  }) async {
    final db = await database;
    final trimmed = query.trim();
    if (trimmed.isEmpty) {
      final rows = await db.query(
        'chapters',
        where: 'book_id = ?',
        whereArgs: [bookId],
        orderBy: 'number ASC, id ASC',
      );
      return rows.map(HadithChapter.fromMap).toList();
    }

    final like = '%${_escapeLike(trimmed)}%';
    final rows = await db.query(
      'chapters',
      where:
          "book_id = ? AND (name LIKE ? ESCAPE '\\' OR CAST(number AS TEXT) LIKE ? ESCAPE '\\')",
      whereArgs: [bookId, like, like],
      orderBy: 'number ASC, id ASC',
    );
    return rows.map(HadithChapter.fromMap).toList();
  }

  Future<List<Hadith>> getAhadithPage({
    required int chapterId,
    int? bookId,
    String query = '',
    int limit = pageSize,
    int offset = 0,
  }) async {
    final db = await database;
    final where = StringBuffer('chapter_id = ?');
    final args = <Object?>[chapterId];

    if (bookId != null && bookId > 0) {
      where.write(' AND book_id = ?');
      args.add(bookId);
    }

    final trimmed = query.trim();
    if (trimmed.isNotEmpty) {
      final number = extractHadithNumber(trimmed);
      if (number != null) {
        where.write(' AND CAST(hadith_number AS INTEGER) = ?');
        args.add(number);
      } else {
        final like = '%${_escapeLike(trimmed)}%';
        final textColumns = [
          HadithEditions.textArColumn,
          for (final spec in HadithEditions.translations) spec.column!,
        ];
        where.write(
          " AND ("
          "CAST(hadith_number AS TEXT) LIKE ? ESCAPE '\\'",
        );
        args.add(like);
        for (final column in textColumns) {
          where.write(" OR $column LIKE ? ESCAPE '\\'");
          args.add(like);
        }
        where.write(')');
      }
    }

    final rows = await db.query(
      'ahadith',
      where: where.toString(),
      whereArgs: args,
      orderBy: 'hadith_number ASC, id ASC',
      limit: limit,
      offset: offset,
    );
    return rows.map(Hadith.fromMap).toList();
  }

  Future<Hadith?> getHadithById(int id) async {
    if (id <= 0) return null;
    final rows = await (await database).query(
      'ahadith',
      where: 'id = ?',
      whereArgs: [id],
      limit: 1,
    );
    if (rows.isEmpty) return null;
    return Hadith.fromMap(rows.first);
  }

  Future<HadithBook?> getBookById(int id) async {
    if (id <= 0) return null;
    final rows = await (await database).query(
      'books',
      where: 'id = ?',
      whereArgs: [id],
      limit: 1,
    );
    if (rows.isEmpty) return null;
    return HadithBook.fromMap(rows.first);
  }

  Future<HadithChapter?> getChapterById(int id) async {
    if (id <= 0) return null;
    final rows = await (await database).query(
      'chapters',
      where: 'id = ?',
      whereArgs: [id],
      limit: 1,
    );
    if (rows.isEmpty) return null;
    return HadithChapter.fromMap(rows.first);
  }

  Future<Database> _open() async {
    _ensureFfi();
    final databasesPath = await getDatabasesPath();
    await Directory(databasesPath).create(recursive: true);
    final path = p.join(databasesPath, fileName);
    await _copyAssetIfNeeded(path);
    return openDatabase(path, readOnly: true, singleInstance: false);
  }

  Future<void> _copyAssetIfNeeded(String path) async {
    final file = File(path);
    final marker = File('$path.v$schemaVersion');
    if (file.existsSync() && marker.existsSync()) return;

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

  static int? extractHadithNumber(String query) {
    final trimmed = query.trim();
    if (!RegExp(r'^\d+$').hasMatch(trimmed)) return null;
    return int.tryParse(trimmed);
  }

  static String _escapeLike(String value) {
    return value
        .replaceAll(r'\', r'\\')
        .replaceAll('%', r'\%')
        .replaceAll('_', r'\_');
  }

  static void _ensureFfi() {
    if (_ffiReady) return;
    if (Platform.isWindows || Platform.isLinux || Platform.isMacOS) {
      sqfliteFfiInit();
      databaseFactory = databaseFactoryFfi;
    }
    _ffiReady = true;
  }
}
