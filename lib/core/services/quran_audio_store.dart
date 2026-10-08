import 'dart:io';

import 'package:flutter/services.dart';
import 'package:path/path.dart' as p;
import 'package:path_provider/path_provider.dart';

import '../constants/app_assets.dart';

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
    final cleaned = reciterId.trim().replaceAll(RegExp(r'[^A-Za-z0-9._-]'), '_');
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
