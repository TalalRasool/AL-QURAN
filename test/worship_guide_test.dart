import 'dart:convert';

import 'package:alquran/core/constants/app_assets.dart';
import 'package:alquran/core/data/json_utils.dart';
import 'package:alquran/features/worship/worship_guide_model.dart';
import 'package:alquran/features/worship/worship_l10n.dart';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  test('empty translations fall back to English', () {
    final item = WorshipGuideItem.fromJson({
      'id': 'zakat.basic',
      'category_id': 'zakat',
      'content': {
        'en': {
          'title': 'Basic zakat',
          'summary': 'Give the due share.',
          'steps': ['Calculate nisab.'],
          'common_problems': ['Do not delay without cause.'],
        },
        'ur': {
          'title': '',
          'summary': '   ',
          'steps': [],
          'common_problems': [''],
        },
      },
    }, index: 3);

    expect(item.id, 4);
    expect(item.category, 'zakat');
    expect(item.titleFor('ur'), 'Basic zakat');
    expect(item.summaryFor('ur'), 'Give the due share.');
    expect(item.stepsFor('ur'), ['Calculate nisab.']);
    expect(item.problemsFor('ur'), ['Do not delay without cause.']);
    expect(WorshipL10n.direction('ur'), TextDirection.rtl);
    expect(WorshipL10n.direction('fa'), TextDirection.rtl);
    expect(WorshipL10n.direction('en'), TextDirection.ltr);
    expect(WorshipL10n.direction('hi'), TextDirection.ltr);
    expect(WorshipL10n.direction('bn'), TextDirection.ltr);
    expect(WorshipL10n.direction('id'), TextDirection.ltr);
  });

  test('bundled guide keeps Namaz separate from Hajj and Zakat', () async {
    final raw = await rootBundle.loadString(AppAssets.worshipGuideJson);
    final dataset = WorshipDataset.fromJson(asStringKeyMap(jsonDecode(raw)));
    final grouped = dataset.guidesByCategory;

    expect(grouped['salah'], isNotEmpty);
    expect(grouped['hajj'], isNotEmpty);
    expect(grouped['zakat'], isNotEmpty);
    expect(grouped['fasting'], isNotEmpty);
    expect(grouped['salah']!.every((item) => item.category == 'salah'), isTrue);
    expect(grouped['hajj']!.every((item) => item.category == 'hajj'), isTrue);

    final namaz = grouped['salah']!.first;
    expect(namaz.id, isPositive);
    expect(namaz.titleFor('ur'), isNotEmpty);
    expect(namaz.titleFor('fa'), isNotEmpty);
    expect(namaz.stepsFor('bn'), isNotEmpty);
    expect(namaz.detailedStepsFor('en'), isNotEmpty);
    expect(namaz.preparationFor('ur'), isNotEmpty);
    expect(namaz.scopeNoteFor('fa'), isNotEmpty);
    expect(
      AppAssets.worshipGuideJson,
      'assets/worship_guide/alquran_islamic_worship_guide_6_languages_detailed.json',
    );
    expect(WorshipL10n.categoryName('salah', 'ur'), 'نماز');
    expect(WorshipL10n.categoryName('hajj', 'en'), 'Hajj');
  });
}
