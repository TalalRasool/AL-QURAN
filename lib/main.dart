import 'dart:io';

import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:get/get.dart';
import 'package:just_audio_background/just_audio_background.dart';
import 'package:supabase_flutter/supabase_flutter.dart';

import 'core/controllers/settings_controller.dart';
import 'core/routes/app_pages.dart';
import 'core/routes/app_routes.dart';
import 'core/services/app_services.dart';
import 'core/services/auth_service.dart';
import 'core/services/storage_service.dart';
import 'core/theme/app_theme.dart';
import 'features/hadith/data/hadith_db_helper.dart';
import 'screens/startup/startup_failure_screen.dart';
import 'services/database_helper.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await _initBackgroundAudio();

  SystemChrome.setSystemUIOverlayStyle(
    const SystemUiOverlayStyle(
      statusBarColor: Colors.transparent,
      statusBarIconBrightness: Brightness.dark,
      statusBarBrightness: Brightness.light,
    ),
  );

  await Supabase.initialize(
    url: 'https://rzsepwsdieiskibxsilg.supabase.co',
    publishableKey: 'sb_publishable_ygaNLXG1Cl_CJY_jm34-1w_GPjAIxRr',
  );

  await initAppServices();
  Get.find<AuthService>().attach();

  runApp(const AlQuranApp());
}

Future<void> _initBackgroundAudio() async {
  if (kIsWeb || (!Platform.isAndroid && !Platform.isIOS)) return;
  await JustAudioBackground.init(
    androidNotificationChannelId: 'com.example.alquran.channel.audio',
    androidNotificationChannelName: 'Quran recitation',
    androidNotificationChannelDescription: 'Plays surah recitation in the background.',
    androidNotificationOngoing: true,
  );
}

class AlQuranApp extends StatefulWidget {
  const AlQuranApp({super.key});

  @override
  State<AlQuranApp> createState() => _AlQuranAppState();
}

class _AlQuranAppState extends State<AlQuranApp> {
  var _retrying = false;

  String? get _databaseFailure {
    final messages = <String>[
      if (Get.isRegistered<DatabaseHelper>())
        ?Get.find<DatabaseHelper>().initError,
      if (Get.isRegistered<HadithDbHelper>())
        ?Get.find<HadithDbHelper>().initError,
    ];
    if (messages.isEmpty) return null;
    return messages.join('\n\n');
  }

  Future<void> _retryDatabases() async {
    setState(() => _retrying = true);
    await DatabaseHelper.instance.init();
    await HadithDbHelper.instance.init();
    if (mounted) setState(() => _retrying = false);
  }

  @override
  Widget build(BuildContext context) {
    final failure = _databaseFailure;
    if (failure != null) {
      return MaterialApp(
        debugShowCheckedModeBanner: false,
        home: StartupFailureScreen(
          message: failure,
          isRetrying: _retrying,
          onRetry: _retryDatabases,
        ),
      );
    }

    return ScreenUtilInit(
      designSize: const Size(390, 844),
      minTextAdapt: true,
      splitScreenMode: true,
      builder: (context, child) {
        final settings = Get.find<SettingsController>();
        return GetMaterialApp(
          debugShowCheckedModeBanner: false,
          title: 'AL QURAN',
          theme: AppTheme.light,
          darkTheme: AppTheme.dark,
          themeMode: settings.themeMode,
          initialRoute: Get.find<StorageService>().hasCompletedOnboarding.value
              ? AppRoutes.home
              : AppRoutes.onboarding,
          getPages: AppPages.pages,
          defaultTransition: Transition.cupertino,
        );
      },
    );
  }
}
