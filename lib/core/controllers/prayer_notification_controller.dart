import 'dart:async';

import 'package:adhan/adhan.dart';
import 'package:flutter/material.dart';
import 'package:flutter_local_notifications/flutter_local_notifications.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:geolocator/geolocator.dart';
import 'package:get/get.dart';
import 'package:timezone/data/latest_all.dart' as tzdata;
import 'package:timezone/timezone.dart' as tz;

import '../constants/app_colors.dart';
import '../constants/app_text_styles.dart';
import '../services/storage_service.dart';

class PrayerNotificationController extends GetxService {
  static const _channelId = 'prayer_times';
  static const _channelName = 'Prayer Times';
  static const _channelDescription =
      'Reminders 15 minutes before each prayer';
  static const _advance = Duration(minutes: 15);
  static const _todayIds = [1, 2, 3, 4, 5];
  static const _tomorrowIds = [6, 7, 8, 9, 10];

  final FlutterLocalNotificationsPlugin _plugin =
      FlutterLocalNotificationsPlugin();
  final StorageService _storage = Get.find<StorageService>();

  final isBusy = false.obs;
  var _initialized = false;
  var _timeZoneReady = false;

  RxBool get isEnabled => _storage.prayerNotificationsEnabled;

  Future<PrayerNotificationController> init() async {
    try {
      _configureLocalTimeZone();
      await _ensureNotificationsInitialized();
      if (isEnabled.value) {
        unawaited(_rescheduleFromSavedLocation());
      }
    } catch (_) {}
    return this;
  }

  Future<void> requestLocationAndEnableNotifications() async {
    if (isBusy.value) return;
    isBusy.value = true;
    try {
      await _ensureNotificationsInitialized();
      if (!await _requestNotificationPermissions()) {
        await disableNotifications(silent: true);
        _showMessage(
          'Notifications',
          'Notification permission is required to remind you before Salah.',
        );
        return;
      }

      final position = await _requestLocation();
      if (position == null) return;

      await _storage.savePrayerCoordinates(
        latitude: position.latitude,
        longitude: position.longitude,
      );

      final coordinates = Coordinates(position.latitude, position.longitude);
      await _scheduleForCoordinates(coordinates);
      await _storage.savePrayerNotificationsEnabled(true);
      _showMessage(
        'Prayer notifications',
        'You will be reminded 15 minutes before each prayer.',
      );
    } catch (_) {
      await disableNotifications(silent: true);
      _showMessage(
        'Prayer notifications',
        'Unable to enable prayer notifications right now.',
      );
    } finally {
      isBusy.value = false;
    }
  }

  Future<void> disableNotifications({bool silent = false}) async {
    try {
      await _cancelPrayerNotifications();
    } catch (_) {}
    await _storage.savePrayerNotificationsEnabled(false);
    if (!silent) {
      _showMessage(
        'Prayer notifications',
        'Prayer reminders have been turned off.',
      );
    }
  }

  Future<void> schedulePrayerNotifications(PrayerTimes prayerTimes) async {
    await _ensureNotificationsInitialized();
    final ids = _idsFor(prayerTimes);
    final prayerDay = _prayerDay(prayerTimes);
    final now = DateTime.now();
    final isToday = prayerDay.year == now.year &&
        prayerDay.month == now.month &&
        prayerDay.day == now.day;
    final isJummah = (isToday ? now : prayerDay).weekday == DateTime.friday;

    await _scheduleOne(
      id: ids[0],
      time: prayerTimes.fajr,
      title: 'Fajr · فجر',
      body:
          'Fajr time is approaching in 15 minutes. Prepare for Salah.\n'
          'فجر کی اذان 15 منٹ میں ہے۔ وضو کریں اور نماز کی تیاری کریں۔',
    );

    if (isJummah) {
      await _scheduleOne(
        id: ids[1],
        time: prayerTimes.dhuhr,
        title: 'Jummah · جمعہ المبارک',
        body:
            'Today is Jummah! Prepare for Jummah prayer and don\'t forget to read Surah Al-Kahf.\n'
            'آج جمعہ مبارک ہے! جمعہ کی نماز کی تیاری کریں اور سورة الکہف پڑھنا نہ بھولیں۔',
      );
    } else {
      await _scheduleOne(
        id: ids[1],
        time: prayerTimes.dhuhr,
        title: 'Dhuhr · ظہر',
        body:
            'Dhuhr time is approaching in 15 minutes. Prepare for Salah.\n'
            'ظہر کی اذان 15 منٹ میں ہے۔ نماز کی تیاری کریں۔',
      );
    }

    await _scheduleOne(
      id: ids[2],
      time: prayerTimes.asr,
      title: 'Asr · عصر',
      body:
          'Asr time is approaching in 15 minutes. Prepare for Salah.\n'
          'عصر کی اذان 15 منٹ میں ہے۔ نماز کی تیاری کریں۔',
    );
    await _scheduleOne(
      id: ids[3],
      time: prayerTimes.maghrib,
      title: 'Maghrib · مغرب',
      body:
          'Maghrib time is approaching in 15 minutes. Prepare for Salah.\n'
          'مغرب کی اذان 15 منٹ میں ہے۔ نماز کی تیاری کریں۔',
    );
    await _scheduleOne(
      id: ids[4],
      time: prayerTimes.isha,
      title: 'Isha · عشاء',
      body:
          'Isha time is approaching in 15 minutes. Prepare for Salah.\n'
          'عشاء کی اذان 15 منٹ میں ہے۔ نماز کی تیاری کریں۔',
    );
  }

  Future<void> _scheduleForCoordinates(Coordinates coordinates) async {
    await _cancelPrayerNotifications();
    final params = _calculationParameters();
    final today = PrayerTimes.today(coordinates, params);
    final tomorrowDate = DateTime.now().add(const Duration(days: 1));
    final tomorrow = PrayerTimes(
      coordinates,
      DateComponents(
        tomorrowDate.year,
        tomorrowDate.month,
        tomorrowDate.day,
      ),
      params,
    );
    await schedulePrayerNotifications(today);
    await schedulePrayerNotifications(tomorrow);
  }

  Future<void> _rescheduleFromSavedLocation() async {
    final latitude = _storage.prayerLatitude.value;
    final longitude = _storage.prayerLongitude.value;
    if (latitude == null || longitude == null) return;
    try {
      await _ensureNotificationsInitialized();
      await _scheduleForCoordinates(Coordinates(latitude, longitude));
    } catch (_) {}
  }

  CalculationParameters _calculationParameters() {
    final params = CalculationMethod.karachi.getParameters();
    params.madhab = Madhab.hanafi;
    return params;
  }

  Future<Position?> _requestLocation() async {
    final serviceEnabled = await Geolocator.isLocationServiceEnabled();
    if (!serviceEnabled) {
      _showMessage(
        'Location',
        'Turn on location services so prayer times can be calculated for your area.',
      );
      await Geolocator.openLocationSettings();
      await disableNotifications(silent: true);
      return null;
    }

    var permission = await Geolocator.checkPermission();
    if (permission == LocationPermission.denied) {
      permission = await Geolocator.requestPermission();
    }

    if (permission == LocationPermission.denied) {
      await disableNotifications(silent: true);
      _showMessage(
        'Location',
        'Location permission is needed to calculate prayer times.',
      );
      return null;
    }

    if (permission == LocationPermission.deniedForever) {
      await disableNotifications(silent: true);
      _showMessage(
        'Location',
        'Location is blocked. Enable it in Settings to receive prayer reminders.',
      );
      await Geolocator.openAppSettings();
      return null;
    }

    try {
      return await Geolocator.getCurrentPosition(
        locationSettings: const LocationSettings(
          accuracy: LocationAccuracy.medium,
          timeLimit: Duration(seconds: 20),
        ),
      );
    } catch (_) {
      final last = await Geolocator.getLastKnownPosition();
      if (last != null) return last;
      await disableNotifications(silent: true);
      _showMessage(
        'Location',
        'Could not read your current location. Please try again.',
      );
      return null;
    }
  }

  Future<bool> _requestNotificationPermissions() async {
    final android = _plugin
        .resolvePlatformSpecificImplementation<
            AndroidFlutterLocalNotificationsPlugin>();
    if (android != null) {
      final allowed = await android.requestNotificationsPermission();
      await android.requestExactAlarmsPermission();
      if (allowed == false) return false;
    }

    final ios = _plugin
        .resolvePlatformSpecificImplementation<
            IOSFlutterLocalNotificationsPlugin>();
    if (ios != null) {
      final allowed = await ios.requestPermissions(
        alert: true,
        badge: true,
        sound: true,
      );
      if (allowed == false) return false;
    }

    final mac = _plugin
        .resolvePlatformSpecificImplementation<
            MacOSFlutterLocalNotificationsPlugin>();
    if (mac != null) {
      final allowed = await mac.requestPermissions(
        alert: true,
        badge: true,
        sound: true,
      );
      if (allowed == false) return false;
    }

    return true;
  }

  Future<void> _scheduleOne({
    required int id,
    required DateTime time,
    required String title,
    required String body,
  }) async {
    final scheduled = _toTz(time).subtract(_advance);
    if (!scheduled.isAfter(tz.TZDateTime.now(tz.local))) return;

    const details = NotificationDetails(
      android: AndroidNotificationDetails(
        _channelId,
        _channelName,
        channelDescription: _channelDescription,
        importance: Importance.high,
        priority: Priority.high,
        playSound: true,
        icon: '@mipmap/launcher_icon',
      ),
      iOS: DarwinNotificationDetails(
        presentAlert: true,
        presentBadge: true,
        presentSound: true,
      ),
      macOS: DarwinNotificationDetails(
        presentAlert: true,
        presentBadge: true,
        presentSound: true,
      ),
    );

    await _plugin.zonedSchedule(
      id,
      title,
      body,
      scheduled,
      details,
      androidScheduleMode: AndroidScheduleMode.exactAllowWhileIdle,
    );
  }

  Future<void> _cancelPrayerNotifications() async {
    for (final id in [..._todayIds, ..._tomorrowIds]) {
      await _plugin.cancel(id);
    }
  }

  List<int> _idsFor(PrayerTimes prayerTimes) {
    final day = _prayerDay(prayerTimes);
    final today = DateTime.now();
    final isToday =
        day.year == today.year && day.month == today.month && day.day == today.day;
    return isToday ? _todayIds : _tomorrowIds;
  }

  DateTime _prayerDay(PrayerTimes prayerTimes) {
    final local = prayerTimes.fajr.toLocal();
    return DateTime(local.year, local.month, local.day);
  }

  tz.TZDateTime _toTz(DateTime time) {
    final local = time.isUtc ? time.toLocal() : time;
    return tz.TZDateTime(
      tz.local,
      local.year,
      local.month,
      local.day,
      local.hour,
      local.minute,
      local.second,
    );
  }

  void _configureLocalTimeZone() {
    if (_timeZoneReady) return;
    tzdata.initializeTimeZones();
    final offset = DateTime.now().timeZoneOffset;
    tz.setLocalLocation(_locationForOffset(offset) ?? tz.UTC);
    _timeZoneReady = true;
  }

  tz.Location? _locationForOffset(Duration offset) {
    const preferred = [
      'Asia/Karachi',
      'Asia/Kolkata',
      'Asia/Dhaka',
      'Asia/Riyadh',
      'Asia/Dubai',
      'Asia/Jakarta',
      'Asia/Kuala_Lumpur',
      'Europe/Istanbul',
      'Africa/Cairo',
      'Africa/Lagos',
      'Europe/London',
      'America/New_York',
    ];
    for (final name in preferred) {
      try {
        final location = tz.getLocation(name);
        if (tz.TZDateTime.now(location).timeZoneOffset == offset) {
          return location;
        }
      } catch (_) {}
    }
    for (final location in tz.timeZoneDatabase.locations.values) {
      if (tz.TZDateTime.now(location).timeZoneOffset == offset) {
        return location;
      }
    }
    return null;
  }

  Future<void> _ensureNotificationsInitialized() async {
    if (_initialized) return;
    const android = AndroidInitializationSettings('@mipmap/launcher_icon');
    const darwin = DarwinInitializationSettings(
      requestAlertPermission: false,
      requestBadgePermission: false,
      requestSoundPermission: false,
    );
    const settings = InitializationSettings(
      android: android,
      iOS: darwin,
      macOS: darwin,
    );
    await _plugin.initialize(settings);
    _initialized = true;
  }

  void _showMessage(String title, String message) {
    if (Get.isSnackbarOpen) return;
    Get.snackbar(
      title,
      message,
      snackPosition: SnackPosition.BOTTOM,
      backgroundColor: AppColors.primary,
      colorText: AppColors.white,
      margin: EdgeInsets.fromLTRB(16.w, 0, 16.w, 16.h),
      borderRadius: 12.r,
      titleText: Text(
        title,
        style: AppTextStyles.heading3.copyWith(color: AppColors.white),
      ),
      messageText: Text(
        message,
        style: AppTextStyles.bodySmall.copyWith(color: AppColors.white),
      ),
    );
  }
}
