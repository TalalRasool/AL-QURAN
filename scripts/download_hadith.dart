import 'dart:convert';
import 'dart:io';

import 'package:http/http.dart' as http;

const _baseUrl =
    'https://raw.githubusercontent.com/fawazahmed0/hadith-api/1/editions';

const _books = <({String slug, String name})>[
  (slug: 'bukhari', name: 'Sahih al-Bukhari'),
  (slug: 'muslim', name: 'Sahih Muslim'),
  (slug: 'abudawud', name: 'Sunan Abu Dawud'),
  (slug: 'tirmidhi', name: 'Jami at-Tirmidhi'),
  (slug: 'nasai', name: "Sunan an-Nasa'i"),
  (slug: 'ibnmajah', name: 'Sunan Ibn Majah'),
];

const _languages = <({String code, String label})>[
  (code: 'ara', label: 'Arabic'),
  (code: 'eng', label: 'English'),
  (code: 'urd', label: 'Urdu'),
];

Future<void> main() async {
  final directory = Directory('assets/json');
  if (!directory.existsSync()) {
    stdout.writeln('Creating assets/json/ ...');
    await directory.create(recursive: true);
  }

  final total = _books.length * _languages.length;
  var index = 0;
  var failed = false;

  for (final book in _books) {
    for (final language in _languages) {
      index++;
      final filename = '${language.code}-${book.slug}.json';
      stdout.writeln(
        '[$index/$total] Downloading ${language.label} ${book.name}...',
      );

      final url = '$_baseUrl/$filename';
      final response = await _getWithRetry(url);
      if (response == null) {
        stderr.writeln('Failed $filename after retries.');
        failed = true;
        continue;
      }

      final file = File('${directory.path}/$filename');
      await file.writeAsString(
        utf8.decode(response.bodyBytes),
        encoding: utf8,
      );
      stdout.writeln('Saved $filename successfully!');
    }
  }

  if (failed) {
    stderr.writeln('One or more Hadith downloads failed.');
    exit(1);
  }

  stdout.writeln('All Sihah Sittah JSON files saved in assets/json/.');
}

Future<http.Response?> _getWithRetry(String url, {int retries = 4}) async {
  for (var attempt = 1; attempt <= retries; attempt++) {
    try {
      final response = await http.get(Uri.parse(url));
      if (response.statusCode == 200) return response;
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
  return null;
}
