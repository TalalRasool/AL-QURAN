int asInt(dynamic value, {int fallback = 0}) {
  if (value is int) return value;
  if (value is num) return value.toInt();
  return int.tryParse('$value') ?? fallback;
}

num asNum(dynamic value, {num fallback = 0}) {
  if (value is num) return value;
  return num.tryParse('$value') ?? fallback;
}

Map<String, dynamic> asStringKeyMap(dynamic value) {
  if (value is Map<String, dynamic>) return value;
  if (value is Map) return Map<String, dynamic>.from(value);
  return {};
}

Map<String, String> asLocalizedMap(dynamic value) {
  if (value is String && value.trim().isNotEmpty) {
    return {'en': value};
  }
  if (value is! Map) return {};
  return {
    for (final entry in value.entries)
      if ('${entry.value}'.trim().isNotEmpty)
        '${entry.key}': '${entry.value}',
  };
}

String localizedText(Map<String, String> values, String languageCode) {
  final code = languageCode.trim().toLowerCase();
  final direct = values[code];
  if (direct != null && direct.trim().isNotEmpty) return direct;
  final english = values['en'];
  if (english != null && english.trim().isNotEmpty) return english;
  for (final value in values.values) {
    if (value.trim().isNotEmpty) return value;
  }
  return '';
}
