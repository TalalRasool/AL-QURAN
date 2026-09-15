# -*- coding: utf-8 -*-
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "assets" / "json" / "sahaba.json"


def D(en, ur, hi, bn, idn):
    return {"en": en.strip(), "ur": ur.strip(), "hi": hi.strip(), "bn": bn.strip(), "id": idn.strip()}


data = json.loads(PATH.read_text(encoding="utf-8"))


def chapter(cid):
    for ch in data:
        if ch["chapter_id"] == cid:
            return ch
    raise KeyError(cid)


# --- 1 Abu Bakr as-Siddiq ---
ch = chapter(1)
ch["details"] = D(
    """Abu Bakr Abdullah ibn Abi Quhafa رضي الله عنه, of Banu Taym of Quraysh, was the closest friend of the Prophet Muhammad ﷺ before and after prophethood. Ibn Sa'd in al-Tabaqat al-Kubra and Ibn Hisham's sirah record his lineage, his trade in cloth, and his known honesty in Makkah. He was born about two or three years after the Year of the Elephant. His father Uthman was called Abu Quhafa; his mother Salma bint Sakhr was called Umm al-Khayr. Sunni historians count him the best of this ummah after its Prophet ﷺ.

He was the first adult free man to accept Islam. Khadijah رضي الله عنها believed first among women, and Ali رضي الله عنه as a boy in the household; Abu Bakr's Islam as a free man of standing opened a door for others. Through his invitation Uthman ibn Affan, al-Zubayr ibn al-Awwam, Abd al-Rahman ibn Awf, Sa'd ibn Abi Waqqas, and Talha ibn Ubayd Allah رضي الله عنهم entered the faith, as Ibn Ishaq relates. He spent his wealth to free those tortured for tawhid, above all Bilal ibn Rabah رضي الله عنه.

When Quraysh denied the Isra' and Mi'raj, Abu Bakr affirmed the Messenger ﷺ at once and was named as-Siddiq, the confirmer of truth. He said he already believed him in revelation from heaven, so a night journey was not harder than that. The title remained his honour in hadith and tabaqat. Bukhari and Muslim preserve many reports of his truthfulness, weeping heart, and steadfastness in trial.

In 1 AH / 622 CE he prepared two mounts and accompanied the Prophet ﷺ on the Hijrah. They hid three nights in the cave of Thawr while searchers stood at the mouth. The Quran names him the second of two when they were in the cave (al-Tawbah 9:40). Asma' bint Abi Bakr رضي الله عنها brought food; Amir ibn Fuhayrah رضي الله عنه tended the flock. They then took the coastal road to Quba' and Madinah. That companionship became a proof of tawakkul and sacrifice.

In Madinah he was present at Badr, Uhud, Khandaq, and the later campaigns. In 9 AH the Prophet ﷺ sent him to lead the Hajj. In the final illness of Rabi' al-Awwal 11 AH / 632 CE, Abu Bakr was ordered to lead the people in prayer, a public trust recorded in Sahih al-Bukhari. After the Wafat, the Ansar gathered at the Saqifah of Banu Sa'idah. After discussion, bay'ah was given to Abu Bakr, and the community remained under one imam.

His caliphate of about two years and three months (11–13 AH / 632–634 CE) met the Wars of Apostasy (Riddah). Some tribes withheld zakah; others followed false claimants such as Musaylimah in al-Yamamah, al-Aswad al-Ansi in Yemen, and Tulayhah. Abu Bakr refused to separate salah from zakah and dispatched the armies. At Yamamah many huffaz fell. On Umar's counsel he commissioned Zayd ibn Thabit رضي الله عنه to collect the Quran from palm midribs, bones, parchments, and the breasts of men into one suhuf, as Bukhari reports.

Near death he consulted senior Companions and nominated Umar ibn al-Khattab رضي الله عنه, writing a covenant so the ummah would not be left in confusion. He died in Jumada al-Akhirah 13 AH (August 634 CE) at about sixty-three years. He was buried beside the Prophet ﷺ in the chamber of Aisha رضي الله عنها. Sunni tradition honours him without diminishing any other Companion; all the Sahaba رضي الله عنهم are held in respect.""",
    """ابو بکر عبد اللہ بن ابی قحافہ رضی اللہ عنہ قریش کے بنو تیم سے تھے اور نبوت سے پہلے اور بعد نبی محمد ﷺ کے سب سے قریبی دوست رہے۔ ابن سعد کی طبقات الکبریٰ اور ابن ہشام کی سیرت نسب، کپڑے کی تجارت اور مکہ میں ان کی امانت بیان کرتی ہیں۔ ولادت ہاتھی والے سال کے دو تین برس بعد ہوئی۔ والد عثمان ابو قحافہ کہلائے، والدہ سلمیٰ بنت صخر ام الخیر کہلائیں۔ اہل سنت کے نزدیک آپ ﷺ کے بعد اس امت کے افضل ہیں۔

وہ پہلے بالغ آزاد مرد تھے جنہوں نے اسلام قبول کیا۔ خواتین میں خدیجہ رضی اللہ عنہا اور گھر کے لڑکے علی رضی اللہ عنہ ایمان لا چکے تھے؛ ابو بکر کے اسلام نے دوسروں کے لیے دروازہ کھولا۔ ابن اسحاق کے بیان کے مطابق ان کی دعوت سے عثمان بن عفان، زبیر بن عوام، عبد الرحمن بن عوف، سعد بن ابی وقاص اور طلحہ بن عبید اللہ رضی اللہ عنہم ایمان لائے۔ مال خرچ کر کے توحید پر ستائے جانے والوں کو آزاد کیا، سب سے مشہور بلال بن رباح رضی اللہ عنہ ہیں۔

جب قریش نے اسراء و معراج کا انکار کیا تو ابو بکر نے فوراً تصدیق کی اور صدیق کہلائے۔ فرمایا کہ وہ آسمان کی خبر پر پہلے سے ایمان رکھتے ہیں تو رات کا سفر اس سے زیادہ مشکل نہیں۔ یہ لقب حدیث اور طبقات میں ان کا شرف رہا۔ بخاری و مسلم میں سچائی، رقت قلب اور آزمائش میں ثابت قدمی کی بہت سی روایات ہیں۔

1ھ / 622ء میں دو سواریاں تیار کیں اور ہجرت میں نبی ﷺ کے ساتھ رہے۔ غار ثور میں تین راتیں چھپے رہے جب تلاش کرنے والے دہانے پر کھڑے تھے۔ قرآن نے انہیں غار میں دو میں سے دوسرا کہا (التوبہ 9:40)۔ اسماء بنت ابی بکر رضی اللہ عنہا کھانا لاتیں، عامر بن فہیرہ رضی اللہ عنہ ریوڑ چراتے۔ پھر ساحلی راستے سے قباء اور مدینہ پہنچے۔ یہ رفاقت توکل اور قربانی کی دلیل بنی۔

مدینہ میں بدر، احد، خندق اور بعد کی مہمات میں شریک رہے۔ 9ھ میں نبی ﷺ نے حج کی امامت کے لیے بھیجا۔ ربیع الاول 11ھ / 632ء کی آخری بیماری میں نماز کی امامت کا حکم ہوا، یہ امانت صحیح بخاری میں محفوظ ہے۔ وفات کے بعد انصار سعدیفہ بنی ساعدہ میں جمع ہوئے۔ مشورے کے بعد ابو بکر کو بیعت ہوئی اور امت ایک امام کے نیچے رہی۔

تقریباً دو سال تین مہینے کی خلافت (11–13ھ / 632–634ء) میں ردّہ کی جنگیں ہوئیں۔ کچھ قبائل نے زکوٰۃ روک لی، کچھ یمامہ میں مسیلمہ، یمن میں اسود عنسی اور طلیحہ جیسے جھوٹے مدعیوں کے پیچھے لگے۔ ابو بکر نے نماز سے زکوٰۃ جدا نہ کی اور لشکر بھیجے۔ یمامہ میں بہت سے حفاظ شہید ہوئے۔ عمر کی رائے پر زید بن ثابت رضی اللہ عنہ کو حکم دیا کہ کھجور کی شاخوں، ہڈیوں، چمڑے اور سینوں سے قرآن ایک صحیفے میں جمع کریں، جیسا کہ بخاری میں ہے۔

وفات کے قریب اکابر صحابہ سے مشورہ کر کے عمر بن خطاب رضی اللہ عنہ کو نامزد کیا تاکہ امت بے امام نہ رہے۔ جمادی الاخریٰ 13ھ (اگست 634ء) میں تقریباً تریسٹھ برس کی عمر میں وفات ہوئی۔ عائشہ رضی اللہ عنہا کے حجرے میں نبی ﷺ کے پہلو میں دفن ہوئے۔ اہل سنت انہیں عزت دیتے ہیں بغیر کسی اور صحابی کی تنقیص کے؛ تمام صحابہ رضی اللہ عنہم قابل احترام ہیں۔""",
    """अबू बक्र अब्दुल्लाह इब्न अबी कुहाफा رضي الله عنه कुरैश के बनू तैम से थे और नबुव्वत से पहले और बाद नबी मुहम्मद ﷺ के सबसे क़रीबी दोस्त रहे। इब्न साद की तबाक़ात और इब्न हिशाम की सीरत उनका नसब, कपड़े की तिजारत और मक्का में अमानत बयान करती हैं। विलादत हाथी वाले साल के दो-तीन बरस बाद हुई। वालिद उस्मान अबू कुहाफा कहलाए, वालिदा सल्मा बिन्त सख़्र उम्मुल ख़ैर कहलाईं। अहले सुन्नत के नज़दीक आप ﷺ के बाद इस उम्मत के अफ़ज़ल हैं।

वे पहले बालिग आज़ाद मर्द थे जिन्होंने इस्लाम क़ुबूल किया। औरतों में ख़दीजा رضي الله عنها और घर के लड़के अली رضي الله عنه ईमान ला चुके थे; अबू बक्र के इस्लाम ने दूसरों के लिए दरवाज़ा खोला। इब्न इसहाक के बयान के मुताबिक उनकी दावत से उस्मान, ज़ुबैर, अब्दुर्रहमान बिन औफ़, साद बिन अबी वक़्क़ास और तलहा رضي الله عنهم ईमान लाए। माल ख़र्च कर के तौहीद पर सताए जाने वालों को आज़ाद किया, सबसे मशहूर बिलाल इब्न रबाह رضي الله عنه हैं।

जब कुरैश ने इसरा और मिराज का इन्कार किया तो अबू बक्र ने फ़ौरन तस्दीक की और सिद्दीक कहलाए। फ़रमाया कि वह आसमान की ख़बर पर पहले से ईमान रखते हैं तो रात का सफ़र उससे ज़्यादा मुश्किल नहीं। यह लक़ब हदीस और तबाक़ात में उनका शرف रहा। बुख़ारी व मुस्लिम में सच्चाई, रक़्क़ते क़ल्ब और आज़माइश में साबित क़दमी की बहुत सी रिवायात हैं।

1 हिजरी / 622 ई. में दो सवारियाँ तैयार कीं और हिजरत में नबी ﷺ के साथ रहे। ग़ार-ए-सौर में तीन रातें छिपे रहे जब तलाश करने वाले दहाने पर खड़े थे। कुरआन ने उन्हें ग़ार में दो में से दूसरा कहा (तौबा 9:40)। अस्मा बिन्त अबी बक्र رضي الله عنها खाना लातीं, आमिर बिन फुहैरा رضي الله عنه रेवड़ चराते। फिर साहिली रास्ते से क़ुबा और मदीना पहुँचे। यह रफ़ाक़त तवक्कुल और क़ुरबानी की दलील बनी।

मदीना में बद्र, उहुद, खंदक और बाद की मुहिमों में शरीक रहे। 9 हिजरी में नबी ﷺ ने हज की इमामत के लिए भेजा। रबीउल अव्वल 11 हिजरी / 632 ई. की आख़िरी बीमारी में नमाज़ की इमामत का हुक्म हुआ, यह अमानत सहीह बुख़ारी में महफ़ूज़ है। विसाल के बाद अनसार सक़ीफ़ा बनी साईदा में जमा हुए। मशवरे के बाद अबू बक्र को बैअत हुई और उम्मत एक इमाम के नीचे रही।

क़रीब दो साल तीन महीने की खिलाफ़त (11–13 हिजरी / 632–634 ई.) में रिद्दा की जंगें हुईं। कुछ क़बीलों ने ज़कात रोक ली, कुछ यमामा में मुसैलिमा, यमन में असवद अनसी और तुलैहा जैसे झूठे मुदइयों के पीछे लगे। अबू बक्र ने नमाज़ से ज़कात जुदा न की और लश्कर भेजे। यमामा में बहुत से हुफ़्फ़ाज़ शहीद हुए। उमर की राय पर ज़ैद बिन साबित رضي الله عنه को हुक्म दिया कि खजूर की शाख़ों, हड्डियों, चमड़े और सीनों से कुरआन एक सहीफे में जमा करें, जैसा बुख़ारी में है।

वफ़ात के क़रीब अकाबिर सहाबा से मशवरा कर के उमर इब्न अल-खत्ताब رضي الله عنه को नामज़द किया ताकि उम्मत बे-इमाम न रहे। जमादीउल आख़िरा 13 हिजरी (अगस्त 634 ई.) में क़रीब तिरेसठ बरस की उम्र में वफ़ात हुई। आयशा رضي الله عنها के हुजरे में नबी ﷺ के पहलू में दफ़न हुए। अहले सुन्नत उन्हें इज़्ज़त देते हैं बिना किसी और सहाबी की तनक़ीस के; तमाम सहाबा رضي الله عنهم क़ाबिले एहतिराम हैं।""",
    """আবু বকর আবদুল্লাহ ইবন আবি কুহাফা رضي الله عنه কুরাইশের বনু তাইম গোত্রের এবং নবুয়তের আগে ও পরে নবী মুহাম্মদ ﷺ-এর ঘনিষ্ঠতম বন্ধু ছিলেন। ইবন সাদের তাবাকাত ও ইবন হিশামের সিরাত তাঁর বংশ, কাপড়ের বাণিজ্য এবং মক্কায় সততা বর্ণনা করে। হস্তিবর্ষের দুই-তিন বছর পর তাঁর জন্ম। পিতা উসমান আবু কুহাফা নামে পরিচিত; মাতা সালমা বিনত সাখর উম্মুল খায়র নামে খ্যাত। আহলুস সুন্নাহর মতে তিনি নবী ﷺ-এর পর এই উম্মাহর শ্রেষ্ঠ।

তিনি ইসলাম গ্রহণকারী প্রথম প্রাপ্তবয়স্ক স্বাধীন পুরুষ। নারীদের মধ্যে খাদিজাহ رضي الله عنها এবং গৃহের বালক আলী رضي الله عنه ইতিমধ্যে ঈমান এনেছিলেন; আবু বকরের ইসলাম অন্যদের জন্য দুয়ার খুলে দেয়। ইবন ইসহাকের বর্ণনায় তাঁর দাওয়াতে উসমান, যুবায়র, আব্দুর রহমান ইবন আওফ, সাদ ইবন আবি ওয়াক্কাস ও তালহা رضي الله عنهم ঈমান আনেন। তাওহিদের জন্য নির্যাতিতদের মুক্ত করতে সম্পদ ব্যয় করেন, সর্বাধিক প্রসিদ্ধ বিলাল ইবন রাবাহ رضي الله عنه।

কুরাইশ যখন ইসরা ও মিরাজ অস্বীকার করল, আবু বকর তৎক্ষণাৎ সত্যায়ন করেন এবং সিদ্দিক নামে খ্যাত হন। তিনি বলেন, আকাশের সংবাদে তিনি আগেই বিশ্বাস করেন, রাতের সফর তার চেয়ে কঠিন নয়। এই উপাধি হাদিস ও তাবাকাতে তাঁর সম্মান। বুখারি ও মুসলিমে সত্যতা, কোমল হৃদয় ও পরীক্ষায় অবিচলতার অনেক বর্ণনা আছে।

১ হিজরি / ৬২২ খ্রিষ্টাব্দে দুটি বাহন প্রস্তুত করে হিজরতে নবী ﷺ-এর সঙ্গী হন। সওর গুহায় তিন রাত লুকিয়ে থাকেন যখন অনুসন্ধানকারীরা মুখে দাঁড়িয়েছিল। কুরআন তাঁকে গুহায় দুজনের দ্বিতীয়জন বলে (আত-তাওবা ৯:৪০)। আসমা বিনত আবি বকর رضي الله عنها খাবার আনতেন; আমির ইবন ফুহায়রাহ رضي الله عنه পাল চরাতেন। তারপর উপকূলীয় পথে কুবা ও মদিনায় পৌঁছান। এই সাহচর্য তাওয়াক্কুল ও কুরবানির প্রমাণ হয়।

মদিনায় বদর, উহুদ, খন্দক ও পরবর্তী অভিযানে শরিক ছিলেন। ৯ হিজরিতে নবী ﷺ তাঁকে হজের ইমামতি দিতে পাঠান। রবিউল আউয়াল ১১ হিজরি / ৬৩২ খ্রিষ্টাব্দের শেষ অসুস্থতায় নামাজের ইমামতির আদেশ হয়, যা সহীহ বুখারিতে সংরক্ষিত। ওফাতের পর আনসার বনু সাইদার সাকিফায় সমবেত হন। পরামর্শের পর আবু বকরকে বাইআত দেওয়া হয় এবং উম্মাহ এক ইমামের অধীনে থাকে।

প্রায় দুই বছর তিন মাসের খিলাফতে (১১–১৩ হিজরি / ৬৩২–৬৩৪) রিদ্দার যুদ্ধ হয়। কিছু গোত্র যাকাত আটকে রাখে; কেউ ইয়ামামায় মুসাইলিমা, ইয়েমেনে আসওয়াদ আনসি ও তুলায়হার মতো মিথ্যা দাবিদারদের অনুসরণ করে। আবু বকর সালাত থেকে যাকাত পৃথক করেননি এবং সেনা পাঠান। ইয়ামামায় অনেক হাফিজ শহীদ হন। উমরের পরামর্শে যায়েদ ইবন সাবিত رضي الله عنه-কে খেজুর ডাল, হাড়, চামড়া ও স্মৃতি থেকে কুরআন এক সহীফে সংগ্রহের নির্দেশ দেন, বুখারির বর্ণনায়।

মৃত্যুর কাছাকাছি শীর্ষ সাহাবিদের পরামর্শে উমর ইবনুল খাত্তাব رضي الله عنه-কে মনোনীত করেন যাতে উম্মাহ ইমামহীন না থাকে। জুমাদাল আখিরা ১৩ হিজরি (আগস্ট ৬৩৪) প্রায় তেষট্টি বছর বয়সে ইন্তেকাল করেন। আয়িশা رضي الله عنها-এর হুজরায় নবী ﷺ-এর পাশে দাফন হন। আহলুস সুন্নাহ তাঁকে সম্মান করেন অন্য কোনো সাহাবিকে খাটো না করে; সকল সাহাবি رضي الله عنهم সম্মানার্হ।""",
    """Abu Bakar Abdullah bin Abi Quhafah رضي الله عنه dari Bani Taim Quraisy adalah sahabat terdekat Nabi Muhammad ﷺ sebelum dan sesudah kenabian. Ibnu Sa'd dalam al-Tabaqat al-Kubra dan sirah Ibnu Hisyam mencatat nasabnya, dagang kain, dan kejujurannya di Makkah. Ia lahir sekitar dua atau tiga tahun setelah Tahun Gajah. Ayahnya Utsman dipanggil Abu Quhafah; ibunya Salma binti Sakhr dipanggil Ummul Khair. Ulama Ahlusunah menilainya manusia terbaik umat ini setelah Nabinya ﷺ.

Ia orang merdeka dewasa pertama yang masuk Islam. Khadijah رضي الله عنها beriman pertama di kalangan wanita, dan Ali رضي الله عنه sebagai anak di rumah; Islam Abu Bakar sebagai orang merdeka yang terhormat membuka jalan bagi yang lain. Melalui dakwahnya Utsman, Zubair, Abdurrahman bin Auf, Sa'd bin Abi Waqqas, dan Thalhah رضي الله عنهم masuk Islam, sebagaimana diriwayatkan Ibnu Ishaq. Ia membelanjakan harta untuk memerdekakan orang yang disiksa karena tauhid, terutama Bilal bin Rabah رضي الله عنه.

Ketika Quraisy mengingkari Isra dan Mikraj, Abu Bakar membenarkan Rasulullah ﷺ seketika dan dinamai ash-Shiddiq, pembenar kebenaran. Ia berkata bahwa ia sudah membenarkan berita dari langit, maka perjalanan malam tidak lebih sulit dari itu. Gelar itu tetap kemuliaannya dalam hadis dan tabaqat. Bukhari dan Muslim menyimpan banyak riwayat tentang kejujuran, kelembutan hati, dan keteguhannya dalam ujian.

Pada 1 H / 622 M ia menyiapkan dua tunggangan dan menemani Nabi ﷺ dalam Hijrah. Mereka bersembunyi tiga malam di Gua Tsur sementara pencari berdiri di mulut gua. Al-Qur'an menyebutnya orang kedua dari dua ketika mereka di gua (at-Taubah 9:40). Asma binti Abi Bakar رضي الله عنها membawa makanan; Amir bin Fuhairah رضي الله عنه menggembala. Mereka lalu menempuh jalan pantai ke Quba dan Madinah. Persahabatan itu menjadi bukti tawakkal dan pengorbanan.

Di Madinah ia hadir di Badar, Uhud, Khandaq, dan ekspedisi kemudian. Pada 9 H Nabi ﷺ mengutusnya memimpin haji. Pada sakit terakhir Rabiul Awal 11 H / 632 M, Abu Bakar diperintahkan mengimami salat, amanah yang tercatat dalam Sahih Bukhari. Setelah Wafat, Ansar berkumpul di Saqifah Bani Saidah. Setelah musyawarah, baiat diberikan kepada Abu Bakar, dan umat tetap di bawah satu imam.

Khilafahnya sekitar dua tahun tiga bulan (11–13 H / 632–634 M) menghadapi Perang Riddah. Sebagian kabilah menahan zakat; yang lain mengikuti pengaku palsu seperti Musailamah di Yamamah, al-Aswad al-Ansi di Yaman, dan Tulaihah. Abu Bakar menolak memisahkan salat dari zakat dan mengirim pasukan. Di Yamamah banyak huffaz gugur. Atas nasihat Umar ia menugaskan Zaid bin Tsabit رضي الله عنه mengumpulkan Al-Qur'an dari pelepah kurma, tulang, kulit, dan hafalan dada menjadi satu suhuf, sebagaimana diriwayatkan Bukhari.

Menjelang wafat ia bermusyawarah dengan sahabat senior dan menunjuk Umar bin Khattab رضي الله عنه agar umat tidak dibiarkan tanpa imam yang dikenal. Ia wafat pada Jumadil Akhir 13 H (Agustus 634 M) sekitar usia enam puluh tiga tahun. Ia dimakamkan di sisi Nabi ﷺ di kamar Aisyah رضي الله عنها. Tradisi Ahlusunah memuliakannya tanpa merendahkan sahabat lain; seluruh Sahabat رضي الله عنهم dihormati.""",
)
ch["items"][0]["details"] = D(
    """Abu Bakr رضي الله عنه was one of the ten promised Paradise, the asharah mubashsharah, a rank the Prophet ﷺ announced in well-known hadith collected by the sunan compilers. That promise did not make him independent of worship; he fasted, wept in prayer, and feared a slip more than he trusted a title. Sunni creed holds all ten in honour together, without setting the Sahaba against one another.

His daughter Aisha رضي الله عنها became a Mother of the Believers and one of the most learned of the ummah. After the Prophet's ﷺ death she transmitted a great body of hadith on worship, household sunnah, and fiqh. The marriage tied Abu Bakr's house to the Messenger ﷺ by love as well as by faith. Respect for Aisha is part of respect for her father and for the Prophet's ﷺ household.

His caliphate lasted only about two years and a few months, yet it decided whether the community would remain one after its Prophet ﷺ. Many Arabs thought zakah had been a tribute paid to Muhammad ﷺ personally. Abu Bakr declared that he would fight whoever separated salah from zakah, even if they withheld only a young camel. That stand kept the pillars of the din from breaking apart in the first crisis.

The zakah wars were not a hunger for rule. They were a defence of the rights of the poor and of the public treasury that the Prophet ﷺ had organised. Commanders went out in several directions while Madinah itself was guarded. Reports in the maghazi and in Ibn Sa'd show the hardship of those months: scarce men, simultaneous fronts, and the need for a single political centre.

False prophets rose in the vacuum. Musaylimah in Yamamah gathered a large host; the battle there was among the fiercest of the Riddah. Many reciters of the Quran were martyred, which directly prompted the written compilation. Other pretenders collapsed more quickly. Abu Bakr's policy was to invite return to Islam, then to use force where rebellion and bloodshed continued.

When death approached he did not leave the ummah to a sudden contest. He consulted Uthman, Abd al-Rahman ibn Awf, and other seniors, heard Umar's known sternness discussed, and still judged him the strongest to bear the load. He wrote a testament nominating Umar رضي الله عنه. The people pledged to Umar after Abu Bakr's janazah. That shura-within-nomination became a model of responsible succession among the Rashidun.

Later Sunni historians, from al-Tabari to Ibn Kathir, treat this short reign as the shield of the community. They praise his companionship in the cave, his prayer-leadership, his Riddah resolve, and his care for the mushaf, while they also honour Umar, Uthman, Ali, and the rest of the Sahaba رضي الله عنهم. No classical Sunni encyclopedia makes the first caliph an excuse to attack other Companions.""",
    """ابو بکر رضی اللہ عنہ عشرہ مبشرہ میں سے تھے، وہ دس جنہیں نبی ﷺ نے جنت کی خوشخبری دی، جیسا کہ سنن کی مشہور احادیث میں ہے۔ اس وعدے نے انہیں عبادت سے بے نیاز نہ کیا؛ روزے رکھتے، نماز میں روتے، اور لقب سے زیادہ لغزش کا خوف رکھتے۔ اہل سنت کے عقیدے میں یہ دسوں اکٹھے محترم ہیں، صحابہ کو آپس میں ٹکرانے کے بغیر۔

بیٹی عائشہ رضی اللہ عنہا ام المؤمنین اور امت کی سب سے عالم خواتین میں سے ہوئیں۔ نبی ﷺ کی وفات کے بعد عبادت، گھریلو سنت اور فقہ پر بہت سی احادیث روایت کیں۔ یہ نکاح ابو بکر کے گھر کو رسول ﷺ سے ایمان کے ساتھ محبت میں بھی جوڑتا تھا۔ عائشہ کی عزت والد اور نبی ﷺ کے گھر کی عزت کا حصہ ہے۔

خلافت صرف تقریباً دو سال چند مہینے رہی، مگر اسی سے طے ہوا کہ نبی ﷺ کے بعد امت ایک رہے گی یا نہیں۔ بہت سے عرب سمجھے زکوٰۃ محمد ﷺ کی ذاتی محصول تھی۔ ابو بکر نے اعلان کیا کہ جو نماز سے زکوٰۃ جدا کرے اس سے جنگ کریں گے، گو ایک اونٹنی کا بچہ ہی روکے۔ اس موقف نے دین کے ارکان کو پہلی آزمائش میں ٹوٹنے سے بچایا۔

زکوٰۃ کی جنگیں سلطنت کی ہوس نہ تھیں۔ یہ غریبوں کے حق اور اس بیت المال کی حفاظت تھیں جو نبی ﷺ نے منظم کیا تھا۔ کئی سمتوں میں لشکر گئے، مدینہ کی حفاظت بھی ہوئی۔ مغازی اور ابن سعد ان مہینوں کی تنگی دکھاتے ہیں: کم آدمی، کئی محاذ، اور ایک سیاسی مرکز کی ضرورت۔

خلا میں جھوٹے نبی اٹھے۔ یمامہ میں مسیلمہ بڑی فوج اکٹھی کی؛ وہاں کی جنگ ردّہ کی سخت ترین میں سے تھی۔ بہت سے قاری قرآن شہید ہوئے، اسی سے تحریری جمع کا سبب بنا۔ دوسرے مدعی جلد گرے۔ ابو بکر کی سیاست پہلے اسلام کی طرف واپسی کی دعوت، پھر جہاں بغاوت اور خون جاری رہے قوت کا استعمال تھی۔

موت قریب آئی تو امت کو اچانک جھگڑے پر نہ چھوڑا۔ عثمان، عبد الرحمن بن عوف اور دیگر اکابر سے مشورہ کیا، عمر کی معروف سختی سنی، پھر بھی انہیں بار اٹھانے کے لیے سب سے مضبوط جانا۔ عمر رضی اللہ عنہ کی نامزدگی کا عہد لکھا۔ جنازے کے بعد لوگوں نے عمر سے بیعت کی۔ نامزدگی کے اندر یہ شوریٰ خلافت راشدہ میں ذمہ دار جانشینی کی مثال بنی۔

بعد کے سنی مورخ، طبری سے ابن کثیر تک، اس مختصر دور کو امت کی ڈھال قرار دیتے ہیں۔ غار کی رفاقت، امامتِ نماز، عزمِ ردّہ اور مصحف کی فکر کی تعریف کرتے ہیں، اور عمر، عثمان، علی اور باقی صحابہ رضی اللہ عنہم کو بھی عزت دیتے ہیں۔ کوئی کلاسیکی سنی دائرۃ المعارف پہلے خلیفہ کو دوسرے صحابہ پر حملے کا بہانہ نہیں بناتی۔""",
    """अबू बक्र رضي الله عنه अशरा-ए-मुबश्शिरा में से थे, वे दस जिन्हें नबी ﷺ ने जन्नत की खुशख़बरी दी, जैसा सुनन की मशहूर अहादीस में है। उस वादे ने उन्हें इबादत से बेनियाज़ न किया; रोज़े रखते, नमाज़ में रोते, और लक़ब से ज़्यादा लग़ज़िश का ख़ौफ़ रखते। अहले सुन्नत के अक़ीदे में ये दसों इकट्ठे मुहतरम हैं, सहाबा को आपस में टकराने के बिना।

बेटी आयशा رضي الله عنها उम्मुल मुमिनीन और उम्मत की सबसे आलिम औरतों में से हुईं। नबी ﷺ की वफ़ात के बाद इबादत, घरेलू सुन्नत और फ़िक़्ह पर बहुत सी हदीसें रिवायत कीं। यह निकाह अबू बक्र के घर को रसूल ﷺ से ईमान के साथ मुहब्बत में भी जोड़ता था। आयशा की इज़्ज़त वालिद और नबी ﷺ के घर की इज़्ज़त का हिस्सा है।

खिलाफ़त सिर्फ़ क़रीब दो साल कुछ महीने रही, मगर इसी से तय हुआ कि नबी ﷺ के बाद उम्मत एक रहेगी या नहीं। बहुत से अरब समझे ज़कात मुहम्मद ﷺ की ज़ाती महसूल थी। अबू बक्र ने एलान किया कि जो नमाज़ से ज़कात जुदा करे उससे जंग करेंगे, गो एक ऊँटनी का बच्चा ही रोके। इस मौक़िफ़ ने दीन के अरकान को पहली आज़माइश में टूटने से बचाया।

ज़कात की जंगें सल्तनत की हवस न थीं। यह ग़रीबों के हक़ और उस बैतुलमाल की हिफ़ाज़त थीं जो नबी ﷺ ने मुनज़्ज़म किया था। कई सिम्तों में लश्कर गए, मदीना की हिफ़ाज़त भी हुई। मग़ाज़ी और इब्न साद उन महीनों की तंगी दिखाते हैं: कम आदमी, कई मोर्चे, और एक सियासी मर्कज़ की ज़रूरत।

ख़ला में झूठे नबी उठे। यमामा में मुसैलिमा बड़ी फ़ौज इकट्ठी की; वहाँ की जंग रिद्दा की सख़्ततरीन में से थी। बहुत से क़ारी-ए-कुरआन शहीद हुए, इसी से तहरीरि जमा का सबब बना। दूसरे मुदई जल्द गिरे। अबू बक्र की सियासत पहले इस्लाम की तरफ़ वापसी की दावत, फिर जहाँ बग़ावत और ख़ून जारी रहे क़ुव्वत का इस्तेमाल थी।

मौत क़रीब आई तो उम्मत को अचानक झगड़े पर न छोड़ा। उस्मान, अब्दुर्रहमान बिन औफ़ और अन्य अकाबिर से मशवरा किया, उमर की मारूफ़ सख़्ती सुनी, फिर भी उन्हें बोझ उठाने के लिए सबसे मज़बूत जाना। उमर رضي الله عنه की नामज़दगी का अहद लिखा। जनाज़े के बाद लोगों ने उमर से बैअत की। नामज़दगी के अंदर यह शूरा खिलाफ़त-ए-राशिदा में ज़िम्मेदार जानशिनी की मिसाल बनी।

बाद के सुन्नी मुवर्रिख़, तबरी से इब्न कसीर तक, इस मुख़्तसर दौर को उम्मत की ढाल क़रार देते हैं। ग़ार की रफ़ाक़त, इमामत-ए-नमाज़, अज़्म-ए-रिद्दा और मुसहफ़ की फ़िक्र की तारीफ़ करते हैं, और उमर, उस्मान, अली और बाक़ी सहाबा رضي الله عنهم को भी इज़्ज़त देते हैं। कोई क्लासिकी सुन्नी दाइरतुल मआरिफ़ पहले ख़लीफा को दूसरे सहाबा पर हमले का बहाना नहीं बनाती।""",
    """আবু বকর رضي الله عنه আশারায়ে মুবাশশারার একজন, সেই দশজন যাঁদের নবী ﷺ জান্নাতের সুসংবাদ দিয়েছেন, সুনানের প্রসিদ্ধ হাদিসে। সেই প্রতিশ্রুতি তাঁকে ইবাদত থেকে নিষ্প্রয়োজন করেনি; তিনি রোজা রাখতেন, নামাজে কাঁদতেন, উপাধির চেয়ে পদস্খলনের ভয় রাখতেন। আহলুস সুন্নাহর আকিদায় এই দশজন একত্রে সম্মানিত, সাহাবিদের পরস্পরের বিরুদ্ধে দাঁড় করানো হয় না।

কন্যা আয়িশা رضي الله عنها উম্মুল মুমিনীন এবং উম্মাহর শ্রেষ্ঠ আলিমাদের একজন হন। নবী ﷺ-এর ওফাতের পর ইবাদত, গৃহস্থলী সুন্নাত ও ফিকহে বিপুল হাদিস বর্ণনা করেন। এই বিবাহ আবু বকরের ঘরকে রাসূল ﷺ-এর সঙ্গে ঈমানের সাথে ভালোবাসায়ও যুক্ত করে। আয়িশার সম্মান পিতা ও নবী ﷺ-এর ঘরের সম্মানের অংশ।

খিলাফত মাত্র প্রায় দুই বছর কিছু মাস স্থায়ী হলেও এতেই নির্ধারিত হয় নবী ﷺ-এর পর উম্মাহ এক থাকবে কি না। অনেক আরব মনে করল যাকাত মুহাম্মদ ﷺ-এর ব্যক্তিগত কর। আবু বকর ঘোষণা করেন, সালাত থেকে যাকাত পৃথক করলে তিনি যুদ্ধ করবেন, একটি উষ্ট্রীশাবক আটকালেও। এই অবস্থান দীনের স্তম্ভগুলোকে প্রথম সংকটে ভাঙতে দেয়নি।

যাকাতের যুদ্ধ রাজত্বলোভ ছিল না। এগুলো ছিল দরিদ্রের অধিকার ও নবী ﷺ-এর গঠিত বায়তুলমালের রক্ষা। কয়েক দিকে সেনা যায়, মদিনাও রক্ষিত হয়। মাগাজি ও ইবন সাদ সেই মাসগুলোর কষ্ট দেখায়: কম লোক, একাধিক ফ্রন্ট, একটি রাজনৈতিক কেন্দ্রের প্রয়োজন।

শূন্যতায় মিথ্যা নবী উঠে। ইয়ামামায় মুসাইলিমা বিশাল বাহিনী জড়ায়; সেখানকার যুদ্ধ রিদ্দার তীব্রতমগুলোর একটি। অনেক কুরআন পাঠক শহীদ হন, এতেই লিখিত সংকলনের কারণ হয়। অন্য দাবিদাররা দ্রুত পতিত হয়। আবু বকরের নীতি ছিল প্রথমে ইসলামে প্রত্যাবর্তনের আহ্বান, তারপর যেখানে বিদ্রোহ ও রক্তপাত চলতে থাকে শক্তি প্রয়োগ।

মৃত্যু ঘনিয়ে এলে তিনি উম্মাহকে আকস্মিক বিবাদে ছাড়েননি। উসমান, আব্দুর রহমান ইবন আওফ ও অন্য শীর্ষদের পরামর্শ নেন, উমরের পরিচিত কঠোরতা শোনেন, তবু তাঁকেই ভার বহনের জন্য সবচেয়ে শক্তিশালী মনে করেন। উমর رضي الله عنه-এর মনোনয়নের অসিয়ত লেখেন। জানাজার পর লোকেরা উমরকে বাইআত দেয়। মনোনয়নের অভ্যন্তরে এই শূরা রাশিদুন খিলাফতে দায়িত্বশীল উত্তরাধিকারের আদর্শ হয়।

পরবর্তী সুন্নি ঐতিহাসিক, তাবারি থেকে ইবন কাসির, এই সংক্ষিপ্ত শাসনকে উম্মাহর ঢাল বলে। গুহার সাহচর্য, নামাজের ইমামতি, রিদ্দার সংকল্প ও মুশাফের যত্নের প্রশংসা করেন, এবং উমর, উসমান, আলী ও অবশিষ্ট সাহাবি رضي الله عنهم-কেও সম্মান করেন। কোনো ক্লাসিক সুন্নি বিশ্বকোষ প্রথম খলিফাকে অন্য সাহাবিদের আক্রমণের অজুহাত করে না।""",
    """Abu Bakar رضي الله عنه termasuk sepuluh yang dijamin surga, al-asyarah al-mubasysyarah, martabat yang diumumkan Nabi ﷺ dalam hadis masyhur para penyusun sunan. Janji itu tidak membuatnya lepas dari ibadah; ia berpuasa, menangis dalam salat, dan lebih takut tergelincir daripada mengandalkan gelar. Akidah Ahlusunah memuliakan kesepuluhnya bersama, tanpa mempertentangkan para Sahabat.

Putrinya Aisyah رضي الله عنها menjadi Ummul Mukminin dan salah satu wanita paling berilmu di umat. Setelah Nabi ﷺ wafat ia meriwayatkan banyak hadis tentang ibadah, sunah rumah tangga, dan fikih. Pernikahan itu mengikat rumah Abu Bakar kepada Rasul ﷺ dengan cinta sekaligus iman. Menghormati Aisyah adalah bagian dari menghormati ayahnya dan rumah Nabi ﷺ.

Khilafahnya hanya sekitar dua tahun beberapa bulan, namun justru itu yang menentukan apakah umat tetap satu setelah Nabinya ﷺ. Banyak orang Arab mengira zakat adalah upeti pribadi kepada Muhammad ﷺ. Abu Bakar menyatakan akan memerangi siapa yang memisahkan salat dari zakat, sekalipun mereka menahan seekor anak unta. Sikap itu menjaga rukun agama agar tidak pecah pada krisis pertama.

Perang zakat bukan lapar kekuasaan. Itu pembelaan hak orang miskin dan baitulmal yang diatur Nabi ﷺ. Panglima dikirim ke beberapa arah sementara Madinah dijaga. Riwayat maghazi dan Ibnu Sa'd menunjukkan beratnya bulan-bulan itu: sedikit pasukan, banyak front, dan perlunya satu pusat politik.

Nabi palsu muncul dalam kekosongan. Musailamah di Yamamah mengumpulkan pasukan besar; pertempuran di sana termasuk paling dahsyat dalam Riddah. Banyak penghafal Al-Qur'an syahid, dan itu langsung mendorong kodifikasi tertulis. Pengaku lain runtuh lebih cepat. Kebijakan Abu Bakar adalah mengajak kembali ke Islam, lalu memakai kekuatan di mana pemberontakan dan pertumpahan darah berlanjut.

Ketika ajal mendekat ia tidak meninggalkan umat pada sengketa mendadak. Ia bermusyawarah dengan Utsman, Abdurrahman bin Auf, dan senior lain, mendengar sifat tegas Umar yang sudah dikenal, lalu tetap menilainya paling kuat memikul beban. Ia menulis wasiat menunjuk Umar رضي الله عنه. Orang-orang berbaiat kepada Umar setelah jenazah Abu Bakar. Syura di dalam penunjukan itu menjadi teladan suksesi yang bertanggung jawab di kalangan Khulafaur Rasyidin.

Sejarawan Ahlusunah kemudian, dari ath-Thabari hingga Ibnu Katsir, memandang masa singkat ini sebagai perisai umat. Mereka memuji persahabatan di gua, imamah salat, ketegasan Riddah, dan perhatian pada mushaf, sambil tetap memuliakan Umar, Utsman, Ali, dan Sahabat lainnya رضي الله عنهم. Tidak ada ensiklopedia klasik Ahlusunah yang menjadikan khalifah pertama alasan untuk menyerang Sahabat lain.""",
)

# --- 2 Umar ibn al-Khattab ---
ch = chapter(2)
ch["details"] = D(
    """Umar ibn al-Khattab ibn Nufayl رضي الله عنه was from Banu Adi of Quraysh, a clan known for arbitration and strength in Makkah. Ibn Sa'd and the sirah of Ibn Hisham describe his early life as that of a vigorous man, a wrestler and a herdsman, feared by the weak Muslims before his conversion. He was born about thirteen years after the Year of the Elephant. His mother was Hantamah bint Hashim of Banu Makhzum. Until the sixth year of Prophethood he remained among the opponents of the new faith.

His Islam, in about the sixth year of the mission (around 616 CE), is among the most famous stories of the Makkan period. Reports in Ibn Ishaq say he set out in anger, then found his sister Fatimah and her husband Sa'id ibn Zayd رضي الله عنهما reciting verses of Ta-Ha with Khabbab ibn al-Aratt. After striking them he was ashamed, asked to hear the parchment, and went to the house of al-Arqam. There he declared the shahadah before the Prophet ﷺ. From that day the Muslims prayed openly at the Ka'bah, for his stature among Quraysh made concealment harder to maintain.

He later migrated to Madinah openly, sword in view, challenging anyone who would prevent him, as later historians retell from early reports. In Madinah the Prophet ﷺ often sought his counsel; many verses of agreement with Umar's view are discussed in tafsir, such as the station of Ibrahim and the hijab. He fought at Badr, Uhud, Khandaq, and Hunayn. The Prophet ﷺ named him al-Faruq, the one who distinguishes truth from falsehood. He was among the asharah mubashsharah.

After Abu Bakr's death in 13 AH / 634 CE he became the second khalifah by the written nomination and the bay'ah of the people. His reign lasted ten years (13–23 AH / 634–644 CE). In that decade Syria, Iraq, Persia, and Egypt were opened under commanders such as Abu Ubaydah ibn al-Jarrah, Sa'd ibn Abi Waqqas, Amr ibn al-As, and Khalid ibn al-Walid رضي الله عنهم. The battles of Yarmuk, Qadisiyyah, and the later campaigns into the Sasanian heartland reshaped the region. Umar organised provinces, stipends, and treaties rather than leaving conquest as mere raid.

He established the Hijri calendar from the year of the Hijrah, set up the diwan to register names and 'ata' (stipends) for the fighters and their families, and walked the streets of Madinah at night to hear the needs of the poor. Classical reports of his patched cloak, his carrying of a sack for a widow, and his questioning of governors became the moral image of his justice. He dismissed or checked officials who lived above the people. The title al-Faruq in public memory is tied as much to this domestic justice as to the fronts of war.

In Dhul-Hijjah 23 AH / November 644 CE, while leading Fajr in the Prophet's Mosque, he was stabbed by Abu Lu'lu'ah, a Persian craftsman with a grievance. He lingered about three days, performed salah as long as he could, and arranged a shura for succession. He asked Aisha رضي الله عنها for permission to be buried beside his two companions. He died and was buried next to the Prophet ﷺ and Abu Bakr رضي الله عنه. Sunni tradition counts him among the greatest of the Rashidun and does not use his honour as a weapon against other Sahaba.

His last concern was the ummah, not a dynasty. He refused to appoint his son Abdullah as caliph despite Abdullah's piety and knowledge, saying one house should not bear two caliphates in succession in that way. He left a council of six. The combination of conquest, law, and night patrols is why later fuqaha and historians, from al-Tabari to Ibn al-Jawzi, treat Umar as the archetype of the just imam after the Prophet ﷺ and Abu Bakr.""",
    """عمر بن خطاب بن نفیل رضی اللہ عنہ قریش کے بنو عدی سے تھے، ایک شاخ جو مکہ میں فیصلے اور قوت کے لیے جانی جاتی تھی۔ ابن سعد اور ابن ہشام کی سیرت ان کی جوانی کو طاقتور آدمی، پہلوان اور چرواہے کے طور پر بیان کرتی ہے، اسلام سے پہلے کمزور مسلمان جن سے ڈرتے تھے۔ ولادت ہاتھی والے سال کے تقریباً تیرہ برس بعد ہوئی۔ والدہ حنتمہ بنت ہاشم بنو مخزوم سے تھیں۔ نبوت کے چھٹے سال تک نئے دین کے مخالفین میں رہے۔

ان کا اسلام تقریباً چھٹے سالِ دعوت (قریب 616ء) مکی دور کی مشہور ترین داستانوں میں سے ہے۔ ابن اسحاق کی روایت ہے کہ غصے میں نکلے، پھر بہن فاطمہ اور شوہر سعید بن زید رضی اللہ عنہما کو خباب بن ارت کے ساتھ طٰہ کی آیتیں پڑھتے پایا۔ مارنے کے بعد شرمندہ ہوئے، صحیفہ سنا، ارقم کے گھر گئے اور نبی ﷺ کے سامنے کلمہ پڑھا۔ اسی دن سے مسلمان کعبہ میں کھل کر نماز پڑھنے لگے، کیونکہ قریش میں ان کی حیثیت سے چھپنا دشوار ہو گیا۔

بعد میں مدینہ علانیہ ہجرت کی، تلوار سامنے، جو روکے مقابلے کو کہا، جیسا کہ متقدم روایات سے مورخ نقل کرتے ہیں۔ مدینہ میں نبی ﷺ اکثر مشورہ لیتے؛ تفسیر میں عمر کی رائے سے موافقت کی بہت سی آیتیں ذکر ہوتی ہیں، جیسے مقام ابراہیم اور حجاب۔ بدر، احد، خندق اور حنین میں لڑے۔ نبی ﷺ نے فاروق کا لقب دیا، حق و باطل میں فرق کرنے والا۔ عشرہ مبشرہ میں سے تھے۔

ابو بکر کی وفات 13ھ / 634ء کے بعد تحریری نامزدگی اور لوگوں کی بیعت سے دوسرے خلیفہ بنے۔ دس سال کی حکومت (13–23ھ / 634–644ء)۔ اس دہائی میں ابو عبیدہ بن جراح، سعد بن ابی وقاص، عمرو بن عاص اور خالد بن ولید رضی اللہ عنہم جیسے کمانڈروں کے تحت شام، عراق، فارس اور مصر کھلے۔ یرموک، قادسیہ اور ساسانی قلب تک مہمات نے خطے کی شکل بدل دی۔ عمر نے محض چھاپے نہیں چھوڑے بلکہ صوبے، وظائف اور معاہدے منظم کیے۔

ہجرت کے سال سے ہجری کیلنڈر قائم کیا، دیوان بنا کر جنگجوؤں اور گھرانوں کے نام اور عطاء درج کیے، اور رات مدینہ کی گلیوں میں گھوم کر غریبوں کی حاجت سنتی۔ پیوند لگے جبے، بیوہ کے لیے بوریا اٹھانے، اور گورنروں سے حساب کی کلاسیکی روایات عدل کی تصویر بن گئیں۔ جو حاکم رعایا سے اوپر رہتے انہیں ہٹایا یا جھنجھوڑا۔ عوامی یاد میں فاروق کا لقب جنگ کے محاذوں جتنا گھریلو انصاف سے جڑا ہے۔

ذوالحجہ 23ھ / نومبر 644ء میں مسجد نبوی میں فجر پڑھا رہے تھے کہ ابو لؤلؤہ نے زخمی کیا، ایک فارسی کاریگر جسے شکایت تھی۔ تقریباً تین دن زندہ رہے، جب تک ہو سکا نماز ادا کی، جانشینی کی شوریٰ بنائی۔ عائشہ رضی اللہ عنہا سے اجازت مانگی کہ دونوں ساتھیوں کے پاس دفن ہوں۔ وفات کے بعد نبی ﷺ اور ابو بکر رضی اللہ عنہ کے پہلو میں دفن ہوئے۔ اہل سنت انہیں خلفائے راشدین کے عظیم ترین میں شمار کرتے ہیں اور ان کی عزت کو دوسرے صحابہ کے خلاف ہتھیار نہیں بناتے۔

آخری فکر امت تھی نہ خاندان۔ بیٹے عبد اللہ کو خلیفہ نہ بنایا حالانکہ وہ پرہیزگار اور عالم تھے، فرمایا ایک گھر پر اس طرح دو خلافتیں نہ آئیں۔ چھ آدمیوں کی مجلس چھوڑی۔ فتح، قانون اور رات کی گشت کا یہ امتزاج ہے جس کی وجہ سے فقہا و مورخین، طبری سے ابن جوزی تک، عمر کو نبی ﷺ اور ابو بکر کے بعد عادل امام کی مثال سمجھتے ہیں۔""",
    """उमर इब्न अल-खत्ताब इब्न नुफैल رضي الله عنه कुरैश के बनू अदी से थे, एक शाख़ जो मक्का में फ़ैसले और क़ुव्वत के लिए जानी जाती थी। इब्न साद और इब्न हिशाम की सीरत उनकी जवानी को ताक़तवर आदमी, पहलवान और चरवाहे के तौर पर बयान करती है, इस्लाम से पहले कमज़ोर मुसलमान जिनसे डरते थे। विलादत हाथी वाले साल के क़रीब तेरह बरस बाद हुई। वालिदा हन्तमह बिन्त हाशिम बनू मख़ज़ूम से थीं। नबुव्वत के छठे साल तक नए दीन के मुख़ालिफ़ीन में रहे।

उनका इस्लाम क़रीब छठे साल-ए-दावत (लगभग 616 ई.) मक्की दौर की मशहूरतरीन दास्तानों में से है। इब्न इसहाक की रिवायत है कि ग़ुस्से में निकले, फिर बहन फ़ातिमा और शौहर सईद बिन ज़ैद رضي الله عنهما को ख़ब्बाब बिन अरत के साथ ता-हा की आयतें पढ़ते पाया। मारने के बाद शर्मिंदा हुए, सहीफ़ा सुना, अरक़म के घर गए और नबी ﷺ के सामने कलिमा पढ़ा। उसी दिन से मुसलमान काबा में खुल कर नमाज़ पढ़ने लगे, क्योंकि कुरैश में उनकी हैसियत से छिपना दुश्वार हो गया।

बाद में मदीना एलानिया हिजरत की, तलवार सामने, जो रोके मुक़ाबले को कहा, जैसा मुतक़द्दिम रिवायात से मुवर्रिख़ नक़्ल करते हैं। मदीना में नबी ﷺ अक्सर मशवरा लेते; तफ़सीर में उमर की राय से मुवाफ़क़त की बहुत सी आयतें ज़िक्र होती हैं, जैसे मक़ाम-ए-इबराहीम और हिजाब। बद्र, उहुद, खंदक और हुनैन में लड़े। नबी ﷺ ने फ़ारूक़ का लक़ब दिया, हक़ व बातिल में फ़र्क़ करने वाला। अशरा-ए-मुबश्शिरा में से थे।

अबू बक्र की वफ़ात 13 हिजरी / 634 ई. के बाद तहरीरि नामज़दगी और लोगों की बैअत से दूसरे ख़लीफा बने। दस साल की हुकूमत (13–23 हिजरी / 634–644 ई.)। उस दहाई में अबू उबैदा बिन जर्राह, साद बिन अबी वक़्क़ास, अम्र बिन आस और ख़ालिद बिन वलीद رضي الله عنهم जैसे कमांडरों के तहत शाम, इराक, फ़ारस और मिस्र खुले। यरमूक, क़ादिसिया और सासानी क़ल्ब तक मुहिमें ने इल्तके की शक्ल बदल दी। उमर ने महज़ छापे नहीं छोड़े बल्कि सूबे, वज़ािफ़ और मुआहिदे मुनज़्ज़म किए।

हिजरत के साल से हिजरी कैलेंडर क़ायम किया, दीवान बना कर जंगजूओं और घरानों के नाम और अता दर्ज किए, और रात मदीना की गलियों में घूम कर ग़रीबों की हाजत सुनते। पैवंद लगे जुब्बे, बेवा के लिए बोरी उठाने, और गवर्नरों से हिसाब की क्लासिकी रिवायात अदल की तस्वीर बन गईं। जो हाकिम रआया से ऊपर रहते उन्हें हटाया या झिंझोड़ा। अवामी याद में फ़ारूक़ का लक़ब जंग के मोर्चों जितना घरेलू इंसाफ़ से जुड़ा है।

जुलहिज्जा 23 हिजरी / नवंबर 644 ई. में मस्जिद-ए-नबवी में फज्र पढ़ा रहे थे कि अबू लुलुआ ने ज़ख़्मी किया, एक फ़ारसी कारीगर जिसे शिकायत थी। क़रीब तीन दिन ज़िंदा रहे, जब तक हो सका नमाज़ अदा की, जानशिनी की शूरा बनाई। आयशा رضي الله عنها से इजाज़त मांगी कि दोनों साथियों के पास दफ़न हों। वफ़ात के बाद नबी ﷺ और अबू बक्र رضي الله عنه के पहलू में दफ़न हुए। अहले सुन्नत उन्हें ख़ुलफ़ा-ए-राशिदीन के अज़ीमतरीन में शुमार करते हैं और उनकी इज़्ज़त को दूसरे सहाबा के ख़िलाफ़ हथियार नहीं बनाते।

आख़िरी फ़िक्र उम्मत थी न ख़ानदान। बेटे अब्दुल्लाह को ख़लीफा न बनाया हालांकि वह परहेज़गार और आलिम थे, फ़रमाया एक घर पर इस तरह दो खिलाफ़तें न आएँ। छह आदमियों की मजलिस छोड़ी। फ़तह, क़ानून और रात की गश्त का यह इम्तिज़ाज है जिसकी वजह से फ़ुक़हा व मुवर्रिख़ीन, तबरी से इब्न जौज़ी तक, उमर को नबी ﷺ और अबू बक्र के बाद आदिल इमाम की मिसाल समझते हैं।""",
    """উমর ইবনুল খাত্তাব ইবন নুফায়ল رضي الله عنه কুরাইশের বনু আদি গোত্রের, মক্কায় সালিশি ও শক্তির জন্য পরিচিত একটি শাখা। ইবন সাদ ও ইবন হিশামের সিরাত তাঁর যৌবনকে শক্তিশালী পুরুষ, মল্লযোদ্ধা ও পশুপালক হিসেবে বর্ণনা করে, ইসলামের আগে দুর্বল মুসলিমরা যাঁকে ভয় করত। হস্তিবর্ষের প্রায় তেরো বছর পর জন্ম। মাতা হানতামাহ বিনত হাশিম বনু মাখজুমের। নবুয়তের ষষ্ঠ বছর পর্যন্ত তিনি নতুন দীনের বিরোধীদের মধ্যে ছিলেন।

তাঁর ইসলাম প্রায় দাওয়াতের ষষ্ঠ বর্ষে (আনুমানিক ৬১৬ খ্রি.) মক্কী যুগের বিখ্যাততম কাহিনিগুলোর একটি। ইবন ইসহাকের বর্ণনায় তিনি রাগে বের হন, তারপর বোন ফাতিমা ও স্বামী সাঈদ ইবন যায়দ رضي الله عنهما-কে খাব্বাব ইবন আরাতের সঙ্গে তা-হা-র আয়াত পাঠ করতে দেখেন। আঘাতের পর লজ্জিত হয়ে পত্র শোনেন, আরকামের ঘরে যান এবং নবী ﷺ-এর সামনে শাহাদাহ পাঠ করেন। সেদিন থেকে মুসলিমরা কাবায় প্রকাশ্যে নামাজ পড়ে, কারণ কুরাইশে তাঁর মর্যাদায় গোপন থাকা কঠিন হয়ে পড়ে।

পরে তিনি প্রকাশ্যে মদিনায় হিজরত করেন, তলোয়ার সামনে, কেউ বাধা দিলে মোকাবিলার আহ্বান জানিয়ে—যেমন প্রাথমিক বর্ণনা থেকে ঐতিহাসিকরা উল্লেখ করেন। মদিনায় নবী ﷺ প্রায়ই তাঁর পরামর্শ নিতেন; তাফসিরে উমরের মতের সঙ্গে মিলের অনেক আয়াত আলোচিত, যেমন মাকামে ইবরাহিম ও হিজাব। তিনি বদর, উহুদ, খন্দক ও হুনাইনে যুদ্ধ করেন। নবী ﷺ তাঁকে ফারুক নাম দেন, সত্য-মিথ্যার পার্থক্যকারী। তিনি আশারায়ে মুবাশশারার একজন।

আবু বকরের ওফাত ১৩ হিজরি / ৬৩৪ খ্রি. পর লিখিত মনোনয়ন ও জনগণের বাইআতে তিনি দ্বিতীয় খলিফা হন। শাসনকাল দশ বছর (১৩–২৩ হিজরি / ৬৩৪–৬৪৪)। সেই দশকে আবু উবায়দাহ ইবনুল জাররাহ, সাদ ইবন আবি ওয়াক্কাস, আমর ইবনুল আস ও খালিদ ইবন আল-ওয়ালিদ رضي الله عنهم-এর নেতৃত্বে সিরিয়া, ইরাক, পারস্য ও মিশর বিজিত হয়। ইয়ারমুক, কাদিসিয়া ও সাসানীয় অন্তঃদেশে অভিযান অঞ্চলের রূপ বদলে দেয়। উমর শুধু অভিযান নয়, প্রদেশ, ভাতা ও সন্ধি সংগঠিত করেন।

হিজরতের বর্ষ থেকে হিজরি বর্ষপঞ্জি প্রতিষ্ঠা করেন, দিওয়ান গঠন করে যোদ্ধা ও পরিবারের নাম ও আতা নথিভুক্ত করেন, এবং রাতে মদিনার পথে ঘুরে দরিদ্রের প্রয়োজন শোনেন। তালি-লাগা চাদর, বিধবার জন্য বস্তা বহন, গভর্নরদের জবাবদিহির ক্লাসিক বর্ণনা তাঁর ন্যায়ের প্রতিমূর্তি হয়। প্রজার ঊর্ধ্বে থাকা কর্মকর্তাদের সরান বা কঠোর হিসাব নেন। জনস্মৃতিতে ফারুক উপাধি যুদ্ধক্ষেত্রের মতোই অভ্যন্তরীণ ন্যায়ের সঙ্গে জড়িত।

জিলহজ ২৩ হিজরি / নভেম্বর ৬৪৪ খ্রি. নবীর মসজিদে ফজর পড়াচ্ছিলেন, আবু লুলুআহ তাঁকে ছুরিকাঘাত করে—এক পারস্য কারিগর যার অভিযোগ ছিল। প্রায় তিন দিন জীবিত থাকেন, যতক্ষণ পারেন সালাত আদায় করেন, উত্তরাধিকারের শূরা গঠন করেন। আয়িশা رضي الله عنها-এর কাছে দুই সঙ্গীর পাশে দাফনের অনুমতি চান। ইন্তেকালের পর নবী ﷺ ও আবু বকর رضي الله عنه-এর পাশে দাফন হন। আহলুস সুন্নাহ তাঁকে রাশিদুনের শ্রেষ্ঠদের মধ্যে গণ্য করে এবং তাঁর সম্মানকে অন্য সাহাবিদের বিরুদ্ধে অস্ত্র করে না।

শেষ চিন্তা ছিল উম্মাহ, রাজবংশ নয়। পুত্র আব্দুল্লাহকে খলিফা করেননি যদিও তিনি পরহেজগার ও আলিম ছিলেন; বলেন এক ঘরে সেভাবে দুই খিলাফত না আসুক। ছয়জনের পরিষদ রেখে যান। বিজয়, আইন ও রাতের টহলের এই মিশ্রণেই ফকিহ ও ঐতিহাসিক, তাবারি থেকে ইবনুল জাওজি, উমরকে নবী ﷺ ও আবু বকরের পর ন্যায়পরায়ণ ইমামের আদর্শ মনে করেন।""",
    """Umar bin Khattab bin Nufail رضي الله عنه berasal dari Bani Adi Quraisy, cabang yang dikenal dengan tahkim dan kekuatan di Makkah. Ibnu Sa'd dan sirah Ibnu Hisyam menggambarkan masa mudanya sebagai lelaki gagah, pegulat dan penggembala, ditakuti muslim yang lemah sebelum ia masuk Islam. Ia lahir sekitar tiga belas tahun setelah Tahun Gajah. Ibunya Hantamah binti Hasyim dari Bani Makhzum. Hingga tahun keenam kenabian ia masih termasuk penentang agama baru.

Islamnya, sekitar tahun keenam risalah (kira-kira 616 M), termasuk kisah paling terkenal periode Makkah. Riwayat Ibnu Ishaq menyebutkan ia keluar dalam marah, lalu mendapati saudarinya Fatimah dan suaminya Said bin Zaid رضي الله عنهما membaca ayat Thaha bersama Khabbab bin al-Aratt. Setelah memukul mereka ia malu, meminta mendengar lembaran itu, lalu pergi ke rumah al-Arqam. Di sana ia mengucapkan syahadat di hadapan Nabi ﷺ. Sejak hari itu kaum muslimin salat terang-terangan di Ka'bah, karena kedudukannya di Quraisy membuat penyembunyian sulit dipertahankan.

Ia kemudian hijrah ke Madinah secara terbuka, pedang terlihat, menantang siapa yang menghalangi, sebagaimana sejarawan kemudian menukil dari riwayat awal. Di Madinah Nabi ﷺ sering meminta pendapatnya; banyak ayat yang dibahas dalam tafsir sebagai selaras dengan pandangan Umar, seperti Maqam Ibrahim dan hijab. Ia berperang di Badar, Uhud, Khandaq, dan Hunain. Nabi ﷺ menamainya al-Faruq, yang memisahkan yang hak dari yang batil. Ia termasuk al-asyarah al-mubasysyarah.

Setelah Abu Bakar wafat pada 13 H / 634 M ia menjadi khalifah kedua melalui penunjukan tertulis dan baiat umat. Masa pemerintahannya sepuluh tahun (13–23 H / 634–644 M). Dalam dasawarsa itu Syam, Irak, Persia, dan Mesir terbuka di bawah panglima seperti Abu Ubaidah bin al-Jarrah, Sa'd bin Abi Waqqas, Amr bin al-As, dan Khalid bin al-Walid رضي الله عنهم. Pertempuran Yarmuk, Qadisiyah, dan ekspedisi ke jantung Sasani mengubah kawasan. Umar menata wilayah, tunjangan, dan perjanjian, bukan membiarkan penaklukan sebagai sekadar razia.

Ia menetapkan kalender Hijriah dari tahun Hijrah, membentuk diwan untuk mendaftar nama dan 'atha (tunjangan) bagi pejuang dan keluarga, dan berkeliling malam di jalan Madinah untuk mendengar kebutuhan orang miskin. Riwayat klasik tentang jubah bertambal, mengangkat karung bagi janda, dan memeriksa gubernur menjadi citra keadilannya. Ia memberhentikan atau menegur pejabat yang hidup di atas rakyat. Gelar al-Faruq dalam ingatan publik terikat pada keadilan dalam negeri sama banyaknya dengan front perang.

Pada Zulhijah 23 H / November 644 M, saat mengimami Subuh di Masjid Nabawi, ia ditikam Abu Lu'lu'ah, seorang perajin Persia yang punya keluhan. Ia bertahan sekitar tiga hari, salat selama mampu, dan menyusun syura untuk suksesi. Ia meminta izin Aisyah رضي الله عنها untuk dimakamkan di sisi dua sahabatnya. Ia wafat dan dimakamkan di samping Nabi ﷺ dan Abu Bakar رضي الله عنه. Tradisi Ahlusunah menilainya di antara yang terbesar dari Khulafaur Rasyidin dan tidak memakai kemuliaannya sebagai senjata terhadap Sahabat lain.

Perhatian terakhirnya adalah umat, bukan dinasti. Ia menolak mengangkat putranya Abdullah sebagai khalifah meski Abdullah saleh dan berilmu, dengan berkata satu rumah tidak perlu memikul dua khilafah berturut-turut dengan cara itu. Ia meninggalkan dewan enam orang. Gabungan penaklukan, hukum, dan patroli malam itulah sebab fukaha dan sejarawan kemudian, dari ath-Thabari hingga Ibnul Jauzi, memandang Umar sebagai arketipe imam yang adil setelah Nabi ﷺ dan Abu Bakar.""",
)
ch["items"][0]["details"] = D(
    """Hafsah bint Umar رضي الله عنها was a Mother of the Believers. After her first husband died of wounds from Uhud, the Prophet ﷺ married her. In her keeping later lay the suhuf of the Quran compiled in Abu Bakr's time, which Uthman borrowed for the official copies. Her apartment, like Aisha's, was a place of teaching. Honouring Hafsah is part of honouring Umar's house and the Mothers of the Believers together.

Umar appointed governors over the new provinces and held them to account. He required that they ride ordinary mounts, eat ordinary food, and not close their doors to petitioners. Letters preserved in the histories warn against luxury and delay of justice. When a complaint reached Madinah he summoned the amir or sent an investigator. This administrative sternness is as famous as the victories of his generals.

He lived simply while the treasuries filled. Night patrols in Madinah let him hear a hungry child's cry or a woman's verse of need. He set prices of concern, forbade the sale of slave mothers in ways that split families when reports reached him, and expanded the mosque. The poor of Madinah knew the caliph as a man who might knock in the dark with flour on his back.

The openings of Syria, Iraq, Persia, and Egypt were organised with treaties for People of the Book, registers of land, and stipends for those who had fought. He visited al-Jabiya in Syria to arrange affairs. He is associated with the covenant of Jerusalem in the famous reports of his entry in 15–16 AH, walking in humility rather than in silk. Sunni historians stress that victory was attributed to Allah, not to the pride of a ruler.

Before death he named a shura of six senior Companions: Uthman, Ali, Talha, al-Zubayr, Sa'd ibn Abi Waqqas, and Abd al-Rahman ibn Awf رضي الله عنهم, with his son Abdullah as adviser without candidacy for the caliphate. After three days of consultation Abd al-Rahman asked the people and the two leading candidates. The choice fell on Uthman ibn Affan رضي الله عنه. Sunni narrative presents this as a lawful, consultative transfer, not as a slight to Ali رضي الله عنه, who pledged bay'ah.

The six were all of the asharah, men of Badr and of long companionship. Abd al-Rahman withdrew himself from seeking the office so that he could poll the ummah. Reports say he spent nights asking women, pilgrims, and commanders. When Uthman was chosen, Ali gave the pledge. Later fitnah is not read back by Ahl al-Sunnah as proof that this shura was a conspiracy; it is treated as a sincere effort in 23 AH / 644 CE.

Umar's combination of Hafsah's household link to revelation, strict governors, conquest under law, and a six-man shura is why encyclopedias of the Rashidun linger on his last days. He asked to be judged as a man who feared Allah more than he feared the loss of office. The Sunni mainstream remembers him beside Abu Bakr and does not set him against Uthman or Ali in belief.""",
    """حفصہ بنت عمر رضی اللہ عنہا ام المؤمنین تھیں۔ پہلے شوہر احد کے زخموں سے فوت ہوئے تو نبی ﷺ نے نکاح فرمایا۔ بعد میں ابو بکر کے عہد کا جمع شدہ صحیفۂ قرآن انہی کے پاس رہا، جسے عثمان نے سرکاری نسخوں کے لیے مستعار لیا۔ ان کا حجرہ عائشہ کی طرح درس کا مقام تھا۔ حفصہ کی عزت عمر کے گھر اور تمام امهات المؤمنین کی عزت کا حصہ ہے۔

عمر نے نئے صوبوں پر گورنر مقرر کیے اور سخت احتساب کیا۔ حکم تھا عام سواری پر چلیں، عام کھانا کھائیں، سائل پر دروازہ نہ بند کریں۔ تواریخ میں محفوظ خطوط تجمل اور انصاف میں تاخیر سے ڈراتے ہیں۔ مدینہ شکایت پہنچتی تو امیر کو بلاتے یا تحقیق بھیجتے۔ یہ انتظامی سختی ان کے جرنیلوں کی فتوحات جتنی مشہور ہے۔

خزانے بھرے تو خود سادہ رہے۔ مدینہ کی رات گشت میں بھوکے بچے کی آواز یا عورت کے شعرِ حاجت سنتی۔ نرخوں کی فکر کی، جب اطلاع ملی تو ایسی فروخت روکی جو ماں غلام کو گھرانے سے توڑے، مسجد وسیع کی۔ مدینہ کے غریب خلیفہ کو وہ آدمی جانتے جو اندھیرے میں پیٹھ پر آٹا لیے دستک دے سکتا تھا۔

شام، عراق، فارس اور مصر کی فتوحات اہل کتاب کے معاہدوں، زمین کے دفاتر اور لڑنے والوں کے وظائف کے ساتھ منظم ہوئیں۔ شام میں جابیہ جا کر امور ترتیب دیے۔ بیت المقدس کے مشہور عہد اور 15–16ھ میں عاجزی سے دخول کی روایات ان سے وابستہ ہیں، ریشم میں نہیں۔ سنی مورخ زور دیتے ہیں کہ فتح اللہ کی طرف سے تھی، حاکم کے غرور سے نہیں۔

وفات سے پہلے چھ اکابر صحابہ کی شوریٰ نامزد کی: عثمان، علی، طلحہ، زبیر، سعد بن ابی وقاص اور عبد الرحمن بن عوف رضی اللہ عنہم، بیٹے عبد اللہ کو مشیر بنایا بغیر خلافت کے امیدوار ہونے کے۔ تین دن مشورے کے بعد عبد الرحمن نے لوگوں اور دونوں بڑے امیدواروں سے پوچھا۔ انتخاب عثمان بن عفان رضی اللہ عنہ پر پڑا۔ سنی بیان اسے قانونی مشوراتی انتقال کہتا ہے، علی رضی اللہ عنہ کی توہین نہیں؛ انہوں نے بیعت کی۔

چھوں عشرہ میں سے تھے، بدری اور دیرینہ رفاقت والے۔ عبد الرحمن نے خود عہدہ نہ مانگا تاکہ امت سے رائے لے سکیں۔ روایات ہیں راتیں عورتوں، حاجیوں اور کمانڈروں سے پوچھتے۔ عثمان چنے گئے تو علی نے بیعت دی۔ بعد کی فتنہ کو اہل سنت 23ھ / 644ء کی اس شوریٰ پر سازش نہیں پڑھتے۔ اسے مخلصانہ کوشش مانتے ہیں۔

حفصہ کے گھر کا وحی سے تعلق، سخت گورنر، قانون کے تحت فتح، اور چھ رکنی شوریٰ وہ وجہ ہے کہ خلفائے راشدین کے دائرۃ المعارف ان کے آخری دنوں پر ٹھہرتے ہیں۔ انہوں نے چاہا کہ ایسے آدمی کی طرح جانچا جائے جو عہدے کے جانے سے زیادہ اللہ سے ڈرے۔ اہل سنت انہیں ابو بکر کے ساتھ یاد کرتے ہیں اور عقیدے میں عثمان یا علی کے مقابل نہیں کرتے۔""",
    """हफ़्सा बिन्त उमर رضي الله عنها उम्मुल मुमिनीन थीं। पहले शौहर उहुद के ज़ख़्मों से फ़ौत हुए तो नबी ﷺ ने निकाह फ़रमाया। बाद में अबू बक्र के अहद का जमाशुदा सहीफ़ा-ए-कुरआन उन्हीं के पास रहा, जिसे उस्मान ने सरकारी नुस्ख़ों के लिए उधार लिया। उनका हुजरा आयशा की तरह दर्स का मक़ाम था। हफ़्सा की इज़्ज़त उमर के घर और तमाम उम्महातुल मुमिनीन की इज़्ज़त का हिस्सा है।

उमर ने नए सूबों पर गवर्नर मुक़र्रर किए और सख़्त एहतिसाब किया। हुक्म था आम सवारी पर चलें, आम खाना खाएँ, साइल पर दरवाज़ा न बंद करें। तवारीख़ में महफ़ूज़ ख़तूत तजम्मुल और इंसाफ़ में ताख़ीर से डराते हैं। मदीना शिकायत पहुँचती तो अमीर को बुलाते या तहक़ीक़ भेजते। यह इंतिज़ामी सख़्ती उनके जरनैलों की फ़ुतूहात जितनी मशहूर है।

ख़ज़ाने भरे तो ख़ुद सादा रहे। मदीना की रात गश्त में भूखे बच्चे की आवाज़ या औरत के शेर-ए-हाजत सुनते। दरख़ों की फ़िक्र की, जब इत्तिला मिली तो ऐसी फ़रोख़्त रोकी जो माँ ग़ुलाम को घराने से तोड़े, मस्जिद वसीअ की। मदीना के ग़रीब ख़लीफा को वह आदमी जानते जो अँधेरे में पीठ पर आटा लिए दस्तक दे सकता था।

शाम, इराक, फ़ारस और मिस्र की फ़ुतूहात अहले किताब के मुआहिदों, ज़मीन के दफ़्तरों और लड़ने वालों के वज़ािफ़ के साथ मुनज़्ज़म हुईं। शाम में जाबिया जा कर उमूर तरतीब दी। बैतुल मुक़द्दस के मशहूर अहद और 15–16 हिजरी में अज्ज़ी से दख़ूल की रिवायात उनसे वाबस्ता हैं, रेशम में नहीं। सुन्नी मुवर्रिख़ ज़ोर देते हैं कि फ़तह अल्लाह की तरफ़ से थी, हाकिम के ग़ुरूर से नहीं।

वफ़ात से पहले छह अकाबिर सहाबा की शूरा नामज़द की: उस्मान, अली, तलहा, ज़ुबैर, साद बिन अबी वक़्क़ास और अब्दुर्रहमान बिन औफ़ رضي الله عنهم, बेटे अब्दुल्लाह को मुशीर बनाया बिना खिलाफ़त के उमीदवार होने के। तीन दिन मशवरे के बाद अब्दुर्रहमान ने लोगों और दोनों बड़े उमीदवारों से पूछा। इंतिख़ाब उस्मान इब्न अफ़्फ़ान رضي الله عنه पर पड़ा। सुन्नी बयान इसे क़ानूनी मशवराती इंतिक़ाल कहता है, अली رضي الله عنه की तौहीन नहीं; उन्होंने बैअत की।

छहों अशरा में से थे, बद्री और दैरिना रफ़ाक़त वाले। अब्दुर्रहमान ने ख़ुद ओहदा न माँगा ताकि उम्मत से राय ले सकें। रिवायात हैं रातें औरतों, हाजियों और कमांडरों से पूछते। उस्मान चुने गए तो अली ने बैअत दी। बाद की फ़ितना को अहले सुन्नत 23 हिजरी / 644 ई. की इस शूरा पर साज़िश नहीं पढ़ते। इसे मुख़्लिसाना कोशिश मानते हैं।

हफ़्सा के घर का वही से ताल्लुक़, सख़्त गवर्नर, क़ानून के तहत फ़तह, और छह रुक्नी शूरा वह वजह है कि ख़ुलफ़ा-ए-राशिदीन के दाइरतुल मआरिफ़ उनके आख़िरी दिनों पर ठहरते हैं। उन्होंने चाहा कि ऐसे आदमी की तरह जाँचा जाए जो ओहदे के जाने से ज़्यादा अल्लाह से डरे। अहले सुन्नत उन्हें अबू बक्र के साथ याद करते हैं और अक़ीदे में उस्मान या अली के मुक़ाबिल नहीं करते।""",
    """হাফসাহ বিনত উমর رضي الله عنها উম্মুল মুমিনীন ছিলেন। প্রথম স্বামী উহুদের ক্ষতে মারা গেলে নবী ﷺ তাঁকে বিয়ে করেন। পরে আবু বকরের আমলের সংকলিত কুরআনের সহীফা তাঁর কাছেই ছিল, যা উসমান সরকারি কপির জন্য ধার নেন। তাঁর হুজরা আয়িশার মতো শিক্ষার স্থান ছিল। হাফসাহর সম্মান উমরের ঘর ও সকল উম্মুল মুমিনীনের সম্মানের অংশ।

উমর নতুন প্রদেশে গভর্নর নিয়োগ করেন এবং কঠোর জবাবদিহি করেন। নির্দেশ ছিল সাধারণ বাহনে চলতে, সাধারণ খাবার খেতে, আবেদনকারীর কাছে দরজা বন্ধ না করতে। ইতিহাসে সংরক্ষিত পত্র বিলাস ও ন্যায়ে বিলম্ব সম্পর্কে সতর্ক করে। মদিনায় অভিযোগ পৌঁছলে আমিরকে ডাকতেন বা তদন্তকারী পাঠাতেন। এই প্রশাসনিক কঠোরতা তাঁর সেনাপতিদের বিজয়ের মতোই প্রসিদ্ধ।

ভান্ডার ভরলেও তিনি সাদাসিধে থাকতেন। মদিনার রাতের টহলে ক্ষুধার্ত শিশুর কান্না বা নারীর প্রয়োজনের কবিতা শুনতেন। মূল্য নিয়ে চিন্তা করতেন, খবর পেলে এমন বিক্রি নিষেধ করতেন যা দাসী মাতাকে পরিবার থেকে ছিন্ন করে, মসজিদ সম্প্রসারণ করেন। মদিনার দরিদ্র খলিফাকে এমন মানুষ হিসেবে চিনত যিনি অন্ধকারে পিঠে আটা নিয়ে দরজায় করাঘাত করতে পারেন।

সিরিয়া, ইরাক, পারস্য ও মিশরের বিজয় আহলে কিতাবের সন্ধি, ভূমির দফতর ও যোদ্ধাদের ভাতার সঙ্গে সংগঠিত হয়। তিনি সিরিয়ার জাবিয়ায় গিয়ে বিষয় সাজান। বায়তুল মুকাদ্দাসের প্রসিদ্ধ অঙ্গীকার ও ১৫–১৬ হিজরিতে বিনয়ে প্রবেশের বর্ণনা তাঁর সঙ্গে জড়িত, রেশমে নয়। সুন্নি ঐতিহাসিক জোর দেন বিজয় আল্লাহর পক্ষ থেকে, শাসকের অহংকার থেকে নয়।

মৃত্যুর আগে ছয় শীর্ষ সাহাবির শূরা মনোনীত করেন: উসমান, আলী, তালহা, যুবায়র, সাদ ইবন আবি ওয়াক্কাস ও আব্দুর রহমান ইবন আওফ رضي الله عنهم, পুত্র আব্দুল্লাহকে উপদেষ্টা করেন খিলাফতের প্রার্থী না করে। তিন দিন পরামর্শের পর আব্দুর রহমান জনগণ ও দুই প্রধান প্রার্থীকে জিজ্ঞাসা করেন। নির্বাচন উসমান ইবন আফফান رضي الله عنه-এর উপর পড়ে। সুন্নি বর্ণনা একে বৈধ পরামর্শভিত্তিক হস্তান্তর বলে, আলী رضي الله عنه-এর অবমাননা নয়; তিনি বাইআত দেন।

ছয়জনই আশারার, বদরী ও দীর্ঘ সাহচর্যের মানুষ। আব্দুর রহমান নিজে পদ চাননি যাতে উম্মাহর মত নিতে পারেন। বর্ণনায় তিনি রাত্রি নারী, হাজি ও সেনাপতিদের জিজ্ঞাসা করেন। উসমান নির্বাচিত হলে আলী বাইআত দেন। পরবর্তী ফিতনাকে আহলুস সুন্নাহ ২৩ হিজরি / ৬৪৪ খ্রি. এই শূরার ষড়যন্ত্র হিসেবে পড়ে না; একে আন্তরিক প্রচেষ্টা মানে।

হাফসাহর গৃহের ওহির সঙ্গে সম্পর্ক, কঠোর গভর্নর, আইনের অধীনে বিজয় এবং ছয়জনের শূরা—এ কারণে রাশিদুন বিশ্বকোষ তাঁর শেষ দিনে দাঁড়ায়। তিনি চান বিচার হোক এমন মানুষ হিসেবে যিনি পদ হারানোর চেয়ে আল্লাহকে বেশি ভয় করেন। আহলুস সুন্নাহ তাঁকে আবু বকরের সঙ্গে স্মরণ করে এবং আকিদায় উসমান বা আলীর বিপক্ষে দাঁড় করায় না।""",
    """Hafshah binti Umar رضي الله عنها adalah Ummul Mukminin. Setelah suami pertamanya meninggal karena luka Uhud, Nabi ﷺ menikahinya. Di sisinya kemudian tersimpan suhuf Al-Qur'an yang dikumpulkan pada masa Abu Bakar, yang dipinjam Utsman untuk salinan resmi. Kamarnya, seperti kamar Aisyah, menjadi tempat pengajaran. Memuliakan Hafshah adalah bagian dari memuliakan rumah Umar dan para Ummul Mukminin bersama.

Umar mengangkat gubernur atas wilayah baru dan meminta pertanggungjawaban. Ia mensyaratkan mereka menunggang kendaraan biasa, makan makanan biasa, dan tidak menutup pintu dari pemohon. Surat-surat dalam tarikh memperingatkan kemewahan dan penundaan keadilan. Ketika pengaduan sampai ke Madinah ia memanggil amir atau mengirim penyelidik. Ketegasan administratif ini sama terkenalnya dengan kemenangan para jenderalnya.

Ia hidup sederhana sementara perbendaharaan penuh. Patroli malam di Madinah memungkinkannya mendengar tangis anak lapar atau syair kebutuhan seorang wanita. Ia memperhatikan harga, melarang penjualan yang memisahkan ibu budak dari keluarga ketika laporan sampai, dan memperluas masjid. Orang miskin Madinah mengenal khalifah sebagai orang yang mungkin mengetuk di gelap dengan tepung di punggung.

Pembukaan Syam, Irak, Persia, dan Mesir diatur dengan perjanjian untuk Ahlulkitab, daftar tanah, dan tunjangan bagi yang berperang. Ia mengunjungi al-Jabiyah di Syam untuk menata urusan. Ia dikaitkan dengan perjanjian Yerusalem dalam riwayat terkenal tentang masuknya pada 15–16 H, berjalan dalam kerendahan hati bukan sutra. Sejarawan Ahlusunah menekankan bahwa kemenangan dinisbahkan kepada Allah, bukan kepada kesombongan penguasa.

Sebelum wafat ia menunjuk syura enam sahabat senior: Utsman, Ali, Thalhah, az-Zubair, Sa'd bin Abi Waqqas, dan Abdurrahman bin Auf رضي الله عنهم, dengan putranya Abdullah sebagai penasihat tanpa kandidasi khilafah. Setelah tiga hari musyawarah Abdurrahman menanyai umat dan dua calon utama. Pilihan jatuh pada Utsman bin Affan رضي الله عنه. Narasi Ahlusunah menampilkannya sebagai pemindahan yang sah dan musyawarah, bukan penghinaan kepada Ali رضي الله عنه, yang kemudian berbaiat.

Keenamnya termasuk asyarah, ahli Badar dan sahabat lama. Abdurrahman menarik diri dari mencari jabatan agar dapat menjaring pendapat umat. Riwayat menyebutkan ia bermalam menanyai wanita, jamaah haji, dan panglima. Ketika Utsman dipilih, Ali memberi baiat. Fitnah kemudian tidak dibaca balik oleh Ahlusunah sebagai bukti bahwa syura ini konspirasi; ia dipandang sebagai ikhtiar tulus pada 23 H / 644 M.

Gabungan tautan rumah Hafshah kepada wahyu, gubernur yang ketat, penaklukan di bawah hukum, dan syura enam orang itulah sebab ensiklopedia Khulafaur Rasyidin berlama pada hari-hari terakhirnya. Ia ingin diadili sebagai orang yang lebih takut kepada Allah daripada takut kehilangan jabatan. Arus utama Ahlusunah mengingatnya di sisi Abu Bakar dan tidak mempertentangkannya dengan Utsman atau Ali dalam akidah.""",
)

# --- 3 Uthman ibn Affan ---
ch = chapter(3)
ch["details"] = D(
    """Uthman ibn Affan ibn Abi al-As رضي الله عنه was from Banu Umayyah of Quraysh, a wealthy merchant known in Makkah for modesty and for never having worshipped an idol even before Islam, according to reports in the tabaqat. Ibn Sa'd records his lineage through Abd Manaf, sharing a distant ancestor with the Prophet ﷺ. He accepted Islam early at the hand of Abu Bakr رضي الله عنه, among the first group of men. His wealth later equipped armies; his character was shyness, generosity, and recitation of the Quran.

He married Ruqayyah, daughter of the Prophet ﷺ, and after her death he married her sister Umm Kulthum رضي الله عنهما. For this he was called Dhun-Nurayn, Possessor of Two Lights, a unique honour in the household of the Messenger ﷺ. No other Companion is recorded as having married two daughters of a prophet in succession. When Ruqayyah was ill at the time of Badr in 2 AH / 624 CE, Uthman stayed in Madinah to nurse her by the Prophet's ﷺ permission and was granted the reward of Badr.

He migrated twice: first to Abyssinia with Ruqayyah in the early years of persecution, then to Madinah. Ibn Hisham mentions this double hijrah as a mark of early sacrifice. In Madinah he bought the well of Rumah and made it free for the Muslims, and he enlarged the Prophet's Mosque with his money. At the expedition of Tabuk in 9 AH / 630 CE he equipped the army so fully—camels, horses, and thousands of dinars—that the Prophet ﷺ said, 'Nothing will harm Uthman after this day.'

He was among the asharah mubashsharah and among those who pledged under the tree at Hudaybiyyah; when he was absent in Makkah as an envoy, the Prophet ﷺ clasped his own hand for Uthman's pledge. After Umar's shura in 23 AH / 644 CE the people chose him as third khalifah. His reign lasted twelve years (23–35 AH / 644–656 CE). In the first years the ummah enjoyed expansion into North Africa, Armenia, and towards Central Asia, and the Mediterranean saw the first Muslim navy under Mu'awiyah رضي الله عنه with Uthman's leave.

The most lasting work of his caliphate was the unification of the written Quran, the Uthmani mushaf. Recitation differences in the provinces, especially those heard by Hudhayfah ibn al-Yaman رضي الله عنه on the Armenian-Azerbaijan front, moved him to act. A committee under Zayd ibn Thabit copied the suhuf kept with Hafsah رضي الله عنها into standard copies sent to the cities. This rasm remains the written form of the ummah.

In the later years complaints about governors and distribution arose. Sunni historians such as al-Tabari record the unrest without cursing Uthman or the Sahaba who differed. Rebels from Egypt, Kufa, and Basra besieged his house in Madinah. He refused to shed Muslim blood in the streets to save himself, and he refused to abdicate in a manner that would abandon the trust. He remained fasting and reciting.

He was killed on 18 Dhul-Hijjah 35 AH (June 656 CE) while reading the Quran, at about eighty-two years of age. His blood fell upon the mushaf, a scene remembered with grief in Sunni memory. He was buried in al-Baqi'. Ahl al-Sunnah honour him as the third of the Rashidun, Dhun-Nurayn, and the caliph of the mushaf, and they forbid reviling him or any of the Companions رضي الله عنهم.""",
    """عثمان بن عفان بن ابی العاص رضی اللہ عنہ قریش کے بنو امیہ سے تھے، مالدار تاجر، مکہ میں حیا کے لیے مشہور، اور طبقات کی روایات کے مطابق اسلام سے پہلے بھی بت نہیں پوچھتے۔ ابن سعد نسب عبد مناف تک بیان کرتے ہیں، نبی ﷺ سے دوری جد مشترک۔ ابو بکر رضی اللہ عنہ کے ہاتھ جلد اسلام لائے، اولین مردوں میں۔ مال سے لشکر تیار کیے؛ مزاج حیا، سخاوت اور قرآن کی تلاوت تھا۔

نبی ﷺ کی صاحبزادی رقیہ سے نکاح ہوا، ان کی وفات کے بعد بہن ام کلثوم رضی اللہ عنہما سے۔ اس لیے ذوالنورین کہلائے، رسول ﷺ کے گھر میں انوکھا شرف۔ کسی اور صحابی کا دو بیٹیوں سے پے در پے نکاح ثابت نہیں۔ 2ھ / 624ء میں بدر کے وقت رقیہ بیمار تھیں تو نبی ﷺ کی اجازت سے مدینہ میں تیمارداری کی اور بدر کا اجر پایا۔

دو ہجرتیں کیں: پہلے رقیہ کے ساتھ حبشہ ظلم کے ابتدائی برسوں میں، پھر مدینہ۔ ابن ہشام اس دوہری ہجرت کو ابتدائی قربانی کا نشان کہتے ہیں۔ مدینہ میں بئر رومہ خرید کر مسلمانوں کے لیے وقف کی، اپنے مال سے مسجد نبوی وسیع کی۔ 9ھ / 630ء کے غزوہ تبوک میں اونٹ، گھوڑے اور ہزاروں دینار سے لشکر اس قدر تیار کیا کہ نبی ﷺ نے فرمایا آج کے بعد عثمان کو کچھ نقصان نہ دے گا۔

عشرہ مبشرہ میں سے تھے اور حدیبیہ میں شجر کے نیچے بیعت کرنے والوں میں؛ مکہ سفیر تھے تو نبی ﷺ نے ان کی بیعت اپنے ہاتھ سے کی۔ عمر کی شوریٰ 23ھ / 644ء کے بعد لوگ انہیں تیسرے خلیفہ چنے۔ بارہ سال حکومت (23–35ھ / 644–656ء)۔ ابتدائی برسوں میں شمالی افریقہ، آرمینیا اور وسط ایشیا کی سمت توسیع ہوئی، اور معاویہ رضی اللہ عنہ نے عثمان کی اجازت سے پہلی مسلم بحریہ بحیرہ روم میں چلائی۔

خلافت کا ماندگار کام قرآن کی تحریری وحدت، عثمانی مصحف ہے۔ علاقوں میں قراءت کے فرق، خاص طور پر حذیفہ بن یمان رضی اللہ عنہ نے آرمینیا آذربائیجان محاذ پر جو سنا، نے عمل پر آمادہ کیا۔ زید بن ثابت کی کمیٹی نے حفصہ رضی اللہ عنہا کے صحیفے سے معیاری نسخے لکھ کر شہروں کو بھیجے۔ یہی رسم آج تک امت کا لکھا ہوا قرآن ہے۔

بعد کے برسوں میں گورنروں اور تقسیم کی شکایتیں اٹھیں۔ طبری جیسے سنی مورخ اضطراب لکھتے ہیں بغیر عثمان یا اختلاف کرنے والے صحابہ کو گالی دیے۔ مصر، کوفہ، بصرہ کے باغوں نے مدینہ میں گھر گھیر لیا۔ انہوں نے خود بچانے کے لیے گلیوں میں مسلمانوں کا خون بہانا قبول نہ کیا، اور امانت چھوڑ کر استعفا ایسے ڈھنگ سے نہ دیا۔ روزے اور تلاوت میں رہے۔

18 ذوالحجہ 35ھ (جون 656ء) میں قرآن پڑھتے ہوئے شہید ہوئے، تقریباً بیاسی برس کی عمر۔ خون مصحف پر گرا، اہل سنت کی یاد میں غم کا منظر۔ بقیع میں دفن ہوئے۔ اہل سنت انہیں تیسرے راشد خلیفہ، ذوالنورین اور مصحف کے خلیفہ مان کر عزت دیتے ہیں، اور انہیں یا کسی صحابی رضی اللہ عنہم کو برا کہنے سے منع کرتے ہیں۔""",
    """उस्मान इब्न अफ़्फ़ान इब्न अबी अल-आस رضي الله عنه कुरैश के बनू उमैया से थे, मालदार तاجر, मक्का में हया के लिए मशहूर, और तबाक़ात की रिवायात के मुताबिक इस्लाम से पहले भी बुत नहीं पूजते। इब्न साद नसब अब्द मनाफ़ तक बयान करते हैं, नबी ﷺ से दूरी जद्द मुश्तरिक। अबू बक्र رضي الله عنه के हाथ जल्द इस्लाम लाए, अव्वलीन मर्दों में। माल से लश्कर तैयार किए; मिज़ाज हया, सख़ावत और कुरआन की तिलावत था।

नबी ﷺ की साहिबज़ादी रुकय्या से निकाह हुआ, उनकी वफ़ात के बाद बहन उम्म कुलसूम رضي الله عنهما से। इसलिए ज़ुन-नूरैन कहलाए, रसूल ﷺ के घर में अनोखा शرف। किसी और सहाबी का दो बेटियों से पे-दर-पे निकाह साबित नहीं। 2 हिजरी / 624 ई. में बद्र के वक्त रुकय्या बीमार थीं तो नबी ﷺ की इजाज़त से मदीना में तीमारदारी की और बद्र का अज्र पाया।

दो हिजरतें कीं: पहले रुकय्या के साथ हबशा ज़ुल्म के इब्तिदाई बरसों में, फिर मदीना। इब्न हिशाम इस दोहरी हिजरत को इब्तिदाई क़ुरबानी का निशान कहते हैं। मदीना में बिअर-ए-रूमा ख़रीद कर मुसलमानों के लिए वक़्फ़ की, अपने माल से मस्जिद-ए-नबवी वसीअ की। 9 हिजरी / 630 ई. के ग़ज़वा-ए-तबूक में ऊँट, घोड़े और हज़ारों दीनार से लश्कर इतना तैयार किया कि नबी ﷺ ने फ़रमाया आज के बाद उस्मान को कुछ नुक़सान न देगा।

अशरा-ए-मुबश्शिरा में से थे और हुदैबिया में दरख़्त के नीचे बैअत करने वालों में; मक्का में सफीर थे तो नबी ﷺ ने उनकी बैअत अपने हाथ से की। उमर की शूरा 23 हिजरी / 644 ई. के बाद लोग उन्हें तीसरे ख़लीफा चुने। बारह साल हुकूमत (23–35 हिजरी / 644–656 ई.)। इब्तिदाई बरसों में शिमाली अफ़्रीक़ा, अर्मेनिया और वस्त एशिया की सिम्त तौसीअ हुई, और मुआविया رضي الله عنه ने उस्मान की इजाज़त से पहली मुस्लिम बहरीया बह्री-ए-रूम में चलाई।

खिलाफ़त का मांदगार काम कुरआन की तहरीरि वहदत, उस्मानी मुसहफ़ है। इलाक़ों में क़िराअत के फ़र्क़, ख़ास तौर पर हुज़ैफ़ा बिन यमान رضي الله عنه ने अर्मेनिया-आज़रबाइजान मोर्चे पर जो सुना, ने अमल पर आमादा किया। ज़ैद बिन साबित की कमेटी ने हफ़्सा رضي الله عنها के सहीफ़ों से मेयारी नुस्ख़े लिख कर शहरों को भेजे। यही रस्म आज तक उम्मत का लिखा हुआ कुरआन है।

बाद के बरसों में गवर्नरों और तक़सीम की शिकायतें उठीं। तबरी जैसे सुन्नी मुवर्रिख़ इज़तिराब लिखते हैं बिना उस्मान या इख़्तिलाफ़ करने वाले सहाबा को गाली दिए। मिस्र, कूफ़ा, बसरा के बाग़ियों ने मदीना में घर घेर लिया। उन्होंने ख़ुद बचाने के लिए गलियों में मुसलमानों का ख़ून बहाना क़ुबूल न किया, और अमानत छोड़ कर इस्तिफा ऐसे ढंग से न दिया। रोज़े और तिलावत में रहे।

18 ज़ुलहिज्जा 35 हिजरी (जून 656 ई.) में कुरआन पढ़ते शहीद हुए, क़रीब बयासी बरस की उम्र। ख़ून मुसहफ़ पर गिरा, अहले सुन्नत की याद में ग़म का मंज़र। बक़ीअ में दफ़न हुए। अहले सुन्नत उन्हें तीसरे राशिद ख़लीफा, ज़ुन-नूरैन और मुसहफ़ के ख़लीफा मान कर इज़्ज़त देते हैं, और उन्हें या किसी सहाबी رضي الله عنهم को बुरा कहने से मना करते हैं।""",
    """উসমান ইবন আফফান ইবন আবি আল-আস رضي الله عنه কুরাইশের বনু উমাইয়ার, ধনী ব্যবসায়ী, মক্কায় লজ্জশীলতার জন্য খ্যাত, এবং তাবাকাতের বর্ণনায় ইসলামের আগেও মূর্তি পূজা করেননি। ইবন সাদ আব্দ মানাফ পর্যন্ত বংশ লেখেন, নবী ﷺ-এর সঙ্গে দূর পূর্বপুরুষ অভিন্ন। আবু বকর رضي الله عنه-এর হাতে অল্পকালে ইসলাম গ্রহণ করেন, প্রথম পুরুষদের মধ্যে। সম্পদ দিয়ে সেনা সজ্জিত করেন; চরিত্র ছিল লজ্জা, দানশীলতা ও কুরআন তিলাওয়াত।

তিনি নবী ﷺ-এর কন্যা রুকায়্যাহকে বিয়ে করেন, তাঁর মৃত্যুর পর বোন উম্মু কুলসুম رضي الله عنهما-কে। এজন্য যুন-নূরাইন নামে খ্যাত, রাসূল ﷺ-এর ঘরে অনন্য সম্মান। অন্য কোনো সাহাবির দুই কন্যার সঙ্গে পরপর বিবাহ প্রমাণিত নয়। ২ হিজরি / ৬২৪ খ্রি. বদরের সময় রুকায়্যাহ অসুস্থ থাকায় নবী ﷺ-এর অনুমতিতে মদিনায় সেবা করেন এবং বদরের সওয়াব পান।

দুই হিজরত করেন: প্রথমে রুকায়্যাহর সঙ্গে হাবশায় নির্যাতনের প্রথম বছরগুলোতে, তারপর মদিনায়। ইবন হিশাম এই দ্বৈত হিজরতকে প্রাথমিক কুরবানির চিহ্ন বলেন। মদিনায় রুমার কূপ কিনে মুসলিমদের জন্য ওয়াকফ করেন, নিজ সম্পদে নবীর মসজিদ সম্প্রসারণ করেন। ৯ হিজরি / ৬৩০ খ্রি. তাবুক অভিযানে উট, ঘোড়া ও হাজার হাজার দিনার দিয়ে সেনা এমন সজ্জিত করেন যে নবী ﷺ বলেন, আজকের পর উসমানের কোনো ক্ষতি হবে না।

তিনি আশারায়ে মুবাশশারার এবং হুদায়বিয়ায় বৃক্ষতলে বাইআতকারীদের একজন; মক্কায় দূত থাকায় নবী ﷺ তাঁর বাইআত নিজ হাতে করেন। উমরের শূরা ২৩ হিজরি / ৬৪৪-এর পর লোকেরা তাঁকে তৃতীয় খলিফা বাছেন। শাসনকাল বারো বছর (২৩–৩৫ হিজরি / ৬৪৪–৬৫৬)। প্রথম বছরগুলোতে উত্তর আফ্রিকা, আর্মেনিয়া ও মধ্য এশিয়ার দিকে বিস্তার হয়, এবং মুয়াবিয়া رضي الله عنه উসমানের অনুমতিতে ভূমধ্যসাগরে প্রথম মুসলিম নৌবহর চালান।

খিলাফতের স্থায়ী কাজ কুরআনের লিখিত ঐক্য, উসমানি মুশাফ। প্রদেশে কিরাআতের পার্থক্য, বিশেষত হুযাইফাহ ইবনুল ইয়ামান رضي الله عنه আর্মেনিয়া-আজারবাইজান ফ্রন্টে যা শোনেন, তাঁকে কর্মে প্রবৃত্ত করে। যায়েদ ইবন সাবিতের কমিটি হাফসাহ رضي الله عنها-এর সহীফা থেকে প্রমিত কপি লিখে নগরে পাঠায়। এই রসম আজও উম্মাহর লিখিত কুরআন।

পরবর্তী বছরগুলোতে গভর্নর ও বণ্টন নিয়ে অভিযোগ ওঠে। তাবারির মতো সুন্নি ঐতিহাসিক অস্থিরতা লেখেন উসমান বা ভিন্নমত সাহাবিদের গালি না দিয়ে। মিশর, কুফা, বসরার বিদ্রোহীরা মদিনায় তাঁর ঘর অবরোধ করে। তিনি নিজেকে বাঁচাতে রাস্তায় মুসলিম রক্তপাত স্বীকার করেননি, এবং আমানত ফেলে এমনভাবে পদত্যাগ করেননি। রোজা ও তিলাওয়াতে থাকেন।

১৮ জিলহজ ৩৫ হিজরি (জুন ৬৫৬) কুরআন পাঠরত অবস্থায় শহীদ হন, প্রায় বিরাশি বছর বয়সে। রক্ত মুশাফে পড়ে, আহলুস সুন্নাহর স্মৃতিতে শোকের দৃশ্য। বাকীতে দাফন হন। আহলুস সুন্নাহ তাঁকে তৃতীয় রাশিদ খলিফা, যুন-নূরাইন ও মুশাফের খলিফা বলে সম্মান করে, এবং তাঁকে বা কোনো সাহাবি رضي الله عنهم-কে নিন্দা করতে নিষেধ করে।""",
    """Utsman bin Affan bin Abil Ash رضي الله عنه berasal dari Bani Umayyah Quraisy, saudagar kaya yang dikenal di Makkah karena malu dan, menurut riwayat tabaqat, tidak pernah menyembah berhala bahkan sebelum Islam. Ibnu Sa'd mencatat nasabnya melalui Abd Manaf, leluhur jauh yang sama dengan Nabi ﷺ. Ia masuk Islam awal melalui Abu Bakar رضي الله عنه, termasuk kelompok lelaki pertama. Hartanya kemudian membekali pasukan; wataknya malu, dermawan, dan tilawah Al-Qur'an.

Ia menikahi Ruqayyah putri Nabi ﷺ, dan setelah ia wafat menikahi saudarinya Ummu Kultsum رضي الله عنهما. Karena itu ia disebut Dzan-Nurain, Pemilik Dua Cahaya, kemuliaan unik di rumah Rasul ﷺ. Tidak ada sahabat lain yang tercatat menikahi dua putri seorang nabi secara berurutan. Ketika Ruqayyah sakit pada masa Badar 2 H / 624 M, Utsman tinggal di Madinah merawatnya dengan izin Nabi ﷺ dan diberi pahala Badar.

Ia hijrah dua kali: pertama ke Habasyah bersama Ruqayyah pada tahun-tahun awal penyiksaan, lalu ke Madinah. Ibnu Hisyam menyebut hijrah ganda ini sebagai tanda pengorbanan awal. Di Madinah ia membeli sumur Rumah dan mewakafkannya bagi kaum muslimin, serta memperluas Masjid Nabawi dengan hartanya. Pada ekspedisi Tabuk 9 H / 630 M ia membekali pasukan begitu lengkap—unta, kuda, dan ribuan dinar—sehingga Nabi ﷺ bersabda, 'Tidak ada yang akan membahayakan Utsman setelah hari ini.'

Ia termasuk al-asyarah al-mubasysyarah dan termasuk yang berbaiat di bawah pohon di Hudaibiyah; ketika ia absen di Makkah sebagai utusan, Nabi ﷺ menggenggam tangan sendiri untuk baiat Utsman. Setelah syura Umar pada 23 H / 644 M umat memilihnya sebagai khalifah ketiga. Masa pemerintahannya dua belas tahun (23–35 H / 644–656 M). Pada tahun-tahun pertama umat menikmati perluasan ke Afrika Utara, Armenia, dan menuju Asia Tengah, dan Laut Tengah melihat angkatan laut muslim pertama di bawah Muawiyah رضي الله عنه dengan izin Utsman.

Karya paling abadi khilafahnya adalah penyeragaman Al-Qur'an tertulis, mushaf Utsmani. Perbedaan qiraat di wilayah, terutama yang didengar Huzaifah bin al-Yaman رضي الله عنه di front Armenia-Azerbaijan, mendorongnya bertindak. Panitia di bawah Zaid bin Tsabit menyalin suhuf yang disimpan Hafshah رضي الله عنها menjadi salinan standar yang dikirim ke kota-kota. Rasm ini tetap bentuk tertulis umat.

Pada tahun-tahun kemudian muncul keluhan tentang gubernur dan pembagian. Sejarawan Ahlusunah seperti ath-Thabari mencatat keresahan tanpa mencela Utsman atau Sahabat yang berbeda pendapat. Pemberontak dari Mesir, Kufah, dan Basrah mengepung rumahnya di Madinah. Ia menolak menumpahkan darah muslim di jalan untuk menyelamatkan diri, dan menolak mundur dengan cara yang akan menyia-nyiakan amanah. Ia tetap berpuasa dan membaca Al-Qur'an.

Ia terbunuh pada 18 Zulhijah 35 H (Juni 656 M) sambil membaca Al-Qur'an, sekitar usia delapan puluh dua tahun. Darahnya jatuh di mushaf, pemandangan yang dikenang dengan duka dalam ingatan Ahlusunah. Ia dimakamkan di Baqi. Ahlusunah memuliakannya sebagai yang ketiga dari Khulafaur Rasyidin, Dzan-Nurain, dan khalifah mushaf, dan mereka melarang mencelanya atau mencela Sahabat mana pun رضي الله عنهم.""",
)
ch["items"][0]["details"] = D(
    """The written Quran had already been gathered into suhuf in Abu Bakr's time after Yamamah, kept first with Abu Bakr, then with Umar, then with Hafsah رضي الله عنهم. That collection used the dialect and the last review (arda) of the Prophet ﷺ as Zayd understood it. It was not yet sent as identical bound copies to every garrison. Reciters in Kufa, Basra, Sham, and the frontiers still taught from their personal sheets and from memory.

Hudhayfah ibn al-Yaman رضي الله عنه, returning from the campaigns in Armenia and Azerbaijan in the later years of Uthman, heard Muslims disputing recitations as the people of Iraq and Sham mixed. He feared the kind of disagreement that had split earlier communities over their books. He went to Uthman and said, 'Save this ummah before they differ about the Book as the Jews and Christians differed.' This counsel is reported in Sahih al-Bukhari.

Uthman assembled a committee headed by Zayd ibn Thabit, with Abdullah ibn al-Zubayr, Sa'id ibn al-As, and Abd al-Rahman ibn al-Harith ibn Hisham رضي الله عنهم. He told the Qurashi members that if they differed with Zayd in spelling, they should write in the tongue of Quraysh, for the Quran was revealed in their tongue. They copied from Hafsah's sheets. Several complete mushafs were produced.

Those official copies were sent to the major cities—typically listed as Makkah, Madinah, Kufa, Basra, and Sham, with a copy retained in Madinah—and a reciter was often sent with the book. Uthman ordered that other scattered personal collections be set aside so that teaching would not fracture around variant spellings of the same revelation. The people of knowledge accepted this as service to the Book, not as a new text.

The Uthmani rasm became the skeleton upon which the canonical qira'at were later written. The seven, then ten, readings taught in the schools all fit that consonantal frame. Sunni usul al-qira'at hold that Uthman did not abolish the seven ahruf by whim; he united the ummah on the written form that matched the final presentation to Jibril. Difference of recitation that is mutawatir remained inside that mushaf.

Hafsah's suhuf were returned to her after the work. The story of later storage and of copies such as those attributed to the cities belongs to the history of manuscripts. What matters for the encyclopedia of the Sahaba is that the caliph who equipped Tabuk also spent the authority of the state to protect one Book. Zayd, who had written wahyi for the Prophet ﷺ, was again the scribe of record.

Sunni encyclopedias treat the Uthmani mushaf as a glory of the third caliph and a mercy for later centuries. They mention Hudhayfah's fear, Zayd's committee, Hafsah's sheets, and the provincial copies together. They do not turn the project into a charge against other Companions who had taught slightly different spellings in good faith. The ummah still prays from that rasm.""",
    """تحریری قرآن ابو بکر کے عہد میں یمامہ کے بعد صحیفوں میں جمع ہو چکا تھا، پہلے ابو بکر، پھر عمر، پھر حفصہ رضی اللہ عنہم کے پاس رہا۔ اس جمع میں زید کی سمجھ کے مطابق قریش کی زبان اور آخری عرضہ شامل تھی۔ ابھی ہر چھاؤنی کو ایک جیسے جلد شدہ نسخے نہیں بھیجے گئے تھے۔ کوفہ، بصرہ، شام اور سرحدوں کے قاری اپنے اوراق اور حافظے سے پڑھاتے رہے۔

حذیفہ بن یمان رضی اللہ عنہ عثمان کے آخری برسوں میں آرمینیا و آذربائیجان کی مہمات سے لوٹے تو عراق و شام کے لوگ مل کر قراءتوں میں جھگڑتے سنا۔ ڈرا کہ پہلی امتوں جیسی کتابوں میں پھوٹ نہ آ جائے۔ عثمان کے پاس آ کر کہا اس امت کو بچاؤ اس سے پہلے کہ یہود و نصاریٰ کی طرح کتاب میں اختلاف کریں۔ یہ مشورہ صحیح بخاری میں ہے۔

عثمان نے زید بن ثابت کی صدارت میں کمیٹی بنائی، ساتھ عبد اللہ بن زبیر، سعید بن العاص اور عبد الرحمن بن حارث بن ہشام رضی اللہ عنہم۔ قریشی ارکان سے کہا زید سے ہجے میں اختلاف ہو تو قریش کی زبان میں لکھیں، قرآن انہی کی زبان میں اترا۔ حفصہ کے اوراق سے نقل ہوئی۔ کئی مکمل مصحف تیار ہوئے۔

سرکاری نسخے بڑے شہروں کو بھیجے گئے—عموماً مکہ، مدینہ، کوفہ، بصرہ، شام، ایک نسخہ مدینہ میں رکھا—اور اکثر قاری کتاب کے ساتھ گیا۔ عثمان نے حکم دیا بکھرے ذاتی مجموعے کنارے رکھے جائیں تاکہ ایک ہی وحی کے مختلف ہجوں پر درس نہ ٹوٹے۔ اہل علم نے اسے کتاب کی خدمت مانا، نیا متن نہیں۔

عثمانی رسم وہ ڈھانچہ بنا جس پر بعد کی متواتر قراءتیں لکھی گئیں۔ مکاتب کی سات پھر دس قراءتیں اسی حرفی فریم میں سماتیں۔ اہل سنت کے اصولِ قراءت کے مطابق عثمان نے سات حروف ہوے سے منسوخ نہیں کیے؛ امت کو اس لکھے ہوئے پر اکٹھا کیا جو جبریل پر آخری پیشکش سے میل کھاتا تھا۔ متواتر اختلافِ قراءت اسی مصحف کے اندر رہا۔

کام کے بعد حفصہ کے صحیفے واپس کیے گئے۔ بعد کے ذخیرے اور شہروں سے منسوب نسخے مخطوطات کی تاریخ ہیں۔ صحابہ کے دائرۃ المعارف کے لیے بات یہ ہے کہ جس خلیفہ نے تبوک تیار کیا اسی نے ریاست کی طاقت ایک کتاب کی حفاظت پر خرچی۔ زید جو نبی ﷺ کے لیے وحی لکھتے رہے، پھر سند کے کاتب بنے۔

سنی دائرۃ المعارف عثمانی مصحف کو تیسرے خلیفہ کا فخر اور بعد کی صدیوں کی رحمت مانتی ہیں۔ حذیفہ کا ڈر، زید کی کمیٹی، حفصہ کے اوراق اور صوبائی نسخے اکٹھے ذکر ہوتے ہیں۔ اس منصوبے کو دوسرے صحابہ پر الزام نہیں بناتے جنہوں نے نیک نیتی سے قدرے مختلف ہجے پڑھائے۔ امت آج بھی اسی رسم سے نماز پڑھتی ہے۔""",
    """तहरीरि कुरआन अबू बक्र के अहद में यमामा के बाद सहीफ़ों में जमा हो चुका था, पहले अबू बक्र, फिर उमर, फिर हफ़्सा رضي الله عنهم के पास रहा। उस जमा में ज़ैद की समझ के मुताबिक कुरैश की ज़बान और आख़िरी अर्दा शामिल थी। अभी हर छावनी को एक जैसे जिल्दशुदा नुस्ख़े नहीं भेजे गए थे। कूफ़ा, बसरा, शाम और सरहदों के क़ारी अपने औराक़ और हिफ़्ज़ से पढ़ाते रहे।

हुज़ैफ़ा बिन यमान رضي الله عنه उस्मान के आख़िरी बरसों में अर्मेनिया व आज़रबाइजान की मुहिमातों से लौटे तो इराक व शाम के लोग मिल कर क़िराअतों में झगड़ते सुना। डरा कि पिछली उम्मतों जैसी किताबों में फूट न आ जाए। उस्मान के पास आ कर कहा इस उम्मत को बचाओ इससे पहले कि यहूद व नसारा की तरह किताब में इख़्तिलाफ़ करें। यह मशवरा सहीह बुख़ारी में है।

उस्मान ने ज़ैद बिन साबित की सदारत में कमेटी बनाई, साथ अब्दुल्लाह बिन ज़ुबैर, सईद बिन अल-आस और अब्दुर्रहमान बिन हारिस बिन हिशाम رضي الله عنهم। कुरैशी अरकान से कहा ज़ैद से हिज्जे में इख़्तिलाफ़ हो तो कुरैश की ज़बान में लिखें, कुरआन उन्हीं की ज़बान में उतरा। हफ़्सा के औराक़ से नक़्ल हुई। कई मुकम्मल मुसहफ़ तैयार हुए।

सरकारी नुस्ख़े बड़े शहरों को भेजे गए—उमूमन मक्का, मदीना, कूफ़ा, बसरा, शाम, एक नुस्ख़ा मदीना में रखा—और अक्सर क़ारी किताब के साथ गया। उस्मान ने हुक्म दिया बिखरे ज़ाती मज्मूए किनारे रखे जाएँ ताकि एक ही वही के मुख़्तलिफ़ हिज्जों पर दर्स न टूटे। अहले इल्म ने इसे किताब की ख़िदमत माना, नया मत्न नहीं।

उस्मानी रस्म वह ढाँचा बना जिस पर बाद की मुतवातिर क़िराअतें लिखी गईं। मकातिब की सात फिर दस क़िराअतें उसी हर्फ़ी फ्रेम में समातीं। अहले सुन्नत के उसूल-ए-क़िराअत के मुताबिक उस्मान ने सात अहरूफ़ होए से मन्सूख़ नहीं किए; उम्मत को उस लिखे हुए पर इकट्ठा किया जो जिबरील पर आख़िरी पेशकश से मेल खाता था। मुतवातिर इख़्तिलाफ़-ए-क़िराअत उसी मुसहफ़ के अंदर रहा।

काम के बाद हफ़्सा के सहीफ़े वापस किए गए। बाद के ज़ख़ीरे और शहरों से मन्सूब नुस्ख़े मख़तूतात की तारीख़ हैं। सहाबा के दाइरतुल मआरिफ़ के लिए बात यह है कि जिस ख़लीफा ने तबूक तैयार किया उसी ने रियासत की ताक़त एक किताब की हिफ़ाज़त पर ख़र्च की। ज़ैद जो नबी ﷺ के लिए वही लिखते रहे, फिर सनद के कातिब बने।

सुन्नी दाइरतुल मआरिफ़ उस्मानी मुसहफ़ को तीसरे ख़लीफा का फ़ख़्र और बाद की सदियों की रहमत मानती हैं। हुज़ैफ़ा का डर, ज़ैद की कमेटी, हफ़्सा के औराक़ और सूबाई नुस्ख़े इकट्ठे ज़िक्र होते हैं। इस मन्सूबे को दूसरे सहाबा पर इल्ज़ाम नहीं बनाते जिन्होंने नेक नियत से क़दरे मुख़्तलिफ़ हिज्जे पढ़ाए। उम्मत आज भी उसी रस्म से नमाज़ पढ़ती है।""",
    """লিখিত কুরআন আবু বকরের আমলে ইয়ামামার পর সহীফায় সংগৃহীত হয়েছিল, প্রথমে আবু বকর, পরে উমর, তারপর হাফসাহ رضي الله عنهم-এর কাছে ছিল। সেই সংকলনে যায়েদের বোঝাপড়া অনুসারে কুরাইশের ভাষা ও শেষ আরদাহ ছিল। তখনও প্রতি ছাউনিতে একই বাঁধাই কপি পাঠানো হয়নি। কুফা, বসরা, শাম ও সীমান্তের কারি ব্যক্তিগত পত্র ও মুখস্থ থেকে পড়াতেন।

হুযাইফাহ ইবনুল ইয়ামান رضي الله عنه উসমানের শেষ বছরগুলোতে আর্মেনিয়া ও আজারবাইজান অভিযান থেকে ফিরে ইরাক ও শামের লোক মিলে কিরাআত নিয়ে বিবাদ করতে শোনেন। ভয় করেন পূর্ববর্তী উম্মাহর মতো কিতাবে ফাটল না ধরে। উসমানের কাছে গিয়ে বলেন, এই উম্মাহকে বাঁচান ইহুদি-খ্রিষ্টানদের মতো কিতাবে মতভেদ করার আগে। এই পরামর্শ সহীহ বুখারিতে আছে।

উসমান যায়েদ ইবন সাবিতের সভাপতিত্বে কমিটি গঠন করেন, সঙ্গে আব্দুল্লাহ ইবন যুবায়র, সাঈদ ইবনুল আস ও আব্দুর রহমান ইবনুল হারিস ইবন হিশাম رضي الله عنهم। কুরাইশি সদস্যদের বলেন যায়েদের সঙ্গে বানানে ভিন্ন হলে কুরাইশের ভাষায় লিখতে, কুরআন সেই ভাষায় অবতীর্ণ। হাফসাহর পত্র থেকে নকল হয়। কয়েকটি পূর্ণ মুশাফ তৈরি হয়।

সরকারি কপি প্রধান নগরে পাঠানো হয়—সাধারণত মক্কা, মদিনা, কুফা, বসরা, শাম, একটি কপি মদিনায় রাখা—এবং প্রায়ই কারি কিতাবের সঙ্গে যান। উসমান আদেশ দেন ছড়ানো ব্যক্তিগত সংগ্রহ সরিয়ে রাখতে যাতে একই ওহির ভিন্ন বানানে পাঠ না ভাঙে। আহলে ইলম একে কিতাবের খিদমত মানেন, নতুন পাঠ নয়।

উসমানি রসম সেই কাঠামো হয় যার উপর পরবর্তী মুতাওয়াতির কিরাআত লেখা হয়। মাদরাসার সাত তারপর দশ কিরাআত সেই ব্যঞ্জন কাঠামোতেই মাপে। আহলুস সুন্নাহর উসূলে কিরাআত অনুসারে উসমান সাত হরফ খামখেয়ালি বাতিল করেননি; উম্মাহকে সেই লিখিত রূপে এক করেন যা জিবরীলের কাছে শেষ পেশার সঙ্গে মেলে। মুতাওয়াতির কিরাআতের পার্থক্য সেই মুশাফের ভিতরেই থাকে।

কাজের পর হাফসাহর সহীফা ফেরত দেওয়া হয়। পরবর্তী সংরক্ষণ ও নগর-আরোপিত কপির কাহিনি পাণ্ডুলিপির ইতিহাস। সাহাবা বিশ্বকোষের জন্য কথা এই যে, যে খলিফা তাবুক সজ্জিত করেন তিনিই রাষ্ট্রের ক্ষমতা এক কিতাব রক্ষায় ব্যয় করেন। যায়েদ যিনি নবী ﷺ-এর জন্য ওহি লিখতেন, আবার নথির কাতিব হন।

সুন্নি বিশ্বকোষ উসমানি মুশাফকে তৃতীয় খলিফার গৌরব ও পরবর্তী শতাব্দীর রহমত মানে। হুযাইফার ভয়, যায়েদের কমিটি, হাফসাহর পত্র ও প্রাদেশিক কপি একত্রে উল্লেখ করে। এই প্রকল্পকে অন্য সাহাবিদের অভিযোগে পরিণত করে না যাঁরা সদাশয়ে সামান্য ভিন্ন বানান পড়িয়েছেন। উম্মাহ আজও সেই রসম থেকে নামাজ পড়ে।""",
    """Al-Qur'an tertulis sudah dikumpulkan menjadi suhuf pada masa Abu Bakar setelah Yamamah, disimpan mula-mula pada Abu Bakar, lalu Umar, lalu Hafshah رضي الله عنهم. Pengumpulan itu memakai lidah dan aradah terakhir Nabi ﷺ sebagaimana dipahami Zaid. Ia belum dikirim sebagai salinan terjilid yang sama ke setiap garnisun. Qari di Kufah, Basrah, Syam, dan perbatasan masih mengajar dari lembar pribadi dan hafalan.

Huzaifah bin al-Yaman رضي الله عنه, pulang dari ekspedisi Armenia dan Azerbaijan di tahun-tahun akhir Utsman, mendengar kaum muslimin berselisih tentang qiraat ketika orang Irak dan Syam bercampur. Ia khawatir perselisihan semacam yang memecah umat terdahulu tentang kitab mereka. Ia menemui Utsman dan berkata, 'Selamatkan umat ini sebelum mereka berselisih tentang Kitab sebagaimana Yahudi dan Nasrani berselisih.' Nasihat ini diriwayatkan dalam Sahih Bukhari.

Utsman membentuk panitia dipimpin Zaid bin Tsabit, bersama Abdullah bin az-Zubair, Said bin al-As, dan Abdurrahman bin al-Harits bin Hisyam رضي الله عنهم. Ia berpesan kepada anggota Quraisy bahwa jika mereka berbeda dengan Zaid dalam ejaan, hendaklah menulis dengan lidah Quraisy, karena Al-Qur'an turun dengan lidah mereka. Mereka menyalin dari lembaran Hafshah. Beberapa mushaf lengkap dihasilkan.

Salinan resmi dikirim ke kota-kota besar—lazimnya disebut Makkah, Madinah, Kufah, Basrah, dan Syam, dengan satu salinan dipertahankan di Madinah—dan seorang qari sering diutus bersama kitab. Utsman memerintahkan agar kumpulan pribadi yang tercerai disisihkan supaya pengajaran tidak pecah di sekitar ejaan berbeda dari wahyu yang sama. Ahli ilmu menerima ini sebagai khidmah kepada Kitab, bukan teks baru.

Rasm Utsmani menjadi rangka tempat qiraat kanonik kemudian ditulis. Bacaan tujuh, lalu sepuluh, yang diajarkan di madrasah semuanya muat dalam rangka konsonan itu. Usul qiraat Ahlusunah berpegang bahwa Utsman tidak menghapus tujuh ahruf karena hawa nafsu; ia mempersatukan umat pada bentuk tertulis yang selaras dengan presentasi terakhir kepada Jibril. Perbedaan qiraat yang mutawatir tetap di dalam mushaf itu.

Suhuf Hafshah dikembalikan kepadanya setelah pekerjaan selesai. Kisah penyimpanan kemudian dan salinan yang dinisbahkan kepada kota-kota termasuk sejarah naskah. Yang penting bagi ensiklopedia Sahabat adalah bahwa khalifah yang membekali Tabuk juga membelanjakan wewenang negara untuk melindungi satu Kitab. Zaid, yang menulis wahyu bagi Nabi ﷺ, kembali menjadi juru tulis resmi.

Ensiklopedia Ahlusunah memandang mushaf Utsmani sebagai kemuliaan khalifah ketiga dan rahmat bagi abad kemudian. Mereka menyebut ketakutan Huzaifah, panitia Zaid, lembaran Hafshah, dan salinan provinsi bersama. Mereka tidak mengubah proyek itu menjadi tuduhan terhadap Sahabat lain yang mengajarkan ejaan sedikit berbeda dengan niat baik. Umat masih salat dari rasm itu.""",
)

# --- 4 Ali ibn Abi Talib ---
ch = chapter(4)
ch["details"] = D(
    """Ali ibn Abi Talib ibn Abd al-Muttalib رضي الله عنه was the cousin of the Prophet ﷺ, son of the Prophet's uncle Abu Talib and Fatimah bint Asad. He was born inside the Ka'bah according to some later reports, and raised for years in the Prophet's ﷺ house when Abu Talib's means were straitened. He was the first boy to believe, while still a child, as Ibn Ishaq and Ibn Sa'd relate. Sunni historians place his Islam immediately after Khadijah and, among free adult men, after Abu Bakr, without turning that order into a quarrel.

He married Fatimah al-Zahra رضي الله عنها, the youngest daughter of the Prophet ﷺ and Khadijah. Their children included al-Hasan, al-Husayn, Zaynab, and Umm Kulthum رضي الله عنهم. The Prophet ﷺ loved this household; hadith of the cloak and many reports of kissing Hasan and Husayn are in the sahih collections. Ali's kunya Abu Turab is remembered from a smiling word of the Messenger ﷺ when he found Ali sleeping in the dust. He was among the asharah mubashsharah.

On the night of the Hijrah in 1 AH / 622 CE he slept in the Prophet's ﷺ bed so that the assassins of Quraysh would see a body and delay, while the Messenger ﷺ left for the cave of Thawr. He then returned the trusts (wada'i) that Quraysh had lodged with Muhammad ﷺ, and migrated to Madinah. Ibn Hisham records this as one of the great acts of courage of a young man who could have been killed in that bed.

He was a distinguished warrior at Badr, Uhud, Khandaq—where he killed Amr ibn Abd Wudd in single combat—and Khaybar in 7 AH / 628 CE. At Khaybar the Prophet ﷺ said he would give the banner to a man who loves Allah and His Messenger, and they love him; he called Ali, cured his eye, and Ali defeated Marhab and took the fortress of Qamus. These maghazi scenes are in Bukhari, Muslim, and the sirah. Courage in Ali is a Sunni article of praise, not a partisan slogan.

After Uthman's martyrdom in 35 AH / 656 CE the remaining people of Madinah pledged to Ali as fourth khalifah. His caliphate (35–40 AH / 656–661 CE) fell in the years of fitnah. The Battle of the Camel near Basra, Siffin against the army of Sham, and Nahrawan against the Khawarij who had seceded after the arbitration, tore the community. Ahl al-Sunnah withhold their tongues from cursing Aisha, Talha, al-Zubayr, or Mu'awiyah رضي الله عنهم; they describe a trial in which Companions strove, then many regretted bloodshed. Ali moved the capital to Kufa.

On a Fajr in Ramadan 40 AH / January 661 CE Abd al-Rahman ibn Muljam, a Kharijite, struck him with a poisoned sword as he entered the mosque. He died two days later, having ordered that his killer be treated within the limits of the law, not with mutilation. He was buried in Kufa (Najaf in later geography). His sermons and legal verdicts, gathered in later collections with varying chains, made him a fountain of fiqh, courage, and eloquence for the Sunni schools as well as for others who love the Ahl al-Bayt.

Sunni encyclopedias present Ali as the gate of knowledge in the famous hadith, the husband of Fatimah, the fourth Rashidun caliph, and a man who did not instruct the ummah to revile the first three caliphs. Reports of his praise for Abu Bakr and Umar are widely cited in Sunni creed texts. Honouring Ali رضي الله عنه is obligatory; attacking other Sahaba in his name is rejected.""",
    """علی بن ابی طالب بن عبد المطلب رضی اللہ عنہ نبی ﷺ کے چچازاد، چچا ابو طالب اور فاطمہ بنت اسد کے بیٹے تھے۔ بعض متاخر روایات کے مطابق کعبہ کے اندر پیدا ہوئے، اور ابو طالب کی تنگی پر برسوں نبی ﷺ کے گھر پلے۔ ابن اسحاق و ابن سعد کے بیان میں بچپن میں ایمان لانے والے پہلے لڑکے تھے۔ سنی مورخ ان کا اسلام خدیجہ کے بعد اور بالغ آزاد مردوں میں ابو بکر کے بعد رکھتے ہیں، اس ترتیب کو جھگڑا نہیں بناتے۔

فاطمہ الزہرا رضی اللہ عنہا سے نکاح ہوا، نبی ﷺ اور خدیجہ کی چھوٹی بیٹی۔ اولاد میں حسن، حسین، زینب، ام کلثوم رضی اللہ عنہم۔ نبی ﷺ اس گھر سے محبت کرتے؛ حدیث کسا اور حسنین کو چومنے کی بہت سی روایات صحاح میں ہیں۔ کنیت ابو تراب رسول ﷺ کی مسکراہٹ سے یاد ہے جب علی مٹی میں سوئے ملے۔ عشرہ مبشرہ میں سے تھے۔

ہجرت کی رات 1ھ / 622ء نبی ﷺ کے بستر پر سوئے تاکہ قریش کے قاتل جسم دیکھ کر ٹھہریں، رسول ﷺ غار ثور روانہ ہوں۔ پھر وہ امانتیں لوٹائیں جو قریش نے محمد ﷺ کے پاس رکھوائی تھیں، اور مدینہ ہجرت کی۔ ابن ہشام اسے جوان کی بڑی بہادری میں شمار کرتے ہیں جو اس بستر پر قتل ہو سکتے تھے۔

بدر، احد، خندق—جہاں عمرو بن عبد ود کو مبارزے میں قتل کیا—اور 7ھ / 628ء خیبر میں ممتاز جنگجو رہے۔ خیبر پر نبی ﷺ نے فرمایا جھنڈا اس شخص کو دوں گا جو اللہ و رسول سے محبت کرتا ہے اور وہ اس سے محبت کرتے ہیں؛ علی کو بلایا، آنکھ شفا دی، علی نے مرحب کو شکست دی اور قلعہ قموص لیا۔ یہ مغازی بخاری، مسلم اور سیرت میں ہیں۔ علی کی شجاعت سنی تعریف ہے، گروہی نعرہ نہیں۔

عثمان کی شہادت 35ھ / 656ء کے بعد مدینہ کے باقی لوگوں نے علی سے چوتھے خلیفہ کی بیعت کی۔ خلافت (35–40ھ / 656–661ء) فتنے کے برسوں میں پڑی۔ بصرہ کے قریب جنگ جمل، شام کی فوج سے صفین، اور تحکیم کے بعد الگ ہونے والے خوارج سے نہروان نے امت کو پھاڑا۔ اہل سنت عائشہ، طلحہ، زبیر یا معاویہ رضی اللہ عنہم کو گالی سے زبان روکے رکھتے ہیں؛ ایک آزمائش بیان کرتے ہیں جس میں صحابہ نے کوشش کی، پھر بہتوں نے خون پر ندم کی۔ علی نے دار الخلافت کوفہ منتقل کیا۔

رمضان 40ھ / جنوری 661ء کی ایک فجر پر خارجی عبد الرحمن بن ملجم نے مسجد میں داخل ہوتے زہریلی تلوار ماری۔ دو دن بعد شہادت ہوئی، قاتل کے ساتھ قانون کی حد کا حکم دیا، مثلہ نہیں۔ کوفہ (بعد کی جغرافیہ میں نجف) دفن ہوئے۔ خطبے اور فتوے، مختلف سندوں سے بعد کے مجموعوں میں، فقہ، شجاعت اور بلاغت کا چشمہ بنے اہل سنت کے مکاتب کے لیے بھی اور اہل بیت سے محبت کرنے والوں کے لیے بھی۔

سنی دائرۃ المعارف علی کو مشہور حدیث میں بابِ علم، فاطمہ کے شوہر، چوتھے راشد خلیفہ، اور ایسے آدمی کے طور پر پیش کرتے ہیں جنہوں نے امت کو پہلے تین خلفاء کو برا کہنے کی تعلیم نہ دی۔ ابو بکر و عمر کی تعریف کی روایات سنی عقائد کی کتابوں میں بکثرت ہیں۔ علی رضی اللہ عنہ کی عزت فرض ہے؛ ان کے نام پر دوسرے صحابہ پر حملہ مردود ہے۔""",
    """अली इब्न अबी तालिब इब्न अब्दुल मुत्तलिब رضي الله عنه नबी ﷺ के चचेरे भाई, चाचा अबू तालिब और फ़ातिमा बिन्त असद के बेटे थे। कुछ मुताअख्ख़िर रिवायात के मुताबिक काबा के अंदर पैदा हुए, और अबू तालिब की तंगी पर बरसों नबी ﷺ के घर पले। इब्न इसहाक व इब्न साद के बयान में बचपन में ईमान लाने वाले पहले लड़के थे। सुन्नी मुवर्रिख़ उनका इस्लाम ख़दीजा के बाद और बालिग आज़ाद मर्दों में अबू बक्र के बाद रखते हैं, इस तरतीब को झगड़ा नहीं बनाते।

फ़ातिमा अज़-ज़हरा رضي الله عنها से निकाह हुआ, नबी ﷺ और ख़दीजा की छोटी बेटी। औलाद में हसन, हुसैन, ज़ैनब, उम्म कुलसूम رضي الله عنهم। नबी ﷺ इस घर से मुहब्बत करते; हदीस-ए-किसा और हसनैन को चूमने की बहुत सी रिवायात सिहाह में हैं। कुन्यत अबू तुराब रसूल ﷺ की मुस्कुराहट से याद है जब अली मिट्टी में सोए मिले। अशरा-ए-मुबश्शिरा में से थे।

हिजरत की रात 1 हिजरी / 622 ई. नबी ﷺ के बिस्तर पर सोए ताकि कुरैश के क़ातिल जिस्म देख कर ठहरें, रसूल ﷺ ग़ार-ए-सौर रवाना हों। फिर वह अमानतें लौटाईं जो कुरैश ने मुहम्मद ﷺ के पास रखवाई थीं, और मदीना हिजरत की। इब्न हिशाम इसे जवान की बड़ी बहादुरी में शुमार करते हैं जो उस बिस्तर पर क़त्ल हो सकते थे।

बद्र, उहुद, खंदक—जहाँ अम्र बिन अब्द वुद्द को मुबारिज़े में क़त्ल किया—और 7 हिजरी / 628 ई. ख़ैबर में मुमताज़ जंगजू रहे। ख़ैबर पर नबी ﷺ ने फ़रमाया झंडा उस शख़्स को दूँगा जो अल्लाह व रसूल से मुहब्बत करता है और वे उससे मुहब्बत करते हैं; अली को बुलाया, आँख शिफ़ा दी, अली ने मरहब को शिकस्त दी और क़िला-ए-क़ामूस लिया। ये मग़ाज़ी बुख़ारी, मुस्लिम और सीरत में हैं। अली की शुजाअत सुन्नी तारीफ़ है, गिरोही नारा नहीं।

उस्मान की शहादत 35 हिजरी / 656 ई. के बाद मदीना के बाक़ी लोगों ने अली से चौथे ख़लीफा की बैअत की। खिलाफ़त (35–40 हिजरी / 656–661 ई.) फ़ितने के बरसों में पड़ी। बसरा के क़रीब जंग-ए-जमल, शाम की फ़ौज से सिफ़्फ़ीन, और तहकीम के बाद अलग होने वाले ख़वारिज से नहरवान ने उम्मत को फाड़ा। अहले सुन्नत आयशा, तलहा, ज़ुबैर या मुआविया رضي الله عنهم को गाली से ज़बान रोके रखते हैं; एक आज़माइश बयान करते हैं जिसमें सहाबा ने कोशिश की, फिर बहुतों ने ख़ून पर नदम की। अली ने दारुल ख़िलाफ़ा कूफ़ा मुनतक़िल किया।

रमज़ान 40 हिजरी / जनवरी 661 ई. की एक फज्र पर ख़ारिजी अब्दुर्रहमान बिन मुल्जम ने मस्जिद में दाख़िल होते ज़हरीली तलवार मारी। दो दिन बाद शहादत हुई, क़ातिल के साथ क़ानून की हद का हुक्म दिया, मुस्ला नहीं। कूफ़ा (बाद की जुग़राफ़िया में नजफ़) दफ़न हुए। ख़ुत्बे और फतवे, मुख़्तलिफ़ सनदों से बाद के मज्मूओं में, फ़िक़्ह, शुजाअत और बलाग़त का चश्मा बने अहले सुन्नत के मकातिब के लिए भी और अहले बैत से मुहब्बत करने वालों के लिए भी।

सुन्नी दाइरतुल मआरिफ़ अली को मशहूर हदीस में बाब-ए-इल्म, फ़ातिमा के शौहर, चौथे राशिद ख़लीफा, और ऐसे आदमी के तौर पर पेश करते हैं जिन्होंने उम्मत को पहले तीन ख़ुलफ़ा को बुरा कहने की तालीम न दी। अबू बक्र व उमर की तारीफ़ की रिवायात सुन्नी अक़ाइद की किताबों में बकसरत हैं। अली رضي الله عنه की इज़्ज़त फ़र्ज़ है; उनके नाम पर दूसरे सहाबा पर हमला मर्दूद है।""",
    """আলী ইবন আবি তালিব ইবন আব্দুল মুত্তালিব رضي الله عنه নবী ﷺ-এর চাচাতো ভাই, চাচা আবু তালিব ও ফাতিমা বিনত আসাদের পুত্র। কিছু পরবর্তী বর্ণনায় কাবার ভিতরে জন্ম, এবং আবু তালিবের অনটনে বছরের পর বছর নবী ﷺ-এর ঘরে লালিত। ইবন ইসহাক ও ইবন সাদের বর্ণনায় তিনি বাল্যে ঈমান আনা প্রথম বালক। সুন্নি ঐতিহাসিক তাঁর ইসলাম খাদিজার পর এবং প্রাপ্তবয়স্ক স্বাধীন পুরুষদের মধ্যে আবু বকরের পর রাখেন, সেই ক্রমকে বিবাদ করেন না।

তিনি ফাতিমাহ আজ-জাহরা رضي الله عنها-কে বিয়ে করেন, নবী ﷺ ও খাদিজার কনিষ্ঠ কন্যা। সন্তানদের মধ্যে হাসান, হুসাইন, যায়নব, উম্মু কুলসুম رضي الله عنهم। নবী ﷺ এই ঘরকে ভালোবাসতেন; কিসার হাদিস ও হাসান-হুসাইনকে চুম্বনের অনেক বর্ণনা সিহাহ গ্রন্থে আছে। কুনইয়া আবু তুরাব রাসূল ﷺ-এর মুচকি হাসি থেকে স্মরণীয়, যখন আলী ধুলোয় ঘুমন্ত পাওয়া যান। তিনি আশারায়ে মুবাশশারার একজন।

হিজরতের রাতে ১ হিজরি / ৬২২ খ্রি. তিনি নবী ﷺ-এর বিছানায় শয়ন করেন যাতে কুরাইশের ঘাতকেরা দেহ দেখে দেরি করে, রাসূল ﷺ সওর গুহার দিকে যান। তারপর কুরাইশ মুহাম্মদ ﷺ-এর কাছে যে আমানত রেখেছিল ফেরত দেন এবং মদিনায় হিজরত করেন। ইবন হিশাম একে যুবকের মহাসাহস বলে, যিনি সেই বিছানায় নিহত হতে পারতেন।

তিনি বদর, উহুদ, খন্দক—যেখানে আমর ইবন আব্দ ওয়াদ্দকে দ্বন্দ্বযুদ্ধে নিহত করেন—এবং ৭ হিজরি / ৬২৮ খ্রি. খাইবারে বিশিষ্ট যোদ্ধা। খাইবারে নবী ﷺ বলেন, তিনি পতাকা এমন ব্যক্তিকে দেবেন যিনি আল্লাহ ও তাঁর রাসূলকে ভালোবাসেন এবং তাঁরাও তাঁকে ভালোবাসেন; আলীকে ডাকেন, চোখ সুস্থ করেন, আলী মারহাবকে পরাস্ত করে কামুস দুর্গ নেন। এই মাগাজি বুখারি, মুসলিম ও সিরাতে আছে। আলীর সাহস সুন্নি প্রশংসা, দলীয় স্লোগান নয়।

উসমানের শাহাদাত ৩৫ হিজরি / ৬৫৬-এর পর মদিনার অবশিষ্ট লোকেরা আলীকে চতুর্থ খলিফা হিসেবে বাইআত দেয়। তাঁর খিলাফত (৩৫–৪০ হিজরি / ৬৫৬–৬৬১) ফিতনার বছরে পড়ে। বসরার কাছে জামালের যুদ্ধ, শামের সেনার সঙ্গে সিফফিন, এবং সালিশির পর বিচ্ছিন্ন খারিজিদের সঙ্গে নাহরাওয়ান উম্মাহকে ছিন্ন করে। আহলুস সুন্নাহ আয়িশা, তালহা, যুবায়র বা মুয়াবিয়া رضي الله عنهم-কে গালি থেকে জিহ্বা রোকে; একটি পরীক্ষা বর্ণনা করে যাতে সাহাবিরা চেষ্টা করেন, পরে অনেকে রক্তপাতে অনুতপ্ত হন। আলী রাজধানী কুফায় স্থানান্তর করেন।

রমজান ৪০ হিজরি / জানুয়ারি ৬৬১-এর এক ফজরে খারিজি আব্দুর রহমান ইবন মুলজাম মসজিদে প্রবেশকালে বিষাক্ত তলোয়ার দিয়ে আঘাত করেন। দুই দিন পর শাহাদাত, ঘাতকের সঙ্গে আইনের সীমা প্রয়োগের আদেশ, অঙ্গচ্ছেদ নয়। কুফায় (পরবর্তী ভূগোলে নাজাফ) দাফন হন। খুতবা ও ফতোয়া, বিভিন্ন সনদে পরবর্তী সংগ্রহে, ফিকহ, সাহস ও বাগ্মিতার উৎস হয় সুন্নি মাজহাবের জন্যও এবং আহলুল বায়তপ্রেমীদের জন্যও।

সুন্নি বিশ্বকোষ আলীকে প্রসিদ্ধ হাদিসে ইলমের দ্বার, ফাতিমার স্বামী, চতুর্থ রাশিদ খলিফা, এবং এমন মানুষ হিসেবে উপস্থাপন করে যিনি উম্মাহকে প্রথম তিন খলিফাকে নিন্দা শেখাননি। আবু বকর ও উমরের প্রশংসার বর্ণনা সুন্নি আকিদা গ্রন্থে বহুল উদ্ধৃত। আলী رضي الله عنه-এর সম্মান ফরজ; তাঁর নামে অন্য সাহাবিদের আক্রমণ প্রত্যাখ্যাত।""",
    """Ali bin Abi Thalib bin Abdul Muththalib رضي الله عنه adalah sepupu Nabi ﷺ, putra paman Nabi Abu Thalib dan Fatimah binti Asad. Ia dilahirkan di dalam Ka'bah menurut sebagian riwayat kemudian, dan diasuh bertahun-tahun di rumah Nabi ﷺ ketika rezeki Abu Thalib sempit. Ia anak lelaki pertama yang beriman, masih kanak-kanak, sebagaimana diriwayatkan Ibnu Ishaq dan Ibnu Sa'd. Sejarawan Ahlusunah menempatkan Islamnya segera setelah Khadijah dan, di kalangan lelaki merdeka dewasa, setelah Abu Bakar, tanpa mengubah urutan itu menjadi pertengkaran.

Ia menikahi Fatimah az-Zahra رضي الله عنها, putri bungsu Nabi ﷺ dan Khadijah. Anak-anak mereka termasuk al-Hasan, al-Husain, Zainab, dan Ummu Kultsum رضي الله عنهم. Nabi ﷺ mencintai rumah ini; hadis kisak dan banyak riwayat mencium Hasan dan Husain ada dalam kitab sahih. Kunyah Abu Turab dikenang dari ucapan tersenyum Rasul ﷺ ketika mendapati Ali tidur di debu. Ia termasuk al-asyarah al-mubasysyarah.

Pada malam Hijrah 1 H / 622 M ia tidur di tempat tidur Nabi ﷺ agar para pembunuh Quraisy melihat tubuh dan menunda, sementara Rasul ﷺ berangkat ke Gua Tsur. Ia lalu mengembalikan amanah (wada'i) yang dititipkan Quraisy kepada Muhammad ﷺ, dan hijrah ke Madinah. Ibnu Hisyam mencatat ini sebagai salah satu keberanian besar pemuda yang bisa terbunuh di tempat tidur itu.

Ia pejuang terkemuka di Badar, Uhud, Khandaq—di mana ia membunuh Amr bin Abd Wudd dalam duel—dan Khaibar pada 7 H / 628 M. Di Khaibar Nabi ﷺ bersabda akan memberikan bendera kepada orang yang mencintai Allah dan Rasul-Nya, dan keduanya mencintainya; beliau memanggil Ali, menyembuhkan matanya, dan Ali mengalahkan Marhab serta merebut benteng Qamus. Adegan maghazi ini ada dalam Bukhari, Muslim, dan sirah. Keberanian Ali adalah pujian Ahlusunah, bukan slogan partisan.

Setelah syahidnya Utsman pada 35 H / 656 M penduduk Madinah yang tersisa berbaiat kepada Ali sebagai khalifah keempat. Khilafahnya (35–40 H / 656–661 M) jatuh pada tahun-tahun fitnah. Perang Jamal dekat Basrah, Shiffin menghadapi pasukan Syam, dan Nahrawan menghadapi Khawarij yang memisah setelah tahkim, merobek umat. Ahlusunah menahan lisan dari mencela Aisyah, Thalhah, az-Zubair, atau Muawiyah رضي الله عنهم; mereka menggambarkan ujian di mana para Sahabat berijtihad, lalu banyak yang menyesali pertumpahan darah. Ali memindahkan ibu kota ke Kufah.

Pada suatu Subuh Ramadan 40 H / Januari 661 M Abdurrahman bin Muljam, seorang Khawarij, memukulnya dengan pedang beracun saat ia memasuki masjid. Ia meninggal dua hari kemudian, setelah memerintahkan agar pembunuhnya diperlakukan dalam batas hukum, bukan dengan mutilasi. Ia dimakamkan di Kufah (Najaf dalam geografi kemudian). Khutbah dan fatwanya, dikumpulkan dalam himpunan kemudian dengan sanad yang beragam, menjadikannya mata air fikih, keberanian, dan kefasihan bagi mazhab Ahlusunah maupun bagi yang mencintai Ahlulbait.

Ensiklopedia Ahlusunah menampilkan Ali sebagai pintu ilmu dalam hadis masyhur, suami Fatimah, khalifah Rasyidin keempat, dan orang yang tidak mengajar umat untuk mencela tiga khalifah pertama. Riwayat pujiannya kepada Abu Bakar dan Umar banyak dikutip dalam kitab akidah Ahlusunah. Memuliakan Ali رضي الله عنه wajib; menyerang Sahabat lain atas namanya ditolak.""",
)
ch["items"][0]["details"] = D(
    """Al-Hasan and al-Husayn رضي الله عنهما are called the masters of the youth of Paradise in hadith recorded by al-Tirmidhi and others. They grew in the house of Ali and Fatimah under the eye of their grandfather ﷺ. Sunni love for them is part of love for the Ahl al-Bayt, without the claim that this love requires hatred of Abu Bakr, Umar, or Uthman رضي الله عنهم. Their names are invoked in blessings after salah in many lands.

Ali's knowledge of the Quran, of qada', and of the sunnah made him a reference for the fuqaha of Kufa. Sermons attributed to him, and verdicts on inheritance, hudud, and jihad, circulated widely. Chains vary in strength; the Sunni method is to weigh each report. What is solid is that the Prophet ﷺ prayed for Ali's judgement and that Companions asked him difficult questions. Eloquence and zuhd are constant themes in his remembered speech.

After Ali's death in 40 AH, al-Hasan رضي الله عنه was pledged in Kufa as caliph for a brief time. Civil war threatened to continue. In 41 AH / 661 CE he yielded authority to Mu'awiyah رضي الله عنه in a settlement that spared Muslim blood. The year was called 'am al-jama'ah, the year of the community. Hasan's act is praised in Sunni history as the fulfilment of the Prophet's ﷺ word that a son of his would reconcile two great groups of Muslims.

That settlement is commonly counted as the end of the era of the Rightly Guided Caliphs as a political sequence: Abu Bakr, Umar, Uthman, Ali, and the short tenure of Hasan. Mu'awiyah's subsequent rule is treated as kingship (mulk) by many Sunni theologians, while he remains a Companion who wrote revelation and is not to be cursed. This distinction—between the special rank of the Rashidun and the duty not to revile later Sahaba—is standard.

The Ahl al-Bayt in Sunni usage includes the wives of the Prophet ﷺ, Ali, Fatimah, Hasan, and Husayn, and more broadly Banu Hashim. Verse 33:33 and the hadith of purification are explained in tafsir without emptying them of honour and without making them a sectarian weapon. Knowledge flowed from this house into tafsir, fiqh, and adab.

Hasan's peace did not erase the grief of Siffin or the Camel; it closed the door on further slaughter among the remaining Companions. Husayn's later stand at Karbala in 61 AH belongs to the next generation and is remembered with sorrow in Sunni as well as other histories, without licensing abuse of the Sahaba of the first rank. Encyclopedias of Ali's item on knowledge therefore end with unity and restraint.

The Sunni mainstream thus holds together four lights: Ali's fiqh, Fatimah's purity, Hasan's sulh, and Husayn's courage, all under the shahadah and under respect for the first three caliphs. To teach Ali is to teach that the family of the Prophet ﷺ and the generality of the Companions are one trust, not two armies.""",
    """حسن و حسین رضی اللہ عنہما ترمذی وغیرہ کی حدیث میں جنتی نوجوانوں کے سردار کہے گئے۔ علی و فاطمہ کے گھر نانا ﷺ کی نظر میں پلے。 اہل بیت سے سنی محبت ابو بکر، عمر یا عثمان رضی اللہ عنہم سے بغض کی شرط نہیں رکھتی۔ بہت سے ملکوں میں نماز کے بعد درود میں ان کے نام آتے ہیں۔

قرآن، قضاء اور سنت کا علی کا علم انہیں کوفہ کے فقہا کا مرجع بنا۔ ان سے منسوب خطبے اور وراثت، حدود، جہاد کے فتوے پھیلے۔ سندیں مختلف طاقت کی ہیں؛ سنی روش ہر روایت کو تولنا ہے۔ پختہ بات یہ ہے کہ نبی ﷺ نے علی کے فیصلے کی دعا کی اور صحابہ مشکل سوال پوچھتے۔ بلاغت اور زہد ان کی یادگار گفتگو کے مستقل مضامین ہیں۔

علی کی شہادت 40ھ کے بعد حسن رضی اللہ عنہ کو کوفہ میں مختصر خلافت کی بیعت ہوئی۔ خانہ جنگی جاری رہنے کا خطرہ تھا۔ 41ھ / 661ء میں انہوں نے معاویہ رضی اللہ عنہ کے حق میں اختیار چھوڑا تاکہ مسلمانوں کا خون بچے۔ سال عام الجماعہ کہلایا، اجتماع کا سال۔ حسن کا یہ فعل سنی تاریخ میں نبی ﷺ کی اس بات کی تکمیل ہے کہ ان کی اولاد دو بڑے گروہوں میں صلح کرائے گی۔

اس صلح کو عموماً خلفائے راشدین کے سیاسی سلسلے کا خاتمہ مانا جاتا ہے: ابو بکر، عمر، عثمان، علی، اور حسن کی مختصر مدت۔ معاویہ کی بعد کی حکومت بہت سے سنی متکلمین ملک کہتے ہیں، مگر وہ صحابی ہیں جنہوں نے وحی لکھی، گالی کے نہیں۔ راشدین کے خاص درجے اور بعد کے صحابہ کو نہ کوسنے کی یہ تفریق معیاری ہے۔

اہل سنت کے استعمال میں اہل بیت ازواجِ نبی ﷺ، علی، فاطمہ، حسن، حسین اور وسیع تر بنو ہاشم کو شامل ہیں۔ آیت 33:33 اور حدیث تطہیر تفسیر میں عزت کے ساتھ سمجھی جاتی ہیں بغیر فرقہ وارانہ ہتھیار بنائے۔ اس گھر سے تفسیر، فقہ اور ادب میں علم بہا۔

حسن کی صلح نے جمل یا صفین کا غم مٹا نہیں دیا؛ باقی صحابہ میں مزید قتل کا دروازہ بند کیا۔ حسین کا بعد کا کربلا 61ھ اگلی نسل کا ہے، سنی اور دیگر تواریخ میں غم سے یاد ہوتا ہے، بغیر اول درجے کے صحابہ پر سب کی اجازت دے۔ علی کے علم والے باب اس لیے اتحاد اور ضبط پر ختم ہوتے ہیں۔

اہل سنت کا دھارا چار روشنیاں اکٹھی پکڑتا ہے: علی کی فقہ، فاطمہ کی طہارت، حسن کی صلح، حسین کی شجاعت، سب کلمے کے نیچے اور پہلے تین خلفاء کے احترام کے نیچے۔ علی سکھانا یہ سکھانا ہے کہ نبی ﷺ کا خاندان اور عموم صحابہ ایک امانت ہیں، دو فوجیں نہیں۔""",
    """हसन व हुसैन رضي الله عنهما तिर्मिज़ी वग़ैरह की हदीस में जन्नती नौजवानों के सरदार कहे गए। अली व फ़ातिमा के घर नाना ﷺ की नज़र में पले। अहले बैत से सुन्नी मुहब्बत अबू बक्र, उमर या उस्मान رضي الله عنهم से बुग़ज़ की शर्त नहीं रखती। बहुत से मुल्कों में नमाज़ के बाद दरूद में उनके नाम आते हैं।

कुरआन, क़ज़ा और सुन्नत का अली का इल्म उन्हें कूफ़ा के फ़ुक़हा का मर्जअ बना। उनसे मन्सूब ख़ुत्बे और विरासत, हुदूद, जिहाद के फतवे फैले। सनदें मुख़्तलिफ़ ताक़त की हैं; सुन्नी रविश हर रिवायत को तौलना है। पुख़्ता बात यह है कि नबी ﷺ ने अली के फ़ैसले की दुआ की और सहाबा मुश्किल सवाल पूछते। बलाग़त और ज़ुहद उनकी यादगार गुफ़्तगू के मुस्तक़िल मज़ामीन हैं।

अली की शहादत 40 हिजरी के बाद हसन رضي الله عنه को कूफ़ा में मुख़्तसर खिलाफ़त की बैअत हुई। ख़ानाजंगी जारी रहने का ख़तरा था। 41 हिजरी / 661 ई. में उन्होंने मुआविया رضي الله عنه के हक़ में इख़्तियार छोड़ा ताकि मुसलमानों का ख़ून बचे। साल आम अल-जमाआ कहलाया, इज्तिमाअ का साल। हसन का यह फे'ल सुन्नी तारीख़ में नबी ﷺ की उस बात की तक्मील है कि उनकी औलाद दो बड़े गिरोहों में सुलह कराएगी।

इस सुलह को उमूमन ख़ुलफ़ा-ए-राशिदीन के सियासी सिलसिले का ख़ातिमा माना जाता है: अबू बक्र, उमर, उस्मान, अली, और हसन की मुख़्तसर मुद्दत। मुआविया की बाद की हुकूमत बहुत से सुन्नी मुतकल्लिमीन मुल्क कहते हैं, मगर वह सहाबी हैं जिन्होंने वही लिखी, गाली के नहीं। राशिदीन के ख़ास दर्जे और बाद के सहाबा को न कोसने की यह तफ़रीक़ मेयारी है।

अहले सुन्नत के इस्तेमाल में अहले बैत अज़वाज-ए-नबी ﷺ, अली, फ़ातिमा, हसन, हुसैन और वसीअतर बनू हाशिम को शामिल हैं। आयत 33:33 और हदीस-ए-तत्हीर तफ़सीर में इज़्ज़त के साथ समझी जाती हैं बिना फ़िर्कावाराना हथियार बनाए। इस घर से तफ़सीर, फ़िक़्ह और अदब में इल्म बहा।

हसन की सुलह ने जमल या सिफ़्फ़ीन का ग़म मिटा नहीं दिया; बाक़ी सहाबा में मज़ीद क़त्ल का दरवाज़ा बंद किया। हुसैन का बाद का करबला 61 हिजरी अगली नस्ल का है, सुन्नी और अन्य तवारीख़ में ग़म से याद होता है, बिना अव्वल दर्जे के सहाबा पर सब की इजाज़त दिए। अली के इल्म वाले बाब इसलिए इत्तिहाद और ज़ब्त पर ख़त्म होते हैं।

अहले सुन्नत का धारा चार रौशनियाँ इकट्ठी पकड़ता है: अली की फ़िक़्ह, फ़ातिमा की तहारत, हसन की सुलह, हुसैन की शुजाअत, सब कलिमे के नीचे और पहले तीन ख़ुलफ़ा के एहतिराम के नीचे। अली सिखाना यह सिखाना है कि नबी ﷺ का ख़ानदान और उमूम सहाबा एक अमानत हैं, दो फ़ौजें नहीं।""",
    """হাসান ও হুসাইন رضي الله عنهما তিরমিযি প্রভৃতির হাদিসে জান্নাতের যুবকদের সরদার বলা হয়েছে। তাঁরা আলী ও ফাতিমার ঘরে দাদা ﷺ-এর দৃষ্টিতে বেড়ে ওঠেন। আহলুল বায়তের প্রতি সুন্নি ভালোবাসা আবু বকর, উমর বা উসমান رضي الله عنهم-এর প্রতি ঘৃণার শর্ত রাখে না। অনেক দেশে সালাতের পর দরুদে তাঁদের নাম আসে।

কুরআন, কাজা ও সুন্নাত সম্পর্কে আলীর ইলম তাঁকে কুফার ফকিহদের মারজা করে। তাঁর আরোপিত খুতবা এবং মীরাস, হুদুদ, জিহাদের ফতোয়া ছড়িয়ে পড়ে। সনদের শক্তি ভিন্ন; সুন্নি পদ্ধতি প্রতিটি বর্ণনা ওজন করা। দৃঢ় কথা এই যে নবী ﷺ আলীর ফয়সালার দোয়া করেন এবং সাহাবিরা কঠিন প্রশ্ন করেন। বাগ্মিতা ও যুহদ তাঁর স্মরণীয় বক্তব্যের স্থায়ী বিষয়।

আলীর শাহাদাত ৪০ হিজরির পর হাসান رضي الله عنه-কে কুফায় সংক্ষিপ্ত খিলাফতের বাইআত দেওয়া হয়। গৃহযুদ্ধ চলার আশঙ্কা ছিল। ৪১ হিজরি / ৬৬১ খ্রি. তিনি মুয়াবিয়া رضي الله عنه-এর অনুকূলে ক্ষমতা ছেড়ে দেন যাতে মুসলিম রক্ত রক্ষা পায়। বছরটি আম আল-জামাআহ নামে খ্যাত, সম্প্রদায়ের বছর। হাসানের এই কাজ সুন্নি ইতিহাসে নবী ﷺ-এর সেই বাণীর পূর্ণতা যে তাঁর সন্তান দুই বড় দলের মধ্যে সন্ধি করাবে।

এই সন্ধিকে সাধারণত রাশিদুন খলিফাদের রাজনৈতিক ধারার সমাপ্তি গণ্য করা হয়: আবু বকর, উমর, উসমান, আলী এবং হাসানের সংক্ষিপ্ত কাল। মুয়াবিয়ার পরবর্তী শাসন অনেক সুন্নি মুতাকাল্লিম মুলক বলেন, তবু তিনি সাহাবি যিনি ওহি লিখেছেন, গালির পাত্র নন। রাশিদুনের বিশেষ মর্যাদা এবং পরবর্তী সাহাবিদের নিন্দা না করার এই পার্থক্য মানক।

আহলুস সুন্নাহর ব্যবহারে আহলুল বায়ত নবীর ﷺ স্ত্রীগণ, আলী, ফাতিমা, হাসান, হুসাইন এবং বিস্তৃততর বনু হাশিমকে অন্তর্ভুক্ত করে। আয়াত ৩৩:৩৩ ও তাহারার হাদিস তাফসিরে সম্মানের সঙ্গে ব্যাখ্যাত হয়, সাম্প্রদায়িক অস্ত্র না বানিয়ে। এই ঘর থেকে তাফসির, ফিকহ ও আদবে ইলম প্রবাহিত হয়।

হাসানের সন্ধি জামাল বা সিফফিনের দুঃখ মুছে দেয়নি; অবশিষ্ট সাহাবিদের মধ্যে আরও হত্যার দুয়ার বন্ধ করে। হুসাইনের পরবর্তী কারবালা ৬১ হিজরি পরবর্তী প্রজন্মের, সুন্নি ও অন্য ইতিহাসে শোকে স্মরণীয়, প্রথম সারির সাহাবিদের গালি দেওয়ার অনুমতি ছাড়া। আলীর ইলমের অধ্যায় তাই ঐক্য ও সংযমে শেষ হয়।

আহলুস সুন্নাহর ধারা চার আলো একত্রে ধরে: আলীর ফিকহ, ফাতিমার পবিত্রতা, হাসানের সন্ধি, হুসাইনের সাহস, সব কালিমার নিচে এবং প্রথম তিন খলিফার সম্মানের নিচে। আলী শেখানো মানে শেখানো যে নবী ﷺ-এর পরিবার ও সাহাবিদের সাধারণতা এক আমানত, দুই সেনা নয়।""",
    """Al-Hasan dan al-Husain رضي الله عنهما disebut pemuka pemuda surga dalam hadis yang dicatat at-Tirmidzi dan lainnya. Mereka tumbuh di rumah Ali dan Fatimah di bawah pandangan kakek mereka ﷺ. Cinta Ahlusunah kepada mereka adalah bagian dari cinta kepada Ahlulbait, tanpa klaim bahwa cinta ini mensyaratkan kebencian kepada Abu Bakar, Umar, atau Utsman رضي الله عنهم. Nama mereka disebut dalam selawat setelah salat di banyak negeri.

Ilmu Ali tentang Al-Qur'an, qada, dan sunah menjadikannya rujukan fukaha Kufah. Khutbah yang dinisbahkan kepadanya, dan fatwa tentang waris, hudud, dan jihad, beredar luas. Sanad beragam kekuatannya; metode Ahlusunah adalah menimbang setiap riwayat. Yang kokoh adalah bahwa Nabi ﷺ mendoakan keputusan Ali dan bahwa para Sahabat menanyainya soal sulit. Kefasihan dan zuhud adalah tema tetap dalam ucapannya yang dikenang.

Setelah Ali wafat pada 40 H, al-Hasan رضي الله عنه dibaiat di Kufah sebagai khalifah untuk waktu singkat. Perang saudara mengancam berlanjut. Pada 41 H / 661 M ia menyerahkan wewenang kepada Muawiyah رضي الله عنه dalam perdamaian yang menyelamatkan darah muslim. Tahun itu disebut 'am al-jama'ah, tahun jamaah. Tindakan Hasan dipuji dalam sejarah Ahlusunah sebagai penunaian sabda Nabi ﷺ bahwa seorang putranya akan mendamaikan dua kelompok besar kaum muslimin.

Perdamaian itu biasa dihitung sebagai akhir era Khulafaur Rasyidin sebagai urutan politik: Abu Bakar, Umar, Utsman, Ali, dan masa singkat Hasan. Pemerintahan Muawiyah kemudian dipandang banyak teolog Ahlusunah sebagai kerajaan (mulk), sementara ia tetap Sahabat yang menulis wahyu dan tidak boleh dicela. Pembedaan ini—antara martabat khusus Rasyidin dan kewajiban tidak mencela Sahabat kemudian—adalah baku.

Ahlulbait dalam pemakaian Ahlusunah mencakup istri-istri Nabi ﷺ, Ali, Fatimah, Hasan, dan Husain, dan secara lebih luas Bani Hasyim. Ayat 33:33 dan hadis pensucian dijelaskan dalam tafsir tanpa mengosongkan kehormatan dan tanpa menjadikannya senjata sektarian. Ilmu mengalir dari rumah ini ke tafsir, fikih, dan adab.

Perdamaian Hasan tidak menghapus duka Shiffin atau Jamal; ia menutup pintu pembantaian lebih lanjut di antara Sahabat yang tersisa. Pendirian Husain kemudian di Karbala pada 61 H termasuk generasi berikutnya dan dikenang dengan duka dalam sejarah Ahlusunah maupun lainnya, tanpa memberi izin mencela Sahabat tingkat pertama. Ensiklopedia butir Ali tentang ilmu karena itu berakhir dengan persatuan dan penahanan diri.

Arus utama Ahlusunah dengan demikian memegang empat cahaya bersama: fikih Ali, kesucian Fatimah, sulh Hasan, dan keberanian Husain, semua di bawah syahadat dan di bawah penghormatan kepada tiga khalifah pertama. Mengajar Ali berarti mengajar bahwa keluarga Nabi ﷺ dan keumuman Sahabat adalah satu amanah, bukan dua pasukan.""",
)

# --- 5 Hamzah ibn Abd al-Muttalib ---
ch = chapter(5)
ch["details"] = D(
    """Hamzah ibn Abd al-Muttalib ibn Hashim رضي الله عنه was a paternal uncle of the Prophet ﷺ, a few years older, of Banu Hashim. Ibn Sa'd and Ibn Hisham describe him as a hunter, a man of physical power, and among the nobles of Makkah before Islam. His mother was Halah bint Wuhayb, so that the Prophet ﷺ and Hamzah were related through Abd al-Muttalib. He was called Asad Allah and Asad Rasul Allah, the Lion of Allah and of His Messenger.

He accepted Islam in Makkah after a confrontation with Abu Jahl, who had insulted the Prophet ﷺ. When Hamzah heard, he struck Abu Jahl in the Haram and declared that he was upon the religion of Muhammad ﷺ. His conversion, in the years when Muslims were few and hidden, greatly strengthened the community. Ibn Ishaq notes that Quraysh became more cautious in harming the Prophet ﷺ once Hamzah stood with him. The weak of Makkah felt a shield had been raised.

He migrated to Madinah and fought at Badr in 2 AH / 624 CE. There he was among those who killed leading men of Quraysh, including Utbah ibn Rabi'ah, father of Hind bint Utbah, in the reports of the duel that opened the battle. Badr's dead planted a vow of revenge in some houses of Makkah. Hamzah's valour at Badr is not denied in any early maghazi work.

At Uhud in Shawwal 3 AH / March 625 CE he fought in the front until Wahshi ibn Harb, an Abyssinian enslaved in Makkah, killed him with a spear, having been promised freedom by Jubayr ibn Mut'im if he slew Hamzah, who had killed Jubayr's uncle at Badr. The Prophet ﷺ found his uncle's body and wept. He named him Sayyid al-Shuhada, Master of the Martyrs. That title in Sunni usage is Hamzah's special honour among the dead of Uhud.

The Prophet ﷺ prayed over him and the other martyrs of Uhud in reports that vary in number of takbir, and he forbade at first that they be washed, saying they would be raised with their wounds the colour of blood and the scent of musk, as in Bukhari. Hamzah was buried at the foot of Uhud with his companions. The grave at Uhud remained a place of visitation and reminder for the people of Madinah.

His Islam, his protection of the Messenger ﷺ in Makkah, his stand at Badr, and his martyrdom at Uhud form a short, bright life. He did not live to see the Conquest of Makkah. Classical sirah does not pad his years with later politics; it leaves him on the mountain as the uncle who died for the nephew who was a prophet. Ahl al-Sunnah mention him with رضي الله عنه and with tears, not with sectarian argument.

Later generations remembered Hamzah when they spoke of courage without cruelty in the cause of tawhid. The Prophet's ﷺ grief over him taught the ummah that even the strongest of Banu Hashim could fall, and that martyrdom was not a slogan but a body on the slope of Uhud. Encyclopedias of the Sahaba therefore give him a chapter among the uncles, beside al-Abbas who lived longer, as the one who went first to Allah.""",
    """حمزہ بن عبد المطلب بن ہاشم رضی اللہ عنہ نبی ﷺ کے چچا تھے، چند برس بڑے، بنو ہاشم سے۔ ابن سعد و ابن ہشام انہیں شکاری، جسمانی قوت والے، اسلام سے پہلے مکہ کے اشراف میں بیان کرتے ہیں۔ والدہ ہالہ بنت وہیب، یوں نبی ﷺ اور حمزہ عبد المطلب سے رشتہ رکھتے تھے۔ اسد اللہ اور اسد رسول اللہ کہلائے، اللہ اور اس کے رسول کے شیر۔

مکہ میں ابو جہل سے مقابلے کے بعد اسلام لائے، جس نے نبی ﷺ کو برا کہا تھا۔ سن کر حرم میں ابو جہل کو مارا اور اعلان کیا کہ محمد ﷺ کے دین پر ہیں۔ ایمان، جب مسلمان کم اور پوشیدہ تھے، جماعت کو بہت قوت دی۔ ابن اسحاق لکھتے ہیں حمزہ ساتھ کھڑے ہوئے تو قریش نبی ﷺ کو تکلیف دینے میں محتاط ہو گئے۔ مکہ کے کمزوروں کو ڈھال محسوس ہوئی۔

مدینہ ہجرت کی اور 2ھ / 624ء بدر میں لڑے۔ وہاں قریش کے سردار مارے جانے والوں میں رہے، بشمول عتبہ بن ربیعہ، ہند بنت عتبہ کے باپ، جنگ کھولنے والے مبارزے کی روایات میں۔ بدر کے مقتولوں نے مکہ کے بعض گھروں میں انتقام کی قسم بوئی۔ بدر پر حمزہ کی بہادری کسی متقدم مغازی میں نہیں جھلائی جاتی۔

شوال 3ھ / مارچ 625ء احد میں آگے لڑے یہاں تک کہ وحشی بن حرب، مکہ کا حبشی غلام، نیزے سے شہید کر گیا؛ جبیر بن مطعم نے آزادی کا وعدہ کیا تھا اگر حمزہ کو مارے، جنہوں نے بدر میں جبیر کے چچا مارے تھے۔ نبی ﷺ نے چچا کی لاش دیکھی اور روئے۔ سید الشہداء فرمایا، شہیدوں کے سردار۔ اہل سنت کے استعمال میں احد کے مقتولوں میں یہ خاص شرف حمزہ کا ہے۔

نبی ﷺ نے ان پر اور احد کے دیگر شہدا پر نماز پڑھی، تکبیروں کی تعداد میں روایات مختلف، اور پہلے غسل سے منع فرمایا، بخاری کے مطابق زخموں کے رنگ خون اور بو مشک کے ساتھ اٹھیں گے۔ حمزہ احد کی دامن میں ساتھیوں کے ساتھ دفن ہوئے۔ احد کی قبر اہل مدینہ کے لیے زیارت اور نصیحت کی جگہ رہی۔

اسلام، مکہ میں رسول ﷺ کی حمایت، بدر کا قیام، احد کی شہادت ایک مختصر روشن زندگی بنتی ہے۔ فتح مکہ نہ دیکھی۔ کلاسیکی سیرت بعد کی سیاست سے ان کے برس نہیں بھرتی؛ پہاڑ پر چچا چھوڑتی ہے جو نبی بھتیجے کے لیے مرا۔ اہل سنت رضی اللہ عنہ اور آنسوؤں سے یاد کرتے ہیں، فرقہ وارانہ بحث سے نہیں۔

بعد کی نسلیں توحید کی راہ میں بے رحم نہ ہونے والی شجاعت پر حمزہ یاد کرتیں۔ نبی ﷺ کا غم سکھاتا ہے کہ بنو ہاشم کا سب سے طاقتور بھی گر سکتا ہے، اور شہادت نعرہ نہیں احد کی ڈھلوان پر جسم ہے۔ اس لیے صحابہ کے دائرۃ المعارف انہیں چچاؤں میں باب دیتے ہیں، عباس کے ساتھ جو زیادہ جیے، اس کے طور پر جو اللہ کی طرف پہلے گئے۔""",
    """हमज़ा इब्न अब्दुल मुत्तलिब इब्न हाशिम رضي الله عنه नबी ﷺ के चाचा थे, कुछ बरस बड़े, बनू हाशिम से। इब्न साद व इब्न हिशाम उन्हें शिकारी, जिस्मानी क़ुव्वत वाले, इस्लाम से पहले मक्का के अशराफ़ में बयान करते हैं। वालिदा हालह बिन्त वुहैब, यूँ नबी ﷺ और हमज़ा अब्दुल मुत्तलिब से रिश्ता रखते थे। असदुल्लाह और असद रसूलिल्लाह कहलाए, अल्लाह और उसके रसूल के शेर।

मक्का में अबू जहल से मुक़ाबले के बाद इस्लाम लाए, जिसने नबी ﷺ को बुरा कहा था। सुन कर हरम में अबू जहल को मारा और एलान किया कि मुहम्मद ﷺ के दीन पर हैं। ईमान, जब मुसलमान कम और पोशीदा थे, जमाअत को बहुत क़ुव्वत दी। इब्न इसहाक लिखते हैं हमज़ा साथ खड़े हुए तो कुरैश नबी ﷺ को तकलीफ़ देने में मुहतति हो गए। मक्का के कमज़ोरों को ढाल महसूस हुई।

मदीना हिजरत की और 2 हिजरी / 624 ई. बद्र में लड़े। वहाँ कुरैश के सरदार मारे जाने वालों में रहे, बशमूल उतबा बिन रबीआ, हिन्द बिन्त उतबा के बाप, जंग खोलने वाले मुबारिज़े की रिवायात में। बद्र के मक़तूलों ने मक्का के कुछ घरों में इंतिक़ाम की क़सम बोई। बद्र पर हमज़ा की बहादुरी किसी मुतक़द्दिम मग़ाज़ी में नहीं झुठलाई जाती।

शव्वाल 3 हिजरी / मार्च 625 ई. उहुद में आगे लड़े यहाँ तक कि वह्शी बिन हर्ब, मक्का का हबशी ग़ुलाम, नेज़े से शहीद कर गया; जुबैर बिन मुतइम ने आज़ादी का वादा किया था अगर हमज़ा को मारे, जिन्होंने बद्र में जुबैर के चाचा मारे थे। नबी ﷺ ने चाचा की लाश देखी और रोए। सय्यिदुश शुहदा फ़रमाया, शहीदों के सरदार। अहले सुन्नत के इस्तेमाल में उहुद के मक़तूलों में यह ख़ास शرف हमज़ा का है।

नबी ﷺ ने उन पर और उहुद के अन्य शुहदा पर नमाज़ पढ़ी, तक्बीरों की तादाद में रिवायात मुख़्तलिफ़, और पहले ग़ुस्ल से मना फ़रमाया, बुख़ारी के मुताबिक ज़ख़्मों के रंग ख़ून और बू मुश्क के साथ उठेंगे। हमज़ा उहुद की दामन में साथियों के साथ दफ़न हुए। उहुद की क़ब्र अहले मदीना के लिए ज़ियारत और नसीहत की जगह रही।

इस्लाम, मक्का में रसूल ﷺ की हिमायत, बद्र का क़ियाम, उहुद की शहादत एक मुख़्तसर रौशन ज़िंदगी बनती है। फत्हे मक्का न देखी। क्लासिकी सीरत बाद की सियासत से उनके बरस नहीं भरती; पहाड़ पर चाचा छोड़ती है जो नबी भतीजे के लिए मरा। अहले सुन्नत رضي الله عنه और आँसुओं से याद करते हैं, फ़िर्कावाराना बहस से नहीं।

बाद की नस्लें तौहीद की राह में बे रहम न होने वाली शुजाअत पर हमज़ा याद करतीं। नबी ﷺ का ग़म सिखाता है कि बनू हाशिम का सबसे ताक़तवर भी गिर सकता है, और शहादत नारा नहीं उहुद की ढलान पर जिस्म है। इसलिए सहाबा के दाइरतुल मआरिफ़ उन्हें चाचाओं में बाब देते हैं, अब्बास के साथ जो ज़्यादा जिए, उस के तौर पर जो अल्लाह की तरफ़ पहले गए।""",
    """হামজাহ ইবন আব্দুল মুত্তালিব ইবন হাশিম رضي الله عنه নবী ﷺ-এর চাচা, কয়েক বছরের বড়, বনু হাশিমের। ইবন সাদ ও ইবন হিশাম তাঁকে শিকারি, শারীরিক শক্তির অধিকারী, ইসলামের আগে মক্কার অভিজাতদের মধ্যে বর্ণনা করেন। মাতা হালাহ বিনত উহাইব, এভাবে নবী ﷺ ও হামজাহ আব্দুল মুত্তালিবের সূত্রে সম্পর্কিত। তিনি আসাদুল্লাহ ও আসাদু রাসূলিল্লাহ নামে খ্যাত, আল্লাহ ও তাঁর রাসূলের সিংহ।

আবু জাহলের সঙ্গে সংঘর্ষের পর মক্কায় ইসলাম গ্রহণ করেন, যে নবী ﷺ-কে অপমান করেছিল। শুনে হারামে আবু জাহলকে আঘাত করেন এবং ঘোষণা করেন তিনি মুহাম্মদ ﷺ-এর দীনে। তাঁর ইমান, যখন মুসলিম কম ও গোপন, সম্প্রদায়কে বহু শক্তি দেয়। ইবন ইসহাক লেখেন হামজাহ পাশে দাঁড়ালে কুরাইশ নবী ﷺ-কে কষ্ট দিতে সাবধান হয়। মক্কার দুর্বলেরা ঢাল অনুভব করে।

তিনি মদিনায় হিজরত করেন এবং ২ হিজরি / ৬২৪ খ্রি. বদরে যুদ্ধ করেন। সেখানে কুরাইশের নেতা নিহতদের মধ্যে ছিলেন, উতবা ইবন রবিআহ—হিন্দ বিনত উতবার পিতা—যুদ্ধ খোলা দ্বন্দ্বের বর্ণনায়। বদরের নিহতেরা মক্কার কিছু ঘরে প্রতিশোধের শপথ বোনে। বদরে হামজাহর বীরত্ব কোনো প্রাথমিক মাগাজিতে অস্বীকৃত নয়।

শাওয়াল ৩ হিজরি / মার্চ ৬২৫ খ্রি. উহুদে সামনে যুদ্ধ করেন যে পর্যন্ত ওয়াহশি ইবন হারব, মক্কার এক হাবশি দাস, বর্শা দিয়ে তাঁকে শহীদ করে; জুবায়র ইবন মুতিম মুক্তির প্রতিশ্রুতি দিয়েছিলেন যদি হামজাহকে হত্যা করে, যিনি বদরে জুবায়রের চাচাকে হত্যা করেছিলেন। নবী ﷺ চাচার দেহ দেখে কাঁদেন। তাঁকে সাইয়িদুশ শুহাদা বলেন, শহীদদের সরদার। আহলুস সুন্নাহর ব্যবহারে উহুদের নিহতদের মধ্যে এই বিশেষ সম্মান হামজাহর।

নবী ﷺ তাঁর ও উহুদের অন্য শহীদদের উপর নামাজ পড়েন, তাকবিরের সংখ্যায় বর্ণনা ভিন্ন, এবং প্রথমে গোসল নিষেধ করেন; বুখারি অনুসারে তাঁরা ক্ষত রক্তবর্ণ ও কস্তूरीগন্ধে উত্থিত হবেন। হামজাহ উহুদের পাদদেশে সঙ্গীদের সঙ্গে দাফন হন। উহুদের কবর মদিনাবাসীর জন্য যিয়ারত ও উপদেশের স্থান থাকে।

তাঁর ইসলাম, মক্কায় রাসূল ﷺ-এর সুরক্ষা, বদরের অবস্থান ও উহুদের শাহাদাত একটি সংক্ষিপ্ত উজ্জ্বল জীবন গড়ে। মক্কা বিজয় তিনি দেখেননি। ক্লাসিক সিরাত পরবর্তী রাজনীতি দিয়ে তাঁর বছর ভরে না; পাহাড়ে চাচাকে রাখে যিনি নবী ভাইপোর জন্য মারা যান। আহলুস সুন্নাহ رضي الله عنه ও অশ্রু দিয়ে স্মরণ করে, সাম্প্রদায়িক তর্ক দিয়ে নয়।

পরবর্তী প্রজন্ম তাওহিদের পথে নিষ্ঠুরতাহীন সাহসে হামজাহ স্মরণ করে। নবী ﷺ-এর শোক শেখায় বনু হাশিমের সবচেয়ে শক্তিশালীও পড়তে পারে, এবং শাহাদাত স্লোগান নয় উহুদের ঢালে দেহ। তাই সাহাবা বিশ্বকোষ তাঁকে চাচাদের মধ্যে অধ্যায় দেয়, আব্বাসের পাশে যিনি দীর্ঘজীবী, সেইজন হিসেবে যিনি আল্লাহর দিকে আগে গেলেন।""",
    """Hamzah bin Abdul Muththalib bin Hasyim رضي الله عنه adalah paman Nabi ﷺ dari pihak ayah, beberapa tahun lebih tua, dari Bani Hasyim. Ibnu Sa'd dan Ibnu Hisyam menggambarkannya sebagai pemburu, lelaki berkekuatan tubuh, dan termasuk pemuka Makkah sebelum Islam. Ibunya Halah binti Wuhayb, sehingga Nabi ﷺ dan Hamzah berkerabat melalui Abdul Muththalib. Ia disebut Asadullah dan Asad Rasulullah, Singa Allah dan Rasul-Nya.

Ia masuk Islam di Makkah setelah konfrontasi dengan Abu Jahal, yang telah menghina Nabi ﷺ. Ketika Hamzah mendengar, ia memukul Abu Jahal di Haram dan menyatakan bahwa ia berada di atas agama Muhammad ﷺ. Keislamannya, pada tahun-tahun ketika muslim sedikit dan tersembunyi, sangat menguatkan jamaah. Ibnu Ishaq mencatat bahwa Quraisy menjadi lebih hati-hati menyakiti Nabi ﷺ setelah Hamzah berdiri bersamanya. Orang lemah di Makkah merasakan perisai telah diangkat.

Ia hijrah ke Madinah dan berperang di Badar pada 2 H / 624 M. Di sana ia termasuk yang membunuh pemuka Quraisy, termasuk Utbah bin Rabi'ah, ayah Hind binti Utbah, dalam riwayat duel yang membuka pertempuran. Orang mati Badar menanam nazar balas di sebagian rumah Makkah. Keberanian Hamzah di Badar tidak diingkari dalam karya maghazi awal mana pun.

Di Uhud pada Syawal 3 H / Maret 625 M ia berperang di depan hingga Wahsyi bin Harb, seorang Habasyah yang diperbudak di Makkah, membunuhnya dengan tombak, setelah dijanjikan kemerdekaan oleh Jubair bin Muth'im jika ia membunuh Hamzah, yang telah membunuh paman Jubair di Badar. Nabi ﷺ menemukan jenazah pamannya dan menangis. Beliau menamainya Sayyidusy Syuhada, Pemuka Para Syuhada. Gelar itu dalam pemakaian Ahlusunah adalah kemuliaan khusus Hamzah di antara yang gugur di Uhud.

Nabi ﷺ menyalatkan dia dan syuhada Uhud lainnya dalam riwayat yang berbeda jumlah takbirnya, dan mula-mula melarang mereka dimandikan, dengan bersabda mereka akan dibangkitkan dengan luka berwarna darah dan bau kesturi, sebagaimana dalam Bukhari. Hamzah dimakamkan di kaki Uhud bersama sahabat-sahabatnya. Kubur di Uhud tetap tempat ziarah dan peringatan bagi penduduk Madinah.

Islamnya, perlindungannya kepada Rasul ﷺ di Makkah, pendiriannya di Badar, dan syahidnya di Uhud membentuk hidup singkat yang terang. Ia tidak hidup untuk melihat Fathu Makkah. Sirah klasik tidak mengisi tahunnya dengan politik kemudian; ia meninggalkannya di gunung sebagai paman yang mati bagi keponakan yang nabi. Ahlusunah menyebutnya dengan رضي الله عنه dan dengan air mata, bukan dengan argumen sektarian.

Generasi kemudian mengingat Hamzah ketika berbicara tentang keberanian tanpa kekejaman di jalan tauhid. Duka Nabi ﷺ atasnya mengajar umat bahwa yang terkuat dari Bani Hasyim pun dapat gugur, dan bahwa syahid bukan slogan melainkan tubuh di lereng Uhud. Ensiklopedia Sahabat karena itu memberinya bab di antara para paman, di samping al-Abbas yang hidup lebih lama, sebagai yang lebih dulu pergi kepada Allah.""",
)
ch["items"][0]["details"] = D(
    """Uhud in 3 AH was a trial after the victory of Badr. Quraysh came with a larger host; Hind bint Utbah had vowed revenge for her father Utbah, her brother, and others slain at Badr. She urged Wahshi to kill Hamzah specifically. The early sirah of Ibn Ishaq, as edited by Ibn Hisham, tells this without delight in gore and without hiding that grief reached the Prophet ﷺ.

Wahshi later described, in reports recorded by Bukhari and others, how he waited for Hamzah, threw the spear, and fled when the Lion of Allah fell. After the battle, some of the dead of Uhud were mutilated in the custom of that jahili revenge. The Prophet ﷺ was deeply pained at what was done to his uncle. Sunni books mention this as a historical wound, not as an excuse for later hatred of Hind, who accepted Islam at the Conquest of Makkah.

When Wahshi accepted Islam after Fath Makkah, the Prophet ﷺ forgave him. Wahshi himself stayed away from the Messenger's ﷺ face out of shame, and later fought Musaylimah at Yamamah, saying he hoped the spear that killed Hamzah would also kill the liar. That arc—from the killer of Hamzah to a Muslim soldier of the Riddah—is told in Sunni history as a proof of the wideness of tawbah, not as a belittling of Hamzah's rank.

Hamzah was buried at Uhud and remains there. Visitors to Madinah still go to the mountain and the graves of the shuhada. The Prophet ﷺ later passed Uhud and said it is a mountain that loves us and that we love, in a famous report. Hamzah's name is tied to that slope more than to any later city.

The lesson drawn by Ahl al-Sunnah is that martyrdom may come from an unexpected hand, that the Prophet ﷺ wept for kin, and that forgiveness after Islam closed a blood feud that jahiliyya would have kept open for generations. Wahshi is not celebrated above Hamzah; Hamzah is not used to curse those who later believed.

Hind's revenge belonged to the ethics of the old vendetta. Islam redirected honour toward sabr and toward the akhirah. The women of the Ansar who went out to Uhud, and Fatimah who later washed the Prophet's ﷺ wounds, stand in the same chapter of sacrifice as Hamzah's death. The mountain holds both the uncle and the memory of the wounded Messenger ﷺ.

Thus the item on Uhud in a Sahaba encyclopedia is not a war-boast. It is a record of a spear, a burial, a pardon, and a title—Sayyid al-Shuhada—that the ummah still recites when it lists the beloved dead of the first generation رضي الله عنهم.""",
    """احد 3ھ بدر کی فتح کے بعد آزمائش تھی۔ قریش بڑی فوج لے کر آئے؛ ہند بنت عتبہ نے باپ عتبہ، بھائی اور بدر کے دیگر مقتولوں کا انتقام قسم کھایا تھا۔ وحشی کو خاص حمزہ مارنے پر اکسایا۔ ابن اسحاق کی سیرت ابن ہشام کی تہذیب میں یہ بیان خونریزی کی لذت کے بغیر ہے اور اس غم کو نہیں چھپاتی جو نبی ﷺ تک پہنچا۔

وحشی نے بعد میں بخاری وغیرہ کی روایات میں بیان کیا کیسے حمزہ کا انتظار کیا، نیزہ پھینکا، اور اسد اللہ گرے تو بھاگا۔ جنگ کے بعد احد کے بعض مقتولوں کے ساتھ جاہلی انتقام کی رسم میں مثلہ ہوئی۔ نبی ﷺ چچا کے ساتھ جو ہوا اس پر سخت رنجیدہ ہوئے۔ سنی کتابیں اسے تاریخی زخم کہتی ہیں، ہند سے بعد کی نفرت کا بہانہ نہیں، جو فتح مکہ پر اسلام لائیں۔

فتح مکہ کے بعد وحشی اسلام لائے تو نبی ﷺ نے معاف فرمایا۔ وحشی خود شرم سے رسول ﷺ کے چہرے سے دور رہے، بعد میں یمامہ مسیلمہ سے لڑے، کہا امید ہے نیزہ جس نے حمزہ مارا جھوٹے کو بھی مارے۔ یہ قوس—حمزہ کے قاتل سے ردّہ کے مسلمان سپاہی تک—سنی تاریخ میں توبہ کی وسعت کی دلیل ہے، حمزہ کے درجے کی تخفیف نہیں۔

حمزہ احد میں دفن ہوئے اور وہیں ہیں۔ مدینہ کے زائر پہاڑ اور شہدا کی قبروں پر آج بھی جاتے ہیں۔ نبی ﷺ بعد میں احد سے گزرے اور فرمایا یہ پہاڑ ہم سے محبت کرتا ہے ہم اس سے، مشہور روایت میں۔ حمزہ کا نام کسی بعد کے شہر سے زیادہ اس ڈھلوان سے بندھا ہے۔

اہل سنت کا سبق یہ ہے کہ شہادت اچانک ہاتھ سے آ سکتی ہے، نبی ﷺ رشتے پر روئے، اور اسلام کے بعد معافی نے خون کا جھگڑا بند کیا جو جاہلیت نسلوں تک کھلا رکھتی۔ وحشی کو حمزہ پر فوقیت نہیں؛ حمزہ سے بعد میں ایمان لانے والوں کو کوسا نہیں جاتا۔

ہند کا انتقام پرانی خون ریزی کی اخلاق سے تھا۔ اسلام عزت کو صبر اور آخرت کی طرف موڑتا ہے۔ انصار کی وہ عورتیں جو احد نکلیں، اور فاطمہ جنہوں نے بعد میں نبی ﷺ کے زخم دھوئے، حمزہ کی موت کے ساتھ قربانی کے اسی باب میں کھڑی ہیں۔ پہاڑ چچا اور زخمی رسول ﷺ دونوں کی یاد رکھتا ہے۔

یوں صحابہ کے دائرۃ المعارف میں احد کا باب جنگی فخر نہیں۔ نیزے، تدفین، معافی، اور سید الشہداء کے لقب کا ریکارڈ ہے جو امت اب بھی پہلی نسل کے محبوب مقتولین رضی اللہ عنہم گنواتے ہوئے پڑھتی ہے۔""",
    """उहुद 3 हिजरी बद्र की फ़तह के बाद आज़माइश थी। कुरैश बड़ी फ़ौज ले कर आए; हिन्द बिन्त उतबा ने बाप उतबा, भाई और बद्र के अन्य मक़तूलों का इंतिक़ाम क़सम खाया था। वह्शी को ख़ास हमज़ा मारने पर उकसाया। इब्न इसहाक की सीरत इब्न हिशाम की तहज़ीब में यह बयान ख़ूनरेज़ी की लज़्ज़त के बिना है और उस ग़म को नहीं छिपाती जो नबी ﷺ तक पहुँचा।

वह्शी ने बाद में बुख़ारी वग़ैरह की रिवायात में बयान किया कैसे हमज़ा का इंतिज़ार किया, नेज़ा फेंका, और असदुल्लाह गिरे तो भागा। जंग के बाद उहुद के कुछ मक़तूलों के साथ जाहिली इंतिक़ाम की रस्म में मुस्ला हुई। नबी ﷺ चाचा के साथ जो हुआ उस पर सख़्त रंजीदा हुए। सुन्नी किताबें इसे तारीख़ी ज़ख़्म कहती हैं, हिन्द से बाद की नफ़रत का बहाना नहीं, जो फत्हे मक्का पर इस्लाम लाईं।

फत्हे मक्का के बाद वह्शी इस्लाम लाए तो नबी ﷺ ने माफ़ फ़रमाया। वह्शी ख़ुद शर्म से रसूल ﷺ के चेहरे से दूर रहे, बाद में यमामा मुसैलिमा से लड़े, कहा उम्मीद है नेज़ा जिसने हमज़ा मारा झूठे को भी मारे। यह क़ौस—हमज़ा के क़ातिल से रिद्दा के मुस्लिम सिपाही तक—सुन्नी तारीख़ में तौबा की वुसअत की दलील है, हमज़ा के दर्जे की तख़्फ़ीफ़ नहीं।

हमज़ा उहुद में दफ़न हुए और वहीं हैं। मदीना के ज़ाइर पहाड़ और शुहदा की क़ब्रों पर आज भी जाते हैं। नबी ﷺ बाद में उहुद से गुज़रे और फ़रमाया यह पहाड़ हम से मुहब्बत करता है हम उससे, मशहूर रिवायत में। हमज़ा का नाम किसी बाद के शहर से ज़्यादा इस ढलान से बंधा है।

अहले सुन्नत का सबक़ यह है कि शहादत अचानक हाथ से आ सकती है, नबी ﷺ रिश्ते पर रोए, और इस्लाम के बाद माफ़ी ने ख़ून का झगड़ा बंद किया जो जाहिलियत नस्लों तक खुला रखती। वह्शी को हमज़ा पर फ़ौकियत नहीं; हमज़ा से बाद में ईमान लाने वालों को कोसा नहीं जाता।

हिन्द का इंतिक़ाम पुरानी ख़ूनरेज़ी की अख़लाक़ से था। इस्लाम इज़्ज़त को सब्र और आख़िरत की तरफ़ मोड़ता है। अनसार की वह औरतें जो उहुद निकलीं, और फ़ातिमा जिन्होंने बाद में नबी ﷺ के ज़ख़्म धोए, हमज़ा की मौत के साथ क़ुरबानी के उसी बाब में खड़ी हैं। पहाड़ चाचा और ज़ख़्मी रसूल ﷺ दोनों की याद रखता है।

यूँ सहाबा के दाइरतुल मआरिफ़ में उहुद का बाब जंगी फ़ख़्र नहीं। नेज़े, तदफ़ीन, माफ़ी, और सय्यिदुश शुहदा के लक़ब का रिकॉर्ड है जो उम्मत अब भी पहली नस्ल के महबूब मक़तूलीन رضي الله عنهم गिनवाते हुए पढ़ती है।""",
    """উহুদ ৩ হিজরি বদরের বিজয়ের পর পরীক্ষা ছিল। কুরাইশ বৃহত্তর বাহিনী নিয়ে আসে; হিন্দ বিনত উতবা পিতা উতবা, ভাই ও বদরের অন্য নিহতদের প্রতিশোধের শপথ করেছিলেন। তিনি ওয়াহশিকে বিশেষভাবে হামজাহ হত্যায় উসসাহিত করেন। ইবন ইসহাকের সিরাত ইবন হিশামের সম্পাদনায় এ বর্ণনা রক্তপাতের আনন্দ ছাড়া, এবং যে শোক নবী ﷺ-এ পৌঁছেছিল তা না লুকিয়ে।

ওয়াহশি পরে বুখারি প্রভৃতিতে বর্ণনা করেন কীভাবে হামজাহর অপেক্ষা করেন, বর্শা নিক্ষেপ করেন, এবং আসাদুল্লাহ পড়লে পালিয়ে যান। যুদ্ধের পর উহুদের কিছু নিহতের সঙ্গে জাহিলি প্রতিশোধের প্রথায় অঙ্গহানি হয়। নবী ﷺ চাচার সঙ্গে যা হয়েছিল তাতে গভীর কষ্ট পান। সুন্নি গ্রন্থ একে ঐতিহাসিক ক্ষত বলে, হিন্দের প্রতি পরবর্তী ঘৃণার অজুহাত নয়, যিনি মক্কা বিজয়ে ইসলাম গ্রহণ করেন।

মক্কা বিজয়ের পর ওয়াহশি ইসলাম গ্রহণ করলে নবী ﷺ ক্ষমা করেন। ওয়াহশি নিজে লজ্জায় রাসূল ﷺ-এর মুখ থেকে দূরে থাকেন, পরে ইয়ামামায় মুসাইলিমার বিরুদ্ধে যুদ্ধ করেন; বলেন আশা করেন যে বর্শা হামজাহকে মেরেছে মিথ্যাবাদীকেও মারবে। এই চাপ—হামজাহর ঘাতক থেকে রিদ্দার মুসলিম সৈনিক—সুন্নি ইতিহাসে তওবার প্রশস্ততার প্রমাণ, হামজাহর মর্যাদার অবমাননা নয়।

হামজাহ উহুদে দাফন হন এবং সেখানেই আছেন। মদিনার যায়ের আজও পাহাড় ও শহীদদের কবরে যান। নবী ﷺ পরে উহুদ অতিক্রম করে বলেন এটি এমন পাহাড় যা আমাদের ভালোবাসে আমরাও তাকে, প্রসিদ্ধ বর্ণনায়। হামজাহর নাম পরবর্তী কোনো নগরের চেয়ে সেই ঢালের সঙ্গে বাঁধা।

আহলুস সুন্নাহর শিক্ষা এই যে শাহাদাত অপ্রত্যাশিত হাত থেকে আসতে পারে, নবী ﷺ আত্মীয়ের জন্য কেঁদেছেন, এবং ইসলামের পর ক্ষমা রক্তঝগড়া বন্ধ করে যা জাহিলিয়াত প্রজন্মের পর প্রজন্ম খোলা রাখত। ওয়াহশিকে হামজাহর উপর স্থান দেওয়া হয় না; হামজাহ দিয়ে পরে ঈমান আনাদের গালি দেওয়া হয় না।

হিন্দের প্রতিশোধ পুরনো রক্তবৈরিতার নীতি থেকে। ইসলাম সম্মানকে সবর ও আখিরাতের দিকে ঘোরায়। আনসারের যে নারীরা উহুদে বেরিয়েছিলেন, এবং ফাতিমা যিনি পরে নবী ﷺ-এর ক্ষত ধুয়েছিলেন, হামজাহর মৃত্যুর সঙ্গে কুরবানির একই অধ্যায়ে দাঁড়ান। পাহাড় চাচা ও আহত রাসূল ﷺ উভয়ের স্মৃতি রাখে।

এভাবে সাহাবা বিশ্বকোষে উহুদের অধ্যায় যুদ্ধদম্ভ নয়। বর্শা, দাফন, ক্ষমা এবং সাইয়িদুশ শুহাদা উপাধির নথি যা উম্মাহ আজও প্রথম প্রজন্মের প্রিয় নিহত رضي الله عنهم গণনা করে পাঠ করে।""",
    """Uhud pada 3 H adalah ujian setelah kemenangan Badar. Quraisy datang dengan pasukan lebih besar; Hind binti Utbah bernazar membalas ayahnya Utbah, saudaranya, dan orang lain yang terbunuh di Badar. Ia mendesak Wahsyi agar membunuh Hamzah secara khusus. Sirah awal Ibnu Ishaq, sebagaimana diedit Ibnu Hisyam, menuturkan ini tanpa suka pada kekerasan dan tanpa menyembunyikan bahwa duka sampai kepada Nabi ﷺ.

Wahsyi kemudian menggambarkan, dalam riwayat yang dicatat Bukhari dan lainnya, bagaimana ia menunggu Hamzah, melempar tombak, dan lari ketika Singa Allah gugur. Setelah pertempuran, sebagian jenazah Uhud dimutilasi dalam adat balas jahiliah itu. Nabi ﷺ sangat sedih atas apa yang dilakukan kepada pamannya. Kitab Ahlusunah menyebut ini sebagai luka sejarah, bukan alasan kebencian kemudian kepada Hind, yang masuk Islam pada Fathu Makkah.

Ketika Wahsyi masuk Islam setelah Fathu Makkah, Nabi ﷺ memaafkannya. Wahsyi sendiri menjauh dari wajah Rasul ﷺ karena malu, dan kemudian memerangi Musailamah di Yamamah, dengan berkata ia berharap tombak yang membunuh Hamzah juga membunuh si pendusta. Busur itu—dari pembunuh Hamzah menjadi prajurit muslim Riddah—diceritakan dalam sejarah Ahlusunah sebagai bukti luasnya tobat, bukan merendahkan martabat Hamzah.

Hamzah dimakamkan di Uhud dan tetap di sana. Peziarah Madinah masih pergi ke gunung dan kubur para syuhada. Nabi ﷺ kemudian melewati Uhud dan bersabda itu gunung yang mencintai kita dan kita mencintainya, dalam riwayat masyhur. Nama Hamzah terikat pada lereng itu lebih daripada pada kota kemudian mana pun.

Pelajaran yang diambil Ahlusunah adalah bahwa syahid bisa datang dari tangan yang tidak terduga, bahwa Nabi ﷺ menangis karena kerabat, dan bahwa ampunan setelah Islam menutup dendam darah yang jahiliah akan biarkan terbuka turun-temurun. Wahsyi tidak diagungkan di atas Hamzah; Hamzah tidak dipakai untuk mencela orang yang kemudian beriman.

Balas Hind termasuk etika vendetta lama. Islam mengalihkan kehormatan kepada sabar dan kepada akhirat. Wanita Ansar yang keluar ke Uhud, dan Fatimah yang kemudian mencuci luka Nabi ﷺ, berdiri di bab pengorbanan yang sama dengan kematian Hamzah. Gunung itu memegang paman dan ingatan Rasul ﷺ yang terluka.

Dengan demikian butir Uhud dalam ensiklopedia Sahabat bukan pamer perang. Ia catatan tombak, penguburan, maaf, dan gelar—Sayyidusy Syuhada—yang masih dibaca umat ketika merinci orang-orang mati tercinta generasi pertama رضي الله عنهم.""",
)

# --- 6 Bilal ibn Rabah ---
ch = chapter(6)
ch["details"] = D(
    """Bilal ibn Rabah رضي الله عنه was an Abyssinian whose mother is named in the tabaqat as Hamamah. He was a slave in Makkah, associated in many reports with the household of Umayyah ibn Khalaf of Jumah. Ibn Sa'd records his early Islam among the weak who had no clan protection. His blackness and his bondage became, in the Quranic ethic the Prophet ﷺ taught, no barrier to the highest honour of the adhan.

He was tortured for saying that Allah is One. The famous scene is that a great rock was placed on his chest in the heat, and he repeated 'Ahad, Ahad'—One, One—while Umayyah and others demanded that he name the idols. The reports are in the sirah of Ibn Ishaq and in later riyad al-salihin-type collections of virtues. His steadfastness became a proverb of tawhid under pain.

Abu Bakr رضي الله عنه purchased him and set him free, as he freed other slaves who were punished for Islam. The Prophet ﷺ took Bilal into the inner circle of Madinah. When the adhan was legislated after the dream of Abdullah ibn Zayd رضي الله عنه, and after Umar heard similar words, Bilal was chosen as the first mu'adhdhin because of the beauty and carrying power of his voice. He called the five prayers in the Prophet's Mosque.

He fought in the major campaigns and was present at Badr, where his former tormentor Umayyah was killed in the fighting, a fact the maghazi mention without teaching personal vengeance as the heart of the din. At the Conquest of Makkah in 8 AH / 630 CE Bilal climbed the Ka'bah and gave the adhan from its roof, a moment Ibn Hisham and the historians of Fath Makkah record as the reversal of years of humiliation. The weak of the earth called to prayer from the House that Quraysh had locked to idols.

After the Prophet's ﷺ death in 11 AH / 632 CE Bilal could seldom complete the adhan in Madinah; grief stopped his voice, according to well-known reports. He asked Abu Bakr for permission to go out in jihad to Syria. He lived in Sham, in Damascus or nearby according to variant notices in the tabaqat. He died around 17–20 AH (c. 638–641 CE). His grave is visited in Damascus in the famous attribution.

His life is a Sunni proof that taqwa, not colour or nasab, is the measure with Allah. The Prophet ﷺ heard his footsteps in Jannah in a dream reported in Bukhari, a virtue that comforted a man who had owned nothing in Makkah. Encyclopedias place him among the mu'adhdhins and among the freedmen whom Islam raised.

The ummah still hears his name whenever the adhan is taught to children. He is رضي الله عنه in every madhhab of Ahl al-Sunnah. No chapter on Bilal is complete without the rock, the purchase by Abu Bakr, the voice in Madinah, the roof of the Ka'bah, and the silence after the Wafat.""",
    """بلال بن رباح رضی اللہ عنہ حبشی تھے، طبقات میں والدہ حماہ مذکور ہیں۔ مکہ میں غلام، بہت سی روایات میں جمعہ کے امیہ بن خلف کے گھر سے وابستہ۔ ابن سعد انہیں کمزوروں میں شمار کرتے ہیں جنہیں قبیلے کی پناہ نہ تھی۔ سیاہی اور غلامی قرآن کی اس اخلاقیات میں جو نبی ﷺ نے سکھائی اذان کے اعلیٰ شرف میں رکاوٹ نہ بنی۔

اللہ کے ایک کہنے پر تشدد سہا۔ مشہور منظر یہ ہے کہ گرمی میں سینے پر بڑا پتھر رکھا گیا اور وہ احد احد دہراتے رہے—ایک، ایک—جب امیہ وغیرہ بتوں کے نام کا تقاضا کرتے۔ روایات ابن اسحاق کی سیرت اور بعد کی ریاض الصالحین طرز کی کتبِ فضائل میں ہیں۔ درد کے نیچے توحید کی ثابت قدمی ضرب المثل بنی۔

ابو بکر رضی اللہ عنہ نے خرید کر آزاد کیا، جیسا کہ اسلام پر ستائے گئے دیگر غلاموں کو۔ نبی ﷺ نے بلال کو مدینہ کے اندرونی حلقے میں لیا۔ اذان عبد اللہ بن زید رضی اللہ عنہ کے خواب اور عمر کے اسی جیسے کلمات سننے کے بعد مشروع ہوئی تو خوبصورت اور پہنچ والی آواز کی وجہ سے بلال پہلے مؤذن چنے گئے۔ مسجد نبوی میں پانچوں نمازوں کی اذان کہتے۔

بڑی مہموں میں لڑے، بدر میں حاضر، جہاں سابق اذیت دینے والا امیہ لڑائی میں مارا گیا، مغازی یہ ذکر کرتے ہیں بغیر ذاتی انتقام کو دین کا دل بنائے۔ فتح مکہ 8ھ / 630ء پر کعبہ پر چڑھ کر چھت سے اذان دی، ابن ہشام اور فتح مکہ کے مورخ اسے سالوں کی ذلت کے الٹ جانے کا لمحہ لکھتے ہیں۔ زمین کے کمزور نے اس گھر سے نماز کی پکار کی جسے قریش نے بتوں کے لیے بند رکھا تھا۔

نبی ﷺ کی وفات 11ھ / 632ء کے بعد مدینہ میں اذان کم پوری کر پاتے؛ غم آواز روک دیتا، مشہور روایات کے مطابق۔ ابو بکر سے شام جہاد کی اجازت مانگی۔ شام میں رہے، دمشق یا قرب و جوار طبقات کے مختلف نوٹس میں۔ تقریباً 17–20ھ (قریب 638–641ء) وفات۔ دمشق میں مشہور نسبت سے قبر زیارت کی جاتی ہے۔

ان کی زندگی سنی دلیل ہے کہ اللہ کے نزدیک پیمانہ تقویٰ ہے رنگ یا نسب نہیں۔ نبی ﷺ نے بخاری کی روایت میں خواب میں جنت میں ان کے قدم سنے، ایک فضیلت جس نے اس آدمی کو تسکین دی جس کے پاس مکہ میں کچھ نہ تھا۔ دائرۃ المعارف انہیں مؤذنوں اور ان آزاد کردہ لوگوں میں رکھتی ہے جنہیں اسلام نے اٹھایا۔

امت اب بھی بچوں کو اذان سکھاتے ہوئے ان کا نام سنتی ہے۔ ہر مذہب اہل سنت میں رضی اللہ عنہ ہیں۔ بلال کا باب پتھر، ابو بکر کی خرید، مدینہ کی آواز، کعبہ کی چھت، اور وفات کے بعد خاموشی کے بغیر مکمل نہیں۔""",
    """बिलाल इब्न रबाह رضي الله عنه हबशी थे, तबाक़ात में वालिदा हमामाह मज़कूर हैं। मक्का में ग़ुलाम, बहुत सी रिवायात में जुमह के उमैया बिन ख़लफ़ के घर से वाबस्ता। इब्न साद उन्हें कमज़ोरों में शुमार करते हैं जिन्हें क़बीले की पनाह न थी। सियाही और ग़ुलामी कुरआन की उस अख़लाक़ियत में जो नबी ﷺ ने सिखाई अज़ान के आला शرف में रुकावट न बनी।

अल्लाह के एक कहने पर तशद्दुद सहा। मशहूर मंज़र यह है कि गर्मी में सीने पर बड़ा पत्थर रखा गया और वह अहद अहद दोहराते रहे—एक, एक—जब उमैया वग़ैरह बुतों के नाम का तक़ाज़ा करते। रिवायात इब्न इसहाक की सीरत और बाद की रियाज़ुस सालिहीन तर्ज़ की कुतुब-ए-फ़ज़ाएल में हैं। दर्द के नीचे तौहीद की साबित क़दमी ज़रबुल मसल बनी।

अबू बक्र رضي الله عنه ने ख़रीद कर आज़ाद किया, जैसा इस्लाम पर सताए गए अन्य ग़ुलामों को। नबी ﷺ ने बिलाल को मदीना के अंदरूनी हलके में लिया। अज़ान अब्दुल्लाह बिन ज़ैद رضي الله عنه के ख़्वाब और उमर के ऐसे ही कलिमात सुनने के बाद मशरू हुई तो ख़ूबसूरत और पहुँच वाली आवाज़ की वजह से बिलाल पहले मुअज़्ज़िन चुने गए। मस्जिद-ए-नबवी में पाँचों नमाज़ों की अज़ान कहते।

बड़ी मुहिमातों में लड़े, बद्र में हाज़िर, जहाँ साबिक़ अज़ीयत देने वाला उमैया लड़ाई में मारा गया, मग़ाज़ी यह ज़िक्र करते हैं बिना ज़ाती इंतिक़ाम को दीन का दिल बनाए। फत्हे मक्का 8 हिजरी / 630 ई. पर काबा पर चढ़ कर छत से अज़ान दी, इब्न हिशाम और फत्हे मक्का के मुवर्रिख़ इसे सालों की ज़िल्लत के उल्ट जाने का लम्हा लिखते हैं। ज़मीन के कमज़ोर ने उस घर से नमाज़ की पुकार की जिसे कुरैश ने बुतों के लिए बंद रखा था।

नबी ﷺ की वफ़ात 11 हिजरी / 632 ई. के बाद मदीना में अज़ान कम पूरी कर पाते; ग़म आवाज़ रोक देता, मशहूर रिवायात के मुताबिक। अबू बक्र से शाम जिहाद की इजाज़त मांगी। शाम में रहे, दिमश्क या क़ुर्बो जवार तबाक़ात के मुख़्तलिफ़ नोटिस में। क़रीब 17–20 हिजरी (लगभग 638–641 ई.) वफ़ात। दिमश्क में मशहूर निस्बत से क़ब्र ज़ियारत की जाती है।

उनकी ज़िंदगी सुन्नी दलील है कि अल्लाह के नज़दीक पैमाना तक़वा है रंग या नसब नहीं। नबी ﷺ ने बुख़ारी की रिवायत में ख़्वाब में जन्नत में उनके क़दम सुने, एक फ़ज़ीलत जिसने उस आदमी को तस्कीन दी जिसके पास मक्का में कुछ न था। दाइरतुल मआरिफ़ उन्हें मुअज़्ज़िनों और उन आज़ाद किए लोगों में रखती है जिन्हें इस्लाम ने उठाया।

उम्मत अब भी बच्चों को अज़ान सिखाते हुए उनका नाम सुनती है। हर मज़हब अहले सुन्नत में رضي الله عنه हैं। बिलाल का बाब पत्थर, अबू बक्र की ख़रीद, मदीना की आवाज़, काबा की छत, और विसाल के बाद ख़ामोशी के बिना मुकम्मल नहीं।""",
    """বিলাল ইবন রাবাহ رضي الله عنه হাবশি ছিলেন, তাবাকাতে মাতা হামামাহ উল্লিখিত। মক্কায় দাস, অনেক বর্ণনায় জুমাহর উমাইয়া ইবন খালাফের ঘরের সঙ্গে যুক্ত। ইবন সাদ তাঁকে দুর্বলদের মধ্যে গণ্য করেন যাঁদের গোত্রীয় আশ্রয় ছিল না। কালোত্ব ও দাসত্ব নবী ﷺ-এর শেখানো কুরআনি নীতিতে আজানের সর্বোচ্চ সম্মানে বাধা হয়নি।

আল্লাহ এক বলার জন্য নির্যাতিত হন। প্রসিদ্ধ দৃশ্য: গরমে বুকে বড় পাথর চাপানো হয় এবং তিনি আহাদ আহাদ পুনরাবৃত্তি করেন—এক, এক—যখন উমাইয়া প্রভৃতি মূর্তির নাম দাবি করে। বর্ণনা ইবন ইসহাকের সিরাত ও পরবর্তী রিয়াদুস সালিহিন ধরনের ফাজায়েল গ্রন্থে। ব্যথার নিচে তাওহিদের অবিচলতা প্রবাদ হয়।

আবু বকর رضي الله عنه তাঁকে কিনে মুক্ত করেন, যেমন ইসলামের জন্য নির্যাতিত অন্য দাসদের। নবী ﷺ বিলালকে মদিনার অন্তরঙ্গ মহলে নেন। আব্দুল্লাহ ইবন যায়দ رضي الله عنه-এর স্বপ্ন ও উমরের অনুরূপ শব্দ শোনার পর আজান বিধিবদ্ধ হলে সুন্দর ও দূরগামী কণ্ঠের জন্য বিলাল প্রথম মুয়াজ্জিন নির্বাচিত হন। নবীর মসজিদে পাঁচ ওয়াক্ত আজান দেন।

বড় অভিযানে যুদ্ধ করেন, বদরে উপস্থিত, যেখানে পূর্ব নির্যাতক উমাইয়া যুদ্ধে নিহত হন; মাগাজি এ কথা বলে ব্যক্তিগত প্রতিশোধকে দীনের মর্ম না বানিয়ে। মক্কা বিজয় ৮ হিজরি / ৬৩০ খ্রি. কাবার ছাদে উঠে আজান দেন; ইবন হিশাম ও ফাতহে মক্কার ঐতিহাসিক একে বছরের অপমানের বিপরীত মুহূর্ত লেখেন। পৃথিবীর দুর্বল সেই ঘর থেকে নামাজের আহ্বান করেন যা কুরাইশ মূর্তির জন্য বন্ধ রেখেছিল।

নবী ﷺ-এর ওফাত ১১ হিজরি / ৬৩২-এর পর মদিনায় আজান কম সম্পূর্ণ করতে পারেন; শোক কণ্ঠ থামিয়ে দেয়, প্রসিদ্ধ বর্ণনায়। আবু বকরের কাছে শামে জিহাদের অনুমতি চান। শামে বাস করেন, দামেশক বা আশপাশ তাবাকাতের ভিন্ন নোটে। প্রায় ১৭–২০ হিজরি (আনু. ৬৩৮–৬৪১) ইন্তেকাল। দামেশকে প্রসিদ্ধ আরোপে কবর যিয়ারত হয়।

তাঁর জীবন সুন্নি প্রমাণ যে আল্লাহর কাছে মাপকাঠি তাকওয়া, বর্ণ বা বংশ নয়। নবী ﷺ বুখারির বর্ণনায় স্বপ্নে জান্নাতে তাঁর পদশব্দ শোনেন, একটি ফজিলত যা সেই মানুষকে সান্ত্বনা দেয় যার মক্কায় কিছু ছিল না। বিশ্বকোষ তাঁকে মুয়াজ্জিন ও ইসলাম-উত্তোলিত মুক্তদাসদের মধ্যে রাখে।

উম্মাহ আজও শিশুদের আজান শেখাতে তাঁর নাম শোনে। আহলুস সুন্নাহর প্রতিটি মাজহাবে তিনি رضي الله عنه। বিলালের অধ্যায় পাথর, আবু বকরের ক্রয়, মদিনার কণ্ঠ, কাবার ছাদ ও ওফাতের পর নীরবতা ছাড়া সম্পূর্ণ নয়।""",
    """Bilal bin Rabah رضي الله عنه adalah orang Habasyah; ibunya disebut Hamamah dalam tabaqat. Ia budak di Makkah, dikaitkan dalam banyak riwayat dengan rumah Umayyah bin Khalaf dari Jumah. Ibnu Sa'd mencatat Islamnya di antara orang lemah yang tidak punya perlindungan klan. Kulit hitam dan perbudakannya, dalam etika Al-Qur'an yang diajarkan Nabi ﷺ, tidak menjadi penghalang kehormatan tertinggi azan.

Ia disiksa karena mengatakan Allah itu Esa. Adegan masyhur adalah batu besar diletakkan di dadanya di panas terik, dan ia mengulang 'Ahad, Ahad'—Esa, Esa—sementara Umayyah dan lainnya menuntut ia menyebut berhala. Riwayat ada dalam sirah Ibnu Ishaq dan himpunan fada'il kemudian. Keteguhannya menjadi peribahasa tauhid di bawah sakit.

Abu Bakar رضي الله عنه membelinya dan memerdekakannya, sebagaimana ia memerdekakan budak lain yang dihukum karena Islam. Nabi ﷺ mengambil Bilal ke lingkaran dalam Madinah. Ketika azan disyariatkan setelah mimpi Abdullah bin Zaid رضي الله عنه, dan setelah Umar mendengar kata serupa, Bilal dipilih sebagai muazin pertama karena keindahan dan jangkauan suaranya. Ia menyeru lima salat di Masjid Nabawi.

Ia berperang dalam ekspedisi besar dan hadir di Badar, di mana mantan penyiksanya Umayyah terbunuh dalam pertempuran, fakta yang disebut maghazi tanpa menjadikan dendam pribadi sebagai jantung agama. Pada Fathu Makkah 8 H / 630 M Bilal naik ke Ka'bah dan azan dari atapnya, momen yang dicatat Ibnu Hisyam dan sejarawan Fathu Makkah sebagai pembalikan tahun-tahun penghinaan. Orang lemah di bumi menyeru salat dari Rumah yang dikunci Quraisy untuk berhala.

Setelah Nabi ﷺ wafat pada 11 H / 632 M Bilal jarang dapat menyelesaikan azan di Madinah; duka menghentikan suaranya, menurut riwayat terkenal. Ia meminta izin Abu Bakar untuk keluar jihad ke Syam. Ia tinggal di Syam, di Damaskus atau sekitarnya menurut catatan berbeda dalam tabaqat. Ia wafat sekitar 17–20 H (k. 638–641 M). Kuburnya diziarahi di Damaskus dalam nisbah yang masyhur.

Hidupnya adalah bukti Ahlusunah bahwa takwa, bukan warna atau nasab, adalah ukuran di sisi Allah. Nabi ﷺ mendengar langkahnya di Jannah dalam mimpi yang diriwayatkan Bukhari, keutamaan yang menghibur orang yang tidak punya apa-apa di Makkah. Ensiklopedia menempatkannya di antara para muazin dan di antara orang merdeka yang diangkat Islam.

Umat masih mendengar namanya setiap azan diajarkan kepada anak-anak. Ia رضي الله عنه di setiap mazhab Ahlusunah. Tidak ada bab tentang Bilal yang lengkap tanpa batu, pembelian oleh Abu Bakar, suara di Madinah, atap Ka'bah, dan keheningan setelah Wafat.""",
)
ch["items"][0]["details"] = D(
    """Reports say that when Bilal later returned and gave the adhan in Madinah, the people wept until their beards were wet, because the voice brought back the days of the Prophet ﷺ. Some versions place this on a visit from Sham; chains are discussed by the hadith critics, but the meaning is loved in Sunni piety: loyalty to a voice that had belonged to the Messenger's ﷺ mosque.

His grief after the Wafat was not a leaving of the din. It was too much love to say 'ashhadu anna Muhammadan rasul Allah' in the same courtyard without the one who had taught him. Abu Bakr and then Umar honoured his wish to serve on the Syrian front. Taqwa expressed itself as jihad and as silence, not as desertion of salah.

The Prophet ﷺ had said that a person is not better than another by red or black skin, only by taqwa. Bilal's chapter is the lived tafsir of that teaching. Quraysh had ranked men by bayt and by colour; the adhan ranked them by the hour of prayer. Children of every land who call the adhan walk, in a sense, in Bilal's path.

He accompanied the Prophet ﷺ on journeys and stood at the back of the camel with the extra water-skin in reports of travel. He was among those who entered the Ka'bah with the Messenger ﷺ on the day of Fath. These small companionships matter as much as the famous roof. They show a freedman as a daily companion, not a symbol only.

In Sham he is said to have given the adhan on occasion for the armies. His death around 20 AH closed a life that began under a rock and ended in a land opened for Islam. Variant death-dates in Ibn Sa'd do not disturb the outline. He left no dynasty; he left a call.

Sunni encyclopedias refuse to treat Bilal as a token in later racial polemics. They tell the torture, the manumission, the voice, the Ka'bah, and the weeping of Madinah as one story of iman. Colour is mentioned to refute pride, not to build a new pride.

Thus adhan and loyalty are one theme: the man who would not say the names of idols under the rock would not cheapen the shahadah after the Prophet ﷺ was buried. The ummah answers his loyalty every dawn.""",
    """روایات ہیں بعد میں بلال لوٹے اور مدینہ میں اذان دی تو لوگ روئے یہاں تک کہ داڑھیاں بھیگ گئیں، کیونکہ آواز نبی ﷺ کے دن واپس لے آئی۔ بعض روایتیں شام سے آمد پر یہ واقعہ رکھتی ہیں؛ محدثین سند پر کلام کرتے ہیں، مگر معنی سنی دینداری میں محبوب ہے: اس آواز سے وفا جو رسول ﷺ کی مسجد کی تھی۔

وفات کے بعد ان کا غم دین چھوڑنا نہ تھا۔ محبت اتنی تھی کہ اسی صحن میں اشہد ان محمدا رسول اللہ کہنا اس کے بغیر نہ بنتا جس نے سکھایا تھا۔ ابو بکر پھر عمر نے شامی محاذ پر خدمت کی خواہش عزت دی۔ تقویٰ جہاد اور خاموشی سے ظاہر ہوا، نماز سے فرار سے نہیں۔

نبی ﷺ نے فرمایا آدمی سرخ یا کالے رنگ سے دوسرے سے بہتر نہیں، صرف تقویٰ سے۔ بلال کا باب اس تعلیم کی جی ہوئی تفسیر ہے۔ قریش نے گھرانے اور رنگ سے درجے دیے تھے؛ اذان نے نماز کی گھڑی سے۔ ہر سرزمین کے بچے جو اذان کہتے ہیں ایک معنی میں بلال کے راستے چلتے ہیں۔

سفر میں نبی ﷺ کے ساتھ رہتے، روایات میں اونٹ کے پیچھے پانی کی مشک لیے کھڑے ملتے۔ فتح کے دن رسول ﷺ کے ساتھ کعبہ میں داخل ہونے والوں میں تھے۔ یہ چھوٹی رفاقتیں مشہور چھت جتنی اہم ہیں۔ آزاد کردہ غلام کو روز کا ساتھی دکھاتی ہیں، صرف علامت نہیں۔

شام میں کبھی لشکروں کے لیے اذان کہی گئی۔ تقریباً 20ھ وفات نے اس زندگی کا دروازہ بند کیا جو پتھر تلے شروع ہوئی اور اسلام کے لیے کھلی سرزمین پر ختم۔ ابن سعد کی مختلف تاریخیں خاکہ نہیں بگاڑتیں۔ خاندان نہ چھوڑا؛ پکار چھوڑی۔

سنی دائرۃ المعارف بلال کو بعد کی نسلی بحثوں کا نشان نہیں بناتے۔ تشدد، آزادی، آواز، کعبہ، اور مدینہ کا رونا ایمان کی ایک داستان کہتے ہیں۔ رنگ تکبر توڑنے کو ذکر ہوتا ہے، نیا تکبر بنانے کو نہیں۔

یوں اذان اور وفا ایک موضوع ہیں: جو پتھر تلے بتوں کے نام نہ کہتا وہ نبی ﷺ کی تدفین کے بعد شہادت سستی نہ کرتا۔ امت ہر فجر ان کی وفا کا جواب دیتی ہے۔""",
    """रिवायात हैं बाद में बिलाल लौटे और मदीना में अज़ान दी तो लोग रोए यहाँ तक कि दाढ़ियाँ भीग गईं, क्योंकि आवाज़ नबी ﷺ के दिन वापस ले आई। कुछ रिवायतें शाम से आमद पर यह वाक़िया रखती हैं; मुहद्दिसीन सनद पर कलाम करते हैं, मगर मानी सुन्नी दीनदारी में महबूब है: उस आवाज़ से वफ़ा जो रसूल ﷺ की मस्जिद की थी।

विसाल के बाद उनका ग़म दीन छोड़ना न था। मुहब्बत इतनी थी कि उसी सहन में अशहदु अन्न मुहम्मदन रसूलुल्लाह कहना उसके बिना न बनता जिसने सिखाया था। अबू बक्र फिर उमर ने शामी मोर्चे पर ख़िदमत की ख़्वाहिश इज़्ज़त दी। तक़वा जिहाद और ख़ामोशी से ज़ाहिर हुआ, नमाज़ से फ़रार से नहीं।

नबी ﷺ ने फ़रमाया आदमी सुरख़ या काले रंग से दूसरे से बेहतर नहीं, सिर्फ़ तक़वा से। बिलाल का बाब इस तालीम की जी हुई तफ़सीर है। कुरैश ने घराने और रंग से दर्जे दिए थे; अज़ान ने नमाज़ की घड़ी से। हर सरज़मीन के बच्चे जो अज़ान कहते हैं एक मानी में बिलाल के रास्ते चलते हैं।

सफ़र में नबी ﷺ के साथ रहते, रिवायात में ऊँट के पीछे पानी की मश्क लिए खड़े मिलते। फ़तह के दिन रसूल ﷺ के साथ काबा में दाख़िल होने वालों में थे। ये छोटी रफ़ाक़तें मशहूर छत जितनी अहम हैं। आज़ाद किए ग़ुलाम को रोज़ का साथी दिखाती हैं, सिर्फ़ अलामत नहीं।

शाम में कभी लश्करों के लिए अज़ान कही गई। क़रीब 20 हिजरी वफ़ात ने उस ज़िंदगी का दरवाज़ा बंद किया जो पत्थर तले शुरू हुई और इस्लाम के लिए खुली सरज़मीन पर ख़त्म। इब्न साद की मुख़्तलिफ़ तारीख़ें ख़ाका नहीं बिगाड़तीं। ख़ानदान न छोड़ा; पुकार छोड़ी।

सुन्नी दाइरतुल मआरिफ़ बिलाल को बाद की नस्ली बहसों का निशान नहीं बनातीं। तशद्दुद, आज़ादी, आवाज़, काबा, और मदीना का रोना ईमान की एक दास्तान कहती हैं। रंग तकब्बुर तोड़ने को ज़िक्र होता है, नया तकब्बुर बनाने को नहीं।

यूँ अज़ान और वफ़ा एक मौज़ू हैं: जो पत्थर तले बुतों के नाम न कहता वह नबी ﷺ की तदफ़ीन के बाद शहादत सस्ती न करता। उम्मत हर फज्र उनकी वफ़ा का जवाब देती है।""",
    """বর্ণনায় পরে বিলাল ফিরে মদিনায় আজান দিলে মানুষ কাঁদে দাড়ি ভিজে যায়, কারণ কণ্ঠ নবী ﷺ-এর দিন ফিরিয়ে আনে। কিছু সনদ এ ঘটনা শাম থেকে আগমনে রাখে; মুহাদ্দিসরা সনদ নিয়ে আলোচনা করেন, তবু অর্থ সুন্নি ধার্মিকতায় প্রিয়: সেই কণ্ঠের প্রতি আনুগত্য যা রাসূল ﷺ-এর মসজিদের ছিল।

ওফাতের পর তাঁর শোক দীন ত্যাগ নয়। এত ভালোবাসা যে একই প্রাঙ্গণে ‘আশহাদু আন্না মুহাম্মাদান রাসূলুল্লাহ’ বলা সেইজন ছাড়া যায় না যিনি শিখিয়েছিলেন। আবু বকর তারপর উমর শাম ফ্রন্টে খিদমতের ইচ্ছা সম্মান করেন। তাকওয়া জিহাদ ও নীরবতায় প্রকাশ পায়, সালাত থেকে পলায়নে নয়।

নবী ﷺ বলেছেন মানুষ লাল বা কালো ত্বকে অন্যের চেয়ে শ্রেষ্ঠ নয়, কেবল তাকওয়ায়। বিলালের অধ্যায় সেই শিক্ষার জীবিত তাফসির। কুরাইশ ঘর ও বর্ণ দিয়ে মর্যাদা দিত; আজান নামাজের ঘণ্টা দিয়ে। প্রতি দেশের শিশু যারা আজান দেয় এক অর্থে বিলালের পথে হাঁটে।

সফরে নবী ﷺ-এর সঙ্গী, বর্ণনায় উটের পেছনে পানির মশক নিয়ে দাঁড়ান। বিজয়ের দিন রাসূল ﷺ-এর সঙ্গে কাবায় প্রবেশকারীদের মধ্যে। এই ক্ষুদ্র সাহচর্য প্রসিদ্ধ ছাদের মতোই গুরুত্বপূর্ণ। মুক্তদাসকে দৈনিক সঙ্গী দেখায়, কেবল প্রতীক নয়।

শামে কখনো সেনার জন্য আজান দেন। প্রায় ২০ হিজরির মৃত্যু সেই জীবনের দুয়ার বন্ধ করে যা পাথরের নিচে শুরু হয়ে ইসলামের জন্য খোলা ভূমিতে শেষ হয়। ইবন সাদের ভিন্ন তারিখ রূপরেখা নষ্ট করে না। রাজবংশ রাখেননি; আহ্বান রেখে গেছেন।

সুন্নি বিশ্বকোষ বিলালকে পরবর্তী বর্ণবাদী বিতর্কের চিহ্ন করে না। নির্যাতন, মুক্তি, কণ্ঠ, কাবা ও মদিনার কান্না ঈমানের এক কাহিনি বলে। বর্ণ অহংকার ভাঙতে উল্লেখ হয়, নতুন অহংকার গড়তে নয়।

এভাবে আজান ও আনুগত্য এক বিষয়: যিনি পাথরের নিচে মূর্তির নাম বলেননি তিনি নবী ﷺ-এর দাফনের পর শাহাদাহ সস্তা করেননি। উম্মাহ প্রতি ফজরে তাঁর ওফার জবাব দেয়।""",
    """Riwayat menyebutkan ketika Bilal kemudian kembali dan azan di Madinah, orang-orang menangis hingga janggut basah, karena suara itu mengembalikan hari-hari Nabi ﷺ. Sebagian versi menempatkannya pada kunjungan dari Syam; sanad dibahas kritikus hadis, tetapi maknanya dicintai dalam kesalehan Ahlusunah: kesetiaan pada suara yang pernah milik masjid Rasul ﷺ.

Dukanya setelah Wafat bukan meninggalkan agama. Cinta terlalu dalam untuk mengucapkan 'asyhadu anna Muhammadan rasul Allah' di halaman yang sama tanpa orang yang mengajarinya. Abu Bakar lalu Umar menghormati keinginannya berkhidmah di front Syam. Takwa terungkap sebagai jihad dan sebagai diam, bukan sebagai kabur dari salat.

Nabi ﷺ bersabda seseorang tidak lebih baik dari yang lain karena kulit merah atau hitam, hanya karena takwa. Bab Bilal adalah tafsir hidup ajaran itu. Quraisy memeringkat manusia menurut bayt dan warna; azan memeringkat mereka menurut waktu salat. Anak-anak setiap negeri yang menyeru azan, dalam satu arti, berjalan di jalan Bilal.

Ia menemani Nabi ﷺ dalam perjalanan dan berdiri di belakang unta dengan geriba air tambahan dalam riwayat safar. Ia termasuk yang masuk Ka'bah bersama Rasul ﷺ pada hari Fath. Persahabatan kecil ini sama pentingnya dengan atap yang terkenal. Mereka menunjukkan orang merdeka sebagai sahabat harian, bukan hanya lambang.

Di Syam ia dikatakan kadang azan untuk pasukan. Wafatnya sekitar 20 H menutup hidup yang dimulai di bawah batu dan berakhir di negeri yang dibuka untuk Islam. Tanggal wafat yang berbeda dalam Ibnu Sa'd tidak mengganggu garis besar. Ia tidak meninggalkan dinasti; ia meninggalkan seruan.

Ensiklopedia Ahlusunah menolak memperlakukan Bilal sebagai token dalam polemik rasial kemudian. Mereka menuturkan siksaan, pemerdekaan, suara, Ka'bah, dan tangisan Madinah sebagai satu kisah iman. Warna disebut untuk menolak sombong, bukan untuk membangun sombong baru.

Dengan demikian azan dan kesetiaan adalah satu tema: orang yang tidak mau menyebut nama berhala di bawah batu tidak akan murahkan syahadat setelah Nabi ﷺ dikubur. Umat menjawab kesetiaannya setiap subuh.""",
)

# --- 7 Salman al-Farisi ---
ch = chapter(7)
ch["details"] = D(
    """Salman al-Farisi رضي الله عنه, also called Salman ibn al-Islam, was born in Persia, in the region of Isfahan (Jayy) according to the famous long hadith in Ahmad and Ibn Sa'd. His people were Magians; he served a fire temple as a boy. A Christian hermit's worship drew him away. He followed monks from land to land, seeking a prophet described in their books, until he was told to go to Arabia, to a place of palms, where a prophet would appear who would not eat charity but would accept a gift, and between whose shoulders would be the seal of prophethood.

He reached Yathrib as a slave after being betrayed on the journey and sold. When the Prophet ﷺ arrived in Madinah in 1 AH / 622 CE, Salman tested the signs: he offered charity, which the Prophet ﷺ did not eat; he offered a gift, which he ate; he saw the seal on the back. He declared Islam. The story is among the most complete conversion narratives in the sirah, a chain of seeking that Sunni preachers still tell as dalil that guidance can come from the east.

He remained a slave until the Prophet ﷺ helped him write a mukatabah, a contract of freedom, with his owner. The price was a large number of date palms to plant and a quantity of gold. The Companions planted with him; the Prophet ﷺ planted some with his own hand and they took. Gold came by a miracle of a piece like an egg in some reports. Manumission by contract and communal help is part of Salman's fiqh legacy as well as his story.

At the Battle of the Trench (Khandaq, Ahzab) in 5 AH / 627 CE he suggested digging a trench on the exposed side of Madinah, a method known in Persian warfare and unknown as a city defence to most Arabs of Hijaz. The Prophet ﷺ accepted the counsel. Muhajirun and Ansar both claimed Salman; the Prophet ﷺ said, 'Salman is of us, the Ahl al-Bayt.' That sentence in Ibn Ishaq and Ibn Sa'd is a badge of belonging beyond nasab.

He later took part in the openings of Iraq and was appointed governor of al-Mada'in (Ctesiphon) in the time of Umar رضي الله عنه. Reports of his zuhd there—eating from the work of his hands, wearing a cloak of little price, refusing the pomp of Kisra's hall—are in the tabaqat. He lived among a newly Muslim and still Persian population as a bridge of language and custom.

He died in the thirties AH, often specified as 35 or 36 AH (c. 655–657 CE), and was buried at Mada'in. His grave there is famous. Dates vary slightly among historians; the outline does not: a Magian boy, a Christian seeker, a Madinan Companion, an engineer of the trench, a governor who remained poor.

Sunni encyclopedias honour Salman without using him to attack other Companions or to invent a lineage quarrel. His Persian origin is a mercy mentioned in hadith that faith would reach the east. He stands for useful knowledge brought into Islam from any land, and for a heart that travelled until it found the Seal of the Prophets ﷺ.""",
    """سلمان فارسی رضی اللہ عنہ، سلمان بن الاسلام بھی کہے گئے، فارس میں پیدا ہوئے، احمد و ابن سعد کی مشہور لمبی حدیث کے مطابق اصفہان (جی) کے علاقے۔ قوم مجوسی تھی؛ لڑکپن میں آتش کدہ کی خدمت کی۔ ایک عیسائی راہب کی عبادت کھینچ لے گئی۔ ملک ملک راہبوں کے ساتھ نبی کی تلاش کی جس کا ذکر ان کی کتابوں میں تھا، یہاں تک کہا گیا عرب جاؤ، کھجوروں والی بستی، جہاں نبی ظاہر ہو گا جو صدقہ نہ کھائے ہدیہ لے، اور دونوں کندھوں کے درمیان مہر نبوت ہو۔

سفر میں دھوکا کھا کر غلام بن کر یثرب پہنچے۔ نبی ﷺ 1ھ / 622ء مدینہ آئے تو نشانیاں آزمائیں: صدقہ پیش کیا جو نبی ﷺ نے نہ کھایا؛ ہدیہ دیا جو کھایا؛ پیٹھ پر مہر دیکھی۔ اسلام کا اعلان کیا۔ یہ سیرت کی سب سے مکمل تبدیلیٔ دین کی داستانیں میں سے ہے، تلاش کی زنجیر جو سنی واعظ اب بھی دلیل بناتے ہیں کہ ہدایت مشرق سے آ سکتی ہے۔

غلام رہے یہاں تک نبی ﷺ نے مالک سے مکاتبہ، آزادی کا عقد، لکھنے میں مدد کی۔ قیمت کھجور کے بہت سے درخت لگانا اور سونا تھا۔ صحابہ ساتھ لگائے؛ نبی ﷺ نے اپنے ہاتھ کچھ لگائے اور پکڑ گئے۔ بعض روایات میں انڈے جیسے ٹکڑے سے سونا آیا۔ عقد سے آزادی اور اجتماعی مدد سلمان کی فقہی میراث بھی ہے داستان بھی۔

غزوہ خندق (احزاب) 5ھ / 627ء میں مدینہ کے کھلے رخ پر خندق کھودنے کی تجویز دی، فارسی حرب کا طریقہ جو حجاز کے اکثر عرب شہر کی دفاع میں نہ جانتے۔ نبی ﷺ نے صلاح مان لی۔ مہاجر و انصار دونوں سلمان کو اپنا کہتے؛ نبی ﷺ نے فرمایا سلمان ہم میں سے ہے، اہل بیت سے۔ ابن اسحاق و ابن سعد میں یہ جملہ نسب سے پرے نسبت کا نشان ہے۔

بعد میں عراق کی فتوحات میں رہے اور عمر رضی اللہ عنہ کے عہد میں مدائن (طیسفون) کے گورنر مقرر ہوئے۔ وہاں زہد کی روایات—ہاتھ کی کمائی کھانا، کم قیمت چادر، کسریٰ کے ایوان کا ٹھاٹ ٹھوکر—طبقات میں ہیں۔ نئے مسلمان اور ابھی فارسی آبادی میں زبان و رواج کا پل بنے۔

تیس کی دہائی ہجری میں وفات، اکثر 35 یا 36ھ (قریب 655–657ء) لکھی جاتی ہے، مدائن دفن۔ قبر وہاں مشہور ہے۔ مورخین کی تاریخیں ذرا مختلف؛ خاکہ نہیں: مجوسی لڑکا، عیسائی طالب، مدنی صحابی، خندق کا مہندس، گورنر جو غریب رہا۔

سنی دائرۃ المعارف سلمان کو عزت دیتی ہیں بغیر دوسرے صحابہ پر حملے یا نسبی جھگڑے گھڑے۔ فارسی اصل احادیث میں مذکور رحمت ہے کہ ایمان مشرق تک پہنچے گا۔ کسی بھی سرزمین سے اسلام میں لائی گئی مفید مہارت اور اس دل کی علامت ہیں جو چلتا رہا یہاں تک خاتم النبیین ﷺ ملے۔""",
    """सल्मान फ़ारसी رضي الله عنه, सल्मान इब्न अल-इस्लाम भी कहे गए, फ़ारस में पैदा हुए, अहमद व इब्न साद की मशहूर लम्बी हदीस के मुताबिक इस्फ़हान (जय्य) के इलाके। क़ौम मजूसी थी; लड़कपन में आतिश कदा की ख़िदमत की। एक ईसाई राहिब की इबादत खींच ले गई। मुल्क मुल्क राहिबों के साथ नबी की तलाश की जिसका ज़िक्र उनकी किताबों में था, यहाँ तक कहा गया अरब जाओ, खजूरों वाली बस्ती, जहाँ नबी ज़ाहिर होगा जो सदक़ा न खाए हदिया ले, और दोनों कंधों के दरमियान मोहर-ए-नबुव्वत हो।

सफ़र में धोखा खा कर ग़ुलाम बन कर यसरिब पहुँचे। नबी ﷺ 1 हिजरी / 622 ई. मदीना आए तो निशानियाँ आज़माईं: सदक़ा पेश किया जो नबी ﷺ ने न खाया; हदिया दिया जो खाया; पीठ पर मोहर देखी। इस्लाम का एलान किया। यह सीरत की सबसे मुकम्मल तबदीली-ए-दीन की दास्तानों में से है, तलाश की ज़ंजीर जो सुन्नी वाईज़ अब भी दलील बनाते हैं कि हिदायत मशरिक़ से आ सकती है।

ग़ुलाम रहे यहाँ तक नबी ﷺ ने मालिक से मुकातबा, आज़ादी का अक़्द, लिखने में मदद की। क़ीमत खजूर के बहुत से दरख़्त लगाना और सोना था। सहाबा साथ लगाए; नबी ﷺ ने अपने हाथ कुछ लगाए और पकड़ गए। कुछ रिवायात में अंडे जैसे टुकड़े से सोना आया। अक़्द से आज़ादी और इज्तिमाई मदद सल्मान की फ़िक़ही मीरास भी है दास्तान भी।

ग़ज़वा-ए-खंदक (अहज़ाब) 5 हिजरी / 627 ई. में मदीना के खुले रुख़ पर खंदक खोदने की तजवीज़ दी, फ़ारसी हर्ब का तरीक़ा जो हिजाज़ के अक्सर अरब शहर की दिफ़ा में न जानते। नबी ﷺ ने सलाह मान ली। मुहाजिर व अनसार दोनों सल्मान को अपना कहते; नबी ﷺ ने फ़रमाया सल्मान हम में से है, अहले बैत से। इब्न इसहाक व इब्न साद में यह जुमला नसब से परे निस्बत का निशान है।

बाद में इराक की फ़ुतूहात में रहे और उमर رضي الله عنه के अहद में मदाइन (तीसिफ़ून) के गवर्नर मुक़र्रर हुए। वहाँ ज़ुहद की रिवायात—हाथ की कमाई खाना, कम क़ीमत चादर, किसरा के ऐवान का ठाठ ठोकर—तबाक़ात में हैं। नए मुस्लिम और अभी फ़ारसी आबादी में ज़बान व रवाज का पुल बने।

तीस की दहाई हिजरी में वफ़ात, अक्सर 35 या 36 हिजरी (क़रीब 655–657 ई.) लिखी जाती है, मदाइन दफ़न। क़ब्र वहाँ मशहूर है। मुवर्रिख़ीन की तारीख़ें ज़रा मुख़्तलिफ़; ख़ाका नहीं: मजूसी लड़का, ईसाई तालिब, मदनी सहाबी, खंदक का मुहंदिस, गवर्नर जो ग़रीब रहा।

सुन्नी दाइरतुल मआरिफ़ सल्मान को इज़्ज़त देती हैं बिना दूसरे सहाबा पर हमले या नसबि झगड़े घड़े। फ़ारसी अस्ल अहादीस में मज़कूर रहमत है कि ईमान मशरिक़ तक पहुँचेगा। किसी भी सरज़मीन से इस्लाम में लाई गई मुफ़ीद महारत और उस दिल की अलामत हैं जो चलता रहा यहाँ तक ख़ातमुन नबिय्यीन ﷺ मिले।""",
    """সালমান আল-ফারিসি رضي الله عنه, সালমান ইবনুল ইসলামও বলা হয়, পারস্যে জন্ম, আহমদ ও ইবন সাদের প্রসিদ্ধ দীর্ঘ হাদিস অনুসারে ইস্পাহান (জায়্য) অঞ্চলে। তাঁর জাতি মাজুসি; বাল্যে অগ্নিকুণ্ডের সেবা করেন। এক খ্রিষ্টান সন্ন্যাসীর ইবাদত তাঁকে টেনে নেয়। দেশে দেশে সন্ন্যাসীদের সঙ্গে এমন নবীর খোঁজ করেন যাঁর উল্লেখ তাদের কিতাবে, শেষে বলা হয় আরবে যাও, খেজুরের নগরী, যেখানে নবী প্রকাশ পাবেন যিনি সদকা খাবেন না হাদিয়া নেবেন, এবং কাঁধের মাঝে নবুয়তের মোহর থাকবে।

সফরে প্রতারিত হয়ে দাস হিসেবে ইয়াসরিবে পৌঁছান। নবী ﷺ ১ হিজরি / ৬২২ খ্রি. মদিনায় এলে তিনি নিদর্শন পরীক্ষা করেন: সদকা দেন নবী ﷺ খান না; হাদিয়া দেন খান; পিঠে মোহর দেখেন। ইসলাম ঘোষণা করেন। এটি সিরাতের পূর্ণতম ধর্মান্তর কাহিনিগুলোর একটি, অন্বেষণের শৃঙ্খল যা সুন্নি ওয়ায়েজ আজও দলিল করেন যে হিদায়াত পূর্ব থেকে আসতে পারে।

তিনি দাস থাকেন যতক্ষণ নবী ﷺ মালিকের সঙ্গে মুকাতাবাহ, মুক্তির চুক্তি, লিখতে সাহায্য করেন। মূল্য ছিল অনেক খেজুরগাছ রোপণ ও স্বর্ণ। সাহাবিরা সঙ্গে রোপণ করেন; নবী ﷺ নিজ হাতে কিছু লাগান এবং সেগুলো টিকে। কিছু বর্ণনায় ডিমের মতো টুকরো থেকে স্বর্ণ আসে। চুক্তিতে মুক্তি ও সমষ্টিগত সাহায্য সালমানের ফিকহি উত্তরাধিকারও, কাহিনিও।

খন্দক (আহজাব) ৫ হিজরি / ৬২৭ খ্রি. তিনি মদিনার খোলা দিকে পরিখা কাটার প্রস্তাব দেন, পারস্য যুদ্ধের পদ্ধতি যা হিজাজের অধিকাংশ আরব নগররক্ষায় জানত না। নবী ﷺ পরামর্শ গ্রহণ করেন। মুহাজির ও আনসার উভয়ে সালমানকে নিজেদের বলে; নবী ﷺ বলেন, ‘সালমান আমাদের, আহলুল বায়তের।’ ইবন ইসহাক ও ইবন সাদে এই বাক্য বংশের বাইরে সম্পর্কের ব্যাজ।

পরে ইরাক বিজয়ে থাকেন এবং উমর رضي الله عنه-এর আমলে মাদাইন (তেসিফোন)-এর গভর্নর নিযুক্ত হন। সেখানকার যুহদের বর্ণনা—হাতের উপার্জন খাওয়া, সস্তা চাদর, কিসরার প্রাসাদের জাঁক প্রত্যাখ্যান—তাবাকাতে আছে। নতুন মুসলিম ও এখনও পারস্য জনগোষ্ঠীর মধ্যে ভাষা ও রীতির সেতু হন।

৩০-এর দশক হিজরিতে ইন্তেকাল, প্রায়ই ৩৫ বা ৩৬ হিজরি (আনু. ৬৫৫–৬৫৭) লেখা হয়, মাদাইনে দাফন। কবর সেখানে প্রসিদ্ধ। ঐতিহাসিকদের তারিখ সামান্য ভিন্ন; রূপরেখা নয়: মাজুসি বালক, খ্রিষ্টান অন্বেষক, মদিনার সাহাবি, পরিখার প্রকৌশলী, গভর্নর যিনি দরিদ্র থাকেন।

সুন্নি বিশ্বকোষ সালমানকে সম্মান করে অন্য সাহাবিদের আক্রমণ বা বংশবিবাদ না গড়ে। পারস্য উৎস হাদিসে উল্লিখিত রহমত যে ঈমান পূর্বে পৌঁছবে। যে কোনো দেশ থেকে ইসলামে আনা উপযোগী জ্ঞান এবং সেই হৃদয়ের প্রতীক যা চলতে থাকে যতক্ষণ খাতামুন নাবিয়্যীন ﷺ পায়।""",
    """Salman al-Farisi رضي الله عنه, disebut juga Salman bin al-Islam, lahir di Persia, di kawasan Isfahan (Jayy) menurut hadis panjang masyhur dalam Ahmad dan Ibnu Sa'd. Kaumnya Majusi; ia melayani kuil api semasa kanak-kanak. Ibadah seorang rahib Nasrani menariknya. Ia mengikuti para rahib dari negeri ke negeri, mencari nabi yang dilukiskan dalam kitab mereka, hingga ia disuruh pergi ke Arab, ke negeri kurma, di mana seorang nabi akan muncul yang tidak makan sedekah tetapi menerima hadiah, dan di antara kedua bahunya ada meterai kenabian.

Ia sampai di Yastrib sebagai budak setelah dikhianati dalam perjalanan dan dijual. Ketika Nabi ﷺ tiba di Madinah pada 1 H / 622 M, Salman menguji tanda: ia memberi sedekah, yang tidak dimakan Nabi ﷺ; ia memberi hadiah, yang dimakan; ia melihat meterai di punggung. Ia menyatakan Islam. Kisah ini termasuk narasi pertobatan paling lengkap dalam sirah, rantai pencarian yang masih diceritakan dai Ahlusunah sebagai dalil bahwa hidayah bisa datang dari timur.

Ia tetap budak hingga Nabi ﷺ membantunya menulis mukatabah, kontrak kemerdekaan, dengan pemiliknya. Harganya sejumlah besar pohon kurma untuk ditanam dan sejumlah emas. Para Sahabat menanam bersamanya; Nabi ﷺ menanam sebagian dengan tangan sendiri dan pohon itu hidup. Emas datang melalui keajaiban sepotong seperti telur dalam sebagian riwayat. Kemerdekaan lewat kontrak dan bantuan jamaah adalah warisan fikih Salman sekaligus kisahnya.

Pada Perang Parit (Khandaq, Ahzab) 5 H / 627 M ia mengusulkan menggali parit di sisi terbuka Madinah, metode perang Persia yang tidak dikenal sebagai pertahanan kota bagi kebanyakan Arab Hijaz. Nabi ﷺ menerima nasihat itu. Muhajirin dan Ansar sama-sama mengklaim Salman; Nabi ﷺ bersabda, 'Salman termasuk kami, Ahlulbait.' Kalimat itu dalam Ibnu Ishaq dan Ibnu Sa'd adalah lencana kepemilikan di luar nasab.

Ia kemudian ikut pembukaan Irak dan diangkat gubernur al-Mada'in (Ctesiphon) pada masa Umar رضي الله عنه. Riwayat zuhudnya di sana—makan dari kerja tangan, memakai jubah murah, menolak kemegahan aula Kisra—ada dalam tabaqat. Ia hidup di antara penduduk yang baru muslim dan masih Persia sebagai jembatan bahasa dan adat.

Ia wafat pada dasawarsa tiga puluhan H, sering disebut 35 atau 36 H (k. 655–657 M), dan dimakamkan di Mada'in. Kuburnya di sana terkenal. Tanggal sedikit berbeda di antara sejarawan; garis besar tidak: anak Majusi, pencari Nasrani, Sahabat Madinah, insinyur parit, gubernur yang tetap miskin.

Ensiklopedia Ahlusunah memuliakan Salman tanpa memakainya untuk menyerang Sahabat lain atau merekayasa sengketa nasab. Asal Persianya adalah rahmat yang disebut dalam hadis bahwa iman akan sampai ke timur. Ia berdiri untuk ilmu berguna yang dibawa ke Islam dari negeri mana pun, dan untuk hati yang berjalan hingga menemukan Penutup para Nabi ﷺ.""",
)
ch["items"][0]["details"] = D(
    """In 5 AH / 627 CE a confederacy of Quraysh, Ghatafan, and Jewish allies from Khaybar's orbit marched on Madinah. The city had no wall on the north. Salman رضي الله عنه advised a trench wide and deep enough that cavalry could not leap it. The Prophet ﷺ assigned sections to teams of Muhajirun and Ansar. He himself dug and recited rajaz. Ibn Hisham describes the cold, the hunger, and the rock that the Prophet ﷺ struck with three sparks of promised openings.

The confederate horse reached the trench and could not cross. Amr ibn Abd Wudd and a few leapt a narrow place and were met; Ali رضي الله عنه killed Amr in the famous duel. The siege lasted weeks. Nu'aym ibn Mas'ud sowed distrust among the allies. A bitter wind, mentioned in the Quran as the hosts of Allah (al-Ahzab), scattered tents. The trench, a Persian skill, had given time for these other means.

The episode is taught as proof that useful technique from any land may serve the din if it does not contradict shari'ah. The Arabs of Madinah did not reject the idea because it was 'ajami. The Prophet ﷺ honoured the counsel. Later fuqaha cite Khandaq when they discuss military engineering, night watches, and consultation (shura) even in war.

Salman's belonging to the Ahl al-Bayt in the Prophet's ﷺ word did not mean a new genealogy; it meant love and inclusion. Sunni commentators explain it as an honourific attachment, like the statement that Salman is of us. It is not used in mainstream Sunni fiqh to rewrite the rules of inheritance of Banu Hashim.

The trench was filled in after the danger passed; its lesson remained. Madinah learned that defence may be patience in a ditch as well as a charge of horses. The Quran's chapter al-Ahzab memorialises the fear of eyes and hearts, then the sending of wind. Salman's name is bound to that chapter in every classroom of sirah.

Encyclopedias therefore pair the man and the ditch: a seeker from Persia, a slave who became kin in love, a counsellor whose idea the Messenger ﷺ took. No Sunni account of Khandaq is complete without him, and no account of him is complete without 5 AH.

The skill of any land, the seal on the back, and the trench in the earth are three signs of one life. Children memorise them together. رضي الله عنه.""",
    """5ھ / 627ء میں قریش، غطفان اور خیبر کے مدار کے یہودی اتحادی مدینہ پر چڑھے۔ شہر کے شمال دیوار نہ تھی۔ سلمان رضی اللہ عنہ نے ایسی چوڑی گہری خندق کی صلاح دی کہ گھڑسوار چھلانگ نہ لگا سکیں۔ نبی ﷺ نے مہاجر و انصار کی ٹیموں کو حصے دیے۔ خود کھودا اور رجز پڑھا۔ ابن ہشام سردی، بھوک، اور وہ چٹان بیان کرتے ہیں جسے نبی ﷺ نے تین چنگاریوں سے مارا، فتوحات کا وعدہ۔

اتحادی گھوڑے خندق تک آئے پار نہ ہو سکے۔ عمرو بن عبد ود اور کچھ تنگ جگہ سے کودے، مقابل ہوئے؛ علی رضی اللہ عنہ نے مشہور مبارزے میں عمرو کو قتل کیا۔ محاصرہ ہفتوں رہا۔ نعیم بن مسعود نے اتحادیوں میں بدگمانی بوئی۔ تیز ہوا، قرآن میں اللہ کے لشکر (الاحزاب)، خیموں کو اڑا لے گئی۔ فارسی مہارت کی خندق نے ان دیگر اسباب کو وقت دیا۔

واقعہ اس دلیل کے طور پر پڑھایا جاتا ہے کہ کسی بھی سرزمین کی مفید تکنیک دین کی خدمت کر سکتی ہے اگر شرع کے خلاف نہ ہو۔ مدینہ کے عرب نے اس لیے رد نہ کیا کہ عجمی ہے۔ نبی ﷺ نے صلاح کی عزت کی۔ بعد کے فقہا خندق پیش کرتے ہیں جب عسکری انجینئرنگ، رات کی چوکیاں، اور جنگ میں بھی شوریٰ کی بات ہو۔

نبی ﷺ کے قول میں سلمان کا اہل بیت سے ہونا نیا شجرہ نہ تھا؛ محبت اور شمولیت تھی۔ سنی شارح اسے تشریفی نسبت کہتے ہیں، جیسے سلمان منا۔ اہل سنت کی عام فقہ میں بنو ہاشم کی وراثت کے قواعد بدلنے کو استعمال نہیں ہوتا۔

خطرہ ٹلا تو خندق بھر دی گئی؛ سبق رہ گیا۔ مدینہ نے سیکھا دفاع گڑھے میں صبر بھی ہو سکتا ہے گھوڑوں کے حملے کی طرح۔ قرآن کا سورہ احزاب آنکھوں اور دلوں کا خوف پھر ہوا بھیجنے کو یاد رکھتا ہے۔ سلمان کا نام سیرت کی ہر جماعت میں اسی سورہ سے بندھا ہے۔

دائرۃ المعارف اس لیے آدمی اور گڑھے کو جوڑتی ہیں: فارس کا طالب، غلام جو محبت میں کنبہ بنا، مشیر جس کی بات رسول ﷺ نے لی۔ خندق کا کوئی سنی بیان ان کے بغیر مکمل نہیں، اور ان کا بیان 5ھ کے بغیر نہیں۔

کسی بھی سرزمین کی مہارت، پیٹھ کی مہر، اور زمین کی خندق ایک زندگی کی تین نشانیاں ہیں۔ بچے اکٹھے یاد کرتے ہیں۔ رضی اللہ عنہ۔""",
    """5 हिजरी / 627 ई. में कुरैश, ग़तफ़ान और ख़ैबर के मदार के यहूदी इत्तिहादी मदीना पर चढ़े। शहर के शिमाल दीवार न थी। सल्मान رضي الله عنه ने ऐसी चौड़ी गहरी खंदक की सलाह दी कि घुड़सवार छलाँग न लगा सकें। नबी ﷺ ने मुहाजिर व अनसार की टीमों को हिस्से दिए। ख़ुद खोदा और रजज़ पढ़ा। इब्न हिशाम सर्दी, भूख, और वह चट्टान बयान करते हैं जिसे नबी ﷺ ने तीन चिंगारियों से मारा, फ़ुतूहात का वादा।

इत्तिहादी घोड़े खंदक तक आए पार न हो सके। अम्र बिन अब्द वुद्द और कुछ तंग जगह से कूदे, मुक़ाबिल हुए; अली رضي الله عنه ने मशहूर मुबारिज़े में अम्र को क़त्ल किया। मुहासरा हफ़्तों रहा। नुऐम बिन मसऊद ने इत्तिहादियों में बदगुमानी बोई। तेज़ हवा, कुरआन में अल्लाह के लश्कर (अल-अहज़ाब), खेमों को उड़ा ले गई। फ़ारसी महारत की खंदक ने उन अन्य असबाब को वक्त दिया।

वाक़िया इस दलील के तौर पर पढ़ाया जाता है कि किसी भी सरज़मीन की मुफ़ीद तकनीक दीन की ख़िदमत कर सकती है अगर शरअ के ख़िलाफ़ न हो। मदीना के अरब ने इसलिए रद्द न किया कि अजमी है। नबी ﷺ ने सलाह की इज़्ज़त की। बाद के फ़ुक़हा खंदक पेश करते हैं जब अस्करी इंजीनियरिंग, रात की चौकियाँ, और जंग में भी शूरा की बात हो।

नबी ﷺ के क़ौल में सल्मान का अहले बैत से होना नया शजरह न था; मुहब्बत और शुमूलियत थी। सुन्नी शारिह इसे तशरीफ़ी निस्बत कहते हैं, जैसे सल्मान मिन्ना। अहले सुन्नत की आम फ़िक़्ह में बनू हाशिम की विरासत के क़वाइद बदलने को इस्तेमाल नहीं होता।

ख़तरा टला तो खंदक भर दी गई; सबक़ रह गया। मदीना ने सीखा दिफ़ा गड्ढे में सब्र भी हो सकता है घोड़ों के हमले की तरह। कुरआन का सूरह अहज़ाब आँखों और दिलों का ख़ौफ़ फिर हवा भेजने को याद रखता है। सल्मान का नाम सीरत की हर जमाअत में उसी सूरह से बंधा है।

दाइरतुल मआरिफ़ इसलिए आदमी और गड्ढे को जोड़ती हैं: फ़ारस का तालिब, ग़ुलाम जो मुहब्बत में कुनबा बना, मुशीर जिसकी बात रसूल ﷺ ने ली। खंदक का कोई सुन्नी बयान उनके बिना मुकम्मल नहीं, और उनका बयान 5 हिजरी के बिना नहीं।

किसी भी सरज़मीन की महारत, पीठ की मोहर, और ज़मीन की खंदक एक ज़िंदगी की तीन निशानियाँ हैं। बच्चे इकट्ठे याद करते हैं। رضي الله عنه।""",
    """৫ হিজরি / ৬২৭ খ্রি. কুরাইশ, গাতাফান ও খাইবারের কক্ষপথের ইহুদি মিত্ররা মদিনায় অভিযান করে। শহরের উত্তরে প্রাচীর ছিল না। সালমান رضي الله عنه এমন প্রশস্ত গভীর পরিখা পরামর্শ দেন যে অশ্বারোহী ডিঙাতে না পারে। নবী ﷺ মুহাজির ও আনসার দলকে অংশ দেন। তিনি নিজে কাটেন ও রজজ পাঠ করেন। ইবন হিশাম শীত, ক্ষুধা এবং সেই শিলা বর্ণনা করেন যা নবী ﷺ তিন স্ফুলিঙ্গে আঘাত করেন, বিজয়ের প্রতিশ্রুতি।

মিত্র অশ্ব পরিখায় এসে পার হতে পারে না। আমর ইবন আব্দ ওয়াদ্দ ও কয়েকজন সংকীর্ণ স্থান দিয়ে লাফায়, মোকাবিলা হয়; আলী رضي الله عنه প্রসিদ্ধ দ্বন্দ্বে আমরকে নিহত করেন। অবরোধ সপ্তাহব্যাপী। নুআয়ম ইবন মাসউদ মিত্রদের মধ্যে অবিশ্বাস বোনেন। তীব্র বায়ু, কুরআনে আল্লাহর বাহিনী (আল-আহজাব), তাঁবু উড়িয়ে নিয়ে যায়। পারস্য দক্ষতার পরিখা অন্য উপায়গুলোকে সময় দেয়।

ঘটনা এই দলিল হিসেবে পড়ানো হয় যে যে কোনো দেশের উপযোগী কৌশল দীনের সেবা করতে পারে যদি শরিয়ার বিরোধী না হয়। মদিনার আরবরা আজমি বলে প্রত্যাখ্যান করেনি। নবী ﷺ পরামর্শ সম্মান করেন। পরবর্তী ফকিহরা খন্দক উদ্ধৃত করেন সামরিক প্রকৌশল, রাতের প্রহর এবং যুদ্ধেও শূরা আলোচনায়।

নবী ﷺ-এর বাক্যে সালমানের আহলুল বায়তভুক্তি নতুন বংশতালিকা নয়; ভালোবাসা ও অন্তর্ভুক্তি। সুন্নি ভাষ্যকার একে সম্মানসূচক সম্পর্ক বলেন, যেমন সালমান মিন্না। আহলুস সুন্নাহর সাধারণ ফিকহে বনু হাশিমের মীরাসের নিয়ম বদলাতে এটি ব্যবহৃত হয় না।

বিপদ কেটে গেলে পরিখা ভরা হয়; শিক্ষা থাকে। মদিনা শেখে রক্ষা খাদে সবরও হতে পারে ঘোড়ার হামলার মতো। কুরআনের সূরা আহজাব চোখ ও হৃদয়ের ভয় তারপর বায়ু প্রেরণ স্মরণ করায়। সালমানের নাম সিরাতের প্রতিটি শ্রেণিতে সেই সূরার সঙ্গে বাঁধা।

বিশ্বকোষ তাই মানুষ ও খাদ জোড়ে: পারস্যের অন্বেষক, দাস যিনি ভালোবাসায় পরিজন হন, উপদেষ্টা যাঁর কথা রাসূল ﷺ নেন। খন্দকের কোনো সুন্নি বর্ণনা তাঁকে ছাড়া সম্পূর্ণ নয়, তাঁর বর্ণনা ৫ হিজরি ছাড়া নয়।

যে কোনো দেশের দক্ষতা, পিঠের মোহর ও মাটির পরিখা এক জীবনের তিন নিদর্শন। শিশুরা একসঙ্গে মুখস্থ করে। رضي الله عنه।""",
    """Pada 5 H / 627 M konfederasi Quraisy, Ghatafan, dan sekutu Yahudi dari orbit Khaibar maju ke Madinah. Kota tidak punya tembok di utara. Salman رضي الله عنه menasihati parit lebar dan dalam sehingga kavaleri tidak bisa meloncatinya. Nabi ﷺ membagi bagian kepada tim Muhajirin dan Ansar. Beliau sendiri menggali dan membaca rajaz. Ibnu Hisyam menggambarkan dingin, lapar, dan batu yang dipukul Nabi ﷺ dengan tiga percikan janji pembukaan.

Kuda konfederasi sampai ke parit dan tidak bisa menyeberang. Amr bin Abd Wudd dan beberapa orang meloncat di tempat sempit dan dihadang; Ali رضي الله عنه membunuh Amr dalam duel masyhur. Pengepungan berlangsung berminggu-minggu. Nu'aim bin Mas'ud menabur curiga di antara sekutu. Angin pahit, disebut dalam Al-Qur'an sebagai bala tentara Allah (al-Ahzab), menyerakkan tenda. Parit, keterampilan Persia, memberi waktu bagi sarana lain itu.

Episode ini diajarkan sebagai dalil bahwa teknik berguna dari negeri mana pun boleh melayani agama jika tidak menyalahi syariat. Orang Arab Madinah tidak menolak gagasan itu karena 'ajami. Nabi ﷺ memuliakan nasihat itu. Fukaha kemudian menukil Khandaq ketika membahas rekayasa militer, jaga malam, dan syura bahkan dalam perang.

Keterikatan Salman kepada Ahlulbait dalam sabda Nabi ﷺ bukan nasab baru; itu cinta dan inklusi. Pensyarah Ahlusunah menjelaskannya sebagai nisbah kehormatan, seperti ucapan Salman termasuk kami. Ia tidak dipakai dalam fikih arus utama Ahlusunah untuk menulis ulang aturan waris Bani Hasyim.

Parit ditimbun setelah bahaya berlalu; pelajarannya tetap. Madinah belajar bahwa pertahanan bisa berupa sabar di parit sekaligus serbuan kuda. Surah al-Ahzab dalam Al-Qur'an mengabadikan ketakutan mata dan hati, lalu pengiriman angin. Nama Salman terikat pada surah itu di setiap kelas sirah.

Ensiklopedia karena itu memasangkan orang dan parit: pencari dari Persia, budak yang menjadi kerabat dalam cinta, penasihat yang gagasannya diambil Rasul ﷺ. Tidak ada kisah Ahlusunah tentang Khandaq yang lengkap tanpanya, dan tidak ada kisah tentangnya yang lengkap tanpa 5 H.

Keterampilan negeri mana pun, meterai di punggung, dan parit di bumi adalah tiga tanda satu hidup. Anak-anak menghafalnya bersama. رضي الله عنه.""",
)

# --- 8 Khalid ibn al-Walid ---
ch = chapter(8)
ch["details"] = D(
    """Khalid ibn al-Walid ibn al-Mughirah رضي الله عنه was from Banu Makhzum of Quraysh, a house of horsemen and banners. Ibn Sa'd describes him as a master of tactics before and after Islam. Until Uhud he fought the Muslims; his cavalry on that day turned the battle when the archers left their post. Sunni history records this without shame-erasure and without eternal condemnation: he was then an unbeliever, and Allah later opened his heart.

He accepted Islam around 8 AH / 629 CE, after Hudaybiyyah, together in the famous cluster of conversions with Amr ibn al-As and Uthman ibn Talha رضي الله عنهم. He came to Madinah, and the Prophet ﷺ received him. The Messenger ﷺ named him Sayf Allah, the Sword of Allah, and prayed that he not be killed by an enemy's blade in a report that later seemed fulfilled when he died on his bed. That title is not a claim that victory is from other than Allah; Umar later reminded the people of that very point.

At Mu'tah in Jumada al-Ula 8 AH / September 629 CE, against a much larger Byzantine-allied force in the Balqa' of Sham, the three appointed commanders—Zayd ibn Harithah, Ja'far ibn Abi Talib, and Abdullah ibn Rawahah رضي الله عنهم—were killed in succession. Khalid took the standard, reorganised the wings, and withdrew the army with skill. The Prophet ﷺ in Madinah described the sequence as if seeing it, and praised the preservation of the force as a victory of a kind.

He fought at the Conquest of Makkah, at Hunayn, and at Ta'if. In the Riddah under Abu Bakr he was among the principal commanders against the apostate concentrations, including the hard fighting of Yamamah. Under Abu Bakr and the first years of Umar he led in Iraq then in Syria. Yarmuk in 15 AH / 636 CE, whether as overall field commander or as the mind of the battle in the reports, is bound to his name. The openings of Damascus and other towns of Sham fill the pages of al-Tabari and al-Baladhuri.

Umar رضي الله عنه later removed him from overall command, appointing Abu Ubaydah ibn al-Jarrah رضي الله عنه, so that the people would not attach victory to a man. Khalid obeyed. Sunni encyclopedias treat this as the justice of Umar and the discipline of Khalid, not as a stain on either Companion. He continued to fight under others until he was retired to Homs (Hims).

He died in Homs around 21 AH / 642 CE. He wept that he had sought shahadah in every battle yet died on his bed as a camel dies, while he had wanted to die by the sword. His shroud was the clothes he owned; reports say his horse and weapons were all he left. He is buried in Homs, and his mausoleum is famous. The Prophet's ﷺ title remained on his grave in the memory of the ummah.

Ahl al-Sunnah honour the Sword of Allah without making him a rival to the Rashidun or a villain of Uhud after tawbah. His life is the arc from the cavalry of Makhzum against Madinah to the cavalry of Islam in Sham, closed by a death that taught that martyrdom is by Allah's decree, not by a general's wish.""",
    """خالد بن ولید بن مغیرہ رضی اللہ عنہ قریش کے بنو مخزوم سے تھے، گھڑسواروں اور جھنڈوں کا گھرانا۔ ابن سعد انہیں اسلام سے پہلے اور بعد حرب کے ماہر بیان کرتے ہیں۔ احد تک مسلمانوں سے لڑے؛ اس دن ان کی گھڑسوار نے پلٹا دیا جب تیراندازوں نے چوکی چھوڑی۔ سنی تاریخ اسے مٹائے بغیر اور ابدی لعنت کے بغیر لکھتی ہے: تب کافر تھے، پھر اللہ نے دل کھولا।

تقریباً 8ھ / 629ء حدیبیہ کے بعد اسلام لائے، عمرو بن عاص اور عثمان بن طلحہ رضی اللہ عنہم کے مشہور گروپ کے ساتھ۔ مدینہ آئے، نبی ﷺ نے استقبال کیا۔ رسول ﷺ نے سیف اللہ نام دیا، اللہ کی تلوار، اور دعا کی کہ دشمن کی دھار سے نہ ماریں، ایک روایت جو بعد میں بستر پر وفات سے پوری دکھائی دی۔ یہ لقب فتح کا غیر اللہ سے دعویٰ نہیں؛ عمر نے بعد میں لوگوں کو یہی بات یاد دلائی۔

جمادی الاولیٰ 8ھ / ستمبر 629ء موتہ میں بلقاء شام کی بہت بڑی رومی اتحادی فوج کے مقابل تین مقرر کمانڈر—زید بن حارثہ، جعفر بن ابی طالب، عبد اللہ بن رواحہ رضی اللہ عنہم—باری باری شہید ہوئے۔ خالد نے جھنڈا سنبھالا، بازو سنوارے، مہارت سے لشکر واپس لیا۔ نبی ﷺ نے مدینہ میں جیسے دیکھ رہے ہوں سلسلہ بیان کیا، اور فوج کی حفاظت کو ایک فتح قرار دیا۔

فتح مکہ، حنین، طائف میں لڑے۔ ابو بکر کے ردّہ میں مرتد اجتماعات کے خلاف اصل کمانڈروں میں رہے، یمامہ کی سخت لڑائی سمیت۔ ابو بکر اور عمر کے پہلے برسوں میں عراق پھر شام کی قیادت کی۔ یرموک 15ھ / 636ء، مجموعی کمان ہو یا روایتوں میں جنگ کا دماغ، ان کے نام سے بندھا ہے۔ دمشق اور شام کے دیگر قصبات کی فتوحات طبری و بلاذری کے اوراق بھرتی ہیں۔

عمر رضی اللہ عنہ نے بعد میں مجموعی کمان ہٹا کر ابو عبیدہ بن جراح رضی اللہ عنہ مقرر کیے تاکہ لوگ فتح آدمی سے نہ باندھیں۔ خالد نے اطاعت کی۔ سنی دائرۃ المعارف اسے عمر کا عدل اور خالد کی ضبط کہتی ہیں، کسی صحابی داغ نہیں۔ دوسروں کے نیچے لڑتے رہے یہاں تک حمص ریٹائر ہوئے۔

حمص میں تقریباً 21ھ / 642ء وفات۔ روئے کہ ہر جنگ میں شہادت چاہی بستر پر اونٹ کی موت مری، تلوار سے مرنا چاہتے تھے۔ کفن وہ کپڑے جو پاس تھے؛ روایات کہتی ہیں گھوڑا اور ہتھیار ہی چھوڑے۔ حمص دفن، مزار مشہور۔ نبی ﷺ کا لقب امت کی یاد میں قبر پر رہا۔

اہل سنت سیف اللہ کو عزت دیتے ہیں بغیر خلفائے راشدین کا حریف یا توبہ کے بعد احد کا ولن بنائے۔ زندگی مخزوم کی گھڑسوار سے جو مدینہ کے خلاف تھی اسلام کی گھڑسوار تک شام میں، موت پر بند جو سکھاتی ہے شہادت اللہ کے فیصلے سے ہے جرنیل کی خواہش سے نہیں۔""",
    """ख़ालिद इब्न अल-वलीद इब्न अल-मुग़ीरा رضي الله عنه कुरैश के बनू मख़ज़ूम से थे, घुड़सवारों और झंडों का घराना। इब्न साद उन्हें इस्लाम से पहले और बाद हर्ब के माहिर बयान करते हैं। उहुद तक मुसलमानों से लड़े; उस दिन उनकी घुड़सवार ने पलटा दिया जब तीरंदाज़ों ने चौकी छोड़ी। सुन्नी तारीख़ इसे मिटाए बिना और अबदी लानत के बिना लिखती है: तब काफ़िर थे, फिर अल्लाह ने दिल खोला।

क़रीब 8 हिजरी / 629 ई. हुदैबिया के बाद इस्लाम लाए, अम्र बिन आस और उस्मान बिन तलहा رضي الله عنهم के मशहूर समूह के साथ। मदीना आए, नबी ﷺ ने इस्तिक़बाल किया। रसूल ﷺ ने सैफुल्लाह नाम दिया, अल्लाह की तलवार, और दुआ की कि दुश्मन की धार से न मारें, एक रिवायत जो बाद में बिस्तर पर वफ़ात से पूरी दिखाई दी। यह लक़ब फ़तह का ग़ैर अल्लाह से दावा नहीं; उमर ने बाद में लोगों को यही बात याद दिलाई।

जमादीउल ऊला 8 हिजरी / सितंबर 629 ई. मूताह में बलक़ा-ए-शाम की बहुत बड़ी रूमी इत्तिहादी फ़ौज के मुक़ाबिल तीन मुक़र्रर कमांडर—ज़ैद बिन हारिसा, जाफ़र बिन अबी तालिब, अब्दुल्लाह बिन रवाहा رضي الله عنهم—बारी बारी शहीद हुए। ख़ालिद ने झंडा संभाला, बाज़ू संवारे, महारत से लश्कर वापस लिया। नबी ﷺ ने मदीना में जैसे देख रहे हों सिलसिला बयान किया, और फ़ौज की हिफ़ाज़त को एक फ़तह क़रार दिया।

फत्हे मक्का, हुनैन, ताइफ़ में लड़े। अबू बक्र के रिद्दा में मुर्तद इज्तिमाआत के ख़िलाफ़ असल कमांडरों में रहे, यमामा की सख़्त लड़ाई समेत। अबू बक्र और उमर के पहले बरसों में इराक फिर शाम की क़ियादत की। यरमूक 15 हिजरी / 636 ई., मज्मूई कमान हो या रिवायात में जंग का दिमाग़, उनके नाम से बंधा है। दिमश्क और शाम के अन्य कसबों की फ़ुतूहात तबरी व बलाज़ुरी के औराक़ भरती हैं।

उमर رضي الله عنه ने बाद में मज्मूई कमान हटा कर अबू उबैदा बिन जर्राह رضي الله عنه मुक़र्रर किए ताकि लोग फ़तह आदमी से न बाँधें। ख़ालिद ने इताअत की। सुन्नी दाइरतुल मआरिफ़ इसे उमर का अदल और ख़ालिद की ज़ब्त कहती हैं, किसी सहाबी दाग़ नहीं। दूसरों के नीचे लड़ते रहे यहाँ तक होम्स में फ़ारिग़ हुए।

होम्स में क़रीब 21 हिजरी / 642 ई. वफ़ात। रोए कि हर जंग में शहादत चाही बिस्तर पर ऊँट की मौत मरे, तलवार से मरना चाहते थे। कफ़न वह कपड़े जो पास थे; रिवायात कहती हैं घोड़ा और हथियार ही छोड़े। होम्स दफ़न, मज़ार मशहूर। नबी ﷺ का लक़ब उम्मत की याद में क़ब्र पर रहा।

अहले सुन्नत सैफुल्लाह को इज़्ज़त देते हैं बिना ख़ुलफ़ा-ए-राशिदीन का हरीफ़ या तौबा के बाद उहुद का विलन बनाए। ज़िंदगी मख़ज़ूम की घुड़सवार से जो मदीना के ख़िलाफ़ थी इस्लाम की घुड़सवार तक शाम में, मौत पर बंद जो सिखाती है शहादत अल्लाह के फ़ैसले से है जरनैल की ख़्वाहिश से नहीं।""",
    """খালিদ ইবন আল-ওয়ালিদ ইবন আল-মুগিরাহ رضي الله عنه কুরাইশের বনু মাখজুমের, অশ্বারোহী ও পতাকার ঘর। ইবন সাদ তাঁকে ইসলামের আগে ও পরে যুদ্ধকৌশলের ওস্তাদ বলেন। উহুদ পর্যন্ত মুসলিমদের বিপক্ষে যুদ্ধ করেন; সেদিন তাঁর অশ্বারোহী যুদ্ধ ঘুরিয়ে দেয় যখন ধনুর্ধরেরা চৌকি ছাড়ে। সুন্নি ইতিহাস এ কথা মুছে না এবং চিরনিন্দা ছাড়া লেখে: তখন তিনি কাফির ছিলেন, পরে আল্লাহ হৃদয় খুলে দেন।

প্রায় ৮ হিজরি / ৬২৯ খ্রি. হুদায়বিয়ার পর ইসলাম গ্রহণ করেন, আমর ইবনুল আস ও উসমান ইবন তালহা رضي الله عنهم-এর প্রসিদ্ধ দলের সঙ্গে। মদিনায় আসেন, নবী ﷺ অভ্যর্থনা করেন। রাসূল ﷺ তাঁকে সাইফুল্লাহ নাম দেন, আল্লাহর তলোয়ার, এবং দোয়া করেন শত্রুর ধার তাঁকে যেন না মারে—এক বর্ণনা যা পরে বিছানায় মৃত্যুতে পূর্ণ বলে মনে হয়। এই উপাধি বিজয় অন্য কারো থেকে দাবি নয়; উমর পরে মানুষকে সে কথাই মনে করান।

জুমাদাল উলা ৮ হিজরি / সেপ্টেম্বর ৬২৯ মুতাহে শামের বালকার অনেক বড় রোমান মিত্রবাহিনীর বিপক্ষে তিন নিযুক্ত সেনাপতি—যায়েদ ইবন হারিসাহ, জাফর ইবন আবি তালিব, আব্দুল্লাহ ইবন রাওয়াহা رضي الله عنهم—পরপর শহীদ হন। খালিদ পতাকা নেন, বাহু পুনর্গঠন করেন, দক্ষতায় সেনা ফিরিয়ে আনেন। নবী ﷺ মদিনায় যেন দেখছেন এমন করে ধারা বলেন, এবং বাহিনী রক্ষাকে এক ধরনের বিজয় বলেন।

মক্কা বিজয়, হুনাইন, তাইফে যুদ্ধ করেন। আবু বকরের রিদ্দায় মুরতাদ কেন্দ্রগুলোর বিরুদ্ধে প্রধান সেনাপতিদের মধ্যে থাকেন, ইয়ামামার কঠিন লড়াইসহ। আবু বকর ও উমরের প্রথম বছরগুলোতে ইরাক তারপর শামে নেতৃত্ব দেন। ইয়ারমুক ১৫ হিজরি / ৬৩৬, সামগ্রিক সেনাপতি হোন বা বর্ণনায় যুদ্ধের মस्तिष्क, তাঁর নামের সঙ্গে বাঁধা। দামেশক ও শামের অন্য নগরীর বিজয় তাবারি ও বালাজুরির পাতা ভরে।

উমর رضي الله عنه পরে সামগ্রিক কমান্ড সরিয়ে আবু উবায়দাহ ইবনুল জাররাহ رضي الله عنه নিয়োগ করেন যাতে মানুষ বিজয় এক ব্যক্তির সঙ্গে না বাঁধে। খালিদ আনুগত্য করেন। সুন্নি বিশ্বকোষ একে উমরের ন্যায় ও খালিদের সংযম বলে, কোনো সাহাবির দাগ নয়। অন্যের অধীনে যুদ্ধ করতে থাকেন হোমসে অবসর পর্যন্ত।

হোমসে প্রায় ২১ হিজরি / ৬৪২ ইন্তেকাল। কাঁদেন যে প্রতি যুদ্ধে শাহাদাত চেয়েছিলেন তবু উটের মতো বিছানায় মরলেন, তলোয়ারে মরতে চেয়েছিলেন। কাফন যে কাপড় ছিল; বর্ণনায় ঘোড়া ও অস্ত্রই রেখে যান। হোমসে দাফন, মাজার প্রসিদ্ধ। নবী ﷺ-এর উপাধি উম্মাহর স্মৃতিতে কবরে থাকে।

আহলুস সুন্নাহ সাইফুল্লাহকে সম্মান করে তাঁকে রাশিদুনের প্রতিদ্বন্দ্বী বা তওবার পর উহুদের খলনায়ক না বানিয়ে। জীবন মাখজুমের অশ্বারোহী থেকে যা মদিনার বিপক্ষে ছিল ইসলামের অশ্বারোহী পর্যন্ত শামে, মৃত্যুতে বন্ধ যা শেখায় শাহাদাত আল্লাহর ফয়সালা, সেনাপতির ইচ্ছা নয়।""",
    """Khalid bin al-Walid bin al-Mughirah رضي الله عنه berasal dari Bani Makhzum Quraisy, rumah penunggang kuda dan panji. Ibnu Sa'd menggambarkannya sebagai ahli taktik sebelum dan sesudah Islam. Hingga Uhud ia memerangi kaum muslimin; kavalerinya pada hari itu membalikkan pertempuran ketika para pemanah meninggalkan pos. Sejarah Ahlusunah mencatat ini tanpa menghapus malu dan tanpa pengutukan abadi: ia ketika itu kafir, lalu Allah membuka hatinya.

Ia masuk Islam sekitar 8 H / 629 M, setelah Hudaibiyah, bersama kelompok pertobatan masyhur dengan Amr bin al-As dan Utsman bin Thalhah رضي الله عنهم. Ia datang ke Madinah, dan Nabi ﷺ menerimanya. Rasul ﷺ menamainya Saifullah, Pedang Allah, dan berdoa agar ia tidak dibunuh bilah musuh dalam riwayat yang kemudian tampak terpenuhi ketika ia mati di pembaringannya. Gelar itu bukan klaim bahwa kemenangan dari selain Allah; Umar kemudian mengingatkan orang akan hal itu.

Di Mutah pada Jumadil Ula 8 H / September 629 M, menghadapi pasukan sekutu Bizantium yang jauh lebih besar di Balqa Syam, tiga panglima yang diangkat—Zaid bin Haritsah, Ja'far bin Abi Thalib, dan Abdullah bin Rawahah رضي الله عنهم—gugur bergantian. Khalid mengambil bendera, menata sayap, dan menarik pasukan dengan terampil. Nabi ﷺ di Madinah menuturkan urutannya seolah melihat, dan memuji pelestarian pasukan sebagai semacam kemenangan.

Ia berperang pada Fathu Makkah, Hunain, dan Taif. Dalam Riddah di bawah Abu Bakar ia termasuk panglima utama terhadap konsentrasi murtad, termasuk pertempuran keras Yamamah. Di bawah Abu Bakar dan tahun-tahun awal Umar ia memimpin di Irak lalu di Syam. Yarmuk pada 15 H / 636 M, apakah sebagai panglima lapangan keseluruhan atau sebagai otak pertempuran dalam riwayat, terikat pada namanya. Pembukaan Damaskus dan kota Syam lain memenuhi halaman ath-Thabari dan al-Baladzuri.

Umar رضي الله عنه kemudian mencopotnya dari komando keseluruhan, mengangkat Abu Ubaidah bin al-Jarrah رضي الله عنه, agar orang tidak menautkan kemenangan kepada seorang manusia. Khalid taat. Ensiklopedia Ahlusunah memandang ini sebagai keadilan Umar dan disiplin Khalid, bukan noda pada salah satu Sahabat. Ia terus berperang di bawah orang lain hingga pensiun ke Homs (Hims).

Ia wafat di Homs sekitar 21 H / 642 M. Ia menangis bahwa ia mencari syahid di setiap pertempuran namun mati di pembaringan seperti unta mati, padahal ia ingin mati oleh pedang. Kafannya adalah pakaian yang ia miliki; riwayat menyebutkan kuda dan senjatanya saja yang ditinggalkan. Ia dimakamkan di Homs, dan makamnya terkenal. Gelar Nabi ﷺ tetap pada kuburnya dalam ingatan umat.

Ahlusunah memuliakan Pedang Allah tanpa menjadikannya saingan Khulafaur Rasyidin atau penjahat Uhud setelah tobat. Hidupnya adalah busur dari kavaleri Makhzum melawan Madinah menjadi kavaleri Islam di Syam, ditutup oleh kematian yang mengajar bahwa syahid adalah ketetapan Allah, bukan keinginan seorang jenderal.""",
)
ch["items"][0]["details"] = D(
    """Mu'tah in 8 AH was the first large clash with the Roman frontier. The Prophet ﷺ named Zayd, then Ja'far, then Ibn Rawahah as commanders in order if the one before fell. All three were martyred. Ja'far fought until both arms were cut, a scene the Prophet ﷺ described with wings in Paradise. Ibn Rawahah dismounted from a hesitation of the self and went forward. These three names are inseparable from Khalid's later command.

Khalid took the standard when it was about to fall. He changed the arrangement of the army so that the Romans thought new troops had arrived, then conducted a fighting withdrawal toward Madinah. Nine swords were broken in his hand in one report. The force returned with losses but was not annihilated. In Madinah some called it a defeat; the Prophet ﷺ called it a victory of preservation and prayed for Khalid.

The news of the three martyrs reached the families. The Prophet ﷺ visited the house of Ja'far and took the children. Asma' bint Umays رضي الله عنها cooked for him. These household scenes sit beside the battlefield in the sirah. Sunni teaching holds all four men—the three dead and Khalid living—in honour. There is no rivalry of fame between the martyrs and the Sword of Allah.

The Syrian later career of Khalid, including Yarmuk, grew from that day of learning how to face a larger imperial army. Abu Bakr sent him north after the Riddah. Umar's later administrative decision did not cancel the praise of Mu'tah. Encyclopedias of the Sahaba therefore keep the item titled Mu'tah and Syria as one arc.

Children of the ummah memorise the order of the three commanders as they memorise Badr. They then learn that a late convert reorganised a desperate field. The lesson is shura in appointment, sabr in death, and skill in withdrawal. None of these lessons requires attacking any Companion.

When Khalid died in Homs he still named Mu'tah among the days he had offered his neck and not been taken. The bed in Homs and the dust of Mu'tah are two ends of one dua for shahadah. Allah chose the bed; the ummah still recites the names of Zayd, Ja'far, Ibn Rawahah, and Khalid رضي الله عنهم together.

Thus the item is not only a battle report. It is the Prophet's ﷺ praise of a living general who saved a remnant, and his tears for three friends who did not return. Sunni memory holds both the praise and the tears.""",
    """موتہ 8ھ رومی سرحد سے پہلی بڑی ٹکر تھی۔ نبی ﷺ نے زید، پھر جعفر، پھر ابن رواحہ کمانڈر نامزد کیے ترتیب سے اگر پہلا گرے۔ تینوں شہید ہوئے۔ جعفر لڑے یہاں تک دونوں بازو کٹے، نبی ﷺ نے جنت میں پر بیان کیے۔ ابن رواحہ نفس کے ہچکچاہٹ سے اتر کر آگے بڑھے۔ یہ تین نام خالد کی بعد کی کمان سے الگ نہیں۔

جھنڈا گرنے کو تھا تو خالد نے سنبھالا۔ لشکر کی ترتیب بدلی تاکہ رومی سمجھیں نئی فوج آئی، پھر مدینہ کی طرف لڑتے ہوئے واپسی کی۔ ایک روایت میں نو تلواریں ہاتھ میں ٹوٹیں۔ فوج نقصان کے ساتھ لوٹی مٹ نہ گئی۔ مدینہ کچھ اسے شکست کہتے؛ نبی ﷺ نے حفاظت کی فتح فرمایا اور خالد کے لیے دعا کی۔

تین شہیدوں کی خبر گھرانوں تک پہنچی۔ نبی ﷺ جعفر کے گھر گئے بچے اٹھائے۔ اسماء بنت عمیس رضی اللہ عنہا نے کھانا پکایا۔ یہ گھریلو منظر سیرت میں میدان جنگ کے پاس بیٹھتے ہیں۔ سنی تعلیم چاروں—تین مقتول اور زندہ خالد—کو عزت دیتی ہے۔ شہدا اور سیف اللہ میں شہرت کی رقابت نہیں۔

خالد کا بعد کا شامی دور بشمول یرموک اسی دن سے پھوٹا جب سیکھا بڑی شاہی فوج کا سامنا کیسے۔ ابو بکر نے ردّہ کے بعد شمال بھیجا۔ عمر کا بعد کا انتظامی فیصلہ موتہ کی تعریف منسوخ نہ کرتا۔ صحابہ کے دائرۃ المعارف اس لیے موتہ اور شام کو ایک قوس رکھتے ہیں۔

امت کے بچے تین کمانڈروں کی ترتیب بدر کی طرح یاد کرتے ہیں۔ پھر سیکھتے ہیں دیر سے مسلمان نے ناامید میدان سنوارا۔ سبق تقرری میں شوریٰ، موت میں صبر، واپسی میں مہارت ہے۔ ان اسباق کو کسی صحابی پر حملے کی حاجت نہیں۔

حمص میں وفات پر اب بھی موتہ ان دنوں میں گنواتے جب گردن پیش کی نہ لی گئی۔ حمص کا بستر اور موتہ کی مٹی شہادت کی ایک دعا کے دو سرے ہیں۔ اللہ نے بستر چنا؛ امت اب بھی زید، جعفر، ابن رواحہ اور خالد رضی اللہ عنہم اکٹھے پڑھتی ہے۔

یوں یہ باب صرف جنگ کی رپورٹ نہیں۔ زندہ جرنیل کی تعریف ہے جس نے باقی بچایا، اور تین دوستوں کے آنسو جو نہ لوٹے۔ سنی یاد تعریف اور آنسو دونوں رکھتی ہے۔""",
    """मूताह 8 हिजरी रूमी सरहद से पहली बड़ी टक्कर थी। नबी ﷺ ने ज़ैद, फिर जाफ़र, फिर इब्न रवाहा कमांडर नामज़द किए तरतीब से अगर पहला गिरे। तीनों शहीद हुए। जाफ़र लड़े यहाँ तक दोनों बाज़ू कटे, नबी ﷺ ने जन्नत में पर बयान किए। इब्न रवाहा नफ्स की हिचकिचाहट से उतर कर आगे बढ़े। ये तीन नाम ख़ालिद की बाद की कमान से अलग नहीं।

झंडा गिरने को था तो ख़ालिद ने संभाला। लश्कर की तरतीब बदली ताकि रूमी समझें नई फ़ौज आई, फिर मदीना की तरफ़ लड़ते हुए वापसी की। एक रिवायत में नौ तलवारें हाथ में टूटीं। फ़ौज नुक़सान के साथ लौटी मिट न गई। मदीना कुछ इसे शिकस्त कहते; नबी ﷺ ने हिफ़ाज़त की फ़तह फ़रमाया और ख़ालिद के लिए दुआ की।

तीन शहीदों की ख़बर घरानों तक पहुँची। नबी ﷺ जाफ़र के घर गए बच्चे उठाए। अस्मा बिन्त उमैस رضي الله عنها ने खाना पकाया। ये घरेलू मंज़र सीरत में मैदान-ए-जंग के पास बैठते हैं। सुन्नी तालीम चारों—तीन मक़तूल और ज़िंदा ख़ालिद—को इज़्ज़त देती है। शुहदा और सैफुल्लाह में शुहरत की रक़ाबत नहीं।

ख़ालिद का बाद का शामी दौर बशमूल यरमूक उसी दिन से फूटा जब सीखा बड़ी शाही फ़ौज का सामना कैसे। अबू बक्र ने रिद्दा के बाद शिमाल भेजा। उमर का बाद का इंतिज़ामी फ़ैसला मूताह की तारीफ़ मन्सूख़ न करता। सहाबा के दाइरतुल मआरिफ़ इसलिए मूताह और शाम को एक क़ौस रखते हैं।

उम्मत के बच्चे तीन कमांडरों की तरतीब बद्र की तरह याद करते हैं। फिर सीखते हैं देर से मुस्लिम ने नाउम्मीद मैदान संवारा। सबक़ तक्ररी में शूरा, मौत में सब्र, वापसी में महारत है। इन असबाक़ को किसी सहाबी पर हमले की हाजत नहीं।

होम्स में वफ़ात पर अब भी मूताह उन दिनों में गिनवाते जब गर्दन पेश की न ली गई। होम्स का बिस्तर और मूताह की मिट्टी शहादत की एक दुआ के दो सिरे हैं। अल्लाह ने बिस्तर चुना; उम्मत अब भी ज़ैद, जाफ़र, इब्न रवाहा और ख़ालिद رضي الله عنهم इकट्ठे पढ़ती है।

यूँ यह बाब सिर्फ़ जंग की रिपोर्ट नहीं। ज़िंदा जरनैल की तारीफ़ है जिसने बाक़ी बचाया, और तीन दोस्तों के आँसू जो न लौटे। सुन्नी याद तारीफ़ और आँसू दोनों रखती है।""",
    """মুতাহ ৮ হিজরি রোমান সীমান্তের সঙ্গে প্রথম বড় সংঘর্ষ। নবী ﷺ যায়েদ, তারপর জাফর, তারপর ইবন রাওয়াহাকে সেনাপতি নাম দেন ক্রমে যদি আগেরজন পড়ে। তিনজনই শহীদ হন। জাফর যুদ্ধ করেন দুই বাহু কাটা পর্যন্ত, নবী ﷺ জান্নাতে ডানা বর্ণনা করেন। ইবন রাওয়াহা নফসের দ্বিধা থেকে নেমে এগিয়ে যান। এই তিন নাম খালিদের পরবর্তী কমান্ড থেকে অবিচ্ছেদ্য।

পতাকা পড়তে যাচ্ছিল খালিদ নেন। সেনার বিন্যাস বদলান যাতে রোমানরা নতুন বাহিনী এসেছে ভাবে, তারপর মদিনার দিকে লড়তে লড়তে সরে আসেন। এক বর্ণনায় হাতে নয় তলোয়ার ভাঙে। বাহিনী ক্ষতি নিয়ে ফিরে নিশ্চিহ্ন হয় না। মদিনায় কেউ একে পরাজয় বলে; নবী ﷺ রক্ষার বিজয় বলেন এবং খালিদের জন্য দোয়া করেন।

তিন শহীদের খবর ঘরে পৌঁছায়। নবী ﷺ জাফরের ঘরে যান সন্তান তোলেন। আসমা বিনত উমাইস رضي الله عنها রান্না করেন। এই গৃহস্থলী দৃশ্য সিরাতে যুদ্ধক্ষেত্রের পাশে বসে। সুন্নি শিক্ষা চারজনকে—তিন নিহত ও জীবিত খালিদ—সম্মান করে। শহীদ ও সাইফুল্লাহর মধ্যে খ্যাতির প্রতিদ্বন্দ্বিতা নেই।

খালিদের পরবর্তী শাম পর্ব ইয়ারমুকসহ সেই দিন থেকে ফোটে যখন শিখেন বৃহত্তর সাম্রাজ্যিক সেনার মুখোমুখি হতে। আবু বকর রিদ্দার পর উত্তরে পাঠান। উমরের পরবর্তী প্রশাসনিক সিদ্ধান্ত মুতাহর প্রশংসা বাতিল করে না। সাহাবা বিশ্বকোষ তাই মুতাহ ও শামকে এক চাপ রাখে।

উম্মাহর শিশুরা তিন সেনাপতির ক্রম বদরের মতো মুখস্থ করে। তারপর শেখে দেরিতে মুসলিম নিরাশ ক্ষেত্র পুনর্গঠন করেন। শিক্ষা নিয়োগে শূরা, মৃত্যুতে সবর, প্রত্যাহার দক্ষতা। এ শিক্ষায় কোনো সাহাবিকে আক্রমণ লাগে না।

হোমসে মৃত্যুতে তিনি এখনও মুতাহ সেই দিনগুলোর মধ্যে গণনা করেন যখন গর্দান পেশ করেও নেওয়া হয়নি। হোমসের বিছানা ও মুতাহর ধুলো শাহাদাতের এক দোয়ার দুই প্রান্ত। আল্লাহ বিছানা বেছেছেন; উম্মাহ আজও যায়েদ, জাফর, ইবন রাওয়াহা ও খালিদ رضي الله عنهم একসঙ্গে পাঠ করে।

এভাবে অধ্যায় কেবল যুদ্ধ প্রতিবেদন নয়। জীবিত সেনাপতির প্রশংসা যিনি অবশিষ্ট বাঁচান, এবং তিন বন্ধুর অশ্রু যাঁরা ফেরেননি। সুন্নি স্মৃতি প্রশংসা ও অশ্রু দুই রাখে।""",
    """Mutah pada 8 H adalah benturan besar pertama dengan perbatasan Romawi. Nabi ﷺ menunjuk Zaid, lalu Ja'far, lalu Ibnu Rawahah sebagai panglima berurutan jika yang sebelumnya gugur. Ketiganya syahid. Ja'far berperang hingga kedua lengan terpotong, adegan yang dilukiskan Nabi ﷺ dengan sayap di surga. Ibnu Rawahah turun dari keraguan nafsu dan maju. Tiga nama ini tidak terpisah dari komando Khalid kemudian.

Khalid mengambil bendera ketika hampir jatuh. Ia mengubah susunan pasukan sehingga orang Romawi menyangka pasukan baru tiba, lalu melakukan undur diri sambil bertempur menuju Madinah. Sembilan pedang patah di tangannya dalam satu riwayat. Pasukan kembali dengan kerugian tetapi tidak musnah. Di Madinah sebagian menyebutnya kekalahan; Nabi ﷺ menyebutnya kemenangan pelestarian dan mendoakan Khalid.

Kabar tiga syuhada sampai ke keluarga. Nabi ﷺ mengunjungi rumah Ja'far dan mengangkat anak-anak. Asma binti Umays رضي الله عنها memasak untuk beliau. Adegan rumah tangga ini duduk di samping medan perang dalam sirah. Ajaran Ahlusunah memuliakan keempatnya—tiga yang mati dan Khalid yang hidup. Tidak ada rivalitas ketenaran antara para syuhada dan Pedang Allah.

Karier Syam Khalid kemudian, termasuk Yarmuk, tumbuh dari hari belajar menghadapi tentara kekaisaran yang lebih besar. Abu Bakar mengirimnya ke utara setelah Riddah. Keputusan administratif Umar kemudian tidak membatalkan pujian Mutah. Ensiklopedia Sahabat karena itu menjaga butir berjudul Mutah dan Syam sebagai satu busur.

Anak-anak umat menghafal urutan tiga panglima sebagaimana menghafal Badar. Mereka lalu belajar bahwa seorang mualaf belakangan menata ulang medan yang putus asa. Pelajaran adalah syura dalam penunjukan, sabar dalam kematian, dan keterampilan dalam undur diri. Tidak satu pun pelajaran ini memerlukan menyerang Sahabat mana pun.

Ketika Khalid wafat di Homs ia masih menyebut Mutah di antara hari-hari ia menawarkan lehernya dan tidak diambil. Pembaringan di Homs dan debu Mutah adalah dua ujung satu doa syahid. Allah memilih pembaringan; umat masih membaca nama Zaid, Ja'far, Ibnu Rawahah, dan Khalid رضي الله عنهم bersama.

Dengan demikian butir ini bukan hanya laporan pertempuran. Ia pujian Nabi ﷺ kepada jenderal hidup yang menyelamatkan sisa, dan air mata beliau untuk tiga sahabat yang tidak pulang. Ingatan Ahlusunah memegang pujian dan air mata.""",
)

# --- 9 Abu Hurayrah ---
ch = chapter(9)
ch["details"] = D(
    """Abd al-Rahman ibn Sakhr al-Dawsi رضي الله عنه, known as Abu Hurayrah, was from Daws of Azd in the Yemeni-Hijazi sphere of tribes. Ibn Sa'd records that he accepted Islam in 7 AH / 628 CE, the year of Khaybar, and came to Madinah. The nickname Abu Hurayrah, Father of the Kitten, came from a small cat he carried; the Prophet ﷺ smiled at it. His given names before Islam are discussed in the tabaqat; Abd al-Rahman is the name used after.

He stayed among the People of the Suffah, the poor Companions who lived in the shaded annex of the Prophet's Mosque with little food and no household. Hunger is a constant theme in his own reports: tying a stone on the belly, waiting for a verse of the Quran so as to follow a host home for supper, serving the Prophet ﷺ on the road. He devoted himself to listening. Because he had no shop and no farm, his hours were the mosque and the door of the Messenger ﷺ.

He narrated thousands of hadith, more in number than any other Companion in the later musnads, though the actual uttered words of the Prophet ﷺ are fewer than the isnad-count suggests when repetitions are collapsed. The Prophet ﷺ spread his cloak for him and made du'a that he not forget, as in Bukhari; Abu Hurayrah said he would not forget after that. Sunni hadith science treats him as a thiqa of the first rank. Attacks on his memory are answered in the works of Ibn Kathir, Ibn Hajar, and the classical radd literature without needing to abuse other schools.

He served briefly as governor of Bahrain in the time of Umar رضي الله عنه, then was removed or withdrew according to variant reports, and returned to teaching in Madinah. He lived through the fitnah years without becoming a banner of a party. He taught in the mosque, issued fatwas, and transmitted to a large circle of Tabi'un such as Sa'id ibn al-Musayyab, Ibn Sirin, and Hammam ibn Munabbih, whose sahifa is among the earliest written hadith collections.

He died in Madinah around 57, 58, or 59 AH (c. 676–679 CE), in the caliphate of Mu'awiyah. He was buried in al-Baqi'. Age reports vary; he had spent some fifty years after Khaybar in the service of transmission. Imam al-Bukhari and Imam Muslim filled their sahihayn with his reports through trustworthy chains. To open Bukhari is to meet Abu Hurayrah again and again on wudu', salah, siyam, and zuhd.

Sunni encyclopedias present him as the Companion of hunger and of memory, not as a courtier of power. His Daws origin, his poverty, and his volume of hadith are one story: Allah chose a late-coming, poor man to carry a great share of the sunnah to the ummah. Respect for him is part of respect for the sahih books.

The ummah says رضي الله عنه after his name in every lesson of mustalah al-hadith. Children learn that the man with the kitten sat at the Suffah and did not leave until his chest was a vessel. That is the chapter of Abu Hurayrah in the encyclopedia of the Sahaba.""",
    """عبد الرحمن بن صخر دوسی رضی اللہ عنہ، ابو ہریرہ کے نام سے مشہور، ازد کے دوس سے تھے یمن حجاز کے قبائلی دائرے میں۔ ابن سعد لکھتے ہیں 7ھ / 628ء خیبر والے سال اسلام لائے اور مدینہ آئے۔ کنیت ابو ہریرہ، بلی کے بچے کا باپ، اس بلی سے جو اٹھائے پھرتے؛ نبی ﷺ مسکرائے۔ اسلام سے پہلے نام طبقات میں بحث؛ بعد میں عبد الرحمن استعمال ہوا۔

اصحاب صفہ میں رہے، غریب صحابہ جو مسجد نبوی کے سایہ دار حصے میں کم کھانے اور بے گھر رہتے۔ بھوک ان کی اپنی روایات کا مستقل مضمون: پیٹ پر پتھر باندھنا، آیت کا انتظار تاکہ میزبان کے ساتھ شام کو چلیں، راستے میں نبی ﷺ کی خدمت۔ سننے کے لیے وقف رہے۔ دکان اور کھیت نہ ہونے سے گھڑیاں مسجد اور رسول ﷺ کے دروازے کی ہوئیں۔

ہزاروں احادیث روایت کیں، متاخر مسانید میں تعداد کے اعتبار سے سب صحابہ سے زیادہ، گو رسول ﷺ کے الفاظ تکرار ہٹانے کے بعد سند گن سے کم ہیں۔ نبی ﷺ نے چادر پھیلائی اور دعا کی بھول نہ جائیں، بخاری میں؛ ابو ہریرہ کہتے اس کے بعد نہ بھولے۔ سنی حدیث انہیں اول درجے کا ثقہ مانتی ہے۔ حافظے پر حملوں کا جواب ابن کثیر، ابن حجر اور کلاسیکی رد میں ہے بغیر دوسرے مکاتب کو گالی دیے۔

عمر رضی اللہ عنہ کے عہد میں کچھ عرصہ بحرین کے گورنر رہے، پھر ہٹائے یا خود ہٹے مختلف روایات میں، مدینہ درس کو لوٹے۔ فتنے کے برس پارٹی کا جھنڈا نہ بنے۔ مسجد میں پڑھاتے، فتوے دیتے، سعید بن مسیب، ابن سیرین، ہمام بن منبہ جیسے بڑے تابعین کو منتقل کیا، جن کی صحیفہ ابتدائی تحریری مجموعوں میں سے ہے۔

مدینہ میں تقریباً 57، 58 یا 59ھ (قریب 676–679ء) معاویہ کی خلافت میں وفات۔ بقیع دفن۔ عمر کی روایات مختلف؛ خیبر کے بعد تقریباً پچاس برس نقل کی خدمت میں۔ امام بخاری و مسلم نے صحیحین ان کی روایات سے بھریں ثقہ سندوں سے۔ بخاری کھولنا بار بار ابو ہریرہ سے وضو، نماز، صیام، زہد پر ملنا ہے۔

سنی دائرۃ المعارف انہیں بھوک اور حافظے کا صحابی پیش کرتی ہیں، اقتدار کے درباری نہیں۔ دوسی اصل، فقر، اور حدیث کا حجم ایک داستان: اللہ نے دیر سے آنے والے غریب کو سنت کا بڑا حصہ امت تک پہنچانے کو چنا۔ ان کی عزت صحیح کتابوں کی عزت کا حصہ ہے۔

امت ہر درس مصطلح الحدیث میں نام کے بعد رضی اللہ عنہ کہتی ہے۔ بچے سیکھتے ہیں بلی والا آدمی صفہ بیٹھا اور نہ ہٹا یہاں تک سینہ برتن بنا۔ یہی ابو ہریرہ کا باب صحابہ کے دائرۃ المعارف میں ہے۔""",
    """अब्दुर्रहमान इब्न सख़्र अल-दौसी رضي الله عنه, अबू हुरैरा के नाम से मशहूर, अज़्द के दौस से थे यमन हिजाज़ के क़बाईली दाइरे में। इब्न साद लिखते हैं 7 हिजरी / 628 ई. ख़ैबर वाले साल इस्लाम लाए और मदीना आए। कुन्यत अबू हुरैरा, बिल्ली के बच्चे का बाप, उस बिल्ली से जो उठाए फिरते; नबी ﷺ मुस्कुराए। इस्लाम से पहले नाम तबाक़ात में बहस; बाद में अब्दुर्रहमान इस्तेमाल हुआ।

अस्हाबे सुफ्फा में रहे, ग़रीब सहाबा जो मस्जिद-ए-नबवी के सायादार हिस्से में कम खाने और बेघर रहते। भूख उनकी अपनी रिवायात का मुस्तक़िल मज़मून: पेट पर पत्थर बाँधना, आयत का इंतिज़ार ताकि मेज़बान के साथ शाम को चलें, रास्ते में नबी ﷺ की ख़िदमत। सुनने के लिए वक़्फ़ रहे। दुकान और खेत न होने से घड़ियाँ मस्जिद और रसूल ﷺ के दरवाज़े की हुईं।

हज़ारों अहादीस रिवायत कीं, मुताअख्ख़िर मसानिद में तादाद के ऐतिबार से सब सहाबा से ज़्यादा, गो रसूल ﷺ के अल्फ़ाज़ तकरार हटाने के बाद सनद गिन से कम हैं। नबी ﷺ ने चादर फैलाई और दुआ की भूल न जाएँ, बुख़ारी में; अबू हुरैरा कहते उसके बाद न भूले। सुन्नी हदीस उन्हें अव्वल दर्जे का सिक़ा मानती है। हिफ़्ज़ पर हमलों का जवाब इब्न कसीर, इब्न हजर और क्लासिकी रद्द में है बिना दूसरे मकातिब को गाली दिए।

उमर رضي الله عنه के अहद में कुछ अर्सा बहरीन के गवर्नर रहे, फिर हटाए या ख़ुद हटे मुख़्तलिफ़ रिवायात में, मदीना दर्स को लौटे। फ़ितने के बरस पार्टी का झंडा न बने। मस्जिद में पढ़ाते, फतवे देते, सईद बिन मुसय्यब, इब्न सीरीन, हम्माम बिन मुनब्बिह जैसे बड़े ताबिईन को मुनतक़िल किया, जिनकी सहीफ़ा इब्तिदाई तहरीरि मज्मूओं में से है।

मदीना में क़रीब 57, 58 या 59 हिजरी (लगभग 676–679 ई.) मुआविया की खिलाफ़त में वफ़ात। बक़ीअ दफ़न। उम्र की रिवायात मुख़्तलिफ़; ख़ैबर के बाद क़रीब पचास बरस नक़्ल की ख़िदमत में। इमाम बुख़ारी व मुस्लिम ने सहीहैन उनकी रिवायात से भरीं सिक़ा सनदों से। बुख़ारी खोलना बार बार अबू हुरैरा से वुज़ू, नमाज़, सियाम, ज़ुहद पर मिलना है।

सुन्नी दाइरतुल मआरिफ़ उन्हें भूख और हाफ़ज़े का सहाबी पेश करती हैं, इक़्तिदार के दरबारी नहीं। दौसी अस्ल, फ़क़्र, और हदीस का परिमाण एक दास्तान: अल्लाह ने देर से आने वाले ग़रीब को सुन्नत का बड़ा हिस्सा उम्मत तक पहुँचाने को चुना। उनकी इज़्ज़त सहीह किताबों की इज़्ज़त का हिस्सा है।

उम्मत हर दर्स मुस्तलह अल-हदीस में नाम के बाद رضي الله عنه कहती है। बच्चे सीखते हैं बिल्ली वाला आदमी सुफ्फा बैठा और न हटा यहाँ तक सीना बर्तन बना। यही अबू हुरैरा का बाब सहाबा के दाइरतुल मआरिफ़ में है।""",
    """আব্দুর রহমান ইবন সাখর আদ-দাওসি رضي الله عنه, আবু হুরাইরাহ নামে খ্যাত, আজদের দাওস গোত্রের, ইয়েমেন-হিজাজ গোত্রীয় বৃত্তে। ইবন সাদ লেখেন তিনি ৭ হিজরি / ৬২৮ খ্রি. খাইবারের বছর ইসলাম গ্রহণ করে মদিনায় আসেন। কুনইয়া আবু হুরাইরাহ, বিড়ালছানার পিতা, যে ছানা তিনি বহন করতেন; নবী ﷺ হাসতেন। ইসলামের আগের নাম তাবাকাতে আলোচিত; পরে আব্দুর রহমান ব্যবহৃত।

তিনি আসহাবে সুফফায় থাকেন, দরিদ্র সাহাবিরা যারা নবীর মসজিদের ছায়াঘেরা অংশে অল্প খাবারে গৃহহীন থাকতেন। ক্ষুধা তাঁর নিজ বর্ণনার স্থায়ী বিষয়: পেটে পাথর বাঁধা, আয়াতের অপেক্ষা যাতে মেজবানের সঙ্গে রাতের খাবারে যান, পথে নবী ﷺ-এর খিদমত। শোনার জন্য নিজেকে উৎসর্গ করেন। দোকান ও ক্ষেত না থাকায় ঘণ্টা মসজিদ ও রাসূল ﷺ-এর দরজার হয়।

হাজার হাজার হাদিস বর্ণনা করেন, পরবর্তী মুসনাদে সংখ্যায় অন্য সাহাবির চেয়ে বেশি, যদিও রাসূল ﷺ-এর উচ্চারিত শব্দ পুনরাবৃত্তি বাদ দিলে সনদ-গণনার চেয়ে কম। নবী ﷺ চাদর বিছিয়ে দোয়া করেন তিনি ভুলবেন না, বুখারিতে; আবু হুরাইরাহ বলেন তার পর আর ভোলেননি। সুন্নি হাদিস বিজ্ঞান তাঁকে প্রথম সারির সিকা মানে। স্মৃতির উপর আক্রমণের জবাব ইবন কাসির, ইবন হাজার ও ক্লাসিক রদ্দ সাহিত্যে অন্য মাজহাবকে গালি না দিয়ে।

উমর رضي الله عنه-এর আমলে সংক্ষেপে বাহরাইনের গভর্নর থাকেন, পরে সরানো বা নিজে সরে যান ভিন্ন বর্ণনায়, মদিনায় শিক্ষায় ফিরে। ফিতনার বছরে দলের পতাকা হননি। মসজিদে পড়ান, ফতোয়া দেন, সাঈদ ইবনুল মুসাইয়্যিব, ইবন সিরিন, হাম্মাম ইবন মুনাব্বিহ-এর মতো বড় তাবিঈদের কাছে পৌঁছান, যাঁর সহীফা প্রাচীনতম লিখিত হাদিস সংগ্রহগুলোর একটি।

মদিনায় প্রায় ৫৭, ৫৮ বা ৫৯ হিজরি (আনু. ৬৭৬–৬৭৯) মুয়াবিয়ার খিলাফতে ইন্তেকাল। বাকীতে দাফন। বয়সের বর্ণনা ভিন্ন; খাইবারের পর প্রায় পঞ্চাশ বছর বর্ণনার খিদমতে। ইমাম বুখারি ও মুসলিম সহীহাইন তাঁর বর্ণনায় ভরেন সিকা সনদে। বুখারি খোলা মানে বারবার আবু হুরাইরাহর সঙ্গে ওজু, সালাত, সিয়াম, যুহদে দেখা।

সুন্নি বিশ্বকোষ তাঁকে ক্ষুধা ও স্মৃতির সাহাবি হিসেবে উপস্থাপন করে, ক্ষমতার দরবারি নয়। দাওসি উৎস, দারিদ্র্য ও হাদিসের আয়তন এক কাহিনি: আল্লাহ দেরিতে আসা দরিদ্রকে সুন্নাতের বড় অংশ উম্মাহয় পৌঁছাতে বেছে নেন। তাঁর সম্মান সহীহ গ্রন্থের সম্মানের অংশ।

উম্মাহ মুস্তালাহ আল-হাদিসের প্রতিটি পাঠে নামের পর رضي الله عنه বলে। শিশুরা শেখে বিড়ালওয়ালা মানুষ সুফফায় বসেন এবং সরলেন না যতক্ষণ বুক পাত্র হয়। এটাই আবু হুরাইরাহর অধ্যায় সাহাবা বিশ্বকোষে।""",
    """Abdurrahman bin Sakhr ad-Dawsi رضي الله عنه, dikenal sebagai Abu Hurairah, berasal dari Daws dari Azd di lingkaran kabilah Yaman-Hijaz. Ibnu Sa'd mencatat ia masuk Islam pada 7 H / 628 M, tahun Khaibar, dan datang ke Madinah. Kunyah Abu Hurairah, Bapak Anak Kucing, berasal dari kucing kecil yang ia bawa; Nabi ﷺ tersenyum padanya. Nama diberinya sebelum Islam dibahas dalam tabaqat; Abdurrahman nama yang dipakai sesudahnya.

Ia tinggal di kalangan Ahlus Suffah, Sahabat miskin yang hidup di serambi Masjid Nabawi dengan sedikit makanan dan tanpa rumah tangga. Lapar adalah tema tetap dalam riwayatnya sendiri: mengikat batu di perut, menunggu ayat Al-Qur'an agar mengikuti tuan rumah untuk makan malam, melayani Nabi ﷺ di jalan. Ia menyerahkan diri untuk mendengar. Karena tidak punya toko dan ladang, jam-jamnya adalah masjid dan pintu Rasul ﷺ.

Ia meriwayatkan ribuan hadis, lebih banyak jumlahnya daripada Sahabat lain dalam musnad kemudian, meski lafaz Nabi ﷺ yang diucapkan lebih sedikit daripada hitungan isnad ketika pengulangan diringkas. Nabi ﷺ membentangkan selendangnya untuknya dan berdoa agar ia tidak lupa, sebagaimana dalam Bukhari; Abu Hurairah berkata ia tidak lupa setelah itu. Ilmu hadis Ahlusunah menilainya thiqah tingkat pertama. Serangan terhadap ingatannya dijawab dalam karya Ibnu Katsir, Ibnu Hajar, dan literatur radd klasik tanpa perlu mencela mazhab lain.

Ia sempat menjadi gubernur Bahrain pada masa Umar رضي الله عنه, lalu dicopot atau mengundurkan diri menurut riwayat berbeda, dan kembali mengajar di Madinah. Ia menjalani tahun-tahun fitnah tanpa menjadi panji suatu partai. Ia mengajar di masjid, berfatwa, dan menyampaikan kepada lingkaran besar Tabi'in seperti Said bin al-Musayyab, Ibnu Sirin, dan Hammam bin Munabbih, yang sahifahnya termasuk himpunan hadis tertulis paling awal.

Ia wafat di Madinah sekitar 57, 58, atau 59 H (k. 676–679 M), pada khilafah Muawiyah. Ia dimakamkan di Baqi. Laporan usia berbeda; ia menghabiskan sekitar lima puluh tahun setelah Khaibar dalam khidmah periwayatan. Imam Bukhari dan Imam Muslim memenuhi sahihain mereka dengan riwayatnya melalui sanad terpercaya. Membuka Bukhari berarti berjumpa Abu Hurairah berulang kali tentang wudu, salat, siyam, dan zuhud.

Ensiklopedia Ahlusunah menampilkannya sebagai Sahabat lapar dan ingatan, bukan abdi istana kekuasaan. Asal Daws, kemiskinannya, dan banyaknya hadis adalah satu kisah: Allah memilih orang miskin yang datang belakangan untuk membawa bagian besar sunah kepada umat. Menghormatinya adalah bagian dari menghormati kitab sahih.

Umat mengucapkan رضي الله عنه setelah namanya di setiap pelajaran mustalah hadis. Anak-anak belajar bahwa lelaki dengan anak kucing duduk di Suffah dan tidak pergi hingga dadanya menjadi wadah. Itulah bab Abu Hurairah dalam ensiklopedia Sahabat.""",
)
ch["items"][0]["details"] = D(
    """The Suffah was a shaded area on the qibla or northern side of the Prophet's Mosque, depending on the stage of building, where emigrants and poor men slept who had no family in Madinah. Food came as sadaqah and as the Prophet's ﷺ own share. Abu Hurayrah رضي الله عنه is the most famous of this company, but he was not alone: other names appear in the tabaqat of Ahl al-Suffah. Their poverty was a school, not a romantic tale only.

Hunger and knowledge were paired. A man who ate his fill every day in the markets of Makkah might hear fewer hadith than a man who waited for a date. Abu Hurayrah said he would faint in prayer from hunger. Yet he asked questions, repeated lessons, and stayed when others went to their palms. The Suffah thus became a college of the sunnah before there were named madrasas.

Later, Imam al-Bukhari (d. 256 AH) and Imam Muslim (d. 261 AH) filled their books with his reports always through isnads they judged sound. The chains pass through Tabi'un of Madinah, Basra, and elsewhere. Hammam's sahifa, transmitted from Abu Hurayrah, shows that writing existed beside memory. Sunni usul reject the claim that volume equals invention; they apply jarh and ta'dil to each link.

Students sat around him in the mosque as they had sat around the Prophet ﷺ. He warned them that the one who lies upon the Messenger ﷺ has his seat in the Fire, the hadith he himself narrated. That warning is part of his reliability in Sunni eyes: a fabricator does not spend his life threatening fabricators. Zuhd reports of his simple food continued into old age.

The People of the Suffah are a standing argument against pride of wealth in the ummah. When a child learns Bukhari's first hadith on intention, he soon meets Abu Hurayrah on wudu and on the cat's sa'b. The poor companion and the sahih chain are one pedagogy. Encyclopedias of Sahaba therefore give this item its own heading.

Sunni teaching does not need to attack those who questioned some reports; it answers with isnad and with the consensus of the hadith imams. Abu Hurayrah remains رضي الله عنه, a pillar of the sunnah, and a man who went hungry so that the ummah would be full of knowledge.

The Suffah is gone as a room; it remains as a meaning: sit, listen, eat little, remember much, and pass on with chains. That is the legacy of Ahl al-Suffah and of their most prolific narrator.""",
    """صفہ مسجد نبوی کے قبلہ یا شمالی رخ کا سایہ دار حصہ تھا، تعمیر کے مرحلے کے مطابق، جہاں مہاجر اور غریب سوते جن کا مدینہ میں گھرانا نہ تھا۔ کھانا صدقہ اور نبی ﷺ کے اپنے حصے سے آتا۔ ابو ہریرہ رضی اللہ عنہ اس جماعت کے سب سے مشہور ہیں، اکیले نہیں: اہل صفہ کی طبقات میں اور نام ہیں۔ فقر مدرسہ تھا، صرف رومانوی قصہ نہیں۔

بھوک اور علم جڑے رہے۔ جو مکہ کے بازار روز سیر کھاتا شاید اس سے کم حدیث سنتا جو کھجور کا انتظار کرتا۔ ابو ہریرہ کہتے بھوک سے نماز میں غش آ جاتا۔ پھر بھی سوال کرتے، سبق دہراتے، جب دوسرے باغوں کو جاتے رہتے۔ صفہ یوں سنت کا کالج بنا مدرسوں کے نام سے پہلے।

بعد میں امام بخاری (256ھ) اور امام مسلم (261ھ) نے اپنی کتابیں ان کی روایات سے بھریں جن سندوں کو صحیح جانا۔ سندیں مدینہ، بصرہ وغیرہ کے تابعین سے گزرتی ہیں۔ ہمام کی صحیفہ، ابو ہریرہ سے، دکھاتی ہے لکھائی حافظے کے ساتھ تھی۔ سنی اصول اس دعوے کو رد کرتے ہیں کہ حجم اختراع ہے؛ ہر کڑی پر جرح تعدیل لگاتے ہیں۔

طلبہ مسجد میں ان کے گرد بیٹھتے جیسے نبی ﷺ کے گرد بیٹھے تھے۔ خبردار کرتے جو رسول ﷺ پر جھوٹ بولے اس کا ٹھکانا آگ، وہ حدیث جو خود روایت کی۔ سنی نظر میں یہ ان کی وثاقت کا حصہ: جعلساز جعلسازوں کو دھمکی دے کر عمر نہیں کاٹتا۔ سادہ کھانے کے زہد کی روایات بڑھاپے تک رہیں۔

اہل صفہ امت میں مال کے غرور کے خلاف کھڑی دلیل ہیں۔ بچہ بخاری کی نیت والی پہلی حدیث سیکھے تو جلد ابو ہریرہ سے وضو اور بلی کے صاع پر ملتا ہے۔ غریب صحابی اور صحیح سند ایک تربیت ہیں۔ اس لیے صحابہ کے دائرۃ المعارف اس باب کو الگ عنوان دیتے ہیں۔

سنی تعلیم کچھ روایات پر سوال کرنے والوں پر حملے کی محتاج نہیں؛ سند اور ائمہ حدیث کے اجماع سے جواب دیتی ہے۔ ابو ہریرہ رضی اللہ عنہ رہتے ہیں، سنت کے ستون، اور وہ آدمی جو بھوکا رہا تاکہ امت علم سے سیر ہو۔

صفہ کمرے کے طور پر نہیں رہی؛ معنی کے طور پر ہے: بیٹھو، سنو، کم کھاؤ، بہت یاد رکھو، سندوں سے آگے پہنچاؤ۔ یہی اہل صفہ اور ان کے سب سے کثیر راوی کی میراث ہے۔""",
    """सुफ्फा मस्जिद-ए-नबवी के क़िबला या शिमाली रुख़ का सायादार हिस्सा था, तामीर के मरहले के मुताबिक, जहाँ मुहाजिर और ग़रीब सोते जिनका मदीना में घराना न था। खाना सदक़ा और नबी ﷺ के अपने हिस्से से आता। अबू हुरैरा رضي الله عنه इस जमाअत के सबसे मशहूर हैं, अकेले नहीं: अहले सुफ्फा की तबाक़ात में और नाम हैं। फ़क़्र मदरसा था, सिर्फ़ रोमानवी क़िस्सा नहीं।

भूख और इल्म जुड़े रहे। जो मक्का के बाज़ार रोज़ सेर खाता शायद उससे कम हदीस सुनता जो खजूर का इंतिज़ार करता। अबू हुरैरा कहते भूख से नमाज़ में ग़श आ जाता। फिर भी सवाल करते, सबक़ दोहराते, जब दूसरे बाग़ों को जाते रहते। सुफ्फा यूँ सुन्नत का दारुल उलूम बना मदरसों के नाम से पहले।

बाद में इमाम बुख़ारी (256 हिजरी) और इमाम मुस्लिम (261 हिजरी) ने अपनी किताबें उनकी रिवायात से भरीं जिन सनदों को सहीह जाना। सनदें मदीना, बसरा वग़ैरह के ताबिईन से गुज़रती हैं। हम्माम की सहीफ़ा, अबू हुरैरा से, दिखाती है लिखाई हाफ़ज़े के साथ थी। सुन्नी उसूल इस दावे को रद्द करते हैं कि परिमाण इख़्तिराअ है; हर कड़ी पर जर्ह तादील लगाते हैं।

तलब मस्जिद में उनके गिर्द बैठते जैसे नबी ﷺ के गिर्द बैठे थे। ख़बरदार करते जो रसूल ﷺ पर झूठ बोले उसका ठिकाना आग, वह हदीस जो ख़ुद रिवायत की। सुन्नी नज़र में यह उनकी वसाक़त का हिस्सा: जालसाज़ जालसाज़ों को धमकी दे कर उम्र नहीं काटता। सादा खाने के ज़ुहद की रिवायात बुढ़ापे तक रहीं।

अहले सुफ्फा उम्मत में माल के ग़ुरूर के ख़िलाफ़ खड़ी दलील हैं। बच्चा बुख़ारी की नीयत वाली पहली हदीस सीखे तो जल्द अबू हुरैरा से वुज़ू और बिल्ली के साअ पर मिलता है। ग़रीब सहाबी और सहीह सनद एक तरबियत हैं। इसलिए सहाबा के दाइरतुल मआरिफ़ इस बाब को अलग उनवान देते हैं।

सुन्नी तालीम कुछ रिवायात पर सवाल करने वालों पर हमले की मुहताज नहीं; सनद और आइम्मा-ए-हदीस के इजमा से जवाब देती है। अबू हुरैरा رضي الله عنه रहते हैं, सुन्नत के सुतून, और वह आदमी जो भूखा रहा ताकि उम्मत इल्म से सेर हो।

सुफ्फा कमरे के तौर पर नहीं रही; मानी के तौर पर है: बैठो, सुनो, कम खाओ, बहुत याद रखो, सनदों से आगे पहुँचाओ। यही अहले सुफ्फा और उनके सबसे कसीर रावी की मीरास है।""",
    """সুফফা ছিল নবীর মসজিদের কিবলা বা উত্তর দিকের ছায়াঘেরা অংশ, নির্মাণের পর্যায় অনুসারে, যেখানে মুহাজির ও দরিদ্র পুরুষ ঘুমাতেন যাঁদের মদিনায় পরিবার ছিল না। খাবার আসত সদকা ও নবী ﷺ-এর নিজ অংশ থেকে। আবু হুরাইরাহ رضي الله عنه এই দলের সর্বাধিক প্রসিদ্ধ, একা নন: আহলুস সুফফার তাবাকাতে অন্য নাম আছে। দারিদ্র্য ছিল মাদরাসা, কেবল রোমান্টিক কাহিনি নয়।

ক্ষুধা ও ইলম জোড়া ছিল। যে মক্কার বাজারে প্রতিদিন তৃপ্ত খেত সে হয়তো তার চেয়ে কম হাদিস শুনত যে খেজুরের অপেক্ষা করত। আবু হুরাইরাহ বলেন ক্ষুধায় নামাজে অচেতন হতেন। তবু প্রশ্ন করতেন, পাঠ আবৃত্তি করতেন, অন্যরা বাগানে গেলেও থাকতেন। সুফফা এভাবে সুন্নাতের কলেজ হয় মাদরাসার নামের আগে।

পরে ইমাম বুখারি (২৫৬ হিজরি) ও ইমাম মুসলিম (২৬১ হিজরি) তাঁদের গ্রন্থ তাঁর বর্ণনায় ভরেন যে সনদ তাঁরা সহীহ জানেন। সনদ মদিনা, বসরা প্রভৃতির তাবিঈদের দিয়ে যায়। হাম্মামের সহীফা, আবু হুরাইরাহ থেকে, দেখায় লেখা স্মৃতির পাশে ছিল। সুন্নি উসূল এই দাবি প্রত্যাখ্যান করে যে আয়তন মানে উদ্ভাবন; প্রতি কড়িতে জারহ ও তাদীল প্রয়োগ করে।

শিক্ষার্থীরা মসজিদে তাঁর চারপাশে বসত যেমন নবী ﷺ-এর চারপাশে বসত। তিনি সতর্ক করতেন যে রাসূল ﷺ-এর উপর মিথ্যা বললে তার ঠিকানা আগুন, যে হাদিস তিনি নিজে বর্ণনা করেন। সুন্নি দৃষ্টিতে এটি তাঁর নির্ভরযোগ্যতার অংশ: জালকারী জালকারীদের হুমকি দিয়ে জীবন কাটায় না। সাদাসিধে খাবারের যুহদ বর্ণনা বার্ধক্য পর্যন্ত চলে।

আহলুস সুফফা উম্মাহয় সম্পদের অহংকারের বিরুদ্ধে দাঁড়ানো দলিল। শিশু বুখারির নিয়তের প্রথম হাদিস শিখলে শীঘ্র আবু হুরাইরাহর সঙ্গে ওজু ও বিড়ালের সাআতে দেখা পায়। দরিদ্র সাহাবি ও সহীহ সনদ এক শিক্ষাপদ্ধতি। তাই সাহাবা বিশ্বকোষ এই অধ্যায়ে আলাদা শিরোনাম দেয়।

সুন্নি শিক্ষার কিছু বর্ণনায় প্রশ্নকারীদের আক্রমণের প্রয়োজন নেই; সনদ ও হাদিস ইমামদের ইজমা দিয়ে জবাব দেয়। আবু হুরাইরাহ رضي الله عنه থাকেন, সুন্নাতের স্তম্ভ, এবং সেই মানুষ যিনি ক্ষুধার্ত থাকেন যাতে উম্মাহ ইলমে তৃপ্ত হয়।

সুফফা ঘর হিসেবে নেই; অর্থ হিসেবে আছে: বসো, শোনো, কম খাও, বেশি মনে রাখো, সনদ দিয়ে পৌঁছে দাও। এটাই আহলুস সুফফা ও তাঁদের সর্বাধিক বর্ণনাকারীর উত্তরাধিকার।""",
    """Suffah adalah area teduh di sisi kiblat atau utara Masjid Nabawi, tergantung tahap bangunan, tempat muhajirin dan orang miskin tidur yang tidak punya keluarga di Madinah. Makanan datang sebagai sedekah dan sebagai bagian Nabi ﷺ sendiri. Abu Hurairah رضي الله عنه adalah yang paling terkenal dari kelompok ini, tetapi ia tidak sendirian: nama lain muncul dalam tabaqat Ahlus Suffah. Kemiskinan mereka adalah sekolah, bukan sekadar kisah romantis.

Lapar dan ilmu dipasangkan. Orang yang kenyang setiap hari di pasar Makkah mungkin mendengar lebih sedikit hadis daripada orang yang menunggu sebutir kurma. Abu Hurairah berkata ia pingsan dalam salat karena lapar. Namun ia bertanya, mengulang pelajaran, dan tinggal ketika yang lain pergi ke kebun kurma. Suffah dengan demikian menjadi perguruan sunah sebelum ada madrasah bernama.

Kemudian Imam Bukhari (w. 256 H) dan Imam Muslim (w. 261 H) memenuhi kitab mereka dengan riwayatnya selalu melalui isnad yang mereka nilai sahih. Sanad melewati Tabi'in Madinah, Basrah, dan tempat lain. Sahifah Hammam, diriwayatkan dari Abu Hurairah, menunjukkan tulisan ada di samping hafalan. Usul Ahlusunah menolak klaim bahwa banyaknya riwayat sama dengan rekaan; mereka menerapkan jarh dan ta'dil pada setiap mata rantai.

Murid duduk di sekelilingnya di masjid sebagaimana mereka duduk di sekeliling Nabi ﷺ. Ia memperingatkan bahwa siapa yang berdusta atas Rasul ﷺ tempatnya di Neraka, hadis yang ia sendiri riwayatkan. Peringatan itu bagian dari keandalannya di mata Ahlusunah: pemalsu tidak menghabiskan hidup mengancam pemalsu. Riwayat zuhud makanan sederhananya berlanjut hingga usia tua.

Ahlus Suffah adalah hujah tegak menentang sombong harta di umat. Ketika anak belajar hadis pertama Bukhari tentang niat, ia segera berjumpa Abu Hurairah tentang wudu dan tentang sa' kucing. Sahabat miskin dan sanad sahih adalah satu pedagogi. Ensiklopedia Sahabat karena itu memberi butir ini judul sendiri.

Ajaran Ahlusunah tidak perlu menyerang orang yang mempertanyakan sebagian riwayat; ia menjawab dengan isnad dan dengan ijmak imam hadis. Abu Hurairah tetap رضي الله عنه, tiang sunah, dan orang yang lapar agar umat kenyang ilmu.

Suffah telah hilang sebagai ruangan; ia tetap sebagai makna: duduk, dengar, makan sedikit, ingat banyak, dan teruskan dengan sanad. Itulah warisan Ahlus Suffah dan perawi paling produktif mereka.""",
)

# --- 10 Fatimah al-Zahra ---
ch = chapter(10)
ch["details"] = D(
    """Fatimah al-Zahra رضي الله عنها was the youngest daughter of the Prophet Muhammad ﷺ and Khadijah bint Khuwaylid رضي الله عنها, born in Makkah about five years before the mission or, in other reports, later in the Makkan period; historians differ on the year but not on her rank. She was the most beloved of his children in the famous reports: he said she is a part of me; what hurts her hurts me. Ibn Sa'd and the books of shamail record his standing when she entered, his kiss, and his seating her beside him.

She married Ali ibn Abi Talib رضي الله عنه in Madinah after Badr, in the early years of the Hijrah. Their household was poor in goods and rich in worship. Children included al-Hasan, al-Husayn, Zaynab, and Umm Kulthum رضي الله عنهم. Through Hasan and Husayn the Prophet's ﷺ surviving lineage of sayyids and sharifs descends. Sunni love for this descent is love for the Messenger ﷺ, without making it a rival imamate to the Rashidun.

The Prophet ﷺ said she is the mistress of the women of Paradise, or of the women of this ummah, in hadith in Bukhari and Muslim. He would stand when she entered and kiss her, a tenderness unique in the sirah of a prophet who was also a father. She suffered at Uhud, walking to the mountain to nurse his wounds and to burn a mat for ash to stop the blood, as the maghazi relate. Grief and sabr were her garment in Makkah and in Madinah.

After the Wafat in Rabi' al-Awwal 11 AH / June 632 CE she lived about six months. She died in Madinah around 11 AH, often dated to Ramadan, at a young age in the mid-twenties by many calculations. She asked to be buried at night, and Ali رضي الله عنه fulfilled that wish; the exact grave in al-Baqi' is not a matter of tourist certainty, and Sunni adab is not to quarrel over it. The ummah agrees that she went to her father soon.

Her titles include al-Zahra, the Radiant, and al-Batul in some reports. She ground grain until her hands blistered; Ali earned from drawing water. The Prophet ﷺ taught them dhikr instead of a servant when they asked, the tasbih of Fatimah famous in the books of adhkar. Zuhd and dhikr, not palaces, are the Sunni image of this house.

Ahl al-Sunnah honour her with رضي الله عنها as they honour Aisha, Hafsah, and the other Mothers and daughters. They do not build her chapter on attacks on Abu Bakr رضي الله عنه or on any Companion. Whatever legal questions arose after the Prophet's ﷺ death, the creed remains: she is the leader of the women of Paradise, and the Sahaba are all to be spoken of with respect.

From her the light of the Ahl al-Bayt continued in Hasan and Husayn, in Zaynab's later patience, and in a lineage that still greets the ummah with the name of Muhammad ﷺ. Encyclopedias of the Sahaba therefore close this tenth chapter with a woman who was daughter, wife, mother, and siddiqa, and who asked for a quiet night burial beside the grief of 11 AH.""",
    """فاطمہ الزہرا رضی اللہ عنہا نبی محمد ﷺ اور خدیجہ بنت خویلد رضی اللہ عنہا کی سب سے چھوٹی بیٹی تھیں، مکہ میں بعثت سے تقریباً پانچ برس پہلے پیدا، یا دیگر روایات میں مکی دور بعد میں؛ مورخین سال پر مختلف رتبے پر نہیں۔ اولاد میں سب سے محبوب مشہور روایات میں: فرمایا میرا ٹکڑا ہے؛ جو اسے دکھ دے مجھے دکھ دے۔ ابن سعد اور شمائل کی کتابیں داخل ہوتے کھڑے ہونا، بوسہ، پاس بٹھانا لکھتی ہیں۔

علی بن ابی طالب رضی اللہ عنہ سے نکاح مدینہ بدر کے بعد ہجرت کے ابتدائی برسوں میں ہوا۔ گھر مال میں تنگ عبادت میں فراخ۔ اولاد حسن، حسین، زینب، ام کلثوم رضی اللہ عنہم۔ حسن و حسین سے نبی ﷺ کی باقی نسل سادات و اشراف چلی۔ اس نسل سے سنی محبت رسول ﷺ سے محبت ہے، خلفائے راشدین کی حریف امامت نہیں۔

نبی ﷺ نے فرمایا یہ جنت کی عورتوں کی سردار ہیں، یا اس امت کی عورتوں کی، بخاری و مسلم کی حدیث میں۔ داخل ہوتیں تو کھڑے ہوتے بوسہ دیتے، باپ نبی کی سیرت میں انوکھی شفقت۔ احد پر پہاڑ زخموں کی تیمارداری کو گئیں، چٹائی جلا کر راکھ خون روکنے کو، مغازی کے بیان میں۔ غم اور صبر مکہ و مدینہ میں ان کا لباس تھے۔

ربیع الاول 11ھ / جون 632ء وفات کے بعد تقریباً چھ مہینے جیں۔ مدینہ میں 11ھ کے قریب وفات، اکثر رمضان لکھی جاتی ہے، بہت سی گنتی میں بیس کی دہائی کے وسط کی عمر۔ رات دفن کی وصیت کی، علی رضی اللہ عنہ نے پوری کی؛ بقیع میں عین قبر سیاح یقین کا معاملہ نہیں، سنی ادب اس پر جھگڑنا نہیں۔ امت متفق ہے جلد والد کے پاس گئیں۔

القاب میں الزہرا، چمکتی ہوئی، اور بعض روایات میں البتول۔ اناج پیسا یہاں تک ہاتھ چھالے پڑے؛ علی پانی کھینچ کر کماتے تھے۔ خادم مانگا تو نبی ﷺ نے ذکر سکھایا، تسبیح فاطمہ کتب اذکار میں مشہور۔ زہد و ذکر، محل نہیں، اس گھر کی سنی تصویر ہیں۔

اہل سنت انہیں رضی اللہ عنہا کہہ کر عزت دیتے ہیں جیسے عائشہ، حفصہ اور دیگر امهات و بیٹیوں کو۔ باب ابو بکر رضی اللہ عنہ یا کسی صحابی پر حملے سے نہیں بناتے۔ نبی ﷺ کی وفات کے بعد جو فقہی سوال اٹھے، عقیدہ یہی: جنت کی عورتوں کی سردار ہیں، اور صحابہ سب احترام سے یاد کیے جائیں۔

ان سے اہل بیت کی روشنی حسن و حسین میں، زینب کے بعد کے صبر میں، اور اس نسل میں چلی جو اب بھی امت کو محمد ﷺ کے نام سے سلام کرتی ہے۔ صحابہ کے دائرۃ المعارف اس لیے دسواں باب اس عورت پر بند کرتے ہیں جو بیٹی، بیوی، ماں، صدیقہ تھی، اور 11ھ کے غم کے پاس خاموش رات کی تدفین مانگتی رہی۔""",
    """फ़ातिमा अज़-ज़हरा رضي الله عنها नबी मुहम्मद ﷺ और ख़दीजा बिन्त ख़ुवैलिद رضي الله عنها की सबसे छोटी बेटी थीं, मक्का में बि'सत से क़रीब पाँच बरस पहले पैदा, या अन्य रिवायात में मक्की दौर बाद में; मुवर्रिख़ीन साल पर मुख़्तलिफ़ रतबे पर नहीं। औलाद में सबसे महबूब मशहूर रिवायात में: फ़रमाया मेरा टुकड़ा है; जो उसे दुख दे मुझे दुख दे। इब्न साद और शमाएल की किताबें दाख़िल होते खड़े होना, बोसा, पास बिठाना लिखती हैं।

अली इब्न अबी तालिब رضي الله عنه से निकाह मदीना बद्र के बाद हिजरत के इब्तिदाई बरसों में हुआ। घर माल में तंग इबादत में फ़राख़। औलाद हसन, हुसैन, ज़ैनब, उम्म कुलसूम رضي الله عنهم। हसन व हुसैन से नबी ﷺ की बाक़ी नस्ल सादात व अशराफ़ चली। इस नस्ल से सुन्नी मुहब्बत रसूल ﷺ से मुहब्बत है, ख़ुलफ़ा-ए-राशिदीन की हरीफ़ इमामत नहीं।

नबी ﷺ ने फ़रमाया यह जन्नत की औरतों की सरदार हैं, या इस उम्मत की औरतों की, बुख़ारी व मुस्लिम की हदीस में। दाख़िल होतीं तो खड़े होते बोसा देते, बाप नबी की सीरत में अनोखी शफ़क़त। उहुद पर पहाड़ ज़ख़्मों की तीमारदारी को गईं, चटाई जला कर राख ख़ून रोकने को, मग़ाज़ी के बयान में। ग़म और सब्र मक्का व मदीना में उनका लिबास थे।

रबीउल अव्वल 11 हिजरी / जून 632 ई. विसाल के बाद क़रीब छह महीने जीं। मदीना में 11 हिजरी के क़रीब वफ़ात, अक्सर रमज़ान लिखी जाती है, बहुत सी गिनती में बीस की दहाई के वस्त की उम्र। रात दफ़न की वसीयत की, अली رضي الله عنه ने पूरी की; बक़ीअ में अयन क़ब्र सय्याह यक़ीन का मामला नहीं, सुन्नी अदब उस पर झगड़ना नहीं। उम्मत मुत्तफ़िक़ है जल्द वालिद के पास गईं।

अलक़ाब में अज़-ज़हरा, चमकती हुई, और कुछ रिवायात में अल-बतूल। अनाज पीसा यहाँ तक हाथ छाले पड़े; अली पानी खींच कर कमाते थे। ख़ादिम माँगा तो नबी ﷺ ने ज़िक्र सिखाया, तस्बीह-ए-फ़ातिमा कुतुब-ए-अज़कार में मशहूर। ज़ुहद व ज़िक्र, महल नहीं, इस घर की सुन्नी तस्वीर हैं।

अहले सुन्नत उन्हें رضي الله عنها कह कर इज़्ज़त देते हैं जैसे आयशा, हफ़्सा और अन्य उम्महात व बेटियों को। बाब अबू बक्र رضي الله عنه या किसी सहाबी पर हमले से नहीं बनाते। नबी ﷺ की वफ़ात के बाद जो फ़िक़ही सवाल उठे, अक़ीदा यही: जन्नत की औरतों की सरदार हैं, और सहाबा सब एहतिराम से याद किए जाएँ।

उनसे अहले बैत की रौशनी हसन व हुसैन में, ज़ैनब के बाद के सब्र में, और उस नस्ल में चली जो अब भी उम्मत को मुहम्मद ﷺ के नाम से सलाम करती है। सहाबा के दाइरतुल मआरिफ़ इसलिए दसवाँ बाब इस औरत पर बंद करते हैं जो बेटी, बीवी, माँ, सिद्दीक़ा थी, और 11 हिजरी के ग़म के पास ख़ामोश रात की तदफ़ीन माँगती रही।""",
    """ফাতিমাহ আজ-জাহরা رضي الله عنها নবী মুহাম্মদ ﷺ ও খাদিজাহ বিনত খুওয়াইলিদ رضي الله عنها-এর কনিষ্ঠ কন্যা, মক্কায় নবুয়তের প্রায় পাঁচ বছর আগে জন্ম, বা অন্য বর্ণনায় মক্কী যুগের পরে; ঐতিহাসিকরা বছরে ভিন্ন মর্যাদায় নন। সন্তানদের মধ্যে সর্বাধিক প্রিয় প্রসিদ্ধ বর্ণনায়: তিনি বলেন তিনি আমার অংশ; যা তাঁকে কষ্ট দেয় আমাকে কষ্ট দেয়। ইবন সাদ ও শামাইল গ্রন্থ প্রবেশে দাঁড়ানো, চুম্বন, পাশে বসানো লেখে।

আলী ইবন আবি তালিব رضي الله عنه-এর সঙ্গে বিবাহ মদিনায় বদরের পর হিজরতের প্রথম বছরগুলোতে। ঘর সম্পদে সংকীর্ণ ইবাদতে প্রশস্ত। সন্তান হাসান, হুসাইন, যায়নব, উম্মু কুলসুম رضي الله عنهم। হাসান ও হুসাইন থেকে নবী ﷺ-এর অবশিষ্ট বংশ সাইয়িদ ও শরিফ চলে। এই বংশের প্রতি সুন্নি ভালোবাসা রাসূল ﷺ-এর প্রতি ভালোবাসা, রাশিদুনের প্রতিদ্বন্দ্বী ইমামত নয়।

নবী ﷺ বলেন তিনি জান্নাতের নারীদের সরদার, বা এই উম্মাহর নারীদের, বুখারি ও মুসলিমের হাদিসে। তিনি ঢুকলে দাঁড়াতেন চুম্বন করতেন, পিতা-নবীর সিরাতে অনন্য স্নেহ। উহুদে পাহাড়ে ক্ষত সেবায় যান, চাটাই পুড়িয়ে ছাই দিয়ে রক্ত থামাতে, মাগাজির বর্ণনায়। শোক ও সবর মক্কা ও মদিনায় তাঁর পোশাক ছিল।

রবিউল আউয়াল ১১ হিজরি / জুন ৬৩২ ওফাতের পর প্রায় ছয় মাস বাঁচেন। মদিনায় ১১ হিজরির কাছাকাছি ইন্তেকাল, প্রায়ই রমজান লেখা হয়, অনেক গণনায় বিশের দশকের মাঝামাঝি বয়স। রাতে দাফনের অসিয়ত করেন, আলী رضي الله عنه পূর্ণ করেন; বাকীতে সঠিক কবর পর্যটক নিশ্চয়তার বিষয় নয়, সুন্নি আদব এ নিয়ে বিবাদ নয়। উম্মাহ একমত তিনি শীঘ্র পিতার কাছে যান।

উপাধিতে আজ-জাহরা, উজ্জ্বল, এবং কিছু বর্ণনায় আল-বাতুল। শস্য পেষেন হাতে ফোসকা পড়া পর্যন্ত; আলী পানি তুলে রোজগার করতেন। খাদেম চাইলে নবী ﷺ জিকির শেখান, তাসবিহে ফাতিমা আজকার গ্রন্থে প্রসিদ্ধ। যুহদ ও জিকির, প্রাসাদ নয়, এই ঘরের সুন্নি চিত্র।

আহলুস সুন্নাহ তাঁকে رضي الله عنها বলে সম্মান করে যেমন আয়িশা, হাফসাহ ও অন্য উম্মুল মুমিনীন ও কন্যাদের। অধ্যায় আবু বকর رضي الله عنه বা কোনো সাহাবির আক্রমণে গড়ে না। নবী ﷺ-এর ওফাতের পর যে ফিকহি প্রশ্ন উঠুক, আকিদা এই: তিনি জান্নাতের নারীদের নেত্রী, এবং সাহাবিরা সবাই সম্মানে স্মরণীয়।

তাঁর থেকে আহলুল বায়তের আলো হাসান ও হুসাইনে, যায়নবের পরবর্তী সবরে, এবং সেই বংশে চলে যা আজও উম্মাহকে মুহাম্মদ ﷺ-এর নামে সালাম করে। সাহাবা বিশ্বকোষ তাই দশম অধ্যায় সেই নারীতে বন্ধ করে যিনি কন্যা, স্ত্রী, মাতা, সিদ্দিকা, এবং ১১ হিজরির শোকের পাশে নীরব রাতের দাফন চেয়েছিলেন।""",
    """Fatimah az-Zahra رضي الله عنها adalah putri bungsu Nabi Muhammad ﷺ dan Khadijah binti Khuwailid رضي الله عنها, lahir di Makkah sekitar lima tahun sebelum risalah atau, dalam riwayat lain, kemudian pada periode Makkah; sejarawan berbeda tentang tahun tetapi tidak tentang martabatnya. Ia paling dicintai di antara anak-anak beliau dalam riwayat masyhur: beliau bersabda ia bagian dariku; apa yang menyakitinya menyakitiku. Ibnu Sa'd dan kitab syamail mencatat beliau berdiri ketika ia masuk, menciumnya, dan mendudukkannya di sisinya.

Ia menikah dengan Ali bin Abi Thalib رضي الله عنه di Madinah setelah Badar, pada tahun-tahun awal Hijrah. Rumah tangga mereka miskin harta dan kaya ibadah. Anak-anak termasuk al-Hasan, al-Husain, Zainab, dan Ummu Kultsum رضي الله عنهم. Melalui Hasan dan Husain nasab Nabi ﷺ yang tersisa dari para sayyid dan syarif turun. Cinta Ahlusunah kepada keturunan ini adalah cinta kepada Rasul ﷺ, tanpa menjadikannya imamah saingan Khulafaur Rasyidin.

Nabi ﷺ bersabda ia tuan wanita surga, atau wanita umat ini, dalam hadis Bukhari dan Muslim. Beliau berdiri ketika ia masuk dan menciumnya, kelembutan unik dalam sirah seorang nabi yang juga ayah. Ia menderita di Uhud, berjalan ke gunung merawat luka beliau dan membakar tikar untuk abu menghentikan darah, sebagaimana dituturkan maghazi. Duka dan sabar adalah pakaiannya di Makkah dan di Madinah.

Setelah Wafat pada Rabiul Awal 11 H / Juni 632 M ia hidup sekitar enam bulan. Ia wafat di Madinah sekitar 11 H, sering ditanggal pada Ramadan, pada usia muda pertengahan dua puluhan menurut banyak hitungan. Ia meminta dimakamkan malam hari, dan Ali رضي الله عنه menunaikan wasiat itu; kubur pasti di Baqi bukan soal kepastian wisatawan, dan adab Ahlusunah tidak bertengkar tentangnya. Umat sepakat ia menyusul ayahnya segera.

Gelarnya termasuk az-Zahra, yang berseri, dan al-Batul dalam sebagian riwayat. Ia menggiling biji hingga tangannya melepuh; Ali mencari nafkah menimba air. Nabi ﷺ mengajar mereka zikir sebagai ganti pelayan ketika mereka meminta, tasbih Fatimah yang masyhur dalam kitab azkar. Zuhud dan zikir, bukan istana, adalah citra Ahlusunah tentang rumah ini.

Ahlusunah memuliakannya dengan رضي الله عنها sebagaimana memuliakan Aisyah, Hafshah, dan Ummul Mukminin serta putri lain. Mereka tidak membangun babnya atas serangan terhadap Abu Bakar رضي الله عنه atau Sahabat mana pun. Apa pun soal fikih yang muncul setelah Nabi ﷺ wafat, akidah tetap: ia pemimpin wanita surga, dan para Sahabat semua harus disebut dengan hormat.

Dari padanya cahaya Ahlulbait berlanjut pada Hasan dan Husain, pada kesabaran Zainab kemudian, dan pada nasab yang masih menyapa umat dengan nama Muhammad ﷺ. Ensiklopedia Sahabat karena itu menutup bab kesepuluh ini dengan wanita yang adalah putri, istri, ibu, dan siddiqah, dan yang meminta penguburan malam yang sunyi di sisi duka 11 H.""",
)
ch["items"][0]["details"] = D(
    """Verse 33:33 of Surat al-Ahzab addresses the household with a will of purification. Sunni tafsir includes the wives of the Prophet ﷺ in the first address of the verse, and includes Ali, Fatimah, Hasan, and Husayn in the hadith of the kisa' (cloak) that explains a special honour of the nearest kin. Both readings are held without emptying either the Mothers of the Believers or the children of Fatimah of dignity. The verse is recited as honour, not as a weapon.

The hadith of the cloak is that the Prophet ﷺ gathered Ali, Fatimah, Hasan, and Husayn under a cloak and prayed for the purification of his Ahl al-Bayt. It is in Muslim and other books. Fatimah is the centre of that gathering as daughter and as mother of the two boys. Al-Zahra, the Radiant, is explained as light of face, or light of faith, or both. Muslims of all Sunni schools kiss this report with love.

Hasan and Husayn as youths of Paradise, Zaynab as a woman of sabr, and Umm Kulthum as a daughter of Ali and Fatimah complete the inner family. The Prophet ﷺ carried Hasan and Husayn on his back in salah in well-known hadith. Love of the Ahl al-Bayt is part of iman in Sunni aqidah texts; it is joined to love of all the Sahaba, not set against Abu Bakr and Umar.

Patience and purity are the moral of her item. She ground wheat, raised orphans of Uhud's grief in a sense as a daughter who had washed blood, and died asking for little of this world. Night burial was her wish for concealment and for zuhd, not a political riddle in Sunni adab. Those who turn her grave into a quarrel leave the path of her zuhd.

The surviving lineage through Hasan and Husayn means that when the ummah sees a descendant of the Prophet ﷺ it remembers Fatimah first. That remembrance is du'a and courtesy. It does not create a caste. Taqwa remains the Quranic measure, as it was for Bilal and for the Qurashi nobles together.

Encyclopedias therefore mention 33:33, the kisa', Ali, Hasan, Husayn, and the name al-Zahra in one paragraph-cluster. They add that Aisha رضي الله عنها also loved Fatimah and that the two honours—daughter and wife—do not cancel. Sunni homes teach children to send salawat on the Prophet ﷺ and to name Hasan, Husayn, and Fatimah with affection.

This tenth item closes the book of ten lives: four caliphs, an uncle, a mu'adhdhin, a Persian seeker, a sword, a narrator, and a daughter. All are رضي الله عنهم / رضي الله عنها. All are taught without sectarian attacks. The Radiant remains the light of the house of Muhammad ﷺ in the memory of Ahl al-Sunnah.""",
    """سورہ احزاب کی آیت 33:33 اہل خانہ کو تطہیر کی ارادے سے مخاطب ہے۔ سنی تفسیر آیت کے پہلے خطاب میں ازواج نبی ﷺ کو شامل کرتی ہے، اور حدیث کسا (چادر) میں علی، فاطمہ، حسن، حسین کو قریبی رشتے کا خاص شرف سمجھتی ہے۔ دونوں پڑھتیں امهات المؤمنین یا اولاد فاطمہ کی عزت خالی کیے بغیر رکھی جاتی ہیں۔ آیت عزت سے پڑھی جاتی ہے ہتھیار سے نہیں۔

حدیث کسا یہ ہے کہ نبی ﷺ نے علی، فاطمہ، حسن، حسین کو چادر تلے جمع کر کے اہل بیت کی تطہیر کی دعا کی۔ مسلم و دیگر کتب میں ہے۔ فاطمہ اس اجتماع کے مرکز بیٹی اور دو لڑکوں کی ماں کے طور پر ہیں۔ الزہرا، چمکتی ہوئی، چہرے کی روشنی یا ایمان کی یا دونوں۔ تمام سنی مکاتب اس روایت کو محبت سے چومتے ہیں۔

حسن و حسین جنتی نوجوان، زینب صبر کی عورت، ام کلثوم علی و فاطمہ کی بیٹی اندرونی خاندان مکمل کرتی ہیں۔ نبی ﷺ نے حسنین کو نماز میں پیٹھ پر اٹھایا مشہور حدیث میں۔ اہل بیت سے محبت سنی عقیدہ میں ایمان کا حصہ ہے؛ تمام صحابہ سے محبت سے جڑی ہے، ابو بکر و عمر کے مقابل نہیں۔

صبر اور پاکیزگی اس باب کا اخلاق ہیں۔ گندم پیسا، احد کے غم کے یتیم معنوں میں پالے بطور بیٹی جس نے خون دھویا، دنیا سے کم مانگتی وفات پائیں۔ رات کی تدفین اخفا و زہد کی خواہش تھی، سنی ادب میں سیاسی پہیلی نہیں۔ جو قبر کو جھگڑا بنائیں ان کے زہد سے نکل جاتے ہیں۔

حسن و حسین سے باقی نسل کا معنی یہ ہے کہ امت نبی ﷺ کی اولاد دیکھے تو پہلے فاطمہ یاد آئے۔ یہ یاد دعا اور ادب ہے۔ ذات پات نہیں بنتی۔ تقویٰ قرآنی پیمانہ رہتا ہے، جیسا بلال اور قریشی اشراف کے لیے اکٹھا تھا۔

دائرۃ المعارف اس لیے 33:33، کسا، علی، حسن، حسین اور الزہرا ایک پیراگراف جھرمٹ میں ذکر کرتی ہیں۔ بڑھاتی ہیں عائشہ رضی اللہ عنہا بھی فاطمہ سے محبت رکھتی تھیں اور دونوں شرف—بیٹی اور بیوی—کاٹتے نہیں۔ سنی گھر بچوں کو درود اور حسن حسین فاطمہ پیار سے سکھاتے ہیں۔

یہ دسواں باب دس زندگیوں کی کتاب بند کرتا ہے: چار خلیفہ، ایک چچا، ایک مؤذن، ایک فارسی طالب، ایک تلوار، ایک راوی، ایک بیٹی۔ سب رضی اللہ عنہم / رضی اللہ عنہا۔ سب بغیر فرقہ وارانہ حملوں کے پڑھائے جاتے ہیں۔ الزہرا اہل سنت کی یاد میں محمد ﷺ کے گھر کی روشنی رہتی ہیں۔""",
    """सूरह अहज़ाब की आयत 33:33 अहले ख़ाना को तत्हीर की इरादे से मुख़ातिब है। सुन्नी तफ़सीर आयत के पहले ख़िताब में अज़वाज-ए-नबी ﷺ को शामिल करती है, और हदीस-ए-किसा (चादर) में अली, फ़ातिमा, हसन, हुसैन को क़रीबी रिश्ते का ख़ास शرف समझती है। दोनों पढ़तें उम्महातुल मुमिनीन या औलाद-ए-फ़ातिमा की इज़्ज़त ख़ाली किए बिना रखी जाती हैं। आयत इज़्ज़त से पढ़ी जाती है हथियार से नहीं।

हदीस-ए-किसा यह है कि नबी ﷺ ने अली, फ़ातिमा, हसन, हुसैन को चादर तले जमा कर के अहले बैत की तत्हीर की दुआ की। मुस्लिम व अन्य कुतुब में है। फ़ातिमा उस इज्तिमाअ के मर्कज़ बेटी और दो लड़कों की माँ के तौर पर हैं। अज़-ज़हरा, चमकती हुई, चेहरे की रौशनी या ईमान की या दोनों। तमाम सुन्नी मकातिब इस रिवायत को मुहब्बत से चूमते हैं।

हसन व हुसैन जन्नती नौजवान, ज़ैनब सब्र की औरत, उम्म कुलसूम अली व फ़ातिमा की बेटी अंदरूनी ख़ानदान मुकम्मल करती हैं। नबी ﷺ ने हसनैन को नमाज़ में पीठ पर उठाया मशहूर हदीस में। अहले बैत से मुहब्बत सुन्नी अक़ीदा में ईमान का हिस्सा है; तमाम सहाबा से मुहब्बत से जुड़ी है, अबू बक्र व उमर के मुक़ाबिल नहीं।

सब्र और पाकीज़गी इस बाब का अख़लाक़ हैं। गेहूँ पीसा, उहुद के ग़म के यतीम मानी में पाले बतौर बेटी जिसने ख़ून धोया, दुनिया से कम माँगती वफ़ात पाईं। रात की तदफ़ीन इख़्फ़ा व ज़ुहद की ख़्वाहिश थी, सुन्नी अदब में सियासी पहेली नहीं। जो क़ब्र को झगड़ा बनाएँ उनके ज़ुहद से निकल जाते हैं।

हसन व हुसैन से बाक़ी नस्ल का मानी यह है कि उम्मत नबी ﷺ की औलाद देखे तो पहले फ़ातिमा याद आए। यह याद दुआ और अदब है। ज़ात पात नहीं बनती। तक़वा कुरआनी पैमाना रहता है, जैसा बिलाल और कुरैशी अशराफ़ के लिए इकट्ठा था।

दाइरतुल मआरिफ़ इसलिए 33:33, किसा, अली, हसन, हुसैन और अज़-ज़हरा एक पैराग्राफ़ झुरमुट में ज़िक्र करती हैं। बढ़ाती हैं आयशा رضي الله عنها भी फ़ातिमा से मुहब्बत रखती थीं और दोनों शرف—बेटी और बीवी—काटते नहीं। सुन्नी घर बच्चों को दरूद और हसन हुसैन फ़ातिमा प्यार से सिखाते हैं।

यह दसवाँ बाब दस ज़िंदगियों की किताब बंद करता है: चार ख़लीफा, एक चाचा, एक मुअज़्ज़िन, एक फ़ारसी तालिब, एक तलवार, एक रावी, एक बेटी। सब رضي الله عنهم / رضي الله عنها। सब बिना फ़िर्कावाराना हमलों के पढ़ाए जाते हैं। अज़-ज़हरा अहले सुन्नत की याद में मुहम्मद ﷺ के घर की रौशनी रहती हैं।""",
    """সূরা আহজাবের আয়াত ৩৩:৩৩ গৃহবাসীকে পবিত্রতার ইচ্ছা দিয়ে সম্বোধন করে। সুন্নি তাফসির আয়াতের প্রথম সম্বোধনে নবী ﷺ-এর স্ত্রীগণকে অন্তর্ভুক্ত করে, এবং কিসার (চাদরের) হাদিসে আলী, ফাতিমা, হাসান, হুসাইনকে নিকট আত্মীয়ের বিশেষ সম্মান বলে। দুই পাঠই উম্মুল মুমিনীন বা ফাতিমার সন্তানের মর্যাদা খালি না করে রাখা হয়। আয়াত সম্মানে পড়া হয় অস্ত্র হিসেবে নয়।

কিসার হাদিস এই যে নবী ﷺ আলী, ফাতিমা, হাসান, হুসাইনকে চাদরের নিচে জড়ো করে আহলুল বায়তের পবিত্রতার দোয়া করেন। মুসলিম ও অন্য গ্রন্থে আছে। ফাতিমা সেই সমাবেশের কেন্দ্র কন্যা ও দুই বালকের মাতা হিসেবে। আজ-জাহরা, উজ্জ্বল, মুখের আলো বা ঈমানের বা দুই। সব সুন্নি মাজহাব এই বর্ণনাকে ভালোবাসায় চুম্বন করে।

হাসান ও হুসাইন জান্নাতের যুবক, যায়নব সবরের নারী, উম্মু কুলসুম আলী ও ফাতিমার কন্যা অন্তরঙ্গ পরিবার পূর্ণ করে। নবী ﷺ হাসান-হুসাইনকে নামাজে পিঠে তোলেন প্রসিদ্ধ হাদিসে। আহলুল বায়তের ভালোবাসা সুন্নি আকিদায় ঈমানের অংশ; সব সাহাবির ভালোবাসার সঙ্গে জোড়া, আবু বকর ও উমরের বিপক্ষে নয়।

সবর ও পবিত্রতা এই অধ্যায়ের নীতি। তিনি গম পেষেন, উহুদের শোকের ইয়াতিম অর্থে লালন করেন সেই কন্যা হিসেবে যিনি রক্ত ধুয়েছিলেন, দুনিয়া থেকে কম চেয়ে মৃত্যুবরণ করেন। রাতের দাফন গোপনতা ও যুহদের ইচ্ছা ছিল, সুন্নি আদবে রাজনৈতিক ধাঁধা নয়। যাঁরা কবরকে বিবাদ বানান তাঁর যুহদ থেকে বেরিয়ে যান।

হাসান ও হুসাইন দিয়ে অবশিষ্ট বংশের অর্থ এই যে উম্মাহ নবী ﷺ-এর বংশধর দেখলে প্রথমে ফাতিমা স্মরণ করে। এই স্মরণ দোয়া ও শিষ্টাচার। জাতিভেদ নয়। তাকওয়া কুরআনি মাপকাঠি থাকে, যেমন বিলাল ও কুরাইশ অভিজাতদের জন্য একসঙ্গে ছিল।

বিশ্বকোষ তাই ৩৩:৩৩, কিসা, আলী, হাসান, হুসাইন ও আজ-জাহরা এক অনুচ্ছেদ-গুচ্ছে উল্লেখ করে। যোগ করে আয়িশা رضي الله عنها-ও ফাতিমাকে ভালোবাসতেন এবং দুই সম্মান—কন্যা ও স্ত্রী—কাটে না। সুন্নি ঘর শিশুদের দরুদ এবং হাসান, হুসাইন, ফাতিমা স্নেহে শেখায়।

এই দশম অধ্যায় দশ জীবনের বই বন্ধ করে: চার খলিফা, এক চাচা, এক মুয়াজ্জিন, এক পারস্য অন্বেষক, এক তলোয়ার, এক বর্ণনাকারী, এক কন্যা। সবাই رضي الله عنهم / رضي الله عنها। সবাই সাম্প্রদায়িক আক্রমণ ছাড়া পড়ানো হয়। আজ-জাহরা আহলুস সুন্নাহর স্মৃতিতে মুহাম্মদ ﷺ-এর ঘরের আলো থাকেন।""",
    """Ayat 33:33 dari Surah al-Ahzab menyapa ahlulbait dengan kehendak pensucian. Tafsir Ahlusunah memasukkan istri-istri Nabi ﷺ dalam sapaan pertama ayat, dan memasukkan Ali, Fatimah, Hasan, dan Husain dalam hadis kisak (selendang) yang menjelaskan kemuliaan khusus kerabat terdekat. Kedua bacaan dipegang tanpa mengosongkan martabat Ummul Mukminin atau anak-anak Fatimah. Ayat dibaca sebagai kehormatan, bukan senjata.

Hadis kisak adalah bahwa Nabi ﷺ mengumpulkan Ali, Fatimah, Hasan, dan Husain di bawah selendang dan berdoa pensucian Ahlulbait-nya. Ia ada dalam Muslim dan kitab lain. Fatimah adalah pusat kumpulan itu sebagai putri dan sebagai ibu dua anak lelaki. Az-Zahra, yang berseri, dijelaskan sebagai cahaya wajah, atau cahaya iman, atau keduanya. Muslim semua mazhab Ahlusunah mencium riwayat ini dengan cinta.

Hasan dan Husain sebagai pemuda surga, Zainab sebagai wanita sabar, dan Ummu Kultsum sebagai putri Ali dan Fatimah menyempurnakan keluarga dalam. Nabi ﷺ menggendong Hasan dan Husain di punggung dalam salat dalam hadis terkenal. Cinta kepada Ahlulbait adalah bagian iman dalam teks akidah Ahlusunah; ia digabung dengan cinta kepada seluruh Sahabat, tidak dipertentangkan dengan Abu Bakar dan Umar.

Sabar dan kesucian adalah akhlak butir ini. Ia menggiling gandum, membesarkan yatim duka Uhud dalam arti sebagai putri yang telah mencuci darah, dan wafat meminta sedikit dari dunia. Penguburan malam adalah keinginannya untuk penyembunyian dan zuhud, bukan teka-teki politik dalam adab Ahlusunah. Siapa yang mengubah kuburnya menjadi pertengkaran meninggalkan jalan zuhudnya.

Nasab tersisa melalui Hasan dan Husain berarti ketika umat melihat keturunan Nabi ﷺ ia mengingat Fatimah terlebih dahulu. Ingatan itu doa dan adab. Ia tidak menciptakan kasta. Takwa tetap ukuran Al-Qur'an, sebagaimana bagi Bilal dan pemuka Quraisy bersama.

Ensiklopedia karena itu menyebut 33:33, kisak, Ali, Hasan, Husain, dan nama az-Zahra dalam satu gugus paragraf. Mereka menambah bahwa Aisyah رضي الله عنها juga mencintai Fatimah dan bahwa dua kemuliaan—putri dan istri—tidak saling membatalkan. Rumah Ahlusunah mengajar anak-anak berselawat atas Nabi ﷺ dan menyebut Hasan, Husain, dan Fatimah dengan kasih.

Butir kesepuluh ini menutup kitab sepuluh hidup: empat khalifah, seorang paman, seorang muazin, seorang pencari Persia, sebuah pedang, seorang perawi, dan seorang putri. Semua رضي الله عنهم / رضي الله عنها. Semua diajarkan tanpa serangan sektarian. Yang Berseri tetap cahaya rumah Muhammad ﷺ dalam ingatan Ahlusunah.""",
)

PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("patched sahaba")






