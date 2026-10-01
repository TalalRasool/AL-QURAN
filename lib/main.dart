import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:get/get.dart';
import 'package:supabase_flutter/supabase_flutter.dart';

import 'core/controllers/settings_controller.dart';
import 'core/routes/app_pages.dart';
import 'core/routes/app_routes.dart';
import 'core/services/app_services.dart';
import 'core/services/auth_service.dart';
import 'core/services/storage_service.dart';
import 'core/theme/app_theme.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();

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

class AlQuranApp extends StatelessWidget {
  const AlQuranApp({super.key});

  @override
  Widget build(BuildContext context) {
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
