import 'dart:io';

import 'package:alquran/features/hadith/data/hadith_editions.dart';
import 'package:http/http.dart' as http;

const _baseUrl =
    'https://cdn.jsdelivr.net/gh/fawazahmed0/hadith-api@1/editions';

const _books = <({String slug, String name})>[
  (slug: 'bukhari', name: 'Sahih al-Bukhari'),
  (slug: 'muslim', name: 'Sahih Muslim'),
  (slug: 'abudawud', name: 'Sunan Abu Dawud'),
  (slug: 'tirmidhi', name: 'Jami at-Tirmidhi'),
  (slug: 'nasai', name: "Sunan an-Nasa'i"),
  (slug: 'ibnmajah', name: 'Sunan Ibn Majah'),
];

Future<void> main() async {
  final bundledDir = Directory('assets/json');
  final downloadDir = Directory('tool/hadith_editions');
  if (!downloadDir.existsSync()) {
    await downloadDir.create(recursive: true);
  }

  final total = _books.length * HadithEditions.specs.length;
  var index = 0;
  var failed = false;

  for (final book in _books) {
    for (final spec in HadithEditions.specs) {
      index++;
      final filename = spec.fileName(book.slug);
      final bundled = File('${bundledDir.path}/$filename');
      final target = File('${downloadDir.path}/$filename');
      final prefix = '[$index/$total]';

      if (_usable(bundled)) {
        stdout.writeln('$prefix Using bundled $filename');
        continue;
      }
      if (_usable(target)) {
        stdout.writeln('$prefix Already downloaded $filename');
        continue;
      }

      stdout.writeln('$prefix Downloading ${spec.label} ${book.name}...');
      final url = '$_baseUrl/${spec.editionCode}-${book.slug}.min.json';
      final result = await _getWithRetry(url);
      if (result.missing) {
        final message =
            'No ${spec.label} edition for ${book.name} (${spec.editionCode}-${book.slug}).';
        if (spec.required) {
          stderr.writeln('$prefix $message');
          failed = true;
        } else {
          stdout.writeln(
            '$prefix $message English fallback will be used.',
          );
        }
        continue;
      }
      final response = result.response;
      if (response == null) {
        stderr.writeln('$prefix Failed $filename after retries.');
        failed = true;
        continue;
      }

      await target.writeAsBytes(response.bodyBytes, flush: true);
      stdout.writeln('$prefix Saved tool/hadith_editions/$filename');
    }
  }

  if (failed) {
    stderr.writeln('One or more required Hadith downloads failed.');
    exit(1);
  }

  stdout.writeln('Hadith editions are ready for scripts/generate_hadith_db.dart.');
}

bool _usable(File file) => file.existsSync() && file.lengthSync() > 100;

class _FetchResult {
  const _FetchResult.ok(this.response) : missing = false;
  const _FetchResult.missing() : response = null, missing = true;
  const _FetchResult.failed() : response = null, missing = false;

  final http.Response? response;
  final bool missing;
}

Future<_FetchResult> _getWithRetry(String url, {int retries = 4}) async {
  for (var attempt = 1; attempt <= retries; attempt++) {
    try {
      final response = await http
          .get(Uri.parse(url))
          .timeout(const Duration(seconds: 90));
      if (response.statusCode == 200) {
        return _FetchResult.ok(response);
      }
      if (response.statusCode == 404) {
        return const _FetchResult.missing();
      }
      stderr.writeln(
        'HTTP ${response.statusCode} (attempt $attempt/$retries)',
      );
    } catch (error) {
      stderr.writeln('Error (attempt $attempt/$retries): $error');
    }
    if (attempt < retries) {
      final wait = Duration(seconds: attempt * 2);
      stdout.writeln('Retrying in ${wait.inSeconds}s...');
      await Future<void>.delayed(wait);
    }
  }
  return const _FetchResult.failed();
}
