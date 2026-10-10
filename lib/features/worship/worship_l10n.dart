import 'package:flutter/material.dart';

import '../../core/data/json_utils.dart';
import '../../screens/study/study_models.dart';

/// Display copy for the worship guide, keyed by the app language code.
class WorshipL10n {
  WorshipL10n._();

  static const homeTitle = <String, String>{
    'en': 'Worship Guide',
    'ur': 'طریقہ عبادات',
    'hi': 'इबादत गाइड',
    'bn': 'ইবাদত গাইড',
    'id': 'Panduan Ibadah',
    'fa': 'راهنمای عبادت',
  };

  static const intro = <String, String>{
    'en': 'A clear Hanafi outline of worship, grouped by topic.',
    'ur': 'عبادات کا حنفی خلاصہ، موضوع کے لحاظ سے۔',
    'hi': 'इबादत की हनफ़ी रूपरेखा, विषय के अनुसार।',
    'bn': 'ইবাদতের হানাফি সংক্ষিপ্তসার, বিষয় অনুসারে।',
    'id': 'Ringkasan ibadah Hanafi, dikelompokkan menurut topik.',
    'fa': 'خلاصه حنفی عبادات، به تفکیک موضوع.',
  };

  static const topics = <String, String>{
    'en': 'topics',
    'ur': 'موضوعات',
    'hi': 'विषय',
    'bn': 'বিষয়',
    'id': 'topik',
    'fa': 'موضوع',
  };

  static const summary = <String, String>{
    'en': 'Summary',
    'ur': 'خلاصہ',
    'hi': 'सारांश',
    'bn': 'সারাংশ',
    'id': 'Ringkasan',
    'fa': 'خلاصه',
  };

  static const steps = <String, String>{
    'en': 'Steps',
    'ur': 'طریقہ',
    'hi': 'चरण',
    'bn': 'ধাপ',
    'id': 'Langkah',
    'fa': 'مراحل',
  };

  static const problems = <String, String>{
    'en': 'Common mistakes',
    'ur': 'عام غلطیاں',
    'hi': 'आम गलतियाँ',
    'bn': 'সাধারণ ভুল',
    'id': 'Kesalahan umum',
    'fa': 'اشتباه‌های رایج',
  };

  static const references = <String, String>{
    'en': 'References',
    'ur': 'حوالہ جات',
    'hi': 'संदर्भ',
    'bn': 'তথ্যসূত্র',
    'id': 'Referensi',
    'fa': 'منابع',
  };

  static const disclaimer = <String, String>{
    'en': 'Educational draft. Confirm details with a qualified scholar.',
    'ur': 'یہ تعلیمی مسودہ ہے۔ تفصیل کسی مستند عالم سے ضرور پوچھیں۔',
    'hi': 'यह शैक्षिक मसौदा है। विवरण किसी योग्य आलिम से पुष्टि करें।',
    'bn':
        'এটি শিক্ষামূলক খসড়া। বিস্তারিত একজন নির্ভরযোগ্য আলেমের কাছে নিশ্চিত করুন।',
    'id': 'Draf edukasi. Konfirmasikan rinciannya kepada ulama yang tepercaya.',
    'fa': 'این پیش‌نویس آموزشی است. جزئیات را از عالم معتبر بپرسید.',
  };

  static const loadError = <String, String>{
    'en': 'Unable to load the worship guide.',
    'ur': 'عبادات کا رہنما لوڈ نہیں ہو سکا۔',
    'hi': 'इबादत गाइड लोड नहीं हो सकी।',
    'bn': 'ইবাদত গাইড লোড করা যায়নি।',
    'id': 'Panduan ibadah tidak dapat dimuat.',
    'fa': 'راهنمای عبادت بارگذاری نشد.',
  };

  static const emptyCategory = <String, String>{
    'en': 'No topics in this category yet.',
    'ur': 'اس موضوع میں ابھی کوئی مضمون نہیں۔',
    'hi': 'इस श्रेणी में अभी कोई विषय नहीं है।',
    'bn': 'এই বিভাগে এখনও কোনো বিষয় নেই।',
    'id': 'Belum ada topik dalam kategori ini.',
    'fa': 'هنوز موضوعی در این دسته نیست.',
  };

  static const retry = <String, String>{
    'en': 'Retry',
    'ur': 'دوبارہ کوشش',
    'hi': 'फिर कोशिश करें',
    'bn': 'আবার চেষ্টা',
    'id': 'Coba lagi',
    'fa': 'تلاش دوباره',
  };

  static const categoryLabels = <String, Map<String, String>>{
    'salah': {
      'en': 'Namaz',
      'ur': 'نماز',
      'hi': 'नमाज़',
      'bn': 'নামাজ',
      'id': 'Salat',
      'fa': 'نماز',
    },
    'purification': {
      'en': 'Purification',
      'ur': 'طہارت',
      'hi': 'पवित्रता',
      'bn': 'পবিত্রতা',
      'id': 'Bersuci',
      'fa': 'طهارت',
    },
    'hajj': {
      'en': 'Hajj',
      'ur': 'حج',
      'hi': 'हज',
      'bn': 'হজ',
      'id': 'Haji',
      'fa': 'حج',
    },
    'umrah': {
      'en': 'Umrah',
      'ur': 'عمرہ',
      'hi': 'उमरा',
      'bn': 'উমরাহ',
      'id': 'Umrah',
      'fa': 'عمره',
    },
    'zakat': {
      'en': 'Zakat',
      'ur': 'زکوٰۃ',
      'hi': 'ज़कात',
      'bn': 'যাকাত',
      'id': 'Zakat',
      'fa': 'زکات',
    },
    'fasting': {
      'en': 'Fasting',
      'ur': 'روزہ',
      'hi': 'रोज़ा',
      'bn': 'রোজা',
      'id': 'Puasa',
      'fa': 'روزه',
    },
    'funeral': {
      'en': 'Janazah',
      'ur': 'نمازِ جنازہ',
      'hi': 'जनाज़ा',
      'bn': 'জানাজার নামাজ',
      'id': 'Salat jenazah',
      'fa': 'نماز جنازه',
    },
    'adhkar': {
      'en': 'Adhkar',
      'ur': 'اذکار و دعا',
      'hi': 'ज़िक्र और दुआ',
      'bn': 'জিকির ও দোয়া',
      'id': 'Zikir dan doa',
      'fa': 'ذکر و دعا',
    },
  };

  static String code(String languageCode) =>
      OfflineLanguage.normalize(languageCode);

  /// Urdu and Persian read right to left. English, Hindi, Bengali, and
  /// Indonesian stay left to right.
  static bool isRtl(String languageCode) {
    final value = code(languageCode);
    return value == 'ur' || value == 'fa';
  }

  static TextDirection direction(String languageCode) =>
      isRtl(languageCode) ? TextDirection.rtl : TextDirection.ltr;

  static String text(Map<String, String> values, String languageCode) =>
      localizedText(values, code(languageCode));

  static String categoryName(
    String id,
    String languageCode, {
    String? fallback,
  }) {
    final labels = categoryLabels[id];
    if (labels == null) {
      final english = (fallback ?? id).trim();
      return english.isEmpty ? id : english;
    }
    final resolved = localizedText(labels, code(languageCode));
    if (resolved.isNotEmpty) return resolved;
    final english = (fallback ?? '').trim();
    return english.isEmpty ? id : english;
  }

  static String topicCount(String languageCode, int count) =>
      '$count ${text(topics, languageCode)}';
}
