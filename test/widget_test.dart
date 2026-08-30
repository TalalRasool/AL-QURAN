import 'dart:io';

import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:get/get.dart';

import 'package:alquran/core/services/app_services.dart';
import 'package:alquran/core/services/storage_service.dart';
import 'package:alquran/main.dart';

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  setUp(() async {
    TestDefaultBinaryMessengerBinding.instance.defaultBinaryMessenger
        .setMockMethodCallHandler(
      const MethodChannel('plugins.flutter.io/path_provider'),
      (call) async {
        if (call.method == 'getApplicationDocumentsDirectory') {
          return Directory.systemTemp.path;
        }
        return null;
      },
    );
    await initAppServices();
    await Get.find<StorageService>().saveProfile(
      name: 'M Talal',
      country: 'Pakistan',
    );
    await Get.find<StorageService>().completeOnboarding();
  });

  tearDown(() => Get.reset());

  testWidgets('app boots into the home screen', (WidgetTester tester) async {
    tester.view.physicalSize = const Size(390, 844);
    tester.view.devicePixelRatio = 1.0;
    addTearDown(tester.view.resetPhysicalSize);
    addTearDown(tester.view.resetDevicePixelRatio);

    await tester.pumpWidget(const AlQuranApp());
    await tester.pump();

    expect(find.byType(GetMaterialApp), findsOneWidget);
    expect(find.text('Assalamu Alaikum'), findsOneWidget);
    expect(find.text('Continue Reading'), findsOneWidget);
  });
}
