import 'dart:convert';
import 'dart:io';

import 'package:http/http.dart' as http;

class _Target {
  const _Target({
    required this.filename,
    required this.urls,
    required this.language,
    required this.type,
  });

  final String filename;
  final List<String> urls;
  final String language;
  final String type;
}

const _targets = <_Target>[
  _Target(
    filename: 'arabic.json',
    urls: ['https://api.alquran.cloud/v1/quran/quran-uthmani'],
    language: 'ar',
    type: 'quran',
  ),
  _Target(
    filename: 'english.json',
    urls: ['https://api.alquran.cloud/v1/quran/en.asad'],
    language: 'en',
    type: 'translation',
  ),
  _Target(
    filename: 'urdu.json',
    urls: [
      'https://api.alquran.cloud/v1/quran/ur.jalandhari',
      'https://api.alquran.cloud/v1/quran/ur.jalandhry',
    ],
    language: 'ur',
    type: 'translation',
  ),
  _Target(
    filename: 'hindi.json',
    urls: ['https://api.alquran.cloud/v1/quran/hi.hindi'],
    language: 'hi',
    type: 'translation',
  ),
  _Target(
    filename: 'indonesian.json',
    urls: ['https://api.alquran.cloud/v1/quran/id.indonesian'],
    language: 'id',
    type: 'translation',
  ),
  _Target(
    filename: 'bengali.json',
    urls: ['https://api.alquran.cloud/v1/quran/bn.bengali'],
    language: 'bn',
    type: 'translation',
  ),
];

Future<void> main() async {
  final directory = Directory('assets/data');
  await directory.create(recursive: true);

  var failed = false;
  for (final target in _targets) {
    final saved = await _downloadEdition(target);
    if (!saved) failed = true;
  }

  if (failed) {
    stderr.writeln('One or more downloads failed.');
    exit(1);
  }

  stdout.writeln('All Quran JSON files saved in assets/data/.');
}

Future<bool> _downloadEdition(_Target target) async {
  Object? lastError;
  for (final url in target.urls) {
    stdout.writeln('Downloading ${target.filename} ...');
    stdout.writeln('  $url');
    try {
      final response = await http.get(Uri.parse(url)).timeout(
        const Duration(minutes: 2),
      );
      if (response.statusCode != 200) {
        lastError = 'HTTP ${response.statusCode}';
        stderr.writeln('  Failed: $lastError');
        continue;
      }

      final mismatch = _payloadMismatch(response.body, target);
      if (mismatch != null) {
        lastError = mismatch;
        stderr.writeln('  Rejected: $mismatch');
        continue;
      }

      final path = 'assets/data/${target.filename}';
      await File(path).writeAsBytes(response.bodyBytes);
      stdout.writeln('  Saved $path (${response.bodyBytes.length} bytes)');
      return true;
    } catch (error) {
      lastError = error;
      stderr.writeln('  Failed: $error');
    }
  }

  stderr.writeln(
    'Could not download ${target.filename} (${lastError ?? 'unknown error'}).',
  );
  return false;
}

String? _payloadMismatch(String body, _Target target) {
  try {
    final decoded = jsonDecode(body);
    if (decoded is! Map) return 'Payload is not a JSON object';

    final code = decoded['code'];
    if (code != 200 && '$code' != '200') {
      return 'Unexpected API payload';
    }

    final data = decoded['data'];
    if (data is! Map) return 'Missing data object';

    final surahs = data['surahs'];
    if (surahs is! List || surahs.isEmpty) return 'Missing surahs list';

    final edition = data['edition'];
    if (edition is! Map) return 'Missing edition metadata';

    final language = '${edition['language'] ?? ''}'.toLowerCase();
    final type = '${edition['type'] ?? ''}'.toLowerCase();
    final identifier = '${edition['identifier'] ?? ''}';

    if (language != target.language) {
      return 'Expected language ${target.language}, got $language ($identifier)';
    }
    if (type != target.type) {
      return 'Expected type ${target.type}, got $type ($identifier)';
    }
    return null;
  } catch (error) {
    return 'Invalid JSON ($error)';
  }
}
