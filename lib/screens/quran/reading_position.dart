import '../../core/data/models/last_read.dart';

typedef AyahRef = ({int surahNumber, int ayahNumber});

/// Index of the ayah that should be on screen after a surah or juz loads.
///
/// An explicit ayah wins. Otherwise the saved position is used when it is
/// inside [ayahs]. Mushaf positions are ignored here because those screens
/// resume by page.
int revealIndex(
  List<AyahRef> ayahs, {
  int? preferredSurah,
  int? preferredAyah,
  LastRead? saved,
}) {
  if (ayahs.isEmpty) return 0;
  final preferred = _indexOf(ayahs, preferredSurah, preferredAyah);
  if (preferred != null) return preferred;
  if (saved != null && !saved.isMushaf) {
    final resume = _indexOf(ayahs, saved.surahNumber, saved.ayahNumber);
    if (resume != null) return resume;
  }
  return 0;
}

int? _indexOf(List<AyahRef> ayahs, int? surahNumber, int? ayahNumber) {
  if (surahNumber == null || ayahNumber == null) return null;
  if (surahNumber < 1 || ayahNumber < 1) return null;
  for (var i = 0; i < ayahs.length; i++) {
    final ayah = ayahs[i];
    if (ayah.surahNumber == surahNumber && ayah.ayahNumber == ayahNumber) {
      return i;
    }
  }
  return null;
}
