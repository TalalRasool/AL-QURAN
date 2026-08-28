import 'package:get/get.dart';
import 'package:get_storage/get_storage.dart';

import '../data/quran_repository.dart';
import '../data/repositories/api_quran_repository_impl.dart';
import 'audio_service.dart';
import 'auth_service.dart';
import 'storage_service.dart';
import 'sync_service.dart';
import '../controllers/settings_controller.dart';

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
