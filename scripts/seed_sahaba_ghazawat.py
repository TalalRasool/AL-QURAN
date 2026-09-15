# -*- coding: utf-8 -*-
"""Seed localized Sahaba and Ghazawat JSON (en, ur, hi, bn, id)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "json"


def L(en, ur, hi, bn, idn):
    return {"en": en, "ur": ur, "hi": hi, "bn": bn, "id": idn}


def item(title, heading, details):
    return {"title": title, "heading": heading, "details": details}


def chapter(chapter_id, title, heading, details, items):
    return {
        "chapter_id": chapter_id,
        "title": title,
        "heading": heading,
        "details": details,
        "items": items,
    }


SAHABA = [
    chapter(
        1,
        L("Abu Bakr as-Siddiq", "ابو بکر صدیق", "अबू बक्र सिद्दीक", "আবু বকর সিদ্দিক", "Abu Bakar ash-Shiddiq"),
        L("The first caliph", "پہلے خلیفہ", "पहले खलीफा", "প্রথম খলিফা", "Khalifah pertama"),
        L(
            "Abu Bakr Abdullah ibn Abi Quhafa, from Banu Taym of Quraysh, was the closest friend of the Prophet ﷺ and the first adult free man to accept Islam. He was called as-Siddiq for immediately affirming the Isra' and Mi'raj. He spent his wealth to free slaves such as Bilal, accompanied the Prophet ﷺ in the Hijrah, and was appointed to lead the prayer in the Prophet's final illness. After the Wafat he was chosen as the first khalifah. He fought the apostasy (Riddah), compiled the Quran into a single collection, and died in 13 AH (634 CE). He is buried beside the Prophet ﷺ.",
            "ابو بکر عبد اللہ بن ابی قحافہ، قریش کے بنو تیم سے، نبی ﷺ کے سب سے قریبی دوست اور پہلے بالغ آزاد مرد تھے جنہوں نے اسلام قبول کیا۔ اسراء و معراج کی تصدیق پر صدیق کہلائے۔ اپنا مال غلام آزاد کرنے پر خرچا، ہجرت میں ساتھ رہے، آخری بیماری میں امامت کے لیے مقرر ہوئے۔ وفات کے بعد پہلے خلیفہ منتخب ہوئے۔ مرتدین سے جنگ کی، قرآن کو ایک مصحف میں جمع کیا، 13ھ (634ء) میں فوت ہوئے اور نبی ﷺ کے پہلو میں دفن ہیں۔",
            "अबू बक्र कुरैश के बनू तैम से, नबी ﷺ के सबसे करीबी दोस्त और पहले बालिग आज़ाद मर्द थे जिन्होंने इस्लाम क़ुबूल किया। हिजरत में साथ रहे, आख़िरी मर्ज़ में इमामत दी गई। विसाल के बाद पहले खलीफा चुने गए। रिद्दा से जंग की, कुरआन को एक मुसहफ़ में जमा किया, 13 हिजरी में वफ़ात, नबी ﷺ के पहलू में दफ़न।",
            "আবু বকর কুরাইশের বনু তাইম গোত্রের, নবী ﷺ-এর ঘনিষ্ঠতম বন্ধু এবং ইসলাম গ্রহণকারী প্রথম প্রাপ্তবয়স্ক স্বাধীন পুরুষ। হিজরতে সঙ্গী ছিলেন, শেষ অসুস্থতায় ইমামতি পান। ওফাতের পর প্রথম খলিফা নির্বাচিত হন। রিদ্দার বিরুদ্ধে যুদ্ধ করেন, কুরআন এক মুশাফে সংকলন করেন, ১৩ হিজরিতে ইন্তেকাল করে নবী ﷺ-এর পাশে দাফন হন।",
            "Abu Bakar dari Bani Taim Quraisy, sahabat terdekat Nabi ﷺ dan orang merdeka dewasa pertama yang masuk Islam. Ia menemani Hijrah, diangkat imam saat Nabi sakit, lalu menjadi khalifah pertama. Ia memerangi riddah, mengumpulkan Al-Qur'an dalam satu mushaf, dan wafat 13 H (634 M), dimakamkan di sisi Nabi ﷺ.",
        ),
        [
            item(
                L("Companionship and caliphate", "صحابیت اور خلافت", "सुहबत और खिलाफ़त", "সাহচর্য ও খিলাফত", "Persahabatan dan khilafah"),
                L("Khulafa-e-Rashideen", "خلفائے راشدین", "खुलफा-ए-राशिदीन", "খুলাফায়ে রাশেদীন", "Khulafaur Rasyidin"),
                L(
                    "He was one of the ten promised Paradise. His daughter Aisha was a Mother of the Believers. In his short caliphate of about two years he preserved the unity of the Ummah when many tribes withheld zakah or followed false prophets. He nominated Umar after consulting senior Companions.",
                    "وہ عشرہ مبشرہ میں سے تھے۔ بیٹی عائشہ ام المؤمنین تھیں۔ تقریباً دو سال کی خلافت میں امت کی وحدت بچائی جب بہت سے قبائل نے زکوٰۃ روک لی یا جھوٹے نبیوں کی پیروی کی۔ مشورے کے بعد عمر کو نامزد کیا۔",
                    "वे अशरा-ए-मुबश्शिरा में से थे। करीब दो साल की खिलाफ़त में उम्मत की एकता बचाई। मशवरे के बाद उमर को नामज़द किया।",
                    "তিনি আশারায়ে মুবাশশারার একজন। প্রায় দুই বছরের খিলাফতে উম্মাহর ঐক্য রক্ষা করেন। পরামর্শের পর উমরকে মনোনীত করেন।",
                    "Ia termasuk sepuluh yang dijamin surga. Dalam khilafah sekitar dua tahun ia menjaga persatuan umat. Setelah musyawarah ia menunjuk Umar.",
                ),
            ),
        ],
    ),
    chapter(
        2,
        L("Umar ibn al-Khattab", "عمر بن خطاب", "उमर इब्न अल-खत्ताब", "উমর ইবনুল খাত্তাব", "Umar bin Khattab"),
        L("The second caliph — al-Faruq", "دوسرے خلیفہ — فاروق", "दूसरे खलीफा — फारूक", "দ্বিতীয় খলিফা — ফারুক", "Khalifah kedua — al-Faruq"),
        L(
            "Umar ibn al-Khattab of Banu Adi accepted Islam in the sixth year of Prophethood, after which the Muslims prayed openly at the Ka'bah. He migrated openly to Madinah. He was among the ten promised Paradise and the Prophet ﷺ often sought his counsel. After Abu Bakr he became the second khalifah (13–23 AH). Under him Syria, Iraq, Persia, and Egypt were opened. He established the Hijri calendar, the diwan (register of stipends), night patrols in Madinah, and a reputation for justice that earned him the title al-Faruq. He was stabbed while leading Fajr in 23 AH (644 CE) by Abu Lu'lu'ah and died three days later. He is buried beside the Prophet ﷺ and Abu Bakr.",
            "عمر بن خطاب بنو عدی سے تھے، نبوت کے چھٹے سال اسلام لائے جس کے بعد مسلمان کعبہ میں کھل کر نماز پڑھنے لگے۔ علانیہ ہجرت کی۔ عشرہ مبشرہ میں سے تھے، نبی ﷺ اکثر مشورہ لیتے تھے۔ ابو بکر کے بعد دوسرے خلیفہ (13–23ھ)۔ شام، عراق، فارس اور مصر فتح ہوئے۔ ہجری کیلنڈر، دیوان، رات گشت اور عدل سے فاروق کہلائے۔ 23ھ میں فجر کی امامت پر ابو لؤلؤہ نے زخمی کیا، تین دن بعد وفات۔ نبی ﷺ اور ابو بکر کے پہلو میں دفن ہیں۔",
            "उमर बनू अदी से, नबुव्वत के छठे साल इस्लाम लाए। खुलेआम हिजरत की। अबू बक्र के बाद दूसरे खलीफा (13–23 हिजरी)। शाम, इराक, फारस, मिस्र फतह हुए। हजरी कैलेंडर और अदल से फारूक कहलाए। 23 हिजरी में फज्र की इमामत पर शहीद।",
            "উমর বনু আদির, নবুয়তের ষষ্ঠ বছরে ইসলাম গ্রহণ করেন। প্রকাশ্যে হিজরত করেন। আবু বকরের পর দ্বিতীয় খলিফা (১৩–২৩ হিজরি)। সিরিয়া, ইরাক, পারস্য ও মিশর বিজিত হয়। হিজরি বর্ষপঞ্জি ও ন্যায়বিচারের জন্য ফারুক খ্যাত। ২৩ হিজরিতে ফজরের ইমামতিতে শহীদ।",
            "Umar dari Bani Adi masuk Islam tahun keenam kenabian. Ia hijrah secara terang-terangan. Khalifah kedua (13–23 H). Syam, Irak, Persia, dan Mesir terbuka. Ia menetapkan kalender Hijriah dan terkenal adil (al-Faruq). Syahid saat imam Subuh tahun 23 H.",
        ),
        [
            item(
                L("Justice and conquests", "عدل اور فتوحات", "अदल और फुतूहात", "ন্যায় ও বিজয়", "Keadilan dan penaklukan"),
                L("Khulafa-e-Rashideen", "خلفائے راشدین", "खुलफा-ए-राशिदीन", "খুলাফায়ে রাশেদীন", "Khulafaur Rasyidin"),
                L(
                    "His daughter Hafsah was a Mother of the Believers. He appointed regional governors, checked them strictly, and lived simply. Before death he appointed a shura of six senior Companions to choose the next caliph; they chose Uthman.",
                    "بیٹی حفصہ ام المؤمنین تھیں۔ صوبوں پر گورنر مقرر کیے، سخت احتساب کیا، سادہ زندگی گزاری۔ وفات سے پہلے چھ اکابر صحابہ کی شوریٰ بنائی جس نے عثمان کو چنا۔",
                    "बेटी हफ़्सा उम्मुल मुमिनीन थीं। वफ़ात से पहले छह सहाबा की शूरा बनाई जिसने उस्मान को चुना।",
                    "কন্যা হাফসাহ উম্মুল মুমিনীন। মৃত্যুর আগে ছয়জন শীর্ষ সাহাবার শূরা গঠন করেন, তাঁরা উসমানকে বেছে নেন।",
                    "Putrinya Hafshah adalah Ummul Mukminin. Sebelum wafat ia membentuk syura enam sahabat senior; mereka memilih Utsman.",
                ),
            ),
        ],
    ),
    chapter(
        3,
        L("Uthman ibn Affan", "عثمان بن عفان", "उस्मान इब्न अफ्फान", "উসমান ইবন আফফান", "Utsman bin Affan"),
        L("The third caliph — Dhun-Nurayn", "تیسرے خلیفہ — ذوالنورین", "तीसरे खलीफा — ज़ुन-नूरैन", "তৃতীয় খলিফা — যুন-নূরাইন", "Khalifah ketiga — Dzan-Nurain"),
        L(
            "Uthman ibn Affan of Banu Umayyah accepted Islam early through Abu Bakr. He married two daughters of the Prophet ﷺ, Ruqayyah and after her death Umm Kulthum, hence Dhun-Nurayn (Possessor of Two Lights). He migrated to Abyssinia and then Madinah, missed Badr while nursing Ruqayyah, and equipped the army of Tabuk so generously that the Prophet ﷺ said nothing would harm him after that day. As third khalifah (23–35 AH) he expanded into North Africa and Central Asia and unified the written Quran (the Uthmani mushaf) sent to the provinces. He was killed in Madinah in 35 AH (656 CE) while reciting the Quran, after a siege of his house.",
            "عثمان بن عفان بنو امیہ سے، ابو بکر کے ہاتھ اسلام لائے۔ نبی ﷺ کی دو بیٹیوں رقیہ اور ان کے بعد ام کلثوم سے نکاح، اس لیے ذوالنورین۔ حبشہ پھر مدینہ ہجرت کی، بدر رقیہ کی تیمارداری کی وجہ سے رہ گئے، تبوک کا لشکر اس قدر ساز و سامان سے تیار کیا کہ نبی ﷺ نے فرمایا آج کے بعد عثمان کو کچھ نقصان نہ دے گا۔ تیسرے خلیفہ (23–35ھ) شمالی افریقہ اور وسط ایشیا کی توسیع، قرآن کا متحد مصحف۔ 35ھ میں گھر کے محاصرے کے بعد قرآن پڑھتے ہوئے شہید ہوئے۔",
            "उस्मान बनू उमैया से, अबू बक्र के जरिए इस्लाम लाए। नबी ﷺ की दो बेटियों से निकाह, ज़ुन-नूरैन। तबूक का लश्कर तैयार किया। तीसरे खलीफा (23–35 हिजरी) ने कुरआन का एक मुसहफ़ जमाया। 35 हिजरी में कुरआन पढ़ते शहीद।",
            "উসমান বনু উমাইয়ার, আবু বকরের মাধ্যমে ইসলাম গ্রহণ করেন। নবী ﷺ-এর দুই কন্যাকে বিয়ে করেন, তাই যুন-নূরাইন। তাবুকের সেনা সজ্জিত করেন। তৃতীয় খলিফা (২৩–৩৫ হিজরি) কুরআনের ঐক্যবদ্ধ মুশাফ প্রেরণ করেন। ৩৫ হিজরিতে কুরআন তিলাওয়াতরত অবস্থায় শহীদ।",
            "Utsman dari Bani Umayyah masuk Islam melalui Abu Bakar. Ia menikahi dua putri Nabi ﷺ, disebut Dzan-Nurain. Ia membekali pasukan Tabuk. Khalifah ketiga (23–35 H) menyeragamkan mushaf. Syahid tahun 35 H sambil membaca Al-Qur'an.",
        ),
        [
            item(
                L("The Uthmani mushaf", "عثمانی مصحف", "उस्मानी मुसहफ़", "উসমানি মুশাফ", "Mushaf Utsmani"),
                L("Khulafa-e-Rashideen", "خلفائے راشدین", "खुलफा-ए-राशिदीन", "খুলাফায়ে রাশেদীন", "Khulafaur Rasyidin"),
                L(
                    "When recitation differences appeared in the provinces, Hudhayfah ibn al-Yaman urged Uthman to act. A committee headed by Zayd ibn Thabit copied the sheets kept with Hafsah into several standard mushafs and sent them to the cities, with orders that other personal copies be set aside. This is the canonical written form still used today.",
                    "جب علاقوں میں قراءت کے اختلاف سامنے آئے تو حذیفہ بن یمان نے عثمان سے درخواست کی۔ زید بن ثابت کی کمیٹی نے حفصہ کے پاس محفوظ اوراق سے کئی معیاری مصحف لکھے اور شہروں کو بھیجے، دیگر نسخے کنارے رکھنے کا حکم ہوا۔ یہی معیاری رسم آج تک ہے۔",
                    "प्रांतों में क़िराअत के इख़्तिलाफ़ पर हुज़ैफ़ा की दरख़्वास्त से ज़ैद बिन साबित की कमेटी ने हफ़्सा के पन्नों से मुसहफ़ नकल किए। यही लिखा रूप आज तक है।",
                    "প্রদেশে কিরাআতের পার্থক্য দেখা দিলে হুযাইফার অনুরোধে যায়েদ ইবন সাবিতের কমিটি হাফসাহর পত্র থেকে প্রমিত মুশাফ নকল করে নগরে পাঠায়। এই লিখিত রূপ আজও চালু।",
                    "Ketika perbedaan qiraat muncul, Huzaifah meminta Utsman bertindak. Panitia Zaid bin Tsabit menyalin suhuf Hafshah menjadi mushaf standar ke kota-kota. Itulah rasm yang dipakai hingga kini.",
                ),
            ),
        ],
    ),
    chapter(
        4,
        L("Ali ibn Abi Talib", "علی بن ابی طالب", "अली इब्न अबी तालिब", "আলী ইবন আবি তালিব", "Ali bin Abi Thalib"),
        L("The fourth caliph — Abu Turab", "چوتھے خلیفہ — ابو تراب", "चौथे खलीफा — अबू तुराब", "চতুর্থ খলিফা — আবু তুরাব", "Khalifah keempat — Abu Turab"),
        L(
            "Ali ibn Abi Talib, cousin of the Prophet ﷺ and husband of Fatimah, was among the first to believe while still a boy. He slept in the Prophet's bed on the night of the Hijrah, was a distinguished warrior at Badr, Uhud, Khandaq, and Khaybar, and was among the ten promised Paradise. He became the fourth khalifah in 35 AH after Uthman. His caliphate (35–40 AH) faced the Battle of the Camel, Siffin, and the Khawarij. He moved the capital to Kufa. He was struck by Abd al-Rahman ibn Muljam while going to Fajr in 40 AH (661 CE) and died two days later. He is a fountain of knowledge in fiqh, courage, and eloquence.",
            "علی بن ابی طالب، نبی ﷺ کے چچازاد اور فاطمہ کے شوہر، بچپن میں ایمان لانے والے اولین میں سے تھے۔ ہجرت کی رات آپ کے بستر پر سوئے، بدر، احد، خندق، خیبر میں بہادر، عشرہ مبشرہ میں سے۔ عثمان کے بعد 35ھ میں چوتھے خلیفہ۔ خلافت (35–40ھ) میں جنگ جمل، صفین اور خوارج۔ دار الخلافت کوفہ۔ 40ھ میں فجر جاتے عبد الرحمن بن ملجم نے زخمی کیا، دو دن بعد شہادت۔ فقہ، شجاعت اور بلاغت کے امام۔",
            "अली नबी ﷺ के चचेरे भाई और फ़ातिमा के शौहर, बचपन में ईमान लाए। हिजरत की रात बिस्तर पर सोए। बद्र, उहुद, खंदक, ख़ैबर में बहादुर। 35 हिजरी में चौथे खलीफा। 40 हिजरी में फज्र जाते शहीद।",
            "আলী নবী ﷺ-এর চাচাতো ভাই ও ফাতিমার স্বামী, বাল্যেই ঈমান আনেন। হিজরতের রাতে নবীর বিছানায় শয়ন করেন। বদর, উহুদ, খন্দক, খাইবারে বীর। ৩৫ হিজরিতে চতুর্থ খলিফা। ৪০ হিজরিতে ফজরে যাওয়ার সময় শহীদ।",
            "Ali, sepupu Nabi ﷺ dan suami Fatimah, beriman sejak kanak-kanak. Ia tidur di tempat Nabi malam Hijrah, gagah di Badar, Uhud, Khandaq, dan Khaibar. Khalifah keempat tahun 35 H. Syahid tahun 40 H menuju Subuh.",
        ),
        [
            item(
                L("Ahl al-Bayt and knowledge", "اہل بیت اور علم", "अहल-ए-बैत और इल्म", "আহলুল বায়ত ও ইলম", "Ahlulbait dan ilmu"),
                L("Khulafa-e-Rashideen", "خلفائے راشدین", "खुलफा-ए-राशिदीन", "খুলাফায়ে রাশেদীন", "Khulafaur Rasyidin"),
                L(
                    "His sons al-Hasan and al-Husayn are masters of the youth of Paradise. Many legal verdicts and sermons are preserved from Ali. After his death, al-Hasan briefly succeeded him then yielded to Mu'awiyah to spare Muslim blood, ending the era commonly called the Rightly Guided Caliphate.",
                    "بیٹے حسن و حسین جنتی نوجوانوں کے سردار ہیں۔ علی سے بہت سے فتوے اور خطبے مروی ہیں۔ شہادت کے بعد حسن نے مختصر خلافت کی پھر معاویہ کے حق میں دستبردار ہوئے تاکہ مسلمانوں کا خون بچے، یہی وہ دور ہے جسے خلفائے راشدین کہا جاتا ہے۔",
                    "बेटे हसन व हुसैन जन्नत के जवानों के सरदार। शहादत के बाद हसन ने मुआविया के हक में किनारा किया ताकि मुसलमानों का खून बचे।",
                    "পুত্র হাসান ও হুসাইন জান্নাতের যুবকদের সরদার। শাহাদাতের পর হাসান সংক্ষিপ্ত খিলাফতের পর মুয়াবিয়ার অনুকূলে সরে দাঁড়ান যাতে মুসলিম রক্ত রক্ষা পায়।",
                    "Putranya Hasan dan Husain adalah pemuka pemuda surga. Setelah syahid, Hasan sempat mengganti lalu menyerahkan kepada Muawiyah demi darah umat.",
                ),
            ),
        ],
    ),
    chapter(
        5,
        L("Hamzah ibn Abd al-Muttalib", "حمزہ بن عبد المطلب", "हमज़ा इब्न अब्दुल मुत्तलिब", "হামজাহ ইবন আব্দুল মুত্তালিব", "Hamzah bin Abdul Muththalib"),
        L("Lion of Allah", "اسد اللہ", "असदुल्लाह", "আসাদুল্লাহ", "Singa Allah"),
        L(
            "Hamzah, paternal uncle of the Prophet ﷺ, accepted Islam in Makkah and greatly strengthened the Muslims. He fought at Badr and was martyred at Uhud by Wahshi. The Prophet ﷺ called him Sayyid al-Shuhada (Master of the Martyrs) and wept over him. His martyrdom is among the most remembered events of Uhud.",
            "حمزہ نبی ﷺ کے چچا، مکہ میں اسلام لائے اور مسلمانوں کو بہت قوت دی۔ بدر میں لڑے، احد میں وحشی کے ہاتھ شہید ہوئے۔ نبی ﷺ نے سید الشہداء فرمایا اور ان پر روئے۔ احد کے سب سے یادگار واقعات میں سے ہے۔",
            "हमज़ा नबी ﷺ के चाचा, मक्का में इस्लाम लाए। बद्र में लड़े, उहुद में शहीद। नबी ﷺ ने सय्यिदुश शुहदा कहा।",
            "হামজাহ নবী ﷺ-এর চাচা, মক্কায় ইসলাম গ্রহণ করেন। বদরে যুদ্ধ করেন, উহুদে শহীদ। নবী ﷺ তাঁকে সাইয়িদুশ শুহাদা বলেন।",
            "Hamzah, paman Nabi ﷺ, masuk Islam di Makkah dan menguatkan kaum muslimin. Gugur di Uhud. Nabi ﷺ menyebutnya Sayyidusy Syuhada.",
        ),
        [
            item(
                L("Uhud", "احد", "उहुद", "উহুদ", "Uhud"),
                L("Martyrdom", "شہادت", "शहादत", "শাহাদাত", "Syahid"),
                L(
                    "Hind bint Utbah had vowed revenge after Badr. Wahshi, an Abyssinian, killed Hamzah. The Prophet ﷺ later forgave Wahshi when he accepted Islam, though Wahshi stayed away out of shame. Hamzah is buried at Uhud.",
                    "ہند بنت عتبہ نے بدر کے بعد انتقام کی قسم کھائی تھی۔ حبشی وحشی نے حمزہ کو شہید کیا। نبی ﷺ نے اسلام لانے پر وحشی کو معاف فرمایا، وہ شرم سے دور رہے۔ حمزہ احد میں دفن ہیں۔",
                    "बद्र के बाद हिन्द ने बदला चाहा। वह्शी ने हमज़ा को शहीद किया। नबी ﷺ ने इस्लाम पर माफ़ किया। हमज़ा उहुद में दफ़न हैं।",
                    "বদরের পর হিন্দ প্রতিশোধের শপথ করেন। ওয়াহশি হামজাহকে শহীদ করেন। নবী ﷺ ইসলাম গ্রহণে ক্ষমা করেন। হামজাহ উহুদে দাফন।",
                    "Setelah Badar, Hind bernazar balas. Wahsyi membunuh Hamzah. Nabi ﷺ memaafkan Wahsyi saat ia masuk Islam. Hamzah dimakamkan di Uhud.",
                ),
            ),
        ],
    ),
    chapter(
        6,
        L("Bilal ibn Rabah", "بلال بن رباح", "बिलाल इब्न रबाह", "বিলাল ইবন রাবাহ", "Bilal bin Rabah"),
        L("The first mu'adhdhin", "پہلے مؤذن", "पहले मुअज़्ज़िन", "প্রথম মুয়াজ্জিন", "Muazin pertama"),
        L(
            "Bilal was an Abyssinian slave in Makkah. He was tortured for Islam, saying 'Ahad, Ahad' (One, One) under the rock. Abu Bakr purchased and freed him. He became the Prophet's ﷺ mu'adhdhin in Madinah, calling the adhan with a beautiful voice. He fought in the major campaigns. After the Conquest of Makkah he climbed the Ka'bah and gave the adhan. After the Prophet's ﷺ death he seldom gave adhan in Madinah out of grief, and later lived in Syria, where he died around 20 AH.",
            "بلال مکہ میں حبشی غلام تھے۔ اسلام پر تشدد سہا، پتھر تلے احد احد کہتے۔ ابو بکر نے خرید کر آزاد کیا۔ مدینہ میں نبی ﷺ کے مؤذن بنے، خوبصورت آواز سے اذان دی۔ بڑی مہموں میں شریک۔ فتح مکہ پر کعبہ پر چڑھ کر اذان دی۔ نبی ﷺ کی وفات کے بعد غم سے مدینہ میں کم اذان کہی، شام میں رہے۔ تقریباً 20ھ میں وفات۔",
            "बिलाल मक्का में हबशी गुलाम थे। इस्लाम पर अज़ाब सहा। अबू बक्र ने आज़ाद किया। मदीना में मुअज़्ज़िन बने। फत्हे मक्का पर काबा पर अज़ान दी।",
            "বিলাল মক্কায় হাবশি দাস ছিলেন। ইসলামের জন্য নির্যাতিত হন। আবু বকর মুক্ত করেন। মদিনায় মুয়াজ্জিন হন। মক্কা বিজয়ে কাবায় আজান দেন।",
            "Bilal budak Habasyah di Makkah, disiksa karena Islam. Abu Bakar memerdekakannya. Ia menjadi muazin Nabi ﷺ di Madinah. Saat Fathu Makkah ia azan di atas Ka'bah.",
        ),
        [
            item(
                L("Adhan and loyalty", "اذان اور وفا", "अज़ान और वफ़ा", "আজান ও আনুগত্য", "Azan dan kesetiaan"),
                L("Prominent Companion", "جلیل القدر صحابی", "जलील सहाबी", "শ্রেষ্ঠ সাহাবি", "Sahabat terkemuka"),
                L(
                    "Reports say that when he later gave adhan in Madinah, the people wept, remembering the Prophet ﷺ. His life is a sign that Islam honours taqwa, not lineage or colour.",
                    "روایات ہیں کہ بعد میں مدینہ میں اذان دی تو لوگ رو پڑے، نبی ﷺ یاد آئے۔ ان کی زندگی اس بات کی دلیل ہے کہ اسلام تقویٰ کو دیکھتا ہے نسب اور رنگ کو نہیں۔",
                    "बाद में मदीना में अज़ान दी तो लोग रोए। उनकी ज़िंदगी दिखाती है इस्लाम तक़वा देखता है, रंग और नसब नहीं।",
                    "পরে মদিনায় আজান দিলে মানুষ কেঁদে ওঠে। তাঁর জীবন দেখায় ইসলাম তাকওয়া দেখে, বর্ণ বা বংশ নয়।",
                    "Ketika ia azan lagi di Madinah, orang menangis ingat Nabi ﷺ. Hidupnya menunjukkan Islam memuliakan takwa, bukan nasab atau warna.",
                ),
            ),
        ],
    ),
    chapter(
        7,
        L("Salman al-Farisi", "سلمان فارسی", "सल्मान फ़ारसी", "সালমান আল-ফারিসি", "Salman al-Farisi"),
        L("From Persia to the Ahl al-Bayt", "فارس سے اہل بیت تک", "फारस से अहल-ए-बैत तक", "পারস্য থেকে আহলুল বায়ত", "Dari Persia ke Ahlulbait"),
        L(
            "Salman was born in Persia, sought the true religion through Christianity, then followed a monk's instruction to Arabia. He met the Prophet ﷺ in Madinah, recognised the signs of prophethood, and accepted Islam. He was a slave until the Prophet ﷺ helped him write a contract of manumission (mukatabah). At Khandaq he suggested digging the trench, a Persian method. The Prophet ﷺ said, 'Salman is of us, the Ahl al-Bayt.' He later governed Mada'in and died in the 30s AH.",
            "سلمان فارس میں پیدا ہوئے، عیسائیت میں حق تلاش کیا، پھر راہب کی ہدایت پر عرب آئے۔ مدینہ میں نبی ﷺ سے ملے، نبوت کی نشانیاں پہچانیں، اسلام لائے۔ غلام تھے یہاں تک کہ مکاتبہ میں مدد ملی۔ خندق میں فارسی طریقے سے خندق کھودنے کی تجویز دی۔ نبی ﷺ نے فرمایا سلمان ہم میں سے ہے، اہل بیت سے۔ بعد میں مدائن کے گورنر، تیس کی دہائی ہجری میں وفات۔",
            "सल्मान फारस में पैदा हुए, हक़ की तलाश में अरब आए। मदीना में इस्लाम लाए। खंदक की तजवीज़ दी। नबी ﷺ ने फ़रमाया सल्मान अहले बैत में से हैं।",
            "সালমান পারস্যে জন্মগ্রহণ করেন, সত্যের খোঁজে আরবে আসেন। মদিনায় ইসলাম গ্রহণ করেন। খন্দকের প্রস্তাব দেন। নবী ﷺ বলেন সালমান আমাদের আহলুল বায়তের।",
            "Salman lahir di Persia, mencari agama yang benar hingga ke Arab. Masuk Islam di Madinah. Di Khandaq ia mengusulkan parit. Nabi ﷺ bersabda, 'Salman termasuk kami, Ahlulbait.'",
        ),
        [
            item(
                L("The trench", "خندق", "खंदक", "খন্দক", "Parit"),
                L("Khandaq", "احزاب", "अहज़ाब", "আহজাব", "Ahzab"),
                L(
                    "When confederate tribes besieged Madinah in 5 AH, Salman advised a trench on the exposed side of the city. The Companions dug it with the Prophet ﷺ, and the cavalry of Quraysh could not cross. This counsel is a famous example of using useful skill from any land in the service of Islam.",
                    "5ھ میں جب احزاب نے مدینہ گھیر لیا تو سلمان نے کھلے رخ پر خندق کی صلاح دی۔ صحابہ نے نبی ﷺ کے ساتھ کھودی، قریش کی گھڑسوار پار نہ ہو سکی۔ یہ اسلام کی خدمت میں ہر سرزمین کی مفید مہارت استعمال کرنے کی مثال ہے۔",
                    "5 हिजरी में जब अहज़ाब ने मदीना घेरा तो सल्मान ने खंदक की सलाह दी। कुरैश की घुड़सवार पार न कर सकी।",
                    "৫ হিজরিতে যখন আহজাব মদিনা অবরোধ করে সালমান পরিখা পরামর্শ দেন। কুরাইশ অশ্বারোহী পার হতে পারেনি।",
                    "Saat Ahzab mengepung Madinah tahun 5 H, Salman mengusulkan parit. Kavaleri Quraisy tidak bisa menyeberang.",
                ),
            ),
        ],
    ),
    chapter(
        8,
        L("Khalid ibn al-Walid", "خالد بن ولید", "ख़ालिद इब्न अल-वलीद", "খালিদ ইবন আল-ওয়ালিদ", "Khalid bin al-Walid"),
        L("Sword of Allah", "سیف اللہ", "सैफुल्लाह", "সাইফুল্লাহ", "Pedang Allah"),
        L(
            "Khalid ibn al-Walid of Banu Makhzum was a master tactician. He fought the Muslims at Uhud, then accepted Islam after Hudaybiyyah, around 8 AH. The Prophet ﷺ named him Sayf Allah (Sword of Allah). He led at Mu'tah after three commanders fell, fought at the Conquest of Makkah and Hunayn, then in the Riddah wars and the openings of Iraq and Syria, including Yarmuk. Umar later removed him from overall command to remind people that victory is from Allah, not from a general. He died in Homs around 21 AH, having said he sought martyrdom in battle yet died on his bed.",
            "خالد بن ولید بنو مخزوم سے، عظیم جرنیل۔ احد میں مسلمانوں کے خلاف لڑے، حدیبیہ کے بعد تقریباً 8ھ میں اسلام لائے۔ نبی ﷺ نے سیف اللہ کا لقب دیا۔ موتہ میں تین کمانڈروں کے شہید ہونے کے بعد لشکر سنبھالا، فتح مکہ، حنین، پھر ردّہ، عراق و شام بشمول یرموک۔ عمر نے بعد میں کمان اس لیے ہٹائی کہ لوگ سمجھیں فتح اللہ کی طرف سے ہے۔ حمص میں تقریباً 21ھ میں بستر پر وفات، حالانکہ شہادت چاہتے تھے۔",
            "ख़ालिद बनू मख़ज़ूम से। उहुद में मुसलमानों के ख़िलाफ़ लड़े, फिर इस्लाम लाए। नबी ﷺ ने सैफुल्लाह कहा। मूताह, फत्हे मक्का, यरमूक। होम्स में करीब 21 हिजरी में वफ़ात।",
            "খালিদ বনু মাখজুমের। উহুদে মুসলিমদের বিপক্ষে যুদ্ধ করেন, পরে ইসলাম গ্রহণ করেন। নবী ﷺ তাঁকে সাইফুল্লাহ বলেন। মুতাহ, মক্কা বিজয়, ইয়ারমুক। হোমসে প্রায় ২১ হিজরিতে ইন্তেকাল।",
            "Khalid dari Bani Makhzum, ahli strategi. Melawan muslim di Uhud, lalu masuk Islam sekitar 8 H. Nabi ﷺ menamainya Pedang Allah. Memimpin di Mutah, Fathu Makkah, Yarmuk. Wafat di Homs sekitar 21 H.",
        ),
        [
            item(
                L("Mu'tah and Syria", "موتہ اور شام", "मूताह और शाम", "মুতাহ ও সিরিয়া", "Mutah dan Syam"),
                L("Prominent Companion", "جلیل القدر صحابی", "जलील सहाबी", "শ্রেষ্ঠ সাহাবি", "Sahabat terkemuka"),
                L(
                    "At Mu'tah (8 AH) against a much larger Byzantine-allied force, Zayd, Ja'far, and Abdullah ibn Rawahah were killed in succession. Khalid took the standard, reorganised the army, and withdrew with skill. The Prophet ﷺ praised this as a victory of preservation.",
                    "موتہ (8ھ) میں بڑی رومی اتحادی فوج کے مقابل زید، جعفر اور عبد اللہ بن رواحہ باری باری شہید ہوئے۔ خالد نے جھنڈا سنبھالا، لشکر سنوارا اور مہارت سے واپس لیا۔ نبی ﷺ نے اسے حفاظت کی فتح قرار دیا।",
                    "मूताह में ज़ैद, जाफ़र, अब्दुल्लाह बिन रवाहा शहीद हुए। ख़ालिद ने लश्कर संभाला और कुशलता से वापस लिया।",
                    "মুতাহে যায়েদ, জাফর ও আব্দুল্লাহ ইবন রাওয়াহা শহীদ হন। খালিদ সেনা পুনর্গঠন করে দক্ষতার সঙ্গে ফিরে আসেন।",
                    "Di Mutah, Zaid, Ja'far, dan Abdullah bin Rawahah syahid bergantian. Khalid mengambil bendera, menata pasukan, dan menarik diri dengan terampil.",
                ),
            ),
        ],
    ),
    chapter(
        9,
        L("Abu Hurayrah", "ابو ہریرہ", "अबू हुरैरा", "আবু হুরাইরাহ", "Abu Hurairah"),
        L("The most prolific hadith narrator", "سب سے زیادہ احادیث روایت کرنے والے", "सबसे ज़्यादा हदीस रिवायत करने वाले", "সর্বাধিক হাদিস বর্ণনাকারী", "Perawi hadis terbanyak"),
        L(
            "Abd al-Rahman ibn Sakhr al-Dawsi, known as Abu Hurayrah, accepted Islam in 7 AH and stayed close to the Prophet ﷺ in the Suffah. He narrated thousands of hadith, more than any other Companion, because he devoted himself to listening and memory and the Prophet ﷺ made du'a for his retention. He later governed Bahrain briefly and taught in Madinah. He died around 57–59 AH.",
            "عبد الرحمن بن صخر دوسی، ابو ہریرہ کے نام سے مشہور، 7ھ میں اسلام لائے اور صفّہ میں نبی ﷺ کے قریب رہے۔ ہزاروں احادیث روایت کیں، سب صحابہ سے زیادہ، کیونکہ سننے اور یادداشت کے لیے وقف رہے اور نبی ﷺ نے حافظے کی دعا دی۔ کچھ عرصہ بحرین کے گورنر، مدینہ میں درس۔ تقریباً 57–59ھ میں وفات।",
            "अबू हुरैरा 7 हिजरी में इस्लाम लाए, सुफ्फा में रहे। हज़ारों हदीस रिवायत कीं। नबी ﷺ ने हिफ़्ज़ की दुआ दी। करीब 57–59 हिजरी में वफ़ात।",
            "আবু হুরাইরাহ ৭ হিজরিতে ইসলাম গ্রহণ করেন, সুফফায় থাকেন। হাজার হাজার হাদিস বর্ণনা করেন। নবী ﷺ তাঁর স্মৃতির জন্য দোয়া করেন। প্রায় ৫৭–৫৯ হিজরিতে ইন্তেকাল।",
            "Abu Hurairah masuk Islam tahun 7 H dan tinggal di Suffah. Ia meriwayatkan ribuan hadis, terbanyak di antara sahabat. Nabi ﷺ mendoakan hafalannya. Wafat sekitar 57–59 H.",
        ),
        [
            item(
                L("The people of the Suffah", "اصحاب صفّہ", "अस्हाबे सुफ्फा", "আসহাবে সুফফা", "Ahlus Suffah"),
                L("Prominent Companion", "جلیل القدر صحابی", "जलील सहाबी", "শ্রেষ্ঠ সাহাবি", "Sahabat terkemuka"),
                L(
                    "The Suffah was a shaded area of the Prophet's Mosque for poor Companions who had no household. Abu Hurayrah often went hungry there while collecting knowledge. Later scholars such as Imam al-Bukhari and Muslim filled their books with his reports, always through trustworthy chains.",
                    "صفّہ مسجد نبوی کا سایہ دار حصہ تھا جہاں بے گھر غریب صحابہ رہتے۔ ابو ہریرہ وہاں بھوکے رہ کر علم جمع کرتے۔ بعد کے ائمہ بخاری و مسلم نے ثقہ سندوں سے ان کی روایات کتابوں میں بھریں।",
                    "सुफ्फा मस्जिदे नबवी का हिस्सा था ग़रीब सहाबा के लिए। अबू हुरैरा वहाँ इल्म जमा करते। बुख़ारी व मुस्लिम ने उनकी रिवायात लीं।",
                    "সুফফা ছিল নবীর মসজিদের ছায়াঘেরা অংশ দরিদ্র সাহাবিদের জন্য। আবু হুরাইরাহ সেখানে ইলম সংগ্রহ করেন। বুখারি ও মুসলিম তাঁর বর্ণনা গ্রহণ করেন।",
                    "Suffah adalah serambi Masjid Nabawi untuk sahabat miskin. Abu Hurairah mengumpulkan ilmu di sana. Bukhari dan Muslim banyak meriwayatkan darinya.",
                ),
            ),
        ],
    ),
    chapter(
        10,
        L("Fatimah al-Zahra", "فاطمہ الزہرا", "फ़ातिमा अज़-ज़हरा", "ফাতিমাহ আজ-জাহরা", "Fatimah az-Zahra"),
        L("Daughter of the Messenger ﷺ", "رسول اللہ ﷺ کی صاحبزادی", "रसूल ﷺ की साहिबज़ादी", "রাসূল ﷺ-এর কন্যা", "Putri Rasulullah ﷺ"),
        L(
            "Fatimah was the youngest daughter of the Prophet ﷺ and Khadijah, the most beloved of his children. She married Ali ibn Abi Talib. Their children included al-Hasan, al-Husayn, Zaynab, and Umm Kulthum. The Prophet ﷺ said she is the mistress of the women of Paradise. He would stand when she entered and kiss her. She suffered grief at Uhud tending his wounds. She died in Madinah six months after her father, around 11 AH, and was buried at night according to her wish. From her descends the Prophet's ﷺ surviving lineage.",
            "فاطمہ نبی ﷺ اور خدیجہ کی سب سے چھوٹی اور محبوب بیٹی۔ علی سے نکاح۔ اولاد میں حسن، حسین، زینب، ام کلثوم۔ نبی ﷺ نے فرمایا یہ جنت کی عورتوں کی سردار ہیں۔ داخل ہوتیں تو آپ کھڑے ہوتے اور بوسہ دیتے۔ احد میں زخموں کی تیمارداری کی۔ والد کی وفات کے چھ مہینے بعد 11ھ کے قریب مدینہ میں وفات، خواہش کے مطابق رات دفن ہوئیں۔ آپ ﷺ کی باقی نسل انہیں سے ہے۔",
            "फ़ातिमा नबी ﷺ और ख़दीजा की सबसे छोटी बेटी। अली से निकाह। हसन, हुसैन उनकी औलाद। नबी ﷺ ने फ़रमाया जन्नत की औरतों की सरदार। वालिद के छह महीने बाद वफ़ात।",
            "ফাতিমাহ নবী ﷺ ও খাদিজাহর কনিষ্ঠ কন্যা। আলীর সঙ্গে বিবাহ। হাসান ও হুসাইন তাঁর সন্তান। নবী ﷺ বলেন তিনি জান্নাতের নারীদের সরদার। পিতার ছয় মাস পর ইন্তেকাল।",
            "Fatimah putri bungsu Nabi ﷺ dan Khadijah, paling dicintai. Menikah dengan Ali. Hasan dan Husain putranya. Nabi ﷺ bersabda ia tuan wanita surga. Wafat enam bulan setelah ayahnya.",
        ),
        [
            item(
                L("Ahl al-Bayt", "اہل بیت", "अहल-ए-बैत", "আহলুল বায়ত", "Ahlulbait"),
                L("The Prophet's family", "نبی ﷺ کا خاندان", "नबी ﷺ का परिवार", "নবী ﷺ-এর পরিবার", "Keluarga Nabi ﷺ"),
                L(
                    "Verse 33:33 and the hadith of the cloak (kisa') mention Fatimah with Ali, al-Hasan, and al-Husayn. Muslims of all schools honour her purity, patience, and nearness to the Messenger ﷺ. Her nickname al-Zahra means the Radiant.",
                    "آیت 33:33 اور حدیث کسا میں فاطمہ علی، حسن و حسین کے ساتھ مذکور ہیں۔ ہر مکتب انہیں پاکیزگی، صبر اور رسول ﷺ سے قرب پر عزت دیتا ہے۔ زہرا کا مطلب چمکتی ہوئی۔",
                    "आयत 33:33 और हदीसे किसा में फ़ातिमा अली, हसन, हुसैन के साथ हैं। ज़हरा मतलब रौशन।",
                    "আয়াত ৩৩:৩৩ ও কিসার হাদিসে ফাতিমাহ আলী, হাসান ও হুসাইনের সঙ্গে উল্লিখিত। জাহরা অর্থ উজ্জ্বল।",
                    "Ayat 33:33 dan hadis kisak menyebut Fatimah bersama Ali, Hasan, dan Husain. Az-Zahra berarti yang berseri.",
                ),
            ),
        ],
    ),
]


GHAZAWAT = [
    chapter(
        1,
        L("Ghazwah Badr", "غزوہ بدر", "ग़ज़वा-ए-बद्र", "গাজওয়ায়ে বদর", "Perang Badar"),
        L("2 AH / 624 CE", "2ھ / 624ء", "2 हिजरी / 624 ई", "২ হিজরি / ৬২৪ খ্রি.", "2 H / 624 M"),
        L(
            "Badr was the first major pitched battle. About 313 Muslims, lightly armed, met a Quraysh caravan-relief force of around one thousand at the wells of Badr, southwest of Madinah. Allah promised angels and a clear victory (8:9–12). Leaders of Quraysh such as Abu Jahl fell. Fourteen Muslims were martyred. The victory confirmed the new community and is called Yawm al-Furqan, the Day of Criterion (8:41).",
            "بدر پہلی بڑی صف آراء جنگ۔ تقریباً 313 ہلکے مسلح مسلمان مدینہ کے جنوب مغرب کنوؤں پر قریش کی تقریباً ہزار نفری سے ٹکرائے۔ اللہ نے فرشتوں اور فتح مبین کا وعدہ کیا (8:9–12)۔ ابو جہل جیسے سردار گرے۔ چودہ مسلمان شہید۔ یہ فتح یوم الفرقان کہلائی (8:41)۔",
            "बद्र पहली बड़ी जंग। करीब 313 मुसलमान लगभग हज़ार कुरैश से टकराए। अल्लाह ने फतह का वादा किया। चौदह शहीद। यौमुल फुरक़ान कही गई।",
            "বদর প্রথম বড় সম্মুখ যুদ্ধ। প্রায় ৩১৩ মুসলিম প্রায় এক হাজার কুরাইশের মুখোমুখি হন। আল্লাহ বিজয়ের ওয়াদা করেন। চৌদ্দজন শহীদ। একে ইয়াওমুল ফুরকান বলা হয়।",
            "Badar pertempuran besar pertama. Sekitar 313 muslim menghadapi sekitar seribu Quraisy. Allah menjanjikan kemenangan. Empat belas syahid. Disebut Yaumul Furqan.",
        ),
        [
            item(
                L("The army and the outcome", "لشکر اور انجام", "लश्कर और अंजाम", "সেনা ও পরিণতি", "Pasukan dan hasil"),
                L("First great battle", "پہلی بڑی جنگ", "पहली बड़ी जंग", "প্রথম বড় যুদ্ধ", "Pertempuran besar pertama"),
                L(
                    "The Prophet ﷺ consulted the Muhajirun and Ansar; Sa'd ibn Mu'adh spoke for the Ansar's loyalty. Rain fell, the Muslims held the wells, and du'a was made until the coat of mail fell from the Prophet's ﷺ shoulders. Captives were treated with mercy; some were freed for teaching literacy. The spoils were distributed by revelation in Surah al-Anfal.",
                    "نبی ﷺ نے مہاجرین و انصار سے مشورہ کیا؛ سعد بن معاذ نے انصار کی وفا بیان کی۔ بارش ہوئی، کنویں مسلمانوں کے پاس رہے، دعا یہاں تک کہ زرہ آپ کے کندھوں سے سرک گئی۔ قیدیوں سے رحم، بعض نے لکھنا پڑھا کر آزادی پائی۔ مال غنیمت سورہ انفال کی وحی سے تقسیم ہوا۔",
                    "नबी ﷺ ने मुशविरा किया। साद बिन मुआज़ ने अनसार की वफ़ा कही। क़ैदियों पर रहम। माले ग़नीमत अनफ़ाल से बांटा गया।",
                    "নবী ﷺ পরামর্শ করেন। সাদ ইবন মুআয আনসারের আনুগত্য বলেন। বন্দিদের প্রতি দয়া। গনিমত সূরা আনফাল অনুসারে বণ্টিত হয়।",
                    "Nabi ﷺ bermusyawarah; Sa'd bin Mu'az menyatakan setia Ansar. Tawanan diperlakukan lembut. Ganimah dibagi menurut Surah al-Anfal.",
                ),
            ),
        ],
    ),
    chapter(
        2,
        L("Ghazwah Uhud", "غزوہ احد", "ग़ज़वा-ए-उहुद", "গাজওয়ায়ে উহুদ", "Perang Uhud"),
        L("3 AH / 625 CE", "3ھ / 625ء", "3 हिजरी / 625 ई", "৩ হিজরি / ৬২৫ খ্রি.", "3 H / 625 M"),
        L(
            "Quraysh returned with about three thousand to avenge Badr. The Muslims, about seven hundred after a withdrawal by Abdullah ibn Ubayy, took positions at Mount Uhud. Archers were posted on a flank with orders not to leave. When they left their post after an early success, Khalid ibn al-Walid's cavalry struck. The Prophet ﷺ was wounded, rumours spread that he had been killed, and about seventy were martyred, including Hamzah. Uhud was a trial teaching obedience and patience (3:139–165).",
            "قریش بدر کا بدلہ لینے تقریباً تین ہزار لے کر آئے۔ عبد اللہ بن ابی کے واپس ہونے کے بعد مسلمان تقریباً سات سو احد پہاڑ پر مورچے باندھے۔ تیراندازوں کو پہलू پر حکم تھا نہ ہٹیں۔ ابتدائی کامیابی پر مورچہ چھوڑنے سے خالد کی گھڑسوار نے وار کیا। نبی ﷺ زخمی، شہادت کی افواہ، تقریباً ستر شہید بشمول حمزہ۔ احد اطاعت اور صبر کی آزمائش تھی (3:139–165)۔",
            "कुरैश ने बद्र का बदला लिया। तीरंदाज़ों ने मोर्चा छोड़ा तो ख़ालिद की घुड़सवार ने हमला किया। नबी ﷺ ज़ख़्मी, हमज़ा शहीद। उहुद इताअत की आज़माइश।",
            "কুরাইশ বদরের প্রতিশোধে আসে। তীরন্দাজরা অবস্থান ছাড়লে খালিদের অশ্বারোহী আঘাত করে। নবী ﷺ আহত, হামজাহ শহীদ। উহুদ আনুগত্যের পরীক্ষা।",
            "Quraisy membalas Badar. Pemanah meninggalkan pos, kavaleri Khalid menyerang. Nabi ﷺ terluka, Hamzah syahid. Uhud adalah ujian ketaatan.",
        ),
        [
            item(
                L("The archers' hill", "تیراندازوں کی پہاڑی", "तीरंदाज़ों की पहाड़ी", "তীরন্দাজদের পাহাড়", "Bukit pemanah"),
                L("A lesson in obedience", "اطاعت کا سبق", "इताअत की सबक", "আনুগত্যের শিক্ষা", "Pelajaran ketaatan"),
                L(
                    "The Prophet ﷺ placed about fifty archers under Abdullah ibn Jubayr and forbade them to leave even if they saw the Muslims winning. Many descended to collect spoils. The reversal followed at once. Those who stood firm, and those who rallied around the Prophet ﷺ when he called, are praised in the Quran.",
                    "نبی ﷺ نے عبد اللہ بن جبیر کے تحت تقریباً پچاس تیرانداز رکھے اور منع کیا کہ فتح دیکھ کر بھی نہ ہٹیں۔ بہت غنیمت کے لیے اترے۔ الٹ فوراً ہوا۔ جو جمے رہے اور پکار پر آپ کے گرد اکٹھے ہوئے قرآن میں تعریف کیے گئے।",
                    "नबी ﷺ ने पचास तीरंदाज़ रखे, मना किया हटना। कई ग़नीमत को उतरे। जो डटे रहे उनकी तारीफ़ कुरआन में है।",
                    "নবী ﷺ প্রায় পঞ্চাশ তীরন্দাজ রাখেন, সরতে নিষেধ করেন। অনেকে গনিমত নিতে নামেন। যারা স্থির থাকেন কুরআনে প্রশংসিত।",
                    "Nabi ﷺ menempatkan sekitar lima puluh pemanah, dilarang turun. Banyak turun mengambil ganimah. Yang tetap bertahan dipuji Al-Qur'an.",
                ),
            ),
        ],
    ),
    chapter(
        3,
        L("Ghazwah al-Khandaq (Ahzab)", "غزوہ خندق (احزاب)", "ग़ज़वा-ए-खंदक (अहज़ाब)", "গাজওয়ায়ে খন্দক (আহজাব)", "Perang Khandaq (Ahzab)"),
        L("5 AH / 627 CE", "5ھ / 627ء", "5 हिजरी / 627 ई", "৫ হিজরি / ৬২৭ খ্রি.", "5 H / 627 M"),
        L(
            "A confederacy of Quraysh, Ghatafan, and other tribes, urged on after the exile of Banu Nadir, besieged Madinah with thousands. Salman al-Farisi suggested digging a trench on the open approach. The siege lasted weeks in cold and hunger. Nu'aym ibn Mas'ud sowed distrust among the allies. Allah sent wind and the coalition broke (33:9–25). The battle is named Ahzab (the Confederates) in the Quran.",
            "بنو نضیر کی جلاوطنی کے بعد قریش، غطفان اور دیگر قبائل کے ہزاروں نے مدینہ گھیر لیا। سلمان فارسی نے کھلے رخ پر خندق کھودنے کو کہا۔ محاصرہ ہفتوں چلا، سردی اور بھوک۔ نعیم بن مسعود نے اتحادیوں میں بدگمانی ڈالی۔ اللہ نے ہوا بھیجی اور اتحاد ٹوٹا (33:9–25)۔ قرآن میں احزاب ہے۔",
            "कुरैश और गतफ़ान ने मदीना घेरा। सल्मान ने खंदक सुझाई। अल्लाह ने हवा भेजी, गठबंधन टूटा। कुरआन में अहज़ाब।",
            "কুরাইশ ও গাতাফান মদিনা অবরোধ করে। সালমান পরিখা প্রস্তাব করেন। আল্লাহ বায়ু পাঠান, জোট ভেঙে যায়। কুরআনে আহজাব।",
            "Koalisi Quraisy dan Gathafan mengepung Madinah. Salman mengusulkan parit. Allah mengirim angin, koalisi pecah. Al-Qur'an menamainya Ahzab.",
        ),
        [
            item(
                L("The siege and Banu Qurayzah", "محاصرہ اور بنو قریظہ", "घेराबंदी और बनू कुरैज़ा", "অবরোধ ও বনু কুরায়জা", "Pengepungan dan Bani Quraizah"),
                L("After the trench", "خندق کے بعد", "खंदक के बाद", "খন্দকের পর", "Setelah parit"),
                L(
                    "During the siege, Banu Qurayzah were accused of breaking their pact with the Prophet ﷺ under pressure from Huyayy ibn Akhtab. After the confederates left, the Muslims besieged Banu Qurayzah. They accepted the judgment of Sa'd ibn Mu'adh, who ruled by the law of their scripture regarding combatants who break a wartime treaty. The episode is reported in the seerah and Surah al-Ahzab.",
                    "محاصرے میں بنو قریظہ پر الزام ہے کہ حیي بن اخطب کے دباؤ پر نبی ﷺ سے عہد توڑا۔ احزاب کے جانے کے بعد محاصرہ ہوا۔ انہوں نے سعد بن معاذ کا فیصلہ ماننا قبول کیا جنہوں نے ان کی کتاب کی جنگ کے عہد توڑنے والے جنگجوؤں والی سزا دی। یہ سیرت اور سورہ احزاب میں ہے۔",
                    "घेरे में बनू कुरैज़ा पर इल्ज़ाम कि उन्होंने अहद तोड़ा। साद बिन मुआज़ का फैसला माना। यह सीरत और सूरह अहज़ाब में है।",
                    "অবরোধে বনু কুরায়জার বিরুদ্ধে অভিযোগ তাঁরা চুক্তি ভঙ্গ করেন। সাদ ইবন মুআযের রায় তাঁরা মানেন। এটি সিরাত ও সূরা আহজাবে আছে।",
                    "Dalam pengepungan, Bani Quraizah dituduh merusak perjanjian. Mereka menerima keputusan Sa'd bin Mu'az. Peristiwa ini ada dalam sirah dan Surah al-Ahzab.",
                ),
            ),
        ],
    ),
    chapter(
        4,
        L("Ghazwah Khaybar", "غزوہ خیبر", "ग़ज़वा-ए-ख़ैबर", "গাজওয়ায়ে খাইবার", "Perang Khaibar"),
        L("7 AH / 628 CE", "7ھ / 628ء", "7 हिजरी / 628 ई", "৭ হিজরি / ৬২৮ খ্রি.", "7 H / 628 M"),
        L(
            "After Hudaybiyyah, the Prophet ﷺ marched on Khaybar, a cluster of fortified oases north of Madinah inhabited by Jewish tribes, some of whom had allied against Madinah. The Muslims took the fortresses one by one. Ali ibn Abi Talib distinguished himself at the fortress of Qamus after the Prophet ﷺ said the standard would go to one who loves Allah and His Messenger. Khaybar agreed to remain and farm, giving a share of the produce (kharaj/half the dates). The poisoned sheep of Zaynab bint al-Harith is reported from this campaign.",
            "حدیبیہ کے بعد نبی ﷺ خیبر گئے، مدینہ کے شمال قلعے دار نخلستان، یہودی قبائل جن میں سے بعض نے مدینہ کے خلاف گٹھ جوڑ کیا تھا۔ قلعے ایک ایک کر کے فتح ہوئے۔ علی نے قموص پر نمایاں کردار ادا کیا جب نبی ﷺ نے فرمایا جھنڈا اس کے ہاتھ جسے اللہ اور اس کا رسول محبوب ہیں۔ خیبر رہ کر کھیتی پر راضی، پیداوار کا حصہ۔ زینب بنت حارث کی زہریلی بکری اسی مہم سے مروی ہے۔",
            "हुदैबिया के बाद ख़ैबर पर चढ़ाई। क़िले एक-एक कर फतह। अली ने क़ामूस पर झंडा उठाया। ख़ैबर खेती पर रहा, पैदावार का हिस्सा देना माना।",
            "হুদায়বিয়ার পর খাইবার অভিযান। দুর্গ একের পর এক বিজিত। আলী কামুস দুর্গে পতাকা তোলেন। খাইবার চাষে থেকে ফসলের অংশ দিতে রাজি হয়।",
            "Setelah Hudaibiyah, Nabi ﷺ menuju Khaibar, oasis berbenteng. Benteng jatuh satu per satu. Ali menonjol di Qamus. Khaibar tetap bertani dengan bagi hasil.",
        ),
        [
            item(
                L("The standard and the treaty", "جھنڈا اور معاہدہ", "झंडा और मुआहिदा", "পতাকা ও চুক্তি", "Bendera dan perjanjian"),
                L("After Hudaybiyyah", "حدیبیہ کے بعد", "हुदैबिया के बाद", "হুদায়বিয়ার পর", "Setelah Hudaibiyah"),
                L(
                    "Abu Bakr and Umar carried the standard on successive days without a decisive breach; then Ali, who had been left behind with eye inflammation, was called, his eyes treated, and he killed Marhab according to famous reports. Safiyyah bint Huyayy was later married by the Prophet ﷺ. Khaybar's arrangement became a model for later land treaties.",
                    "ابو بکر اور عمر نے لگاتار دن جھنڈا اٹھایا بغیر فیصلہ کن فتح؛ پھر علی جو آنکھ کی تکلیف سے پیچھے تھے بلائے گئے، آنکھوں کا علاج ہوا، مشہور روایت کے مطابق مرحب کو قتل کیا۔ صفیہ بنت حیي سے بعد میں نکاح ہوا। خیبر کا بندوبست بعد کے زمینی معاہدوں کی مثال بنا।",
                    "अबू बक्र और उमर ने झंडा उठाया; फिर अली बुलाए गए। सफ़िया से बाद निकाह। ख़ैबर का बंदोबस्त बाद के मुआहिदों की मिसाल बना।",
                    "আবু বকর ও উমর পতাকা তোলেন; পরে আলী আহূত হন। সাফিয়্যাহর সঙ্গে পরে বিবাহ হয়। খাইবারের ব্যবস্থা পরবর্তী ভূমিচুক্তির আদর্শ হয়।",
                    "Abu Bakar dan Umar membawa bendera; lalu Ali dipanggil. Safiyyah kemudian dinikahi Nabi ﷺ. Tata Khaibar menjadi model perjanjian tanah.",
                ),
            ),
        ],
    ),
    chapter(
        5,
        L("Ghazwah Mu'tah", "غزوہ موتہ", "ग़ज़वा-ए-मूताह", "গাজওয়ায়ে মুতাহ", "Perang Mutah"),
        L("8 AH / 629 CE", "8ھ / 629ء", "8 हिजरी / 629 ई", "৮ হিজরি / ৬২৯ খ্রি.", "8 H / 629 M"),
        L(
            "A Muslim envoy, al-Harith ibn Umayr, was killed by Shurahbil ibn Amr of Ghassan on the way to the Byzantine frontier. The Prophet ﷺ sent about three thousand under Zayd ibn Harithah, then Ja'far ibn Abi Talib, then Abdullah ibn Rawahah. They met a far larger force near Mu'tah in the Balqa' (modern Jordan). All three commanders were martyred. Khalid ibn al-Walid took command and extracted the army. In Madinah the Prophet ﷺ described the succession of standards in a vision and named Khalid Sayf Allah.",
            "سفیر حارث بن عمیر کو شراحیل بن عمرو غسانی نے رومی سرحد کی راہ میں قتل کیا۔ نبی ﷺ نے تقریباً تین ہزار زید بن حارثہ، پھر جعفر، پھر عبد اللہ بن رواحہ کی کمان میں بھیجے۔ بلقاء (موجودہ اردن) موتہ کے پاس بہت بڑی فوج سے مقابلہ۔ تینوں کمانڈر شہید۔ خالد نے کمان سنبھالی اور لشکر نکالا। مدینہ میں نبی ﷺ نے جھنڈوں کا منظر بیان کیا اور خالد کو سیف اللہ کہا۔",
            "राजदूत की हत्या के बाद तीन हज़ार भेजे गए। ज़ैद, जाफ़र, अब्दुल्लाह बिन रवाहा शहीद। ख़ालिद ने लश्कर बचाया। नबी ﷺ ने सैफुल्लाह कहा।",
            "দূত নিহত হলে প্রায় তিন হাজার প্রেরিত হন। যায়েদ, জাফর, আব্দুল্লাহ ইবন রাওয়াহা শহীদ। খালিদ সেনা উদ্ধার করেন। নবী ﷺ তাঁকে সাইফুল্লাহ বলেন।",
            "Utusan terbunuh; sekitar tiga ribu diberangkatkan. Zaid, Ja'far, Abdullah bin Rawahah syahid. Khalid menyelamatkan pasukan. Nabi ﷺ menamainya Pedang Allah.",
        ),
        [
            item(
                L("Three commanders", "تین کمانڈر", "तीन कमांडर", "তিন সেনাপতি", "Tiga panglima"),
                L("On the Syrian road", "شام کے راستے", "शाम की सड़क", "সিরিয়ার পথে", "Jalan Syam"),
                L(
                    "Zayd was the Prophet's ﷺ freedman and beloved. Ja'far, Ali's brother, fought until both arms were struck; he was called al-Tayyar in Paradise. Ibn Rawahah, a poet of the Ansar, dismounted reciting verses of resolve. Their graves are honoured at Mu'tah.",
                    "زید نبی ﷺ کے آزاد کردہ اور محبوب تھے۔ جعفر، علی کے بھائی، دونوں بازو کٹنے تک لڑے، جنت میں طیّار کہلائے۔ ابن رواحہ انصاری شاعر عزم کے اشعار پڑھتے اترے۔ ان کی قبریں موتہ میں محترم ہیں۔",
                    "ज़ैद नबी ﷺ के आज़ाद किए हुए। जाफ़र दोनों बाजू कटने तक लड़े। इब्न रवाहा अनसारी शाईर। क़ब्रें मूताह में हैं।",
                    "যায়েদ নবী ﷺ-এর মুক্তদাস। জাফর উভয় বাহু কাটা পর্যন্ত যুদ্ধ করেন। ইবন রাওয়াহা আনসার কবি। তাঁদের কবর মুতাহে।",
                    "Zaid maula kekasih Nabi ﷺ. Ja'far berperang hingga kedua lengan terputus, disebut at-Thayyar. Ibnu Rawahah penyair Ansar. Kubur mereka dimuliakan di Mutah.",
                ),
            ),
        ],
    ),
    chapter(
        6,
        L("Fath Makkah", "فتح مکہ", "फत्हे मक्का", "মক্কা বিজয়", "Fathu Makkah"),
        L("8 AH / 630 CE", "8ھ / 630ء", "8 हिजरी / 630 ई", "৮ হিজরি / ৬৩০ খ্রি.", "8 H / 630 M"),
        L(
            "Quraysh violated Hudaybiyyah by backing an attack on Khuza'ah, allies of the Prophet ﷺ. He marched with about ten thousand. Abu Sufyan accepted Islam at the edge of the city. Makkah was entered with almost no fighting; weapons were sheathed except against a few who resisted. The Prophet ﷺ forgave Quraysh: 'Go, for you are free.' Idols were removed from the Ka'bah, and the city that had driven him out became the heart of the Ummah again.",
            "قریش نے حدیبیہ توڑی، خزاعہ پر حملے کی حمایت کی جو نبی ﷺ کے حلیف تھے۔ تقریباً دس ہزار کے ساتھ روانہ۔ ابو سفیان شہر کے کنارے اسلام لائے۔ مکہ تقریباً بغیر لڑائی داخل، چند مزاحمتیوں کے سوا ہتھیار بند۔ فرمایا جاؤ تم آزاد ہو۔ کعبہ سے بت ہٹائے، وہ شہر جس نے نکالا تھا امت کا مرکز پھر بنا।",
            "कुरैश ने हुदैबिया तोड़ी। दस हज़ार के साथ मक्का लगभग बिना लड़ाई फतह। कुरैश को माफ़ किया। काबा से बुत हटाए।",
            "কুরাইশ হুদায়বিয়া ভঙ্গ করে। প্রায় দশ হাজার নিয়ে প্রায় বিনা যুদ্ধে মক্কা বিজিত। তিনি ক্ষমা করেন। কাবা থেকে মূর্তি সরানো হয়।",
            "Quraisy merusak Hudaibiyah. Sekitar sepuluh ribu masuk Makkah hampir tanpa perang. Beliau memaafkan: 'Pergilah, kalian bebas.' Berhala di Ka'bah dihapus.",
        ),
        [
            item(
                L("Amnesty and the Ka'bah", "عام معافی اور کعبہ", "आम माफ़ी और काबा", "সাধারণ ক্ষমা ও কাবা", "Ampunan dan Ka'bah"),
                L("The conquest", "فتح", "फतह", "বিজয়", "Penaklukan"),
                L(
                    "A few named persons were excepted from general amnesty for crimes; some were later pardoned. Bilal gave adhan from the Ka'bah. The keys remained with the family of Uthman ibn Talhah as the Prophet ﷺ had promised. Many of Quraysh entered Islam after seeing this forbearance.",
                    "چند نامزد افراد عام معافی سے مستثنیٰ تھے سنگین جرائم پر؛ بعض بعد میں معاف ہوئے। بلال نے کعبہ پر اذان دی۔ کنجیاں عثمان بن طلحہ کے خاندان کے پاس رہیں جیسا وعدہ تھا۔ یہ برداشت دیکھ کر بہت سے قریش مسلمان ہوئے۔",
                    "कुछ नाम आम माफ़ी से बाहर थे। बिलाल ने काबा पर अज़ान दी। कुंजियां उसी ख़ानदान के पास रहीं। इस सब्र को देख कुरैश के बहुत इस्लाम लाए।",
                    "কয়েকজন সাধারণ ক্ষমা থেকে বাদ। বিলাল কাবায় আজান দেন। চাবি উসমান ইবন তালহার পরিবারেই থাকে। এই সহিষ্ণুতা দেখে অনেকে ইসলাম গ্রহণ করেন।",
                    "Beberapa orang dikecualikan dari ampunan umum. Bilal azan di Ka'bah. Kunci tetap pada keluarga Utsman bin Thalhah. Banyak Quraisy masuk Islam karena kesabaran ini.",
                ),
            ),
        ],
    ),
    chapter(
        7,
        L("Ghazwah Hunayn and Ta'if", "غزوہ حنین اور طائف", "ग़ज़वा-ए-हुनैन और ताइफ़", "গাজওয়ায়ে হুনাইন ও তায়েফ", "Perang Hunain dan Thaif"),
        L("8 AH / 630 CE", "8ھ / 630ء", "8 हिजरी / 630 ई", "৮ হিজরি / ৬৩০ খ্রি.", "8 H / 630 M"),
        L(
            "Hawazin and Thaqif gathered at Hunayn after the Conquest of Makkah. The large Muslim army was ambushed in a valley and initially fled. The Prophet ﷺ stood firm with a few, and the Muslims rallied to a victory mentioned in the Quran (9:25–26). Captives and flocks were taken, then many of Hawazin were released as a gift. Ta'if was besieged but not stormed; Thaqif accepted Islam later. The Prophet ﷺ lingered at al-Ji'ranah to distribute booty and perform umrah.",
            "فتح مکہ کے بعد ہوازن اور ثقیف حنین پر اکٹھے ہوئے۔ بڑا اسلامی لشکر وادی میں گھात کھا کر پہلے بھگا। نبی ﷺ چند لوگوں کے ساتھ جمے رہے، مسلمان پلٹے، قرآن میں مذکور فتح (9:25–26)۔ قیدی اور ریوڑ، پھر ہوازن کے بہت سے قیدی احساناً چھوڑے گئے۔ طائف کا محاصرہ ہوا مگر زور سے نہ توڑا؛ ثقیف بعد میں اسلام لائے۔ جعرانہ میں مال تقسیم اور عمرہ۔",
            "हवाज़िन और सक़ीफ़ हुनैन पर जमा हुए। पहले मुसलमान घबराए, नबी ﷺ डटे रहे, फतह हुई। ताइफ़ घेरा गया, सक़ीफ़ बाद में इस्लाम लाए।",
            "হাওয়াজিন ও সাকিফ হুনাইনে জড়ো হয়। প্রথমে মুসলিমরা ছত্রভঙ্গ, নবী ﷺ স্থির থাকেন, বিজয় হয়। তায়েফ অবরোধ হয়, সাকিফ পরে ইসলাম গ্রহণ করে।",
            "Hawazin dan Saqif berkumpul di Hunain. Pasukan muslim sempat kocar-kacir, Nabi ﷺ tetap berdiri, lalu menang (9:25–26). Thaif dikepung; Saqif masuk Islam kemudian.",
        ),
        [
            item(
                L("Pride and then victory", "غرور پھر فتح", "घमंड फिर फतह", "অহংকার ও পরে বিজয়", "Bangga lalu menang"),
                L("After Makkah", "فتح مکہ کے بعد", "फत्हे मक्का के बाद", "মক্কা বিজয়ের পর", "Setelah Fathu Makkah"),
                L(
                    "Some newly joined people trusted in numbers. The Quran reminds that Allah helped when they were few. After victory the Prophet ﷺ gave larger gifts to new Muslims of Quraysh (mu'allafa qulubuhum) to reconcile hearts, and the Ansar were reassured that they remained his inner companions.",
                    "کچھ نئے شامل لوگوں نے کثرت پر بھروسہ کیا۔ قرآن یاد دلاتا ہے اللہ نے اس وقت مدد کی جب وہ کم تھے۔ فتح کے بعد نئے مسلماں قریش کو زیادہ حصہ (مؤلفۃ القلوب) دیا تاکہ دل جڑیں، انصار کو یقین دلایا کہ وہ اندرونی ساتھی ہیں۔",
                    "कुछ ने तादाद पर भरोसा किया। फतह के बाद नए मुसलमानों को ज़्यादा हिस्सा दिया दिल जोड़ने को, अनसार को तसल्ली दी।",
                    "কেউ কেউ সংখ্যায় ভরসা করে। বিজয়ের পর নতুন মুসলিমদের বেশি অংশ দিয়ে হৃদয় জয় করা হয়, আনসারকে প্রত্যয় দেওয়া হয়।",
                    "Sebagian mengandalkan jumlah. Setelah menang Nabi ﷺ memberi lebih kepada mualaf Quraisy dan menenangkan Ansar bahwa mereka tetap sahabat inti.",
                ),
            ),
        ],
    ),
    chapter(
        8,
        L("Ghazwah Tabuk", "غزوہ تبوک", "ग़ज़वा-ए-तबूक", "গাজওয়ায়ে তাবুক", "Perang Tabuk"),
        L("9 AH / 630 CE", "9ھ / 630ء", "9 हिजरी / 630 ई", "৯ হিজরি / ৬৩০ খ্রি.", "9 H / 630 M"),
        L(
            "Reports of a Byzantine gathering in the north led the Prophet ﷺ to call an expedition in intense heat and scarcity — the Year of Difficulty (Am al-Usrah). Uthman equipped the army generously. About thirty thousand marched to Tabuk on the road to Syria. No major battle occurred; border tribes made peace. Hypocrites who stayed behind without excuse are rebuked in Surah al-Tawbah. The three who remained behind then told the truth (Ka'b ibn Malik and two others) were boycotted until Allah accepted their repentance (9:118).",
            "شمال میں رومی اجتماع کی خبر پر نبی ﷺ نے شدید گرمی اور تنگی میں لشکر بلاया — عام العسرہ۔ عثمان نے خوب سازو سامان دیا۔ تقریباً تیس ہزار تبوک شام کی راہ پر گئے۔ بڑی لڑائی نہ ہوئی؛ سرحدی قبائل صلح پر آئے۔ بغیر عذر پیچھے رہنے والے منافق سورہ توبہ میں ملامت۔ جو سچ بولے (کعب بن مالک وغیرہ) بائیکاٹ رہے یہاں تک کہ اللہ نے توبہ قبول کی (9:118)۔",
            "उत्तर में रूमी जमाव की ख़बर पर गर्मी में लश्कर। उसमान ने साज़ो सामान दिया। तबूक तक गए, बड़ी लड़ाई नहीं। सुरह तौबा में मुनाफ़िक़ों की मलामत।",
            "উত্তরে রোমান জমায়েতের খবর তীব্র গরমে অভিযান। উসমান সেনা সজ্জিত করেন। তাবুকে বড় যুদ্ধ হয়নি। সূরা তাওবায় মুনাফিকদের নিন্দা।",
            "Kabar pasukan Rum di utara; ekspedisi di panas dan susah. Utsman membekali pasukan. Sekitar tiga puluh ribu ke Tabuk, tanpa pertempuran besar. Surah at-Taubah mencela munafik yang tinggal.",
        ),
        [
            item(
                L("The Year of Difficulty", "عام العسرہ", "आम उल-उसरा", "আম আল-উসরাহ", "Tahun Kesulitan"),
                L("The last campaign he led", "آخری مہم جو خود قیادت کی", "आख़िरी मुहिम जो ख़ुद क़ियादत की", "তাঁর নিজের নেতৃত্বাধীন শেষ অভিযান", "Ekspedisi terakhir yang beliau pimpin"),
                L(
                    "This was the last ghazwah the Prophet ﷺ led in person. On the return, the mosque of dirar (harm) was ordered demolished (9:107–110). Delegations continued to come to Madinah. Tabuk showed that the Ummah could mobilise at scale even in hardship, and that sincerity was tested when there was no booty in sight.",
                    "یہ آخری غزوہ تھا جس کی قیادت نبی ﷺ نے خود کی۔ واپسی پر مسجد ضرار گرانے کا حکم ہوا (9:107–110)۔ وفود مدینہ آتے رہے۔ تبوک نے دکھایا کہ تنگی میں بھی امت بڑے پیمانے پر نکل سکتی ہے، اور جب مال نظر نہ ہو تو اخلاص آزمایا جاتا ہے۔",
                    "यह आख़िरी ग़ज़वा था जिसकी क़ियादत नबी ﷺ ने ख़ुद की। वापसी पर मस्जिदे ज़िरार गिराने का हुक्म। तबूक ने इख़लास आज़माया जब ग़नीमत न थी।",
                    "এটি তাঁর নিজের নেতৃত্বাধীন শেষ গাজওয়া। ফেরার পথে মসজিদে দিরার ভাঙার নির্দেশ। তাবুক দেখায় কষ্টেও উম্মাহ সজ্জিত হতে পারে, গনিমত না থাকলে ইখলাস পরীক্ষিত হয়।",
                    "Ini ghazwah terakhir yang dipimpin Nabi ﷺ sendiri. Sejumlah masjid dhirar diperintahkan dihancurkan. Tabuk menguji keikhlasan saat tidak ada ganimah.",
                ),
            ),
        ],
    ),
]


def _write(name, data):
    path = OUT / name
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(data)} chapters to {path}")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    _write("sahaba.json", SAHABA)
    _write("ghazawat.json", GHAZAWAT)
