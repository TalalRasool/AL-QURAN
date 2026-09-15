# -*- coding: utf-8 -*-
"""Seed localized Seerah JSON (en, ur, hi, bn, id)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "json" / "seerah.json"


def L(en, ur, hi, bn, idn):
    return {"en": en, "ur": ur, "hi": hi, "bn": bn, "id": idn}


def item(title, heading, details):
    return {"title": title, "heading": heading, "details": details}


CHAPTERS = [
    {
        "chapter_id": 1,
        "title": L(
            "Lineage & Family",
            "خاندان اور نسب",
            "वंश और परिवार",
            "বংশ ও পরিবার",
            "Silsilah & Keluarga",
        ),
        "heading": L(
            "Qabila, Father, and Mother",
            "قبیلہ، والد اور والدہ",
            "क़बीला, पिता और माता",
            "গোত্র, পিতা ও মাতা",
            "Suku, Ayah, dan Ibu",
        ),
        "details": L(
            "Prophet Muhammad ﷺ belonged to the noble tribe of Quraysh, from the house of Banu Hashim in Makkah. Classical seerah works (Ibn Ishaq, Ibn Hisham, Ibn Sa'd) record his lineage through Adnan back to Ismail, son of Ibrahim ﷺ. He was an orphan of both parents, raised first by his grandfather Abd al-Muttalib and then by his uncle Abu Talib.",
            "نبی کریم ﷺ کا تعلق مکہ میں بنو ہاشم کے خاندان اور قریش کے معزز قبیلے سے تھا۔ کلاسیکی سیرت کی کتابیں (ابن اسحاق، ابن ہشام، ابن سعد) آپ کا نسب عدنان کے ذریعے اسماعیل بن ابراہیم ﷺ تک بیان کرتی ہیں۔ آپ دونوں والدین سے یتیم تھے؛ پہلے دادا عبد المطلب نے اور پھر چچا ابو طالب نے پرورش کی۔",
            "पैगंबर मुहम्मद ﷺ कुरैश के महान क़बीले और मक्का में बनू हाशिम के घराने से थे। क्लासिकल सीरत (इब्न इसहाक, इब्न हिशाम, इब्न साद) आपका वंश अदनान के ज़रिए इस्माईल बिन इबराहीम ﷺ तक बताती हैं। आप माता-पिता दोनों से यतीम थे; पहले दादा अब्दुल मुत्तलिब ने और फिर चाचा अबू तालिब ने परवरिश की।",
            "নবী মুহাম্মদ ﷺ মক্কায় বনু হাশিম গোষ্ঠী ও সম্মানিত কুরাইশ বংশের অন্তর্ভুক্ত ছিলেন। ক্লাসিক সিরাতগ্রন্থ (ইবন ইসহাক, ইবন হিশাম, ইবন সাদ) আদনানের মাধ্যমে ইসমাইল ইবন ইবরাহিম ﷺ পর্যন্ত তাঁর বংশধারা লিপিবদ্ধ করে। তিনি পিতা-মাতা উভয়ের দিক থেকে ইয়াতিম ছিলেন; প্রথমে দাদা আব্দুল মুত্তালিব ও পরে চাচা আবু তালিব তাঁকে লালন করেন।",
            "Nabi Muhammad ﷺ berasal dari suku Quraisy yang mulia, dari Bani Hasyim di Makkah. Kitab sirah klasik (Ibnu Ishaq, Ibnu Hisyam, Ibnu Sa'd) mencatat nasab beliau melalui Adnan hingga Ismail putra Ibrahim ﷺ. Beliau yatim dari kedua orang tua, diasuh kakeknya Abdul Muththalib kemudian paman Abu Thalib.",
        ),
        "items": [
            item(
                L("The tribe of Quraysh", "قبیلہ قریش", "कुरैश क़बीला", "কুরাইশ গোত্র", "Suku Quraisy"),
                L("Qabila", "قبیلہ", "क़बीला", "গোত্র", "Suku"),
                L(
                    "Quraysh were the custodians of the Ka'bah and the leading tribe of Makkah. Within Quraysh, Banu Hashim were known for honour, generosity, and serving pilgrims with water (siqayah) and hospitality. The Prophet ﷺ said, 'Allah chose Kinanah from the children of Ismail, Quraysh from Kinanah, Banu Hashim from Quraysh, and me from Banu Hashim' (Muslim).",
                    "قریش خانہ کعبہ کے متولی اور مکہ کے سب سے بڑے قبیلے تھے۔ قریش میں بنو ہاشم عزت، سخاوت اور حاجیوں کو پانی پلانے (سقایہ) اور مہمان نوازی کے لیے مشہور تھے۔ نبی ﷺ نے فرمایا: 'اللہ نے اسماعیل کی اولاد سے کنانہ کو چنا، کنانہ سے قریش کو، قریش سے بنو ہاشم کو، اور بنو ہاشم سے مجھے چنا' (مسلم)۔",
                    "कुरैश काबा के रखवाले और मक्का के प्रमुख क़बीले थे। कुरैश में बनू हाशिम इज़्ज़त, سخاवत और हाजियों को पानी (सिक़ाया) देने के लिए मशहूर थे। नबी ﷺ ने फ़रमाया: 'अल्लाह ने इस्माईल की औलाद से किनाना को चुना, किनाना से कुरैश, कुरैश से बनू हाशिम, और बनू हाशिम से मुझे चुना' (मुस्लिम)।",
                    "কুরাইশ ছিল কাবার রক্ষক ও মক্কার প্রধান গোত্র। কুরাইশের মধ্যে বনু হাশিম সম্মান, দানশীলতা এবং হাজীদের পানি সরবরাহ (সিকায়াহ) ও আতিথেয়তার জন্য খ্যাত। নবী ﷺ বলেছেন, 'আল্লাহ ইসমাইলের সন্তানদের থেকে কিনানাহকে বেছে নিয়েছেন, কিনানাহ থেকে কুরাইশকে, কুরাইশ থেকে বনু হাশিমকে, আর বনু হাশিম থেকে আমাকে' (মুসলিম)।",
                    "Quraisy adalah penjaga Ka'bah dan suku terkemuka Makkah. Di antara Quraisy, Bani Hasyim dikenal mulia, dermawan, dan melayani jamaah dengan air (siqayah) serta jamuan. Nabi ﷺ bersabda, 'Allah memilih Kinanah dari anak Ismail, Quraisy dari Kinanah, Bani Hasyim dari Quraisy, dan aku dari Bani Hasyim' (Muslim).",
                ),
            ),
            item(
                L("Abdullah ibn Abd al-Muttalib", "عبد اللہ بن عبد المطلب", "अब्दुल्लाह इब्न अब्दुल मुत्तलिब", "আব্দুল্লাহ ইবন আব্দুল মুত্তালিব", "Abdullah bin Abdul Muththalib"),
                L("Father", "والد", "पिता", "পিতা", "Ayah"),
                L(
                    "His father was Abdullah, son of Abd al-Muttalib (Shaybah), chief of Banu Hashim. He married Aminah bint Wahb of Banu Zuhrah. Abdullah died in Yathrib (later Madinah) while returning from a trade journey to Syria, before the birth of his son, at about twenty-five years of age. Thus the Prophet ﷺ was born a paternal orphan.",
                    "آپ کے والد عبد اللہ تھے، عبد المطلب (شیبہ) کے بیٹے جو بنو ہاشم کے سردار تھے۔ انہوں نے بنو زہرہ کی آمنہ بنت وہب سے شادی کی۔ عبد اللہ شام کے تجارتی سفر سے واپسی پر یثرب (بعد میں مدینہ) میں فوت ہوئے، بیٹے کی ولادت سے پہلے، تقریباً پچیس سال کی عمر میں۔ یوں نبی ﷺ باپ کی طرف سے یتیم پیدا ہوئے۔",
                    "आपके वालिद अब्दुल्लाह थे, अब्दुल मुत्तलिब (शैबा) के बेटे, बनू हाशिम के सरदार। उन्होंने बनू ज़ुहरा की आमिना बिन्त वहब से निकाह किया। अब्दुल्लाह शाम के तिजारती सफ़र से लौटते हुए यसरिब (बाद में मदीना) में फ़ौत हुए, बेटे की विलादत से पहले, लगभग पच्चीस वर्ष की उम्र में। यूँ नबी ﷺ बाप की तरफ़ से यतीम पैदा हुए।",
                    "তাঁর পিতা ছিলেন আব্দুল্লাহ, বনু হাশিমের নেতা আব্দুল মুত্তালিব (শাইবাহ)-এর পুত্র। তিনি বনু যুহরাহর আমিনাহ বিনত ওয়াহাবকে বিয়ে করেন। আব্দুল্লাহ সিরিয়ার বাণিজ্য সফর থেকে ফেরার পথে ইয়াসরিবে (পরে মদিনা) মারা যান, পুত্রের জন্মের আগে, প্রায় পঁচিশ বছর বয়সে। এভাবে নবী ﷺ পিতৃহীন ইয়াতিম হিসেবে জন্মগ্রহণ করেন।",
                    "Ayah beliau adalah Abdullah, putra Abdul Muththalib (Syaibah), pemuka Bani Hasyim. Ia menikah dengan Aminah binti Wahb dari Bani Zuhrah. Abdullah meninggal di Yastrib (kemudian Madinah) saat pulang dari dagang ke Syam, sebelum putranya lahir, sekitar usia dua puluh lima tahun. Dengan itu Nabi ﷺ lahir sebagai yatim piatu dari pihak ayah.",
                ),
            ),
            item(
                L("Aminah bint Wahb", "آمنہ بنت وہب", "आमिना बिन्त वहब", "আমিনাহ বিনত ওয়াহাব", "Aminah binti Wahb"),
                L("Mother", "والدہ", "माता", "মাতা", "Ibu"),
                L(
                    "His mother was Aminah bint Wahb ibn Abd Manaf ibn Zuhrah, from Banu Zuhrah, among the noble clans of Quraysh. After Abdullah's death she cared for the infant Muhammad ﷺ in Makkah. When he was about six, she took him to visit relatives in Yathrib. On the return she died at al-Abwa', between Makkah and Madinah. The Prophet ﷺ later visited her grave in the year of Hudaybiyyah and wept for her.",
                    "آپ کی والدہ آمنہ بنت وہب بن عبد مناف بن زہرہ تھیں، بنو زہرہ سے، قریش کے معزز خاندانوں میں سے۔ عبد اللہ کی وفات کے بعد انہوں نے مکہ میں محمد ﷺ کی پرورش کی۔ جب آپ تقریباً چھ سال کے تھے تو وہ آپ کو یثرب کے رشتہ داروں کے پاس لے گئیں۔ واپسی پر الاواء میں وفات پا گئیں، مکہ اور مدینہ کے درمیان۔ نبی ﷺ نے حدیبیہ کے سال ان کی قبر کی زیارت کی اور رویے۔",
                    "आपकी वालिदा आमिना बिन्त वहब बिन्त अब्द मनाफ़ इब्न ज़ुहरा थीं, बनू ज़ुहरा से, कुरैश के शरीफ़ घरानों में से। अब्दुल्लाह की वफ़ात के बाद उन्होंने मक्का में मुहम्मद ﷺ की परवरिश की। जब आप लगभग छह वर्ष के थे, वे आपको यसरिब के रिश्तेदारों के पास ले गईं। वापसी पर अल-अबवा में उनका इंतिक़ाल हुआ। नबी ﷺ ने हुदैबिया के साल उनकी क़ब्र की ज़ियारत की और रोए।",
                    "তাঁর মাতা ছিলেন আমিনাহ বিনত ওয়াহাব ইবন আব্দ মানাফ ইবন যুহরাহ, সম্মানিত কুরাইশ গোত্র বনু যুহরাহ থেকে। আব্দুল্লাহর মৃত্যুর পর তিনি মক্কায় শিশু মুহাম্মদ ﷺ-কে লালন করেন। প্রায় ছয় বছর বয়সে তিনি তাঁকে ইয়াসরিবের আত্মীয়দের কাছে নিয়ে যান। ফেরার পথে মক্কা ও মদিনার মাঝে আল-আবওয়ায় তিনি মারা যান। নবী ﷺ হুদায়বিয়ার বছরে তাঁর কবর যিয়ারত করে কেঁদেছিলেন।",
                    "Ibu beliau adalah Aminah binti Wahb bin Abd Manaf bin Zuhrah, dari Bani Zuhrah, klan mulia Quraisy. Setelah Abdullah wafat ia merawat bayi Muhammad ﷺ di Makkah. Ketika beliau berusia sekitar enam tahun, Aminah membawanya menemui kerabat di Yastrib. Dalam perjalanan pulang ia wafat di al-Abwa'. Nabi ﷺ kemudian menziarahi kuburnya pada tahun Hudaibiyah dan menangis.",
                ),
            ),
            item(
                L("Abd al-Muttalib and Abu Talib", "عبد المطلب اور ابو طالب", "अब्दुल मुत्तलिब और अबू तालिब", "আব্দুল মুত্তালিব ও আবু তালিব", "Abdul Muththalib dan Abu Thalib"),
                L("Grandfather and uncle", "دادا اور چچا", "दादा और चाचा", "দাদা ও চাচা", "Kakek dan paman"),
                L(
                    "After Aminah's death, grandfather Abd al-Muttalib took him with special affection. Abd al-Muttalib died when the Prophet ﷺ was about eight. Guardianship passed to uncle Abu Talib, who raised him, took him on a Syrian caravan in youth, and later protected him for many years after Prophethood, though Abu Talib remained upon the religion of Quraysh. That protection helped the early Muslims in Makkah survive as a community.",
                    "آمنہ کی وفات کے بعد دادا عبد المطلب نے بڑی شفقت سے آپ کو اپنے پاس رکھا۔ عبد المطلب اس وقت فوت ہوئے جب نبی ﷺ تقریباً آٹھ سال کے تھے۔ کفالت چچا ابو طالب کے سپرد ہوئی جنہوں نے پرورش کی، جوانی میں شام کے قافلے پر ساتھ لے گئے، اور نبوت کے بعد برسوں حفاظت کی حالانکہ وہ قریش کے دین پر رہے۔ یہ حفاظت مکہ میں ابتدائی مسلمانوں کی بقا کی بڑی وجہ بنی۔",
                    "आमिना की वफ़ात के बाद दादा अब्दुल मुत्तलिब ने बड़ी मुहब्बत से आपको अपने पास रखा। अब्दुल मुत्तलिब तब फ़ौत हुए जब नबी ﷺ लगभग आठ वर्ष के थे। किफ़ालत चाचा अबू तालिब को मिली, जिन्होंने परवरिश की, जवानी में शाम के काफ़िले पर साथ लिया, और नबुव्वत के बाद सालों हिफ़ाज़त की।",
                    "আমিনাহর মৃত্যুর পর দাদা আব্দুল মুত্তালিব বিশেষ স্নেহে তাঁকে কাছে রাখেন। নবী ﷺ-এর প্রায় আট বছর বয়সে তিনি মারা যান। অভিভাবকত্ব চাচা আবু তালিবের হাতে যায়, যিনি তাঁকে লালন করেন, যৌবনে সিরিয়ার কাফেলায় নিয়ে যান এবং নবুয়তের পর বহু বছর রক্ষা করেন।",
                    "Setelah Aminah wafat, kakek Abdul Muththalib mengasuhnya dengan kasih sayang istimewa. Ia meninggal ketika Nabi ﷺ berusia sekitar delapan tahun. Perwalian beralih ke paman Abu Thalib, yang membesarkan beliau, membawanya dalam kafilah Syam, dan melindungi beliau bertahun-tahun setelah kenabian.",
                ),
            ),
        ],
    },
    {
        "chapter_id": 2,
        "title": L(
            "Early Life & Marriage",
            "ابتدائی زندگی اور نکاح",
            "प्रारंभिक जीवन और विवाह",
            "প্রাথমিক জীবন ও বিবাহ",
            "Kehidupan Awal & Pernikahan",
        ),
        "heading": L(
            "Childhood, youth, and the first marriage",
            "بچپن، جوانی اور پہلی شادی",
            "बचपन, जवानी और पहला निकाह",
            "শৈশব, যৌবন ও প্রথম বিবাহ",
            "Masa kanak, pemuda, dan pernikahan pertama",
        ),
        "details": L(
            "Before revelation, Muhammad ﷺ was known in Makkah as al-Amin (the Trustworthy) and al-Sadiq (the Truthful). He worked as a shepherd, then in trade. His first marriage, to Khadijah bint Khuwaylid رضي الله عنها, lasted about twenty-five years and was the foundation of his household until her death.",
            "وحی سے پہلے مکہ میں محمد ﷺ امین (ایماندار) اور صادق (سچے) کے نام سے مشہور تھے۔ آپ نے چرواہی کی، پھر تجارت۔ پہلی شادی حضرت خدیجہ بنت خویلد رضی اللہ عنہا سے ہوئی جو تقریباً پچیس سال رہی اور ان کی وفات تک گھر کا مدار رہیں۔",
            "वही से पहले मक्का में मुहम्मद ﷺ अमीन (ईमानदार) और सादिक़ (सच्चे) कहलाते थे। आपने चरवाही की, फिर तिजारत। पहला निकाह हज़रत ख़दीजा बिन्त ख़ुवैलिद رضي الله عنها से हुआ, लगभग पच्चीस साल चला, और उनकी वफ़ात तक घर की बुनियाद रहा।",
            "ওহীর আগে মক্কায় মুহাম্মদ ﷺ আল-আমীন (বিশ্বস্ত) ও আস-সাদিক (সত্যবাদী) নামে পরিচিত ছিলেন। তিনি মেষপালক ও পরে ব্যবসায়ী ছিলেন। প্রথম বিবাহ খাদিজাহ বিনত খুওয়াইলিদ রাদিয়াল্লাহু আনহার সঙ্গে প্রায় পঁচিশ বছর স্থায়ী হয় এবং তাঁর মৃত্যু পর্যন্ত তাঁর ঘরের ভিত্তি ছিল।",
            "Sebelum wahyu, Muhammad ﷺ dikenal di Makkah sebagai al-Amin (yang tepercaya) dan as-Shadiq (yang jujur). Beliau menggembala, lalu berdagang. Pernikahan pertama dengan Khadijah binti Khuwailid radhiyallahu anha berlangsung sekitar dua puluh lima tahun hingga beliau wafat.",
        ),
        "items": [
            item(
                L("Birth and infancy", "ولادت اور بچپن", "विलादत और बचपन", "জন্ম ও শৈশব", "Kelahiran dan masa bayi"),
                L("The Year of the Elephant", "عام الفیل", "हाथी वाला साल", "হস্তী বর্ষ", "Tahun Gajah"),
                L(
                    "He was born in Makkah in the Year of the Elephant, widely dated to 570 or 571 CE, on a Monday in Rabi' al-Awwal. By Qurayshi custom he was nursed in the desert among Banu Sa'd. His wet nurse was Halimah bint Abi Dhu'ayb al-Sa'diyyah. Seerah reports blessing in her household during his stay. A well-known report describes the opening of his chest by angels in childhood.",
                    "آپ مکہ میں عام الفیل میں پیدا ہوئے، عام طور پر 570 یا 571 عیسوی، ربیع الاول کے پیر کے دن۔ قریشی رسم کے مطابق بنو سعد میں صحرا میں دودھ پلایا گیا۔ دایہ حلیمہ بنت ابی ذؤیب سعدیہ تھیں۔ سیرت میں ان کے گھر میں برکت کا ذکر ہے۔ مشہور روایت میں بچپن میں فرشتوں کے سینہ چیرنے کا واقعہ ہے۔",
                    "आप मक्का में आम उल-फ़ील में पैदा हुए, आमतौर पर 570 या 571 ईस्वी, रबीउल अव्वल के सोमवार। कुरैशी रिवायत के मुताबिक बनू सअद में रेगिस्तान में दूध पिलाया गया। दाई हलीमा बिन्त अबी ज़ुऐब सअदिया थीं।",
                    "তিনি মক্কায় হস্তী বর্ষে জন্মগ্রহণ করেন, সাধারণত ৫৭০ বা ৫৭১ খ্রিস্টাব্দ, রবিউল আউয়ালের সোমবার। কুরাইশ রীতি অনুসারে বনু সাদের মধ্যে মরুভূমিতে তাঁকে দুধ পান করানো হয়। ধাত্রী ছিলেন হালিমাহ বিনত আবি যুআইব আস-সাদিয়্যাহ।",
                    "Beliau lahir di Makkah pada Tahun Gajah, umumnya 570 atau 571 M, hari Senin di Rabiul Awal. Menurut adat Quraisy beliau disusui di padang pasir di Bani Sa'd. Ibu susunya Halimah binti Abi Dzu'aib as-Sa'diyyah.",
                ),
            ),
            item(
                L("Youth and the Hilf al-Fudul", "جوانی اور حلف الفضول", "जवानी और हिल्फ़ उल-फ़ुज़ूल", "যৌবন ও হিলফ আল-ফুদুল", "Masa muda dan Hilf al-Fudul"),
                L("Character before Prophethood", "نبوت سے پہلے کردار", "नबुव्वत से पहले चरित्र", "নবুয়তের আগে চরিত্র", "Akhlak sebelum kenabian"),
                L(
                    "He grew up poor but honourable, tending sheep and later accompanying trade. He took part in the Hilf al-Fudul, a pact of Quraysh to defend the oppressed in Makkah, and later said he would still honour such a pact in Islam. When the Ka'bah was rebuilt after a flood, clans disputed who should place the Black Stone. They accepted his judgment: he placed it on a cloak so each clan held an edge, then set it with his own hands, preventing bloodshed.",
                    "آپ غریب مگر باعزت پروان چڑھے، بکریاں چرائیں پھر تجارت میں شریک ہوئے۔ حلف الفضول میں شریک ہوئے، مکہ میں مظلوم کی حمایت کا معاہدہ، اور بعد میں فرمایا اسلام میں بھی ایسے حلف کو پورا کرتے۔ سیلاب کے بعد کعبہ کی تعمیر پر حجر اسود رکھنے پر جھگڑا ہوا تو آپ کے فیصلے سے کپڑے پر پتھر رکھا گیا اور ہر قبیلے نے کنارہ پکڑا، پھر آپ نے خود بٹھایا۔",
                    "आप ग़रीब मगर बाइज़्ज़त बड़े हुए। हिल्फ़ उल-फ़ुज़ूल में शामिल हुए। काबा की मरम्मत पर हजरे असवद रखने का झगड़ा आपके फ़ैसले से टला।",
                    "তিনি দরিদ্র কিন্তু সম্মানিত হয়ে বেড়ে ওঠেন। হিলফ আল-ফুদুলে অংশ নেন, মক্কায় নিপীড়িতদের রক্ষার চুক্তি। কাবা পুনর্নির্মাণে হাজারে আসওয়াদ স্থাপন নিয়ে বিবাদ তাঁর ফয়সালায় মিটে যায়।",
                    "Beliau tumbuh miskin tapi mulia. Beliau ikut Hilf al-Fudul, perjanjian Quraisy membela orang tertindas. Saat Ka'bah dibangun ulang, sengketa Hajar Aswad diselesaikan dengan keputusan beliau.",
                ),
            ),
            item(
                L("Marriage to Khadijah", "حضرت خدیجہ سے نکاح", "ख़दीजा से निकाह", "খাদিজাহর সঙ্গে বিবাহ", "Pernikahan dengan Khadijah"),
                L("First marriage", "پہلی شادی", "पहला निकाह", "প্রথম বিবাহ", "Pernikahan pertama"),
                L(
                    "Khadijah bint Khuwaylid was a noble, wealthy widow of Quraysh. She hired Muhammad ﷺ to take her goods to Syria. Impressed by his honesty, she proposed marriage. He was twenty-five; she was forty according to the most common seerah report. She was his only wife during her lifetime. Their children included al-Qasim, Zaynab, Ruqayyah, Umm Kulthum, Fatimah, and Abdullah. All his children except Ibrahim were from Khadijah. Fatimah رضي الله عنها married Ali ibn Abi Talib; from her come al-Hasan and al-Husayn.",
                    "خدیجہ بنت خویلد قریش کی معزز، مالدار بیوہ تھیں۔ انہوں نے محمد ﷺ کو شام سامان لے جانے پر مقرر کیا۔ دیانت داری دیکھ کر نکاح کی پیشکش کی۔ آپ پچیس سال کے تھے؛ مشہور قول کے مطابق وہ چالیس سال کی تھیں۔ ان کی زندگی میں آپ کی اکیلی بیوی رہیں۔ اولاد میں قاسم، زینب، رقیہ، ام کلثوم، فاطمہ اور عبد اللہ۔ ابراہیم کے سوا سب خدیجہ سے تھیں۔ فاطمہ رضی اللہ عنہا کا نکاح علی سے ہوا، حسن و حسین انہیں سے ہیں۔",
                    "ख़दीजा बिन्त ख़ुवैलिद कुरैश की शरीफ़, दौलतमंद विधवा थीं। उन्होंने मुहम्मद ﷺ को शाम माल ले जाने पर रखा। ईमानदारी देखकर निकाह की पेशकश की। आप पच्चीस थे; मशहूर कौल के मुताबिक वे चालीस थीं। उनकी ज़िंदगी में आप की अकेली बीवी रहीं।",
                    "খাদিজাহ বিনত খুওয়াইলিদ ছিলেন সম্ভ্রান্ত, ধনাঢ্য কুরাইশ বিধবা। তিনি মুহাম্মদ ﷺ-কে সিরিয়ায় পণ্য নিয়ে যেতে নিযুক্ত করেন। সততায় মুগ্ধ হয়ে তিনি বিয়ের প্রস্তাব দেন। তিনি ছিলেন পঁচিশ; প্রসিদ্ধ বর্ণনায় খাদিজাহ চল্লিশ। তাঁর জীবদ্দশায় তিনিই ছিলেন একমাত্র স্ত্রী।",
                    "Khadijah binti Khuwailid adalah janda Quraisy yang mulia dan kaya. Ia mempekerjakan Muhammad ﷺ membawa dagangan ke Syam. Terkesan akan kejujurannya, ia meminang. Beliau berusia dua puluh lima; menurut riwayat terkenal Khadijah berusia empat puluh. Ia satu-satunya istri selama hayatnya.",
                ),
            ),
        ],
    },
    {
        "chapter_id": 3,
        "title": L(
            "Prophethood (Nabawat)",
            "نبوت",
            "नबुव्वत",
            "নবুয়ত",
            "Kenabian (Nubuwah)",
        ),
        "heading": L(
            "When and how revelation began",
            "وحی کب اور کیسے شروع ہوئی",
            "वही कब और कैसे शुरू हुई",
            "ওহী কখন ও কীভাবে শুরু হয়",
            "Kapan dan bagaimana wahyu dimulai",
        ),
        "details": L(
            "Prophethood began when he was forty, in 610 CE, in the cave of Hira' on Jabal al-Nur near Makkah. The first revelation was the opening of Surah al-Alaq. For about thirteen years he called people in Makkah; then Allah permitted the Hijrah to Madinah in 622 CE, from which the Islamic calendar begins.",
            "نبوت چالیس سال کی عمر میں، 610 عیسوی میں، مکہ کے قریب جبل نور پر غار حرا میں شروع ہوئی۔ پہلی وحی سورہ علق کی ابتدائی آیات تھیں۔ تقریباً تیرہ سال مکہ میں دعوت دی؛ پھر 622 عیسوی میں ہجرت مدینہ کی اجازت ہوئی جہاں سے اسلامی تاریخ شروع ہوتی ہے۔",
            "नबुव्वत चालीस वर्ष की उम्र में, 610 ईस्वी में, मक्का के पास जबल नूर पर गार हिर में शुरू हुई। पहली वही सूरह अलक़ की शुरुआती आयतें थीं। करीब तेरह साल मक्का में दावत दी; फिर 622 ईस्वी में हिजरत मदीना की इजाज़त हुई।",
            "নবুয়ত শুরু হয় তাঁর চল্লিশ বছর বয়সে, ৬১০ খ্রিস্টাব্দে, মক্কার কাছে জাবাল আন-নূরের হেরা গুহায়। প্রথম ওহী ছিল সূরা আলাকের সূচনা। প্রায় তেরো বছর তিনি মক্কায় আহ্বান জানান; তারপর ৬২২ খ্রিস্টাব্দে মদিনায় হিজরতের অনুমতি হয়, যেখান থেকে ইসলামি বর্ষপঞ্জি শুরু।",
            "Kenabian dimulai saat beliau berusia empat puluh tahun, tahun 610 M, di Gua Hira di Jabal Nur dekat Makkah. Wahyu pertama adalah pembukaan Surah al-Alaq. Sekitar tiga belas tahun beliau berdakwah di Makkah; lalu Allah mengizinkan Hijrah ke Madinah pada 622 M, awal kalender Islam.",
        ),
        "items": [
            item(
                L("The Cave of Hira'", "غار حرا", "गार हिर", "হেরা গুহা", "Gua Hira"),
                L("The first revelation", "پہلی وحی", "पहली वही", "প্রথম ওহী", "Wahyu pertama"),
                L(
                    "He used to seclude himself in Hira' in Ramadan, worshipping Allah away from idols. Jibril ﷺ came, pressed him, and said 'Iqra' (Read). He said he could not read. After the third pressing, Jibril recited: 'Read in the name of your Lord who created...' (96:1–5). He returned to Khadijah trembling. She reassured him: Allah would not disgrace him, for he kept kinship, spoke truth, helped the poor, honoured guests, and aided the afflicted.",
                    "رمضان میں غار حرا میں خلوت اختیار کرتے، بتوں سے دور اللہ کی عبادت۔ جبرائیل ﷺ آئے، دبایا اور کہا اقرأ۔ آپ نے فرمایا میں پڑھنا نہیں جانتا۔ تیسری بار کے بعد سورہ علق کی آیات پڑھائیں۔ کانپتے ہوئے خدیجہ کے پاس آئے۔ انہوں نے تسلی دی کہ اللہ آپ کو رسوا نہیں کرے گا کیونکہ آپ صلہ رحمی، سچائی، مسکین نوازی اور مہمان نوازی کرتے ہیں۔",
                    "रमज़ान में गार हिर में ख़लवत करते। जिब्रईल ﷺ आए, दबाया और कहा इकरा। आपने कहा मैं पढ़ना नहीं जानता। तीसरी बार सूरह अलक़ की आयतें पढ़ाई गईं। कांपते हुए ख़दीजा के पास आए। उन्होंने तसल्ली दी।",
                    "রমজানে তিনি হেরা গুহায় নির্জনে থাকতেন। জিবরীল ﷺ এসে চাপ দিয়ে বলেন ‘ইকরা’। তিনি বলেন তিনি পড়তে পারেন না। তৃতীয়বারের পর সূরা আলাক পাঠ করানো হয়। তিনি কাঁপতে কাঁপতে খাদিজাহর কাছে ফিরে আসেন। তিনি তাঁকে আশ্বস্ত করেন।",
                    "Beliau berkhalwat di Hira pada Ramadan. Jibril ﷺ datang, meremas, dan berkata 'Iqra'. Beliau menjawab tidak bisa membaca. Setelah yang ketiga, ayat al-Alaq dibacakan. Beliau pulang gemetar kepada Khadijah, yang menenangkannya.",
                ),
            ),
            item(
                L("Waraqah and the pause of revelation", "ورقہ اور وحی کا وقفہ", "वरक़ह और वही का विराम", "ওয়ারাকাহ ও ওহীর বিরতি", "Waraqah dan jeda wahyu"),
                L("Confirmation", "تصدیق", "तस्दीक़", "নিশ্চিতকরণ", "Peneguhan"),
                L(
                    "Khadijah took him to her cousin Waraqah ibn Nawfal, who knew the Scriptures. Waraqah said this was the Namus who had come to Musa, and that his people would drive him out. Revelation then paused (fatrah) until Surah al-Muddaththir: 'O you who wraps himself, arise and warn' (74:1–2). Revelation then continued for twenty-three years: about thirteen in Makkah and ten in Madinah.",
                    "خدیجہ آپ کو اپنے کزن ورقہ بن نوفل کے پاس لے گئیں جو آسمانی کتابیں جانتے تھے۔ ورقہ نے کہا یہ وہی ناموس ہے جو موسیٰ کے پاس آیا، اور قوم نکال دے گی۔ پھر وحی رک گئی یہاں تک کہ مدثر نازل ہوئی۔ وحی تیئس سال جاری رہی: تیرہ مکہ میں، دس مدینہ میں۔",
                    "ख़दीजा आपको वरक़ह बिन नौफ़ल के पास ले गईं। उन्होंने कहा यह वही नामूस है जो मूसा के पास आया। फिर वही रुकी जब तक मुद्दस्सिर नाज़िल हुई। वही तेईस साल जारी रही।",
                    "খাদিজাহ তাঁকে ওয়ারাকাহ ইবন নওফালের কাছে নিয়ে যান। তিনি বলেন এটি সেই নামূস যা মূসার কাছে এসেছিল। তারপর ওহী থেমে যায় যতক্ষণ না সূরা মুদ্দাসসির নাযিল হয়। ওহী তেইশ বছর চলে।",
                    "Khadijah membawanya kepada Waraqah bin Naufal. Waraqah berkata itu Namus yang datang kepada Musa, dan kaumnya akan mengusirnya. Wahyu terhenti hingga al-Muddatsir. Wahyu berlangsung dua puluh tiga tahun.",
                ),
            ),
            item(
                L("The private and public call", "پوشیدہ اور کھلی دعوت", "पोशीदा और खुली दावत", "গোপন ও প্রকাশ্য আহ্বান", "Dakwah rahasia dan terbuka"),
                L("The Makkan years", "مکی دور", "मक्की दौर", "মাক্কী যুগ", "Periode Makkah"),
                L(
                    "At first he called secretly. Early believers included Khadijah, Ali, Zayd ibn Harithah, and Abu Bakr, who brought others. After about three years came the public call. Quraysh persecuted the weak; some migrated to Abyssinia. Hamzah and Umar accepted Islam. Banu Hashim were boycotted. In the Year of Sorrow he lost Khadijah and Abu Talib. After Ta'if, the Isra' and Mi'raj took place and the five prayers were ordained. He pledged with the Ansar at Aqabah, then came the Hijrah.",
                    "پہلے خفیہ دعوت دی۔ اولین ایمان لانے والوں میں خدیجہ، علی، زید اور ابو بکر تھے۔ تقریباً تین سال بعد کھلی دعوت ہوئی۔ قریش نے کمزوروں پر ظلم کیا؛ کچھ حبشہ ہجرت کر گئے۔ حمزہ اور عمر مسلمان ہوئے۔ بنو ہاشم کا بائیکاٹ ہوا۔ عام الحزن میں خدیجہ اور ابو طالب فوت ہوئے۔ طائف کے بعد اسراء و معراج ہوئی اور پانچ نمازیں فرض ہوئیں۔ عقبہ میں انصار سے بیعت، پھر ہجرت۔",
                    "पहले ख़ुफ़ी दावत दी। तीन साल बाद खुली दावत। कुरैश ने कमज़ोरों पर ज़ुल्म किया। आम उल-हुज़्न में ख़दीजा और अबू तालिब का इंतिक़ाल। ताइफ़ के बाद इसरा व मिराज, पांच नमाज़ें फ़र्ज़ हुईं, फिर हिजरत।",
                    "প্রথমে গোপনে আহ্বান। প্রায় তিন বছর পর প্রকাশ্য আহ্বান। কুরাইশ দুর্বলদের নির্যাতন করে; কেউ কেউ হাবশায় হিজরত করেন। দুঃখের বছরে খাদিজাহ ও আবু তালিব মারা যান। তায়েফের পর ইসরা ও মিরাজ, পাঁচ ওয়াক্ত সালাত ফরজ হয়, তারপর হিজরত।",
                    "Awalnya dakwah sembunyi-sembunyi. Setelah sekitar tiga tahun dakwah terbuka. Quraisy menganiaya yang lemah; sebagian hijrah ke Habasyah. Tahun Kesedihan Khadijah dan Abu Thalib wafat. Setelah Thaif, Isra Mi'raj, salat lima waktu diwajibkan, lalu Hijrah.",
                ),
            ),
        ],
    },
    {
        "chapter_id": 4,
        "title": L(
            "Wives of the Prophet (Ummahat-ul-Momineen)",
            "ازواج مطہرات (امہات المؤمنین)",
            "उम्महातुल मुमिनीन",
            "উম্মাহাতুল মুমিনীন",
            "Istri Nabi (Ummul Mukminin)",
        ),
        "heading": L(
            "The Mothers of the Believers",
            "مؤمنوں کی مائیں",
            "मोमिनों की माएँ",
            "মুমিনদের মাতা",
            "Ibu kaum mukmin",
        ),
        "details": L(
            "Allah said: 'The Prophet is closer to the believers than their own selves, and his wives are their mothers' (33:6). After Khadijah's death he married other women, mostly widows, in ways that bound tribes to Islam, taught the Ummah, and honoured companions' households. All are Mothers of the Believers. He ﷺ married no one else during Khadijah's lifetime.",
            "اللہ نے فرمایا: 'نبی مؤمنوں پر ان کی جان سے زیادہ حق رکھتے ہیں اور ان کی بیویاں ان کی مائیں ہیں' (33:6)۔ خدیجہ کی وفات کے بعد آپ نے اور شادیاں کیں، زیادہ تر بیوائیں، جن سے قبائل اسلام سے جڑے، امت کو علم ملا اور صحابہ کے گھرانوں کی عزت ہوئی۔ سب امہات المؤمنین ہیں۔ خدیجہ کی زندگی میں آپ نے کوئی اور نکاح نہیں کیا۔",
            "अल्लाह ने फ़रमाया: 'नबी मोमिनों पर उनकी जान से ज़्यादा हक़ रखते हैं और उनकी बीवियाँ उनकी माएँ हैं' (33:6)। ख़दीजा की वफ़ात के बाद आपने और निकाह किए, ज़्यादातर विधवाएँ। ख़दीजा की ज़िंदगी में कोई और निकाह नहीं किया।",
            "আল্লাহ বলেছেন, ‘নবী মুমিনদের নিকট তাদের নিজেদের চেয়ে ঘনিষ্ঠ, আর তাঁর স্ত্রীগণ তাদের মাতা’ (৩৩:৬)। খাদিজাহর মৃত্যুর পর তিনি আরও বিবাহ করেন, অধিকাংশ বিধবা। খাদিজাহর জীবদ্দশায় তিনি অন্য কাউকে বিয়ে করেননি।",
            "Allah berfirman: 'Nabi lebih utama bagi orang beriman daripada diri mereka, dan istri-istrinya adalah ibu-ibu mereka' (33:6). Setelah Khadijah wafat beliau menikah lagi, sebagian besar janda. Beliau tidak menikah dengan siapa pun semasa Khadijah hidup.",
        ),
        "items": [
            item(
                L("Khadijah bint Khuwaylid", "خدیجہ بنت خویلد", "ख़दीजा बिन्त ख़ुवैलिद", "খাদিজাহ বিনত খুওয়াইলিদ", "Khadijah binti Khuwailid"),
                L("Mother of the Believers", "ام المؤمنین", "उम्मुल मुमिनीन", "উম্মুল মুমিনীন", "Ummul Mukminin"),
                L(
                    "The first wife and the first to believe. She supported him with wealth and heart. He never married another while she lived. Aisha رضي الله عنها said she was not jealous of any woman as of Khadijah, though she had not seen her, because he mentioned her so often. Khadijah died in Makkah about three years before the Hijrah.",
                    "پہلی بیوی اور سب سے پہلے ایمان لانے والیں۔ مال اور دل سے ساتھ دیں۔ ان کی زندگی میں کوئی اور نکاح نہیں کیا۔ عائشہ رضی اللہ عنہا فرماتی ہیں خدیجہ جیسی رشک کسی پر نہیں آیا حالانکہ انہیں دیکھا نہیں کیونکہ آپ ان کا ذکر کثرت سے کرتے تھے۔ ہجرت سے تقریباً تین سال پہلے مکہ میں وفات ہوئی۔",
                    "पहली बीवी और सबसे पहले ईमान लाने वालीं। उनकी ज़िंदगी में कोई और निकाह नहीं। हिजरत से करीब तीन साल पहले मक्का में वफ़ात।",
                    "প্রথম স্ত্রী এবং সর্বপ্রথম ঈমান আনেন। তাঁর জীবদ্দশায় অন্য বিবাহ হয়নি। হিজরতের প্রায় তিন বছর আগে মক্কায় তিনি ইন্তেকাল করেন।",
                    "Istri pertama dan orang pertama yang beriman. Beliau tidak menikah dengan yang lain semasa Khadijah hidup. Ia wafat di Makkah sekitar tiga tahun sebelum Hijrah.",
                ),
            ),
            item(
                L("Sawdah bint Zam'ah", "سودہ بنت زمعہ", "सौदा बिन्त ज़मआ", "সাওদাহ বিনত যামআহ", "Sauda binti Zam'ah"),
                L("Mother of the Believers", "ام المؤمنین", "उम्मुल मुमिनीन", "উম্মুল মুমিনীন", "Ummul Mukminin"),
                L(
                    "A widow who had migrated to Abyssinia. The Prophet ﷺ married her in Makkah after Khadijah. She was older, kind, and known for humour. Later she gifted her night to Aisha out of love for the Messenger ﷺ.",
                    "بیوہ جنہوں نے حبشہ ہجرت کی تھی۔ خدیجہ کے بعد مکہ میں نکاح ہوا۔ عمر میں بڑی، نرم دل، خوش مزاج۔ بعد میں رسول ﷺ کی محبت میں اپنی باری عائشہ کو دے دی۔",
                    "विधवा जो हबशा हिजरत कर चुकी थीं। ख़दीजा के बाद मक्का में निकाह। बाद में अपनी बारी आयशा को दे दी।",
                    "বিধবা যিনি হাবশায় হিজরত করেছিলেন। খাদিজাহর পর মক্কায় বিবাহ। পরে তিনি তাঁর রাত আয়িশাকে দান করেন।",
                    "Janda yang pernah hijrah ke Habasyah. Nabi ﷺ menikahinya di Makkah setelah Khadijah. Kemudian ia menghibahkan malamnya kepada Aisyah.",
                ),
            ),
            item(
                L("Aisha bint Abi Bakr", "عائشہ بنت ابی بکر", "आयशा बिन्त अबी बक्र", "আয়িশাহ বিনত আবি বকর", "Aisyah binti Abu Bakar"),
                L("Mother of the Believers", "ام المؤمنین", "उम्मुल मुमिनीन", "উম্মুল মুমিনীন", "Ummul Mukminin"),
                L(
                    "Daughter of Abu Bakr al-Siddiq. The marriage was contracted in Makkah and consummated in Madinah after the Hijrah. She is the only wife who was not previously married. She became one of the greatest scholars of the Ummah; many hadith are narrated from her. The incident of Ifk was revealed in Surah al-Nur, declaring her innocence.",
                    "ابو بکر صدیق کی صاحبزادی۔ نکاح مکہ میں ہوا، رخصتی ہجرت کے بعد مدینہ میں۔ واحد زوجہ جو پہلے شادی شدہ نہ تھیں۔ امت کی بڑی عالمہ بنیں، بہت احادیث روایت کیں۔ واقعہ افک سورہ نور میں نازل ہوا اور ان کی براءت بیان ہوئی۔",
                    "अबू बक्र सिद्दीक की साहिबज़ादी। निकाह मक्का में, रुख्सती हिजरत के बाद मदीना में। इकलौती बीवी जो पहले शादीशुदा नहीं थीं। उम्मत की बड़ी आलिमा बनीं।",
                    "আবু বকর সিদ্দিকের কন্যা। মক্কায় চুক্তি, হিজরতের পর মদিনায় বাসর। তিনিই একমাত্র স্ত্রী যিনি পূর্বে বিবাহিত ছিলেন না। উম্মাহর অন্যতম শ্রেষ্ঠ আলিমা।",
                    "Putri Abu Bakar ash-Shiddiq. Akad di Makkah, tinggal serumah di Madinah setelah Hijrah. Satu-satunya istri yang belum pernah menikah. Ia menjadi ulama besar umat.",
                ),
            ),
            item(
                L("Hafsah bint Umar", "حفصہ بنت عمر", "हफ़्सा बिन्त उमर", "হাফসাহ বিনত উমর", "Hafshah binti Umar"),
                L("Mother of the Believers", "ام المؤمنین", "उम्मुल मुमिनीन", "উম্মুল মুমিনীন", "Ummul Mukminin"),
                L(
                    "Daughter of Umar ibn al-Khattab, widow of Khunays ibn Hudhafah. The Prophet ﷺ married her, joining the households of Abu Bakr and Umar to his own. A written collection of Quranic sheets (mushaf) was later kept with her in the time of the caliphate.",
                    "عمر بن خطاب کی صاحبزادی، خنیس بن حذافہ کی بیوہ۔ نبی ﷺ نے نکاح کیا جس سے ابو بکر اور عمر کے گھرانے آپ سے جڑے۔ خلافت کے دور میں مصحف ان کے پاس محفوظ رہا۔",
                    "उमर बिन खत्ताब की साहिबज़ादी। नबी ﷺ ने निकाह किया। खिलाफ़त के दौर में मुसहफ़ उनके पास रहा।",
                    "উমর ইবনুল খাত্তাবের কন্যা। নবী ﷺ তাঁকে বিয়ে করেন। খিলাফতের সময়ে মুশাফ তাঁর কাছে সংরক্ষিত ছিল।",
                    "Putri Umar bin Khattab. Nabi ﷺ menikahinya. Pada masa khilafah, mushaf disimpan padanya.",
                ),
            ),
            item(
                L("Zaynab bint Khuzaymah", "زینب بنت خزیمہ", "ज़ैनब बिन्त ख़ुज़ैमा", "যাইনাব বিনত খুযাইমাহ", "Zainab binti Khuzaimah"),
                L("Umm al-Masakin", "ام المساکین", "उम्म उल-मसाकीन", "উম্মুল মাসাকীন", "Ummul Masakin"),
                L(
                    "Known as Umm al-Masakin (Mother of the Poor) for her generosity. The Prophet ﷺ married her in Madinah. She died after only a few months, the only wife besides Khadijah who died during his lifetime.",
                    "سخاوت کی وجہ سے ام المساکین کہلائیں۔ مدینہ میں نکاح ہوا۔ چند ماہ بعد وفات پا گئیں، خدیجہ کے علاوہ واحد زوجہ جو آپ کی حیات میں فوت ہوئیں۔",
                    "सख़ावत की वजह से उम्म उल-मसाकीन कहलातीं। मदीना में निकाह। चंद महीनों बाद वफ़ात।",
                    "দানশীলতার জন্য উম্মুল মাসাকীন নামে পরিচিত। মদিনায় বিবাহ। কয়েক মাস পর তিনি ইন্তেকাল করেন।",
                    "Dikenal Ummul Masakin karena kedermawanannya. Dinikahi di Madinah. Wafat beberapa bulan kemudian, satu-satunya istri selain Khadijah yang meninggal semasa hidup beliau.",
                ),
            ),
            item(
                L("Umm Salamah (Hind bint Abi Umayyah)", "ام سلمہ", "उम्म सलमा", "উম্মু সালামাহ", "Ummu Salamah"),
                L("Mother of the Believers", "ام المؤمنین", "उम्मुल मुमिनीन", "উম্মুল মুমিনীন", "Ummul Mukminin"),
                L(
                    "Widow of Abu Salamah, among the earliest Muslims and emigrants. After he died of wounds from Uhud, the Prophet ﷺ married her. She was wise; her counsel at Hudaybiyyah—that he slaughter and shave so the Companions would follow—is famous.",
                    "ابو سلمہ کی بیوہ، اولین مسلمانوں اور مہاجرین میں سے۔ احد کے زخموں سے ان کے شوہر کی وفات کے بعد نکاح ہوا۔ دانا تھیں؛ حدیبیہ میں مشورہ مشہور ہے کہ قربانی کریں اور سر منڈائیں تاکہ صحابہ پیروی کریں۔",
                    "अबू सलमा की विधवा, शुरुआती मुसलमानों में से। उहुद के ज़ख़्मों के बाद निकाह। हुदैबिया में मशहूर मशवरा दिया।",
                    "আবু সালামাহর বিধবা, প্রথম যুগের মুসলিম ও মুহাজির। উহুদের আঘাতে স্বামীর মৃত্যুর পর নবী ﷺ তাঁকে বিয়ে করেন। হুদায়বিয়ায় তাঁর পরামর্শ বিখ্যাত।",
                    "Janda Abu Salamah, termasuk muslim dan muhajir awal. Setelah suaminya wafat karena luka Uhud, Nabi ﷺ menikahinya. Nasihatnya di Hudaibiyah terkenal.",
                ),
            ),
            item(
                L("Zaynab bint Jahsh", "زینب بنت جحش", "ज़ैनब बिन्त जह्श", "যাইনাব বিনত জাহশ", "Zainab binti Jahsy"),
                L("Mother of the Believers", "ام المؤمنین", "उम्मुल मुमिनीन", "উম্মুল মুমিনীন", "Ummul Mukminin"),
                L(
                    "A cousin of the Prophet ﷺ. She had been married to Zayd ibn Harithah. After that marriage ended, Allah married her to the Prophet ﷺ by revelation (33:37), ending the Jahili custom of treating an adopted son like a biological son in marriage law. She was known for piety and charity. She died in 20 AH.",
                    "نبی ﷺ کی پھوپھی زاد۔ پہلے زید بن حارثہ سے نکاح تھا۔ اس نکاح کے ختم ہونے کے بعد اللہ نے وحی (33:37) سے آپ سے نکاح کر دیا، جس سے جاہلی رسم ختم ہوئی کہ لے پالک بیٹا حقیقی بیٹے کی طرح سمجھا جائے۔ تقویٰ اور صدقے میں مشہور۔ 20 ہجری میں وفات۔",
                    "नबी ﷺ की फूफेरी बहन। पहले ज़ैद से निकाह था। वही से नबी ﷺ से निकाह हुआ (33:37)। 20 हिजरी में वफ़ात।",
                    "নবী ﷺ-এর ফুফাতো বোন। পূর্বে যায়েদ ইবন হারিসার সঙ্গে বিবাহ ছিল। ওহী (৩৩:৩৭) দ্বারা নবী ﷺ-এর সঙ্গে বিবাহ হয়। ২০ হিজরিতে ইন্তেকাল।",
                    "Sepupu Nabi ﷺ. Pernah menikah dengan Zaid bin Haritsah. Setelah itu Allah menikahkannya dengan Nabi ﷺ melalui wahyu (33:37). Wafat tahun 20 H.",
                ),
            ),
            item(
                L("Juwayriyah bint al-Harith", "جویریہ بنت الحارث", "जुवैरिया बिन्त अल-हारिस", "জুওয়াইরিয়াহ বিনত আল-হারিস", "Juwairiyah binti al-Harits"),
                L("Mother of the Believers", "ام المؤمنین", "उम्मुल मुमिनीन", "উম্মুল মুমিনীন", "Ummul Mukminin"),
                L(
                    "Daughter of the chief of Banu al-Mustaliq, taken after the expedition of al-Muraysi'. The Prophet ﷺ married her; Muslims then freed many captives of her tribe as in-laws of the Messenger ﷺ. She was remembered for long dhikr.",
                    "بنو مصطلق کے سردار کی بیٹی، مریسیع کے بعد قید ہوئیں۔ نبی ﷺ نے نکاح کیا؛ مسلمانوں نے ان کے قبیلے کے بہت قیدی اس لیے آزاد کیے کہ وہ رسول ﷺ کے سسرال ہو گئے۔ ذکر کثیر میں یاد کی گئیں۔",
                    "बनू मुस्तलिक़ के सरदार की बेटी। नबी ﷺ ने निकाह किया; मुसलमानों ने उनके क़बीले के कई क़ैदी आज़ाद किए।",
                    "বনু মুস্তালিকের নেতার কন্যা। নবী ﷺ তাঁকে বিয়ে করেন; মুসলিমরা তাঁর গোত্রের অনেক বন্দিকে মুক্ত করে।",
                    "Putri pemuka Bani Mustaliq. Nabi ﷺ menikahinya; kaum muslimin lalu membebaskan banyak tawanan sukunya.",
                ),
            ),
            item(
                L("Umm Habibah (Ramlah bint Abi Sufyan)", "ام حبیبہ", "उम्म हबीबा", "উম্মু হাবিবাহ", "Ummu Habibah"),
                L("Mother of the Believers", "ام المؤمنین", "उम्मुल मुमिनीन", "উম্মুল মুমিনীন", "Ummul Mukminin"),
                L(
                    "Daughter of Abu Sufyan. She embraced Islam early and migrated to Abyssinia. After her husband left Islam and died there, the Prophet ﷺ sent to al-Najashi to contract marriage; the Negus acted as guardian. She died in Madinah around 44 AH.",
                    "ابو سفیان کی صاحبزادی۔ جلد اسلام لائیں اور حبشہ ہجرت کی۔ شوہر نے وہاں اسلام چھوڑا اور فوت ہوا۔ نبی ﷺ نے نجاشی کے پاس نکاح کا پیغام بھیجا۔ تقریباً 44 ہجری میں مدینہ میں وفات۔",
                    "अबू सुफ्यान की साहिबज़ादी। हबशा हिजरत की। नजाशी के ज़रिए निकाह हुआ। करीब 44 हिजरी में मदीना में वफ़ात।",
                    "আবু সুফিয়ানের কন্যা। হাবশায় হিজরত করেন। নাজাশির মাধ্যমে বিবাহ হয়। প্রায় ৪৪ হিজরিতে মদিনায় ইন্তেকাল।",
                    "Putri Abu Sufyan. Hijrah ke Habasyah. Nabi ﷺ menikahinya melalui Najasyi. Wafat di Madinah sekitar 44 H.",
                ),
            ),
            item(
                L("Safiyyah bint Huyayy", "صفیہ بنت حیي", "सफ़िया बिन्त हुयय", "সাফিয়্যাহ বিনত হুয়াইয়্য", "Safiyyah binti Huyay"),
                L("Mother of the Believers", "ام المؤمنین", "उम्मुल मुमिनीन", "উম্মুল মুমিনীন", "Ummul Mukminin"),
                L(
                    "Daughter of Huyayy ibn Akhtab of Banu Nadir. Taken after Khaybar, then freed and married by the Prophet ﷺ. He defended her dignity, saying her father was Harun and her uncle Musa ﷺ. She died around 50 AH.",
                    "بنو نضیر کے حیي بن اخطب کی بیٹی۔ خیبر کے بعد قید ہوئیں، پھر آزاد کر کے نکاح ہوا۔ آپ نے ان کی عزت کی حفاظت کی اور فرمایا ان کے والد ہارون اور چچا موسیٰ ﷺ ہیں۔ تقریباً 50 ہجری میں وفات۔",
                    "बनू नज़ीर के हुयय की बेटी। ख़ैबर के बाद आज़ाद कर निकाह हुआ। करीब 50 हिजरी में वफ़ात।",
                    "বনু নাদিরের হুয়াইয়্য ইবন আখতাবের কন্যা। খাইবারের পর মুক্ত করে বিবাহ করেন। প্রায় ৫০ হিজরিতে ইন্তেকাল।",
                    "Putri Huyay bin Akhthab dari Bani Nadir. Setelah Khaibar dimerdekakan lalu dinikahi Nabi ﷺ. Wafat sekitar 50 H.",
                ),
            ),
            item(
                L("Maymunah bint al-Harith", "میمونہ بنت الحارث", "मैमूना बिन्त अल-हारिस", "মায়মুনাহ বিনত আল-হারিস", "Maimunah binti al-Harits"),
                L("Mother of the Believers", "ام المؤمنین", "उम्मुल मुमिनीन", "উম্মুল মুমিনীন", "Ummul Mukminin"),
                L(
                    "The last woman he married, in 7 AH at Sarif near Makkah, after umrah al-qada'. She was the sister of Umm al-Fadl, wife of al-Abbas. Ibn Abbas, her nephew, narrated much from her. She died at Sarif around 51 AH.",
                    "آخری شادی، 7 ہجری میں مکہ کے قریب سرف میں، عمرہ القضاء کے بعد۔ ام الفضل کی بہن تھیں جو عباس کی بیوی تھیں۔ ابن عباس نے ان سے بہت روایت کی۔ تقریباً 51 ہجری میں سرف میں وفات۔",
                    "आख़िरी निकाह, 7 हिजरी में मक्का के पास सरिफ़ में। करीब 51 हिजरी में वफ़ात।",
                    "শেষ বিবাহ, ৭ হিজরিতে মক্কার কাছে সারিফে। প্রায় ৫১ হিজরিতে সেখানেই ইন্তেকাল।",
                    "Istri terakhir, dinikahi tahun 7 H di Sarif dekat Makkah setelah umrah qadha. Wafat di Sarif sekitar 51 H.",
                ),
            ),
        ],
    },
    {
        "chapter_id": 5,
        "title": L(
            "Major Events & Passing (Wafat)",
            "بڑے واقعات اور وفات",
            "प्रमुख घटनाएँ और विसाल",
            "প্রধান ঘটনা ও ওফাত",
            "Peristiwa Besar & Wafat",
        ),
        "heading": L(
            "Madinan years, the Farewell, and his death",
            "مدنی دور، حجۃ الوداع اور وفات",
            "मदनी दौर, हज्जतुल विदा और विसाल",
            "মাদানী যুগ, বিদায় হজ ও ওফাত",
            "Periode Madinah, haji wada, dan wafat",
        ),
        "details": L(
            "In Madinah the Prophet ﷺ established the mosque, the brotherhood of Muhajirun and Ansar, and a written pact among the city's groups. The major battles and treaties of this period shaped the Ummah. He died in Madinah in Rabi' al-Awwal, 11 AH (June 632 CE), at sixty-three, and was buried in the chamber of Aisha رضي الله عنها.",
            "مدینہ میں نبی ﷺ نے مسجد، مہاجرین و انصار میں مواخات اور شہر کے گروہوں کا تحریری معاہدہ قائم کیا۔ اس دور کی بڑی جنگیں اور صلحیں امت کی بنیاد بنیں۔ ربیع الاول 11 ہجری (جون 632ء) میں ت63 سال کی عمر میں مدینہ میں وفات ہوئی اور عائشہ رضی اللہ عنہا کے حجرے میں دفن ہوئے۔",
            "मदीना में नबी ﷺ ने मस्जिद, मुहाजिरीन व अनसार की मुआख़ात और शहर का लिखी हुई सलह क़ायम की। रबीउल अव्वल 11 हिजरी (जून 632) में तिरेसठ वर्ष की उम्र में विसाल हुआ, आयशा के हुजरे में दफ़न।",
            "মদিনায় নবী ﷺ মসজিদ, মুহাজির ও আনসারের ভ্রাতৃত্ব এবং শহরের দলগুলোর লিখিত চুক্তি প্রতিষ্ঠা করেন। তিনি ১১ হিজরি রবিউল আউয়ালে (জুন ৬৩২) তেষট্টি বছর বয়সে মদিনায় ওফাত লাভ করেন এবং আয়িশার হুজরায় দাফন হন।",
            "Di Madinah Nabi ﷺ menegakkan masjid, persaudaraan Muhajirin-Ansar, dan piagam tertulis. Beliau wafat di Madinah pada Rabiul Awal 11 H (Juni 632 M), usia enam puluh tiga, dimakamkan di kamar Aisyah radhiyallahu anha.",
        ),
        "items": [
            item(
                L("Badr, Uhud, and the Trench", "بدر، احد اور خندق", "बद्र, उहुद और खंदक", "বদর, উহুদ ও খন্দক", "Badar, Uhud, dan Khandaq"),
                L("The great battles", "بڑی جنگیں", "बड़ी जंगें", "প্রধান যুদ্ধ", "Pertempuran besar"),
                L(
                    "Badr (2 AH / 624 CE) was the first major battle: about 313 Muslims faced a much larger Quraysh force and were granted victory. Uhud (3 AH) was a trial; archers left their post, and the Prophet ﷺ was wounded. Hamzah رضي الله عنه was martyred. The Trench (5 AH) saw confederate tribes besiege Madinah; Salman suggested the trench. Allah sent wind and the coalition failed.",
                    "بدر (2ھ / 624ء) پہلی بڑی جنگ: تقریباً 313 مسلمان بڑی فوج کے مقابل، فتح ملی۔ احد (3ھ) آزمائش تھی؛ تیراندازوں نے مورچہ چھوڑا، نبی ﷺ زخمی ہوئے، حمزہ شہید ہوئے۔ خندق (5ھ) میں احزاب نے مدینہ گھیر لیا؛ سلمان نے خندق کی تجویز دی۔ اللہ نے ہوا بھیجی اور اتحاد ٹوٹ گیا۔",
                    "बद्र पहली बड़ी जंग: करीब 313 मुसलमानों को फतह मिली। उहुद आज़माइश थी। खंदक में अहज़ाब ने मदीना घेरा; सलमान ने खंदक सुझाई।",
                    "বদর প্রথম বড় যুদ্ধ: প্রায় ৩১৩ মুসলিম বিজয় পান। উহুদ ছিল পরীক্ষা। খন্দকে সম্মিলিত বাহিনী মদিনা অবরোধ করে; সালমান পরিখা প্রস্তাব করেন।",
                    "Badar (2 H) pertempuran besar pertama: sekitar 313 muslim meraih kemenangan. Uhud (3 H) ujian; Nabi ﷺ terluka, Hamzah syahid. Khandaq (5 H) koalisi mengepung Madinah; Salman mengusulkan parit.",
                ),
            ),
            item(
                L("Hudaybiyyah, Khaybar, and the Conquest of Makkah", "حدیبیہ، خیبر اور فتح مکہ", "हुदैबिया, ख़ैबर और फत्हे मक्का", "হুদায়বিয়া, খাইবার ও মক্কা বিজয়", "Hudaibiyah, Khaibar, dan Fathu Makkah"),
                L("Treaty and victory", "صلح اور فتح", "सुलह और फतह", "সন্ধি ও বিজয়", "Perjanjian dan kemenangan"),
                L(
                    "In 6 AH the Muslims set out for umrah and were barred from the Ka'bah. The Treaty of Hudaybiyyah looked unfavourable, but Allah called it a clear victory (48:1). It opened a truce in which people entered Islam in numbers. Khaybar (7 AH) followed. In 8 AH Quraysh violated the treaty. The Prophet ﷺ entered Makkah with about ten thousand, almost without fighting, and said, 'Go, for you are free.' Idols in the Ka'bah were removed.",
                    "6ھ میں عمرے کو نکلے تو کعبہ سے روک دیا گیا۔ صلح حدیبیہ بظاہر نا موافق تھی مگر اللہ نے اسے فتح مبین کہا (48:1)۔ اس سے وہ وقفہ آیا جس میں لوگ کثرت سے مسلمان ہوئے۔ خیبر 7ھ میں ہوئی۔ 8ھ میں قریش نے عہد توڑا۔ نبی ﷺ تقریباً دس ہزار کے ساتھ مکہ میں داخل ہوئے، لڑائی کم ہوئی، فرمایا جاؤ تم آزاد ہو۔ کعبہ کے بت گرا دیے گئے۔",
                    "6 हिजरी में उमरा के लिए निकले तो काबा से रोका गया। सुलहे हुदैबिया को अल्लाह ने फत्हे मुबीन कहा। 8 हिजरी में फत्हे मक्का हुई, कुरैश को माफ़ किया।",
                    "৬ হিজরিতে উমরার উদ্দেশ্যে বের হন, কাবায় বাধা দেওয়া হয়। হুদায়বিয়ার সন্ধিকে আল্লাহ স্পষ্ট বিজয় বলেন। ৮ হিজরিতে মক্কা বিজয় হয়, তিনি ক্ষমা করেন।",
                    "Tahun 6 H umat Islam umrah terhalang dari Ka'bah. Perjanjian Hudaibiyah disebut kemenangan nyata (48:1). Tahun 8 H Fathu Makkah; beliau memaafkan Quraisy, 'Pergilah, kalian bebas.'",
                ),
            ),
            item(
                L("Tabuk and the Farewell Hajj", "تبوک اور حجۃ الوداع", "तबूक और हज्जतुल विदा", "তাবুক ও বিদায় হজ", "Tabuk dan haji wada"),
                L("The last years", "آخری سال", "आख़िरी साल", "শেষ বছরগুলো", "Tahun-tahun terakhir"),
                L(
                    "In 9 AH he led the expedition of Tabuk in hardship. Many tribes submitted. In 10 AH he performed the Farewell Hajj. At Arafah he delivered the sermon: blood and property are sacred; abolish Jahili usury and revenge; treat women well; hold to the Book of Allah. He asked, 'Have I conveyed?' They said yes. 'Today I have perfected for you your religion' (5:3) was revealed in this context according to the well-known report.",
                    "9ھ میں سختی میں تبوک کا سفر۔ بہت سے قبائل مطیع ہوئے۔ 10ھ میں حجۃ الوداع۔ عرفات پر خطبہ: جان و مال حرام ہیں؛ جاہلی سود اور انتقام ختم؛ عورتوں سے اچھا سلوک؛ اللہ کی کتاب تھامے رہو۔ پوچھا کیا میں نے پہنچا دیا؟ کہا ہاں۔ مشہور روایت کے مطابق اسی موقع پر آیت 'آج میں نے تمہارے دین کو کامل کر دیا' (5:3) نازل ہوئی।",
                    "9 हिजरी में तबूक। 10 हिजरी हज्जतुल विदा। अरफ़ात पर ख़ुत्बा: जान माल हराम हैं, औरतों से अच्छा सुलूक, किताब अल्लाह थामे रहो।",
                    "৯ হিজরিতে তাবুক। ১০ হিজরিতে বিদায় হজ। আরাফাতে খুতবা: জানমাল পবিত্র, নারীদের সঙ্গে সদাচরণ, আল্লাহর কিতাব ধরে থাকো।",
                    "Tahun 9 H ekspedisi Tabuk. Tahun 10 H haji wada. Di Arafah beliau berkhutbah: darah dan harta suci; perlakukan wanita dengan baik; berpegang pada Kitab Allah.",
                ),
            ),
            item(
                L("His illness and Wafat", "مرض اور وفات", "मर्ज़ और विसाल", "অসুস্থতা ও ওফাত", "Sakit dan wafat"),
                L("Rabi' al-Awwal, 11 AH", "ربیع الاول، 11ھ", "रबीउल अव्वल, 11 हिजरी", "রবিউল আউয়াল, ১১ হিজরি", "Rabiul Awal, 11 H"),
                L(
                    "He fell ill with severe fever for about thirteen days and asked to be nursed in Aisha's chamber. He appointed Abu Bakr to lead the prayer. On Monday, 12 Rabi' al-Awwal 11 AH according to the most common report, he ﷺ passed away with his head in Aisha's lap. He was buried where he died, in Aisha's house, now within al-Masjid al-Nabawi. Abu Bakr said: 'Whoever worshipped Muhammad, Muhammad has died. Whoever worships Allah, Allah is Ever-Living and does not die,' and recited 3:144.",
                    "شدید بخار میں تقریباً تیرہ دن بیمار رہے، عائشہ کے حجرے میں رہنا پسند فرمایا۔ ابو بکر کو امامت کے لیے مقرر کیا۔ مشہور قول کے مطابق پیر 12 ربیع الاول 11ھ کو عائشہ کی گود میں سر رکھ کر وفات ہوئی۔ وہیں دفن ہوئے جو اب مسجد نبوی میں ہے۔ ابو بکر نے کہا: جس نے محمد کی عبادت کی وہ فوت ہو گئے، جو اللہ کی عبادت کرتا ہے اللہ زندہ ہے مرتا نہیں، اور 3:144 پڑھی۔",
                    "करीब तेरह दिन बुखार रहा। अबू बक्र को इमामत दी। मशहूर कौल के मुताबिक सोमवार 12 रबीउल अव्वल 11 हिजरी को आयशा की गोद में विसाल। अबू बक्र ने कहा: जिसने मुहम्मद की इबादत की वे फ़ौत हुए, अल्लाह ज़िंदा है।",
                    "প্রায় তেরো দিন জ্বরে অসুস্থ থাকেন। আবু বকরকে ইমামতি দেন। প্রসিদ্ধ বর্ণনায় সোমবার ১২ রবিউল আউয়াল ১১ হিজরিতে আয়িশার কোলে মাথা রেখে ওফাত। আবু বকর বলেন, যারা মুহাম্মদের ইবাদত করত তিনি মারা গেছেন; আল্লাহ চিরঞ্জীব।",
                    "Beliau demam sekitar tiga belas hari, merawat di kamar Aisyah. Abu Bakar diangkat imam. Menurut riwayat terkenal, Senin 12 Rabiul Awal 11 H beliau wafat di pangkuan Aisyah. Abu Bakar berkata: siapa menyembah Muhammad, ia telah wafat; siapa menyembah Allah, Allah Maha Hidup.",
                ),
            ),
        ],
    },
]


if __name__ == "__main__":
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(CHAPTERS, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(CHAPTERS)} chapters to {OUT}")
