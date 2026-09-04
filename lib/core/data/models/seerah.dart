import '../json_utils.dart';

class SeerahItem {
  const SeerahItem({
    required this.titles,
    required this.headings,
    required this.details,
  });

  final Map<String, String> titles;
  final Map<String, String> headings;
  final Map<String, String> details;

  String titleFor(String languageCode) => localizedText(titles, languageCode);

  String headingFor(String languageCode) =>
      localizedText(headings, languageCode);

  String detailsFor(String languageCode) =>
      localizedText(details, languageCode);

  factory SeerahItem.fromJson(Map<String, dynamic> json) {
    return SeerahItem(
      titles: asLocalizedMap(json['title']),
      headings: asLocalizedMap(json['heading']),
      details: asLocalizedMap(json['details'] ?? json['detailed_text']),
    );
  }

  bool get hasContent =>
      _hasLocalizedText(titles) || _hasLocalizedText(details);
}

class SeerahChapter {
  const SeerahChapter({
    required this.chapterId,
    required this.titles,
    required this.headings,
    required this.details,
    this.items = const [],
    this.keyPrefix = 'chapter',
  });

  final int chapterId;
  final Map<String, String> titles;
  final Map<String, String> headings;
  final Map<String, String> details;
  final List<SeerahItem> items;
  final String keyPrefix;

  String get id => '${keyPrefix}_$chapterId';

  String titleFor(String languageCode) => localizedText(titles, languageCode);

  String headingFor(String languageCode) =>
      localizedText(headings, languageCode);

  String detailsFor(String languageCode) =>
      localizedText(details, languageCode);

  factory SeerahChapter.fromJson(
    Map<String, dynamic> json, {
    String keyPrefix = 'chapter',
  }) {
    final rawItems = json['items'];
    return SeerahChapter(
      chapterId: asInt(json['chapter_id'] ?? json['id']),
      titles: asLocalizedMap(json['title']),
      headings: asLocalizedMap(json['heading']),
      details: asLocalizedMap(json['details'] ?? json['detailed_text']),
      items: rawItems is List
          ? [
              for (final item in rawItems)
                if (item is Map)
                  SeerahItem.fromJson(Map<String, dynamic>.from(item)),
            ].where((item) => item.hasContent).toList(growable: false)
          : const [],
      keyPrefix: keyPrefix,
    );
  }

  bool get hasContent =>
      _hasLocalizedText(titles) || _hasLocalizedText(details);

  static List<SeerahChapter> listFrom(
    dynamic raw, {
    String keyPrefix = 'chapter',
  }) {
    if (raw is! List) return const [];
    return [
      for (final item in raw)
        if (item is Map)
          SeerahChapter.fromJson(asStringKeyMap(item), keyPrefix: keyPrefix),
    ].where((chapter) => chapter.hasContent).toList(growable: false);
  }
}

bool _hasLocalizedText(Map<String, String> values) {
  for (final value in values.values) {
    if (value.trim().isNotEmpty) return true;
  }
  return false;
}
