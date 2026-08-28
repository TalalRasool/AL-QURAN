import '../json_utils.dart';

class Reciter {
  const Reciter({
    required this.identifier,
    required this.name,
    required this.englishName,
    required this.type,
  });

  final String identifier;
  final String name;
  final String englishName;
  final String type;

  String get displayName =>
      englishName.isNotEmpty ? englishName : (name.isNotEmpty ? name : identifier);

  String get subtitle => type.isEmpty ? 'Full Quran' : type;

  factory Reciter.fromJson(Map<String, dynamic> json) {
    return Reciter(
      identifier: json['identifier'] as String? ?? '',
      name: json['name'] as String? ?? '',
      englishName: json['englishName'] as String? ?? '',
      type: json['type'] as String? ?? '',
    );
  }

  static Reciter fromDynamic(dynamic json) =>
      Reciter.fromJson(asStringKeyMap(json));
}
