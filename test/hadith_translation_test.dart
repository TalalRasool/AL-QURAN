import 'package:alquran/features/hadith/data/hadith_editions.dart';
import 'package:alquran/features/hadith/data/hadith_models.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  const hadith = Hadith(
    id: 1,
    bookId: 1,
    chapterId: 1,
    hadithNumber: 1,
    textAr: 'عربي',
    translations: {
      'en': 'English text',
      'ur': 'اردو',
      'hi': '',
      'bn': 'বাংলা',
      'id': 'Teks Indonesia',
      'fa': '   ',
    },
  );

  test('maps app languages onto fawazahmed0 edition prefixes', () {
    expect(
      {
        for (final spec in HadithEditions.specs) spec.appCode: spec.editionCode,
      },
      {
        'ar': 'ara',
        'en': 'eng',
        'ur': 'urd',
        'hi': 'hin',
        'bn': 'ben',
        'id': 'ind',
        'fa': 'fas',
      },
    );
  });

  test('returns the selected translation when that edition has text', () {
    expect(hadith.textFor('bn'), 'বাংলা');
    expect(hadith.resolvedLanguage('bn'), 'bn');
    expect(hadith.textFor('ur'), 'اردو');
    expect(hadith.resolvedLanguage('id'), 'id');
    expect(hadith.textFor('en'), 'English text');
  });

  test('falls back to English when the edition is missing or blank', () {
    expect(hadith.textFor('hi'), 'English text');
    expect(hadith.resolvedLanguage('hi'), 'en');
    expect(hadith.textFor('fa'), 'English text');
    expect(hadith.resolvedLanguage('fa'), 'en');
    expect(hadith.textFor('xx'), 'English text');
  });
}
