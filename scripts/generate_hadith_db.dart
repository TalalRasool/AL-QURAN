import 'dart:convert';
import 'dart:io';

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
        text_ar TEXT NOT NULL DEFAULT '',
        text_en TEXT NOT NULL DEFAULT '',
        text_ur TEXT NOT NULL DEFAULT '',
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
    final insertHadith = db.prepare('''
      INSERT INTO ahadith
        (book_id, chapter_id, hadith_number, text_ar, text_en, text_ur)
      VALUES (?, ?, ?, ?, ?, ?);
    ''');

    try {
      for (final book in _books) {
        stdout.writeln('Processing ${book.name}...');
        final arabic = _loadEdition(_path('ara', book.slug));
        final english = _loadEdition(_path('eng', book.slug));
        final urdu = _loadEdition(_path('urd', book.slug));
        if (arabic == null && english == null && urdu == null) {
          stderr.writeln('Skipping ${book.slug}: no JSON editions found.');
          continue;
        }

        insertBook.execute([book.id, book.name]);

        final chapters = _chapterNames(english, arabic, urdu);
        final chapterDbIds = <int, int>{};
        for (final chapter in chapters) {
          insertChapter.execute([book.id, chapter.number, chapter.name]);
          chapterDbIds[chapter.number] = db.lastInsertRowId;
        }

        final hadiths = _mergeHadiths(arabic, english, urdu);
        var inserted = 0;
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
          insertHadith.execute([
            book.id,
            chapterDbId,
            hadith.number,
            hadith.textAr,
            hadith.textEn,
            hadith.textUr,
          ]);
          inserted++;
        }
        stdout.writeln(
          '  ${chapters.length} chapters, $inserted ahadith.',
        );
      }
    } finally {
      insertBook.dispose();
      insertChapter.dispose();
      insertHadith.dispose();
    }

    db.execute('COMMIT;');
  } catch (error) {
    try {
      db.execute('ROLLBACK;');
    } catch (_) {}
    db.dispose();
    stderr.writeln('Failed to generate Hadith database: $error');
    exit(1);
  }

  db.dispose();
  final sizeMb = (dbFile.lengthSync() / (1024 * 1024)).toStringAsFixed(1);
  stdout.writeln('Saved $_outputPath ($sizeMb MB) successfully!');
}

String _path(String language, String slug) =>
    'assets/json/$language-$slug.json';

Map<String, dynamic>? _loadEdition(String path) {
  final file = File(path);
  if (!file.existsSync()) {
    stderr.writeln('Missing $path');
    return null;
  }
  stdout.writeln('Loading $path ...');
  return jsonDecode(file.readAsStringSync(encoding: utf8))
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

List<_HadithRow> _mergeHadiths(
  Map<String, dynamic>? arabic,
  Map<String, dynamic>? english,
  Map<String, dynamic>? urdu,
) {
  final merged = <num, _HadithRow>{};

  void apply(
    Map<String, dynamic>? root,
    void Function(_HadithRow, String) setText,
  ) {
    if (root == null) return;
    final list = root['hadiths'];
    if (list is! List) return;
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
      setText(row, text);
    }
  }

  apply(arabic, (row, text) => row.textAr = text);
  apply(english, (row, text) => row.textEn = text);
  apply(urdu, (row, text) => row.textUr = text);

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
  final int chapterNumber;
  String textAr = '';
  String textEn = '';
  String textUr = '';
}
