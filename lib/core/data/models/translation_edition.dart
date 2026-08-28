import '../json_utils.dart';

class TranslationEdition {
  const TranslationEdition({
    required this.identifier,
    required this.language,
    required this.name,
    required this.englishName,
    this.direction = 'ltr',
  });

  final String identifier;
  final String language;
  final String name;
  final String englishName;
  final String direction;

  String get authorName {
    if (language == 'en' && name.isNotEmpty) return name;
    if (englishName.isNotEmpty) return englishName;
    if (name.isNotEmpty) return name;
    return identifier;
  }

  String get languageLabel => languageNames[language] ?? language.toUpperCase();

  bool get isRtl => direction.toLowerCase() == 'rtl';

  factory TranslationEdition.fromJson(Map<String, dynamic> json) {
    return TranslationEdition(
      identifier: json['identifier'] as String? ?? '',
      language: json['language'] as String? ?? '',
      name: json['name'] as String? ?? '',
      englishName: json['englishName'] as String? ?? '',
      direction: json['direction'] as String? ?? 'ltr',
    );
  }

  static TranslationEdition fromDynamic(dynamic json) =>
      TranslationEdition.fromJson(asStringKeyMap(json));

  @override
  bool operator ==(Object other) =>
      other is TranslationEdition && other.identifier == identifier;

  @override
  int get hashCode => identifier.hashCode;

  static const languageNames = <String, String>{
    'ar': 'Arabic',
    'az': 'Azerbaijani',
    'ber': 'Berber',
    'bn': 'Bengali',
    'bs': 'Bosnian',
    'cs': 'Czech',
    'de': 'German',
    'dv': 'Dhivehi',
    'en': 'English',
    'es': 'Spanish',
    'fa': 'Persian',
    'fr': 'French',
    'ha': 'Hausa',
    'hi': 'Hindi',
    'id': 'Indonesian',
    'it': 'Italian',
    'ja': 'Japanese',
    'ko': 'Korean',
    'ku': 'Kurdish',
    'ml': 'Malayalam',
    'ms': 'Malay',
    'nl': 'Dutch',
    'no': 'Norwegian',
    'pl': 'Polish',
    'pt': 'Portuguese',
    'ro': 'Romanian',
    'ru': 'Russian',
    'sd': 'Sindhi',
    'so': 'Somali',
    'sq': 'Albanian',
    'sv': 'Swedish',
    'sw': 'Swahili',
    'ta': 'Tamil',
    'tg': 'Tajik',
    'th': 'Thai',
    'tr': 'Turkish',
    'tt': 'Tatar',
    'ug': 'Uyghur',
    'ur': 'Urdu',
    'uz': 'Uzbek',
    'zh': 'Chinese',
  };
}
