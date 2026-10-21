import 'package:alquran/core/data/quran_ayah_index.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  test('absolute ayah numbers match the standard Quran order', () {
    expect(QuranAyahIndex.ayahCounts.length, 114);
    expect(QuranAyahIndex.ayahCounts.reduce((a, b) => a + b), 6236);
    expect(QuranAyahIndex.globalNumber(1, 1), 1);
    expect(QuranAyahIndex.globalNumber(1, 7), 7);
    expect(QuranAyahIndex.globalNumber(2, 1), 8);
    expect(QuranAyahIndex.globalNumber(114, 6), 6236);
    expect(QuranAyahIndex.globalNumber(0, 1), 0);
    expect(QuranAyahIndex.globalNumber(1, 8), 0);
  });
}
