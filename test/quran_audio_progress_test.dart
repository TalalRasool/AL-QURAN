import 'package:alquran/core/services/quran_audio_store.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  test('download progress shows a percentage and megabytes', () {
    expect(QuranAudioStore.percent(0, 0), 0);
    expect(QuranAudioStore.percent(45, 100), 45);
    expect(QuranAudioStore.percentLabel(45), '45%');
    expect(QuranAudioStore.percentLabel(45.6), '46%');
    expect(
      QuranAudioStore.sizeLabelFromBytes(13107200, 26214400),
      '12.5 MB / 25.0 MB',
    );
    expect(
      QuranAudioStore.sizeLabelFromBytes(13107200, 0),
      '12.5 MB',
    );
  });
}
