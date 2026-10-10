import '../../core/data/json_utils.dart';

/// One worship article parsed from the bundled guide.
///
/// [title] and [content] are keyed by language code (`en`, `ur`, `hi`, `bn`,
/// `id`, `fa`). [content] holds `summary`, `steps`, and `common_problems`.
class WorshipGuideItem {
  const WorshipGuideItem({
    required this.id,
    required this.category,
    required this.title,
    required this.content,
    this.guideKey = '',
    this.references = const [],
  });

  final int id;
  final String category;
  final Map<String, dynamic> title;
  final Map<String, dynamic> content;
  final String guideKey;
  final List<String> references;

  factory WorshipGuideItem.fromJson(
    Map<String, dynamic> json, {
    required int index,
  }) {
    final rawContent = asStringKeyMap(json['content']);
    final titles = <String, dynamic>{};
    final bodies = <String, dynamic>{};

    for (final entry in rawContent.entries) {
      final block = asStringKeyMap(entry.value);
      final title = block['title'];
      titles[entry.key] = title is String ? title.trim() : '';
      bodies[entry.key] = {
        'summary': block['summary'] is String
            ? (block['summary'] as String).trim()
            : '',
        'steps': _stringList(block['steps']),
        'common_problems': _stringList(block['common_problems']),
      };
    }

    final rawId = json['id'];
    return WorshipGuideItem(
      id: rawId is int ? rawId : index + 1,
      category: '${json['category_id'] ?? json['category'] ?? ''}'.trim(),
      title: titles,
      content: bodies,
      guideKey: rawId == null ? '${index + 1}' : '$rawId',
      references: _references(json['references']),
    );
  }

  String titleFor(String languageCode) => _string(title, languageCode);

  String summaryFor(String languageCode) =>
      _string(_field('summary'), languageCode);

  List<String> stepsFor(String languageCode) => _list(languageCode, 'steps');

  List<String> problemsFor(String languageCode) =>
      _list(languageCode, 'common_problems');

  Map<String, dynamic> _field(String field) {
    final values = <String, dynamic>{};
    for (final entry in content.entries) {
      final block = asStringKeyMap(entry.value);
      values[entry.key] = block[field];
    }
    return values;
  }

  String _string(Map<String, dynamic> values, String languageCode) {
    final strings = <String, String>{
      for (final entry in values.entries)
        if (entry.value is String && (entry.value as String).trim().isNotEmpty)
          entry.key: (entry.value as String).trim(),
    };
    return localizedText(strings, languageCode);
  }

  List<String> _list(String languageCode, String field) {
    final code = languageCode.trim().toLowerCase();
    final direct = _listAt(code, field);
    if (direct.isNotEmpty) return direct;
    if (code != 'en') {
      final english = _listAt('en', field);
      if (english.isNotEmpty) return english;
    }
    return direct;
  }

  List<String> _listAt(String languageCode, String field) {
    final block = asStringKeyMap(content[languageCode]);
    return _stringList(block[field]);
  }

  static List<String> _stringList(dynamic value) {
    if (value is! List) return const [];
    return [
      for (final item in value)
        if ('$item'.trim().isNotEmpty) '$item'.trim(),
    ];
  }

  static List<String> _references(dynamic value) {
    if (value is! List) return const [];
    return [
      for (final item in value)
        if (item is Map && '${item['citation'] ?? ''}'.trim().isNotEmpty)
          '${item['citation']}'.trim(),
    ];
  }
}

class WorshipCategory {
  const WorshipCategory({required this.id, required this.englishLabel});

  final String id;
  final String englishLabel;

  factory WorshipCategory.fromJson(Map<String, dynamic> json) {
    final id = '${json['id'] ?? ''}'.trim();
    final label = '${json['label'] ?? ''}'.trim();
    return WorshipCategory(id: id, englishLabel: label.isEmpty ? id : label);
  }
}

class WorshipDataset {
  const WorshipDataset({required this.categories, required this.guides});

  final List<WorshipCategory> categories;
  final List<WorshipGuideItem> guides;

  /// Articles split so each category list is independent of the others.
  Map<String, List<WorshipGuideItem>> get guidesByCategory {
    final grouped = <String, List<WorshipGuideItem>>{};
    for (final guide in guides) {
      grouped.putIfAbsent(guide.category, () => []).add(guide);
    }
    return grouped;
  }

  factory WorshipDataset.fromJson(Map<String, dynamic> json) {
    final guides = <WorshipGuideItem>[];
    final guidesRaw = json['guides'];
    if (guidesRaw is List) {
      for (var i = 0; i < guidesRaw.length; i++) {
        final item = guidesRaw[i];
        if (item is! Map) continue;
        final guide = WorshipGuideItem.fromJson(asStringKeyMap(item), index: i);
        if (guide.category.isEmpty) continue;
        guides.add(guide);
      }
    }

    final categories = <WorshipCategory>[];
    final seen = <String>{};
    final categoriesRaw = json['categories'];
    if (categoriesRaw is List) {
      for (final item in categoriesRaw) {
        if (item is! Map) continue;
        final category = WorshipCategory.fromJson(asStringKeyMap(item));
        if (category.id.isEmpty || !seen.add(category.id)) continue;
        categories.add(category);
      }
    }

    for (final guide in guides) {
      if (seen.add(guide.category)) {
        categories.add(
          WorshipCategory(id: guide.category, englishLabel: guide.category),
        );
      }
    }

    return WorshipDataset(categories: categories, guides: guides);
  }
}
