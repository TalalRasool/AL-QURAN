import 'package:get/get.dart';
import 'package:get_storage/get_storage.dart';

import '../../features/hadith/data/hadith_db_helper.dart';
import '../../services/database_helper.dart';
import '../controllers/bookmark_controller.dart';
import '../controllers/prayer_notification_controller.dart';
import '../controllers/settings_controller.dart';
import '../data/quran_repository.dart';
import '../data/repositories/api_quran_repository_impl.dart';
import 'audio_service.dart';
import 'auth_service.dart';
import 'storage_service.dart';
import 'sync_service.dart';

Future<void> initAppServices() async {
  await GetStorage.init();

  if (!Get.isRegistered<StorageService>()) {
    await Get.putAsync<StorageService>(
      () => StorageService().init(),
      permanent: true,
    );
  }

  if (!Get.isRegistered<SettingsController>()) {
    await Get.putAsync<SettingsController>(
      () => SettingsController().init(),
      permanent: true,
    );
  }

  if (!Get.isRegistered<QuranRepository>()) {
    Get.put<QuranRepository>(ApiQuranRepositoryImpl(), permanent: true);
  }

  if (!Get.isRegistered<HadithDbHelper>()) {
    await Get.putAsync<HadithDbHelper>(
      () => HadithDbHelper.instance.init(),
      permanent: true,
    );
  }

  if (!Get.isRegistered<DatabaseHelper>()) {
    await Get.putAsync<DatabaseHelper>(
      () => DatabaseHelper.instance.init(),
      permanent: true,
    );
  }

  if (!Get.isRegistered<BookmarkController>()) {
    await Get.putAsync<BookmarkController>(
      () => BookmarkController().init(),
      permanent: true,
    );
  }

  if (!Get.isRegistered<PrayerNotificationController>()) {
    await Get.putAsync<PrayerNotificationController>(
      () => PrayerNotificationController().init(),
      permanent: true,
    );
  }

  if (!Get.isRegistered<AudioService>()) {
    await Get.putAsync<AudioService>(
      () => AudioService().init(),
      permanent: true,
    );
  }

  if (!Get.isRegistered<AuthService>()) {
    await Get.putAsync<AuthService>(
      () => AuthService().init(),
      permanent: true,
    );
  }

  if (!Get.isRegistered<SyncService>()) {
    await Get.putAsync<SyncService>(
      () => SyncService().init(),
      permanent: true,
    );
  }
}
