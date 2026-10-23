import 'dart:io';

import 'package:flutter/services.dart';
import 'package:path/path.dart' as p;
import 'package:path_provider/path_provider.dart';

import '../constants/app_assets.dart';

class LocalSurahAudio {
  const LocalSurahAudio({
    required this.file,
    required this.reciterId,
    required this.surahNumber,
    required this.bytes,
  });

  final File file;
  final String reciterId;
  final int surahNumber;
  final int bytes;

  String get sizeLabel =>
      '${QuranAudioStore.megabytes(bytes).toStringAsFixed(1)} MB';
}

/// Local recitation files and the progress labels shown while they download.
class QuranAudioStore {
  QuranAudioStore._();

  static const _folderName = 'quran_audio';

  static double percent(int received, int total) {
    if (received <= 0 || total <= 0) return 0;
    final value = received / total * 100;
    if (value.isNaN || value.isInfinite) return 0;
    return value.clamp(0, 100).toDouble();
  }

  static double megabytes(int bytes) {
    if (bytes <= 0) return 0;
    return bytes / (1024 * 1024);
  }

  static String percentLabel(double percent) {
    final rounded = percent.round().clamp(0, 100);
    return '$rounded%';
  }

  static String sizeLabelFromBytes(int received, int total) {
    final receivedLabel = megabytes(received).toStringAsFixed(1);
    if (total <= 0) return '$receivedLabel MB';
    final totalLabel = megabytes(total).toStringAsFixed(1);
    return '$receivedLabel MB / $totalLabel MB';
  }

  static String safeReciterId(String reciterId) {
    final cleaned = reciterId.trim().replaceAll(
      RegExp(r'[^A-Za-z0-9._-]'),
      '_',
    );
    return cleaned.isEmpty ? 'reciter' : cleaned;
  }

  static Future<Directory> audioDirectory() async {
    final documents = await getApplicationDocumentsDirectory();
    final directory = Directory(p.join(documents.path, _folderName));
    if (!await directory.exists()) {
      await directory.create(recursive: true);
    }
    return directory;
  }

  static Future<File> surahFile(String reciterId, int surahNumber) async {
    final directory = await audioDirectory();
    final name = '${safeReciterId(reciterId)}/$surahNumber.mp3';
    return File(p.join(directory.path, name));
  }

  static Future<File> ayahFile(String reciterId, int globalAyahNumber) async {
    final directory = await audioDirectory();
    final name = '${safeReciterId(reciterId)}/ayahs/$globalAyahNumber.mp3';
    return File(p.join(directory.path, name));
  }

  /// Saved surah recitations, one file per reciter and surah number.
  static Future<List<LocalSurahAudio>> listSurahFiles() async {
    final directory = await audioDirectory();
    if (!await directory.exists()) return const [];
    final files = <LocalSurahAudio>[];
    await for (final reciterDir in directory.list(followLinks: false)) {
      if (reciterDir is! Directory) continue;
      final reciterId = p.basename(reciterDir.path);
      await for (final entity in reciterDir.list(followLinks: false)) {
        if (entity is! File) continue;
        final name = p.basename(entity.path);
        if (!name.toLowerCase().endsWith('.mp3')) continue;
        final surahNumber = int.tryParse(p.basenameWithoutExtension(name));
        if (surahNumber == null || surahNumber < 1 || surahNumber > 114) {
          continue;
        }
        final bytes = await entity.length();
        if (bytes <= 1024) continue;
        files.add(
          LocalSurahAudio(
            file: entity,
            reciterId: reciterId,
            surahNumber: surahNumber,
            bytes: bytes,
          ),
        );
      }
    }
    files.sort((a, b) {
      final bySurah = a.surahNumber.compareTo(b.surahNumber);
      if (bySurah != 0) return bySurah;
      return a.reciterId.compareTo(b.reciterId);
    });
    return files;
  }

  static Future<bool> isComplete(File file) async {
    if (!await file.exists()) return false;
    return await file.length() > 1024;
  }

  /// Copies the app icon once so the lock screen can show it as artwork.
  static Future<Uri?> artworkUri() async {
    try {
      final directory = await audioDirectory();
      final file = File(p.join(directory.path, 'artwork.png'));
      if (!await file.exists() || await file.length() < 32) {
        final data = await rootBundle.load(AppAssets.appLogo);
        await file.writeAsBytes(
          data.buffer.asUint8List(data.offsetInBytes, data.lengthInBytes),
          flush: true,
        );
      }
      return Uri.file(file.path);
    } catch (_) {
      return null;
    }
  }
}
