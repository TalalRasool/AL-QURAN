import 'package:alquran/core/data/models/last_read.dart';
import 'package:alquran/core/services/sync_merge.dart';
import 'package:alquran/features/hadith/data/hadith_db_helper.dart';
import 'package:alquran/screens/quran/reading_position.dart';
import 'package:alquran/services/database_helper.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  test('newer reading progress wins, equal timestamps keep local', () {
    const local = LastRead(
      surahNumber: 2,
      ayahNumber: 40,
      updatedAtMs: 10,
    );
    const newerCloud = LastRead(
      surahNumber: 18,
      ayahNumber: 5,
      updatedAtMs: 20,
    );
    const olderCloud = LastRead(
      surahNumber: 1,
      ayahNumber: 1,
      updatedAtMs: 5,
    );

    expect(newerProgress(local, newerCloud)?.surahNumber, 18);
    expect(newerProgress(local, olderCloud)?.surahNumber, 2);
    expect(newerProgress(local, local)?.ayahNumber, 40);
    expect(newerProgress(null, newerCloud)?.surahNumber, 18);
    expect(newerProgress(local, null)?.surahNumber, 2);
  });

  test('bookmark tombstones survive a union and a later add restores', () {
    const local = BookmarkSyncDocument(
      items: [
        {'id': 'translation:1', 'createdAt': 10},
        {'id': 'mushaf:4', 'createdAt': 12},
      ],
      tombstones: {'translation:2': 30},
      updatedAtMs: 30,
    );
    const cloud = BookmarkSyncDocument(
      items: [
        {'id': 'translation:1', 'createdAt': 10},
        {'id': 'translation:2', 'createdAt': 8},
        {'id': 'hadith:9', 'createdAt': 15},
      ],
      tombstones: {},
      updatedAtMs: 15,
    );

    final merged = mergeBookmarkDocuments(local, cloud, nowMs: 40);
    final ids = merged.items.map((item) => item['id']).toList();

    expect(ids, containsAll(['translation:1', 'mushaf:4', 'hadith:9']));
    expect(ids, isNot(contains('translation:2')));
    expect(merged.tombstones['translation:2'], 30);

    final restored = mergeBookmarkDocuments(
      merged,
      const BookmarkSyncDocument(
        items: [
          {'id': 'translation:2', 'createdAt': 50},
        ],
        tombstones: {},
        updatedAtMs: 50,
      ),
      nowMs: 60,
    );
    expect(
      restored.items.map((item) => item['id']),
      contains('translation:2'),
    );
    expect(restored.tombstones.containsKey('translation:2'), isFalse);
  });

  test('reading resumes the requested ayah, then a saved surah ayah', () {
    final ayahs = [
      (surahNumber: 2, ayahNumber: 1),
      (surahNumber: 2, ayahNumber: 50),
      (surahNumber: 2, ayahNumber: 51),
    ];
    const saved = LastRead(surahNumber: 2, ayahNumber: 50, updatedAtMs: 1);
    const mushaf = LastRead(
      surahNumber: 2,
      ayahNumber: 50,
      source: LastRead.sourceMushaf,
      mushafPage: 3,
    );

    expect(
      revealIndex(ayahs, preferredSurah: 2, preferredAyah: 51, saved: saved),
      2,
    );
    expect(revealIndex(ayahs, saved: saved), 1);
    expect(revealIndex(ayahs, saved: mushaf), 0);
    expect(
      revealIndex(
        ayahs,
        preferredSurah: 36,
        preferredAyah: 1,
        saved: saved,
      ),
      1,
    );
  });

  test('quran database is recopied until the version marker exists', () {
    expect(
      DatabaseHelper.needsAssetCopy(
        databaseFileExists: true,
        versionMarkerExists: false,
      ),
      isTrue,
    );
    expect(
      DatabaseHelper.needsAssetCopy(
        databaseFileExists: true,
        versionMarkerExists: true,
      ),
      isFalse,
    );
    expect(
      DatabaseHelper.needsAssetCopy(
        databaseFileExists: false,
        versionMarkerExists: true,
      ),
      isTrue,
    );
  });

  test('hadith number search is only an exact number', () {
    expect(HadithDbHelper.extractHadithNumber('42'), 42);
    expect(HadithDbHelper.extractHadithNumber('2 faith'), isNull);
    expect(HadithDbHelper.extractHadithNumber('faith'), isNull);
  });
}
