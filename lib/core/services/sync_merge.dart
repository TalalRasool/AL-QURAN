import '../data/json_utils.dart';
import '../data/models/last_read.dart';

/// Keeps the progress with the later [LastRead.updatedAtMs].
///
/// A missing local value takes the cloud value. Equal timestamps keep local.
LastRead? newerProgress(LastRead? local, LastRead? cloud) {
  if (local == null) return cloud;
  if (cloud == null) return local;
  if (cloud.surahNumber <= 0) return local;
  if (cloud.updatedAtMs > local.updatedAtMs) return cloud;
  return local;
}

bool sameProgress(LastRead? a, LastRead? b) {
  if (identical(a, b)) return true;
  if (a == null || b == null) return false;
  return a.surahNumber == b.surahNumber &&
      a.ayahNumber == b.ayahNumber &&
      a.source == b.source &&
      a.mushafPage == b.mushafPage &&
      a.updatedAtMs == b.updatedAtMs;
}

class BookmarkSyncDocument {
  const BookmarkSyncDocument({
    required this.items,
    required this.tombstones,
    required this.updatedAtMs,
  });

  final List<Map<String, dynamic>> items;
  final Map<String, int> tombstones;
  final int updatedAtMs;

  static const empty = BookmarkSyncDocument(
    items: [],
    tombstones: {},
    updatedAtMs: 0,
  );
}

/// Merges bookmark documents per id.
///
/// A tombstone wins when its time is at least the bookmark's `createdAt`.
/// A later `createdAt` brings the bookmark back.
BookmarkSyncDocument mergeBookmarkDocuments(
  BookmarkSyncDocument local,
  BookmarkSyncDocument remote, {
  int? nowMs,
}) {
  final items = <String, Map<String, dynamic>>{};
  final createdAt = <String, int>{};

  void consider(Map<String, dynamic> raw) {
    final id = '${raw['id'] ?? ''}'.trim();
    if (id.isEmpty) return;
    final stamp = asInt(raw['createdAt']);
    final current = createdAt[id];
    if (current != null && stamp < current) return;
    items[id] = Map<String, dynamic>.from(raw);
    createdAt[id] = stamp;
  }

  for (final item in local.items) {
    consider(item);
  }
  for (final item in remote.items) {
    consider(item);
  }

  final tombstones = <String, int>{};
  void considerTombstone(Map<String, int> source) {
    for (final entry in source.entries) {
      final id = entry.key.trim();
      if (id.isEmpty || entry.value <= 0) continue;
      final current = tombstones[id];
      if (current == null || entry.value > current) {
        tombstones[id] = entry.value;
      }
    }
  }

  considerTombstone(local.tombstones);
  considerTombstone(remote.tombstones);

  items.removeWhere((id, raw) {
    final deletedAt = tombstones[id];
    if (deletedAt == null) return false;
    return deletedAt >= asInt(raw['createdAt']);
  });
  tombstones.removeWhere((id, deletedAt) {
    final item = items[id];
    if (item == null) return false;
    return asInt(item['createdAt']) > deletedAt;
  });

  final mergedItems = items.values.toList()
    ..sort((a, b) => asInt(b['createdAt']).compareTo(asInt(a['createdAt'])));
  final draft = BookmarkSyncDocument(
    items: mergedItems,
    tombstones: tombstones,
    updatedAtMs: 0,
  );
  final localStamp = local.updatedAtMs;
  final remoteStamp = remote.updatedAtMs;
  var stamp = localStamp > remoteStamp ? localStamp : remoteStamp;
  final changed = !bookmarkDocumentsMatch(draft, local) ||
      !bookmarkDocumentsMatch(draft, remote);
  if (changed) {
    final now = nowMs ?? DateTime.now().millisecondsSinceEpoch;
    if (now > stamp) stamp = now;
  }

  return BookmarkSyncDocument(
    items: mergedItems,
    tombstones: tombstones,
    updatedAtMs: stamp,
  );
}

bool bookmarkDocumentsMatch(
  BookmarkSyncDocument a,
  BookmarkSyncDocument b,
) {
  return _canonicalItems(a.items) == _canonicalItems(b.items) &&
      _canonicalTombstones(a.tombstones) == _canonicalTombstones(b.tombstones);
}

int parseSyncTime(dynamic value) {
  if (value is int) return value;
  if (value is num) return value.toInt();
  final text = '$value'.trim();
  if (text.isEmpty || text == 'null') return 0;
  final parsedInt = int.tryParse(text);
  if (parsedInt != null) return parsedInt;
  return DateTime.tryParse(text)?.millisecondsSinceEpoch ?? 0;
}

String _canonicalItems(List<Map<String, dynamic>> items) {
  final copies = [
    for (final item in items)
      if ('${item['id'] ?? ''}'.trim().isNotEmpty)
        Map<String, dynamic>.from(item),
  ]..sort((a, b) => '${a['id']}'.compareTo('${b['id']}'));
  return copies.map((item) => item.toString()).join('|');
}

String _canonicalTombstones(Map<String, int> tombstones) {
  final keys = tombstones.keys.toList()..sort();
  return [
    for (final key in keys)
      if (key.trim().isNotEmpty && tombstones[key]! > 0) '$key=${tombstones[key]}',
  ].join('|');
}
