/// Centralized paths for images and SVG icons.
/// Filenames must match files under [assets/images] and [assets/icons].
class AppAssets {
  AppAssets._();

  static const String _images = 'assets/images';
  static const String _icons = 'assets/icons';
  static const String _data = 'assets/data';

  // ── Images (assets/images/) ────────────────────────────────────────

  static const String quranOnRehal = '$_images/quran_on_rehal.png';
  static const String mosqueSilhouette = '$_images/mosque_silhouette.png';
  static const String avatarPlaceholder = '$_images/avatar_placeholder.png';

  // ── Navigation icons ───────────────────────────────────────────────

  static const String homeIcon = '$_icons/home.svg';
  static const String quranIcon = '$_icons/quran.svg';
  static const String audioIcon = '$_icons/audio.svg';
  static const String qiblaCompass = '$_icons/qibla_compass.svg';
  static const String profileIcon = '$_icons/profile.svg';

  // ── Utility icons ──────────────────────────────────────────────────

  static const String searchIcon = '$_icons/search.svg';
  static const String bookmarkIcon = '$_icons/bookmark.svg';
  static const String settingsIcon = '$_icons/settings.svg';
  static const String tasbihIcon = '$_icons/tasbih.svg';
  static const String notificationIcon = '$_icons/notification.svg';
  static const String juzIcon = '$_icons/juz.svg';
  static const String lastReadIcon = '$_icons/last_read.svg';

  static const String quranArabicJson = '$_data/arabic.json';
  static const String quranEnglishJson = '$_data/english.json';
  static const String quranUrduJson = '$_data/urdu.json';
  static const String quranHindiJson = '$_data/hindi.json';
  static const String quranIndonesianJson = '$_data/indonesian.json';
  static const String quranBengaliJson = '$_data/bengali.json';

  static const String azkarJson = 'assets/json/azkar.json';
  static const String duasJson = 'assets/json/duas.json';
  static const String seerahJson = 'assets/json/seerah.json';
  static const String sahabaJson = 'assets/json/sahaba.json';
  static const String ghazawatJson = 'assets/json/ghazawat.json';
}
