import 'dart:convert';
import 'dart:io';

import 'package:alquran/features/hadith/data/hadith_editions.dart';
import 'package:sqlite3/sqlite3.dart';

const _outputPath = 'assets/databases/hadith.db';

const _books = <({int id, String slug, String name})>[
  (id: 1, slug: 'bukhari', name: 'Sahih al-Bukhari'),
  (id: 2, slug: 'muslim', name: 'Sahih Muslim'),
  (id: 3, slug: 'abudawud', name: 'Sunan Abu Dawud'),
  (id: 4, slug: 'tirmidhi', name: 'Jami at-Tirmidhi'),
  (id: 5, slug: 'nasai', name: "Sunan an-Nasa'i"),
  (id: 6, slug: 'ibnmajah', name: 'Sunan Ibn Majah'),
];

Future<void> main() async {
  final outDir = Directory('assets/databases');
  if (!outDir.existsSync()) {
    await outDir.create(recursive: true);
  }

  final dbFile = File(_outputPath);
  if (dbFile.existsSync()) {
    await dbFile.delete();
  }

  final translationSpecs = HadithEditions.translations;
  final textColumns = [
    HadithEditions.textArColumn,
    for (final spec in translationSpecs) spec.column!,
  ];

  stdout.writeln('Creating $_outputPath ...');
  final db = sqlite3.open(_outputPath);
  try {
    db.execute('PRAGMA journal_mode = OFF;');
    db.execute('PRAGMA synchronous = OFF;');
    db.execute('''
      CREATE TABLE books (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
      );
    ''');
    db.execute('''
      CREATE TABLE chapters (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        book_id INTEGER NOT NULL,
        number INTEGER NOT NULL,
        name TEXT NOT NULL,
        FOREIGN KEY (book_id) REFERENCES books (id)
      );
    ''');
    db.execute('''
      CREATE TABLE ahadith (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        book_id INTEGER NOT NULL,
        chapter_id INTEGER NOT NULL,
        hadith_number REAL NOT NULL,
        ${textColumns.map((column) => '$column TEXT NOT NULL DEFAULT \'\'').join(',\n        ')},
        FOREIGN KEY (book_id) REFERENCES books (id),
        FOREIGN KEY (chapter_id) REFERENCES chapters (id)
      );
    ''');
    db.execute('CREATE INDEX idx_chapters_book ON chapters (book_id, number);');
    db.execute(
      'CREATE INDEX idx_ahadith_chapter ON ahadith (chapter_id, hadith_number);',
    );

    db.execute('BEGIN TRANSACTION;');

    final insertBook = db.prepare(
      'INSERT INTO books (id, name) VALUES (?, ?);',
    );
    final insertChapter = db.prepare(
      'INSERT INTO chapters (book_id, number, name) VALUES (?, ?, ?);',
    );
    final placeholders = List.filled(3 + textColumns.length, '?').join(', ');
    final insertHadith = db.prepare('''
      INSERT INTO ahadith
        (book_id, chapter_id, hadith_number, ${textColumns.join(', ')})
      VALUES ($placeholders);
    ''');

    try {
      for (final book in _books) {
        stdout.writeln('Processing ${book.name}...');
        final editions = <String, Map<String, dynamic>?>{};
        for (final spec in HadithEditions.specs) {
          editions[spec.appCode] = _loadEdition(
            _editionPath(spec, book.slug),
            optional: !spec.required,
            label: '${spec.label} ${book.name}',
          );
        }
        if (editions['ar'] == null && editions['en'] == null) {
          stderr.writeln('Skipping ${book.slug}: Arabic and English are missing.');
          continue;
        }

        insertBook.execute([book.id, book.name]);

        final chapters = _chapterNames(
          editions['en'],
          editions['ar'],
          editions['ur'],
        );
        final chapterDbIds = <int, int>{};
        for (final chapter in chapters) {
          insertChapter.execute([book.id, chapter.number, chapter.name]);
          chapterDbIds[chapter.number] = db.lastInsertRowId;
        }

        final hadiths = _mergeHadiths(editions);
        final filled = <String, int>{
          for (final spec in HadithEditions.specs) spec.appCode: 0,
        };
        for (final hadith in hadiths) {
          var chapterDbId = chapterDbIds[hadith.chapterNumber];
          if (chapterDbId == null) {
            insertChapter.execute([
              book.id,
              hadith.chapterNumber,
              _chapterTitle(hadith.chapterNumber, null, null, null),
            ]);
            chapterDbId = db.lastInsertRowId;
            chapterDbIds[hadith.chapterNumber] = chapterDbId;
          }
          for (final spec in HadithEditions.specs) {
            if ((hadith.texts[spec.appCode] ?? '').isNotEmpty) {
              filled[spec.appCode] = filled[spec.appCode]! + 1;
            }
          }
          insertHadith.execute([
            book.id,
            chapterDbId,
            hadith.number,
            for (final spec in HadithEditions.specs)
              hadith.texts[spec.appCode] ?? '',
          ]);
        }
        final counts = [
          for (final spec in HadithEditions.specs)
            '${spec.appCode}=${filled[spec.appCode]}',
        ].join(', ');
        stdout.writeln(
          '  ${chapterDbIds.length} chapters, ${hadiths.length} ahadith ($counts).',
        );
      }
    } finally {
      insertBook.dispose();
      insertChapter.dispose();
      insertHadith.dispose();
    }

    db.execute('COMMIT;');
    stdout.writeln('Compacting database...');
    db.execute('VACUUM;');
  } catch (error, stack) {
    try {
      db.execute('ROLLBACK;');
    } catch (_) {}
    db.dispose();
    stderr.writeln('Failed to generate Hadith database: $error');
    stderr.writeln('$stack');
    exit(1);
  }

  db.dispose();
  final sizeMb = (dbFile.lengthSync() / (1024 * 1024)).toStringAsFixed(1);
  stdout.writeln('Saved $_outputPath ($sizeMb MB) successfully!');
}

String? _editionPath(HadithEditionSpec spec, String slug) {
  final name = spec.fileName(slug);
  final bundled = File('assets/json/$name');
  if (bundled.existsSync()) return bundled.path;
  final downloaded = File('tool/hadith_editions/$name');
  if (downloaded.existsSync()) return downloaded.path;
  return null;
}

Map<String, dynamic>? _loadEdition(
  String? path, {
  required bool optional,
  required String label,
}) {
  if (path == null) {
    final message = 'No edition file for $label.';
    if (optional) {
      stdout.writeln('  $message English fallback will be used.');
      return null;
    }
    throw StateError(message);
  }
  stdout.writeln('  Loading $path ...');
  return jsonDecode(File(path).readAsStringSync(encoding: utf8))
      as Map<String, dynamic>;
}

List<_Chapter> _chapterNames(
  Map<String, dynamic>? english,
  Map<String, dynamic>? arabic,
  Map<String, dynamic>? urdu,
) {
  final englishSections = _sectionsOf(english);
  final arabicSections = _sectionsOf(arabic);
  final urduSections = _sectionsOf(urdu);
  final ids = {
    ...englishSections.keys,
    ...arabicSections.keys,
    ...urduSections.keys,
  }.toList()
    ..sort();

  return [
    for (final id in ids)
      _Chapter(
        number: id,
        name: _chapterTitle(
          id,
          englishSections[id],
          arabicSections[id],
          urduSections[id],
        ),
      ),
  ];
}

Map<int, String> _sectionsOf(Map<String, dynamic>? root) {
  if (root == null) return {};
  final metadata = root['metadata'];
  if (metadata is! Map) return {};
  final raw = metadata['sections'];
  if (raw is! Map) return {};

  final sections = <int, String>{};
  for (final entry in raw.entries) {
    final id = int.tryParse('${entry.key}');
    if (id == null) continue;
    sections[id] = '${entry.value}'.trim();
  }
  return sections;
}

String _chapterTitle(int id, String? english, String? arabic, String? urdu) {
  if (english != null && english.isNotEmpty) return english;
  if (arabic != null && arabic.isNotEmpty) return arabic;
  if (urdu != null && urdu.isNotEmpty) return urdu;
  return id == 0 ? 'Introduction' : 'Chapter $id';
}

List<_HadithRow> _mergeHadiths(Map<String, Map<String, dynamic>?> editions) {
  final merged = <num, _HadithRow>{};

  for (final spec in HadithEditions.specs) {
    final root = editions[spec.appCode];
    if (root == null) continue;
    final list = root['hadiths'];
    if (list is! List) continue;
    for (final item in list) {
      if (item is! Map) continue;
      final number = item['hadithnumber'];
      if (number is! num) continue;
      final reference = item['reference'];
      final chapterNumber = reference is Map
          ? int.tryParse('${reference['book']}') ?? 0
          : 0;
      final text = '${item['text'] ?? ''}'.trim();
      final row = merged.putIfAbsent(
        number,
        () => _HadithRow(number: number, chapterNumber: chapterNumber),
      );
      if (row.chapterNumber == 0 && chapterNumber != 0) {
        row.chapterNumber = chapterNumber;
      }
      if (text.isNotEmpty) row.texts[spec.appCode] = text;
    }
  }

  final rows = merged.values.toList()
    ..sort((a, b) {
      final chapter = a.chapterNumber.compareTo(b.chapterNumber);
      if (chapter != 0) return chapter;
      return a.number.compareTo(b.number);
    });
  return rows;
}

class _Chapter {
  const _Chapter({required this.number, required this.name});

  final int number;
  final String name;
}

class _HadithRow {
  _HadithRow({required this.number, required this.chapterNumber});

  final num number;
  int chapterNumber;
  final texts = <String, String>{};
}
