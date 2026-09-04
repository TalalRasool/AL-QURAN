import '../json_utils.dart';

class DuaItem {
  const DuaItem({
    required this.id,
    required this.arabicText,
    required this.titles,
    required this.translations,
  });

  final String id;
  final String arabicText;
  final Map<String, String> titles;
  final Map<String, String> translations;

  String titleFor(String languageCode) => localizedText(titles, languageCode);

  String translationFor(String languageCode) =>
      localizedText(translations, languageCode);

  String get title => titleFor('en');

  String get translation => translationFor('en');

  factory DuaItem.fromJson(Map<String, dynamic> json) {
    return DuaItem(
      id: '${json['id'] ?? ''}',
      arabicText: '${json['arabic_text'] ?? ''}',
      titles: asLocalizedMap(json['title']),
      translations: asLocalizedMap(json['translation']),
    );
  }
}

class AzkarItem {
  const AzkarItem({required this.arabic});

  final String arabic;

  factory AzkarItem.fromJson(Map<String, dynamic> json) {
    return AzkarItem(arabic: '${json['arabic'] ?? ''}');
  }
}
