# -*- coding: utf-8 -*-
"""Replace seerah.json details for chapters 4–5 only (Ummahat-ul-Momineen; major events and wafat).

This script was cut off during generation (chapter 5 items 2–4 were never
finished). It must not be executed against the app JSON assets.
"""
raise SystemExit(
    'seerah_ch4_5.py is incomplete and must not be run.'
)

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "assets" / "json" / "seerah.json"


def D(en, ur, hi, bn, idn):
    return {"en": en.strip(), "ur": ur.strip(), "hi": hi.strip(), "bn": bn.strip(), "id": idn.strip()}


data = json.loads(PATH.read_text(encoding="utf-8"))


def chapter(cid):
    for ch in data:
        if ch["chapter_id"] == cid:
            return ch
    raise KeyError(cid)


c = chapter(4)
c["details"] = D(
    """The Qur'an gives the wives of Prophet Muhammad ﷺ a rank no other household shares. Allah says: "The Prophet is closer to the believers than their own selves, and his wives are their mothers" (al-Ahzab 33:6). Sunni tafsir reads this as honour and as law: the Ummah owes them the respect of mothers, and they were not to be married to other men after him (33:53). Classical seerah names them Ummahat al-Mu'minin, the Mothers of the Believers.

He ﷺ married Khadijah bint Khuwaylid رضي الله عنها in Makkah at the age of twenty-five and remained with her alone for about twenty-five years. He took no other wife while she lived. Ibn Ishaq, Ibn Hisham, and Ibn Sa'd record that long monogamy as part of the Makkan years. After her death in the Year of Sorrow, about three years before the Hijrah (around 619 CE), later marriages began in Makkah and then in Madinah.

Those later marriages were mostly to widows who had already entered Islam, suffered hijrah, or lost husbands in the path of Allah. Through them the Messenger ﷺ sheltered women, honoured the households of Abu Bakr and Umar رضي الله عنهما, and tied tribes such as Makhzum, Umayya, and Banu al-Mustaliq to the community. Teaching was another wisdom: the chambers beside al-Masjid al-Nabawi became schools from which wudu, prayer, inheritance, and prophetic manners were learned.

The sequence commonly followed in seerah, and the order of items in this chapter, is: Khadijah bint Khuwaylid; Sawdah bint Zam'ah; Aisha bint Abi Bakr; Hafsah bint Umar; Zaynab bint Khuzaymah; Umm Salamah Hind bint Abi Umayyah; Zaynab bint Jahsh; Juwayriyah bint al-Harith; Umm Habibah Ramlah bint Abi Sufyan; Safiyyah bint Huyayy; and Maymunah bint al-Harith. The nikah with Aisha was contracted in Makkah; the household was established in Madinah after the Hijrah. Maymunah, married at Sarif in 7 AH after umrah al-qada', was the last.

Each Mother of the Believers رضي الله عنهن is remembered with dignity in Bukhari, Muslim, and the books of tabaqat. Aisha and Umm Salamah became among the greatest narrators and jurists among the women of this Ummah. Others are remembered for charity, patience, the Abyssinian hijrah, or a marriage that led to the freeing of captives. None of them is to be spoken of except with the adab owed to the prophetic household.

After his wafat in Rabi' al-Awwal 11 AH (June 632 CE) they remained Mothers of the Believers until their own deaths. They did not remarry. Most were buried in al-Baqi' in Madinah; Maymunah رضي الله عنها died and was buried at Sarif, where she had married him. Their lives run from the first revelation to the later years of the Rightly Guided Caliphate.

This chapter therefore treats not a worldly list of names but the inner history of the da'wah: who stood at the beginning, who entered the household after battles and treaties, and how Allah made those houses a mercy for widows, tribes, and students of knowledge. What follows takes each Mother in the familiar seerah order.""",
    """قرآن نبی کریم ﷺ کی ازواج مطہرات کو وہ مرتبہ دیتا ہے جو کسی اور گھر کو حاصل نہیں۔ اللہ نے فرمایا: «النبی أولى بالمؤمنین من أنفسهم وأزواجه أمهاتهم» (الاحزاب 33:6)۔ اہل سنت کی تفسیر اسے عزت اور حکم دونوں سمجھتی ہے: امت پر ان کا احترام ماں جیسا ہے، اور آپ کے بعد ان سے نکاح حرام قرار پایا (33:53)۔ کلاسیکی سیرت انہیں امہات المؤمنین کہتی ہے۔

آپ ﷺ نے مکہ میں پچیس سال کی عمر میں خدیجہ بنت خویلد رضی اللہ عنہا سے نکاح کیا اور تقریباً پچیس برس تک صرف انہی کے ساتھ رہے۔ ان کی حیات میں کوئی اور زوجہ نہ تھیں۔ ابن اسحاق، ابن ہشام اور ابن سعد اس طویل یک زوجگی کو مکی دور کا حصہ بتاتے ہیں۔ عام الحزن میں، ہجرت سے تقریباً تین سال پہلے (تقریباً 619ء)، خدیجہ کی وفات کے بعد مکہ پھر مدینہ میں مزید نکاح ہوئے۔

بعد کے نکاح زیادہ تر بیواؤں سے تھے جو اسلام لا چکی تھیں، ہجرت کر چکی تھیں، یا اللہ کی راہ میں شوہر کھو چکی تھیں۔ ان کے ذریعے رسول ﷺ نے عورتوں کو پناہ دی، ابو بکر و عمر رضی اللہ عنہما کے گھرانوں کی عزت کی، اور مخزوم، امیہ اور بنو مصطلق جیسے قبائل کو جماعت سے جوڑا۔ تعلیم بھی ایک حکمت تھی: مسجد نبوی سے ملے حجرے امت کے مدرسے بنے جہاں وضو، نماز، میراث اور نبوی اخلاق سیکھے گئے۔

سیرت میں معروف ترتیب، اور اس باب کے عناوین کی ترتیب، یہ ہے: خدیجہ بنت خویلد؛ سودہ بنت زمعہ؛ عائشہ بنت ابی بکر؛ حفصہ بنت عمر؛ زینب بنت خزیمہ؛ ام سلمہ ہند بنت ابی امیہ؛ زینب بنت جحش؛ جویریہ بنت الحارث؛ ام حبیبہ رملہ بنت ابی سفیان؛ صفیہ بنت حیي؛ اور میمونہ بنت الحارث۔ عائشہ سے نکاح مکہ میں ہوا؛ گھر ہجرت کے بعد مدینہ میں آباد ہوا۔ عمرہ القضاء کے بعد 7ھ میں سرف میں میمونہ سے نکاح آخری نکاح تھا۔

ہر ام المؤمنین رضی اللہ عنہن کو بخاری، مسلم اور طبقات کی کتابوں میں عزت سے یاد کیا گیا۔ عائشہ اور ام سلمہ اس امت کی خواتین میں بڑی راویات اور فقیہہ بنیں۔ کچھ صدقے، صبر، حبشہ کی ہجرت، یا قیدیوں کی آزادی والے نکاح سے پہچانی گئیں۔ نبوی گھرانے کے ادب کے بغیر ان کا ذکر نہیں کیا جاتا۔

ربیع الاول 11ھ (جون 632ء) میں آپ کی وفات کے بعد وہ اپنی وفات تک امہات المؤمنین رہیں۔ انہوں نے دوبارہ نکاح نہیں کیا۔ اکثر مدینہ کے بقیع میں دفن ہوئیں؛ میمونہ رضی اللہ عنہا سرف میں وفات پا کر وہیں دفن ہوئیں جہاں نکاح ہوا تھا۔ ان کی زندگیاں پہلی وحی سے خلفائے راشدین کے دور تک پھیلی ہوئی ہیں۔

پس یہ باب صرف ناموں کی فہرست نہیں بلکہ دعوت کی اندرونی تاریخ ہے: آغاز میں کون کھڑی رہیں، غزوات و معاہدات کے بعد کون گھر میں آئیں، اور اللہ نے ان گھروں کو بیواؤں، قبائل اور طالب علموں کے لیے رحمت کیسے بنایا۔ آگے ہر ماں کو اسی معروف سیرتی ترتیب سے بیان کیا گیا ہے۔""",
    """कुरआन नबी मुहम्मद ﷺ की अज़वाज को वह मर्तबा देता है जो किसी और घर को नहीं मिला। अल्लाह ने फ़रमाया: «नबी मोमिनों पर उनकी जान से अधिक हक़ रखते हैं और उनकी बीवियाँ उनकी माएँ हैं» (अल-अहज़ाब 33:6)। अहले सुन्नत की तफ़सीर इसे इज़्ज़त और हुक्म दोनों मानती है: उम्मत पर माँ जैसा एहतिराम है, और आपके बाद उनसे निकाह हराम रहा (33:53)। क्लासिकल सीरत उन्हें उम्महातुल मुमिनीन कहती है।

आप ﷺ ने मक्का में पच्चीस वर्ष की उम्र में ख़दीजा बिन्त ख़ुवैलिद رضي الله عنها से निकाह किया और लगभग पच्चीस वर्ष केवल उन्हीं के साथ रहे। उनकी ज़िंदगी में कोई और ज़ौजा न थीं। इब्न इसहाक, इब्न हिशाम और इब्न साद इस दीर्घ एकपत्नीत्व को मक्की दौर का हिस्सा बताते हैं। आम उल-हुज़्न में, हिजरत से लगभग तीन वर्ष पहले (लगभग 619 ई.), ख़दीजा की वफ़ात के बाद मक्का फिर मदीना में और निकाह हुए।

बाद के निकाह अधिकतर विधवाओं से थे जो इस्लाम ला चुकी थीं, हिजरत कर चुकी थीं, या अल्लाह की राह में शौहर खो चुकी थीं। इनके ज़रिए रसूल ﷺ ने औरतों को पनाह दी, अबू बक्र व उमर رضي الله عنهما के घरानों की इज़्ज़त की, और मख़ज़ूम, उमैया और बनू मुस्तलिक़ जैसे क़बीलों को जमाअत से जोड़ा। तालीम भी एक हिकमत थी: मस्जिद-ए-नबवी से जुड़े हुजरे उम्मत के मदरसे बने जहाँ वुज़ू, नमाज़, मीरास और नबवी अख़लाक़ सीखे गए।

सीरत में मा'रूफ़ तरतीब, और इस बाब के आइटम्स की तरतीब, यह है: ख़दीजा बिन्त ख़ुवैलिद; सौदा बिन्त ज़मआ; आयशा बिन्त अबी बक्र; हफ़्सा बिन्त उमर; ज़ैनब बिन्त ख़ुज़ैमा; उम्म सलमा हिन्द बिन्त अबी उमैया; ज़ैनब बिन्त जह्श; जुवैरिया बिन्त अल-हारिस; उम्म हबीबा रमला बिन्त अबी सुफ़्यान; सफ़िया बिन्त हुयय; और मैमूना बिन्त अल-हारिस। आयशा से निकाह मक्का में हुआ; घर हिजरत के बाद मदीना में आबाद हुआ। उमरा अल-क़ज़ा के बाद 7 हिजरी में सरिफ़ में मैमूना से निकाह आख़िरी निकाह था।

हर उम्मुल मुमिनीन رضي الله عنهن को बुख़ारी, मुस्लिम और तबाक़ात की किताबों में इज़्ज़त से याद किया गया। आयशा और उम्म सलमा इस उम्मत की ख़वातीन में बड़ी राविया और फ़क़ीहा बनीं। कुछ सदक़े, सब्र, हबशा की हिजरत, या क़ैदियों की आज़ादी वाले निकाह से पहचानी गईं। नबवी घराने के अदब के बिना उनका ज़िक्र नहीं किया जाता।

रबीउल अव्वल 11 हिजरी (जून 632 ई.) में आपकी वफ़ात के बाद वे अपनी वफ़ात तक उम्महातुल मुमिनीन रहीं। उन्होंने दोबारा निकाह नहीं किया। अधिकतर मदीना के बक़ी' में दफ़न हुईं; मैमूना رضي الله عنها सरिफ़ में वफ़ात पाकर वहीं दफ़न हुईं जहाँ निकाह हुआ था। उनकी ज़िंदगियाँ पहली वही से ख़ुलफ़ा-ए-राशिदीन के दौर तक फैली हैं।

पस यह बाब केवल नामों की फ़ेहरिस्त नहीं बल्कि दावत की अंदरूनी तारीख़ है: शुरुआत में कौन खड़ी रहीं, ग़ज़वात व मुआहदों के बाद कौन घर में आईं, और अल्लाह ने उन घरों को विधवाओं, क़बीलों और तालिब-ए-इल्म के लिए रहमत कैसे बनाया। आगे हर माँ को इसी मा'रूफ़ सीरती तरतीब से बयान किया गया है।""",
    """কুরআন নবী মুহাম্মদ ﷺ-এর স্ত্রীগণকে এমন মর্যাদা দিয়েছে যা অন্য কোনো ঘর পায়নি। আল্লাহ বলেছেন, ‘নবী মুমিনদের নিকট তাদের নিজেদের চেয়ে ঘনিষ্ঠ, আর তাঁর স্ত্রীগণ তাদের মাতা’ (আল-আহযাব ৩৩:৬)। সুন্নি তাফসির একে সম্মান ও বিধান দুই-ই মানে: উম্মাহর ওপর মায়ের মতো সম্মান, আর তাঁর পর অন্য পুরুষের সঙ্গে তাঁদের বিবাহ নিষিদ্ধ (৩৩:৫৩)। ক্লাসিক সিরাত তাঁদের উম্মাহাতুল মুমিনীন বলে।

তিনি ﷺ মক্কায় পঁচিশ বছর বয়সে খাদিজাহ বিনত খুওয়াইলিদ رضي الله عنها-কে বিয়ে করেন এবং প্রায় পঁচিশ বছর কেবল তাঁর সঙ্গে থাকেন। তাঁর জীবদ্দশায় অন্য কোনো স্ত্রী ছিলেন না। ইবন ইসহাক, ইবন হিশাম ও ইবন সাদ এই দীর্ঘ একবিবাহকে মক্কী যুগের অংশ বলে লেখেন। দুঃখের বছরে, হিজরতের প্রায় তিন বছর আগে (প্রায় ৬১৯ খ্রি.), খাদিজাহর ওফাতের পর মক্কায় ও পরে মদিনায় আরও বিবাহ হয়।

পরবর্তী বিবাহ অধিকাংশই বিধবাদের সঙ্গে, যাঁরা ইতোমধ্যে ইসলাম গ্রহণ করেছেন, হিজরত করেছেন, বা আল্লাহর পথে স্বামী হারিয়েছেন। এদের মাধ্যমে রাসূল ﷺ নারীদের আশ্রয় দেন, আবু বকর ও উমর رضي الله عنهما-এর ঘরের সম্মান করেন, এবং মাখযুম, উমাইয়া ও বনু মুস্তালিকের মতো গোত্রকে জামাতে যুক্ত করেন। শিক্ষাও একটি হিকমত ছিল: মসজিদে নববীর পাশের হুজরাগুলো উম্মাহর মাদরাসা হয়, যেখানে ওযু, সালাত, মিরাস ও নববি চরিত্র শেখা যায়।

সিরাতে প্রচলিত ক্রম, এবং এই অধ্যায়ের আইটেমের ক্রম, এই: খাদিজাহ বিনত খুওয়াইলিদ; সাওদাহ বিনত যামআহ; আয়িশাহ বিনত আবি বকর; হাফসাহ বিনত উমর; যাইনাব বিনত খুযাইমাহ; উম্মু সালামাহ হিন্দ বিনত আবি উমাইয়াহ; যাইনাব বিনত জাহশ; জুওয়াইরিয়াহ বিনত আল-হারিস; উম্মু হাবিবাহ রামলাহ বিনত আবি সুফিয়ান; সাফিয়্যাহ বিনত হুয়াইয়্য; এবং মায়মুনাহ বিনত আল-হারিস। আয়িশার সঙ্গে আকদ মক্কায় হয়; ঘর হিজরতের পর মদিনায় প্রতিষ্ঠিত হয়। উমরাতুল কাদার পর ৭ হিজরিতে সারিফে মায়মুনার সঙ্গে বিবাহ সর্বশেষ।

প্রত্যেক উম্মুল মুমিনীন رضي الله عنهن-কে বুখারি, মুসলিম ও তবাকাত গ্রন্থে মর্যাদার সঙ্গে স্মরণ করা হয়। আয়িশা ও উম্মু সালামাহ এই উম্মাহর নারীদের মধ্যে শ্রেষ্ঠ বর্ণনাকারী ও ফকীহ হন। কেউ দান, ধৈর্য, হাবশা হিজরত, বা বন্দিমুক্তির বিবাহের জন্য স্মরণীয়। নববি ঘরের আদব ছাড়া তাঁদের আলোচনা করা হয় না।

রবিউল আউয়াল ১১ হিজরি (জুন ৬৩২ খ্রি.)-তে তাঁর ওফাতের পর তাঁরা নিজেদের ওফাত পর্যন্ত উম্মাহাতুল মুমিনীন থাকেন। তাঁরা পুনরায় বিয়ে করেননি। অধিকাংশ মদিনার বাকীতে দাফন হন; মায়মুনাহ رضي الله عنها সারিফে ওফাত পেয়ে সেখানেই দাফন হন যেখানে বিবাহ হয়েছিল। তাঁদের জীবন প্রথম ওহী থেকে খুলাফায়ে রাশেদীনের পরবর্তী বছর পর্যন্ত বিস্তৃত।

সুতরাং এই অধ্যায় কেবল নামের তালিকা নয়, দাওয়াতের অন্তর্জীবন: শুরুতে কারা দাঁড়িয়েছিলেন, যুদ্ধ ও সন্ধির পর কারা ঘরে এসেছেন, এবং আল্লাহ সেই ঘরগুলোকে বিধবা, গোত্র ও জ্ঞানপিপাসুদের জন্য কীভাবে রহমত করেছেন। এরপর প্রত্যেক মাতাকে এই পরিচিত সিরাতি ক্রমে বর্ণনা করা হয়েছে।""",
    """Al-Qur'an memberi istri Nabi Muhammad ﷺ kedudukan yang tidak dimiliki rumah tangga lain. Allah berfirman: "Nabi itu lebih utama bagi orang-orang mukmin daripada diri mereka sendiri, dan istri-istrinya adalah ibu-ibu mereka" (al-Ahzab 33:6). Tafsir Ahlus Sunnah membacanya sebagai kehormatan dan hukum: umat wajib menghormati mereka seperti ibu, dan mereka haram dinikahi orang lain setelah beliau (33:53). Sirah klasik menamai mereka Ummahatul Mukminin, ibu kaum mukmin.

Beliau ﷺ menikahi Khadijah binti Khuwailid radhiyallahu anha di Makkah pada usia dua puluh lima tahun dan hidup hanya dengannya sekitar dua puluh lima tahun. Beliau tidak mengambil istri lain semasa Khadijah hidup. Ibnu Ishaq, Ibnu Hisyam, dan Ibnu Sa'd mencatat monogami panjang itu sebagai bagian era Makkah. Setelah kewafatannya pada Tahun Kesedihan, sekitar tiga tahun sebelum Hijrah (sekitar 619 M), pernikahan berikutnya dimulai di Makkah lalu di Madinah.

Pernikahan kemudian sebagian besar dengan janda yang sudah masuk Islam, berhijrah, atau kehilangan suami di jalan Allah. Melalui mereka Rasulullah ﷺ menaungi perempuan, memuliakan rumah Abu Bakar dan Umar radhiyallahu anhuma, dan mengikat suku seperti Makhzum, Umayyah, dan Bani Mustaliq kepada jamaah. Pengajaran adalah hikmah lain: kamar-kamar di sisi Masjid Nabawi menjadi sekolah umat, tempat wudu, salat, waris, dan adab nabi dipelajari.

Urutan yang umum dalam sirah, dan urutan butir bab ini, ialah: Khadijah binti Khuwailid; Saudah binti Zam'ah; Aisyah binti Abu Bakar; Hafshah binti Umar; Zainab binti Khuzaimah; Ummu Salamah Hind binti Abu Umayyah; Zainab binti Jahsy; Juwairiyah binti al-Harits; Ummu Habibah Ramlah binti Abu Sufyan; Safiyyah binti Huyay; dan Maimunah binti al-Harits. Akad dengan Aisyah terjadi di Makkah; rumah tangga tegak di Madinah setelah Hijrah. Maimunah, dinikahi di Sarif tahun 7 H setelah umrah al-qadha, adalah yang terakhir.

Setiap Ummul Mukminin radhiyallahu anhunna dikenang dengan kehormatan dalam Bukhari, Muslim, dan kitab thabaqat. Aisyah dan Ummu Salamah menjadi di antara perawi dan ahli fikih terbesar di kalangan wanita umat ini. Yang lain dikenang karena sedekah, kesabaran, hijrah ke Habasyah, atau pernikahan yang membebaskan tawanan. Tidak seorang pun dari mereka dibicarakan kecuali dengan adab rumah tangga nabi.

Setelah wafat beliau pada Rabiul Awal 11 H (Juni 632 M) mereka tetap ibu kaum mukmin hingga ajal mereka. Mereka tidak menikah lagi. Sebagian besar dimakamkan di Baqi di Madinah; Maimunah radhiyallahu anha wafat dan dimakamkan di Sarif, tempat beliau menikahinya. Hidup mereka terbentang dari wahyu pertama hingga tahun-tahun belakangan Khulafaur Rasyidin.

Bab ini karena itu bukan daftar nama duniawi, melainkan sejarah batin dakwah: siapa yang berdiri di awal, siapa yang masuk rumah tangga setelah peperangan dan perjanjian, dan bagaimana Allah menjadikan rumah-rumah itu rahmat bagi janda, suku, dan penuntut ilmu. Berikutnya setiap ibu diuraikan menurut urutan sirah yang dikenal.""",
)

c["items"][0]["details"] = D(
    """Khadijah bint Khuwaylid ibn Asad رضي الله عنها, of Banu Asad of Quraysh, was the first wife of the Prophet ﷺ and the first to believe in him. She was a woman of wealth and judgement, a merchant of Makkah whose caravans were known in the markets. Twice widowed before him, she employed Muhammad ﷺ to trade to Syria, then, seeing his honesty, sought marriage through her friend Nafisah. He was twenty-five; the well-known report in Ibn Ishaq gives her age as forty. The marriage was in Makkah, before prophethood, and it lasted until her death.

She supported him with wealth and with her heart. When the first revelation came in the cave of Hira' he returned trembling; she wrapped him, calmed him, and took him to her cousin Waraqah ibn Nawfal, who recognised the Namus of Musa ﷺ. She said: "Never! By Allah, Allah will never disgrace you. You keep ties of kinship, speak truth, bear the burden, honour the guest, and help in the causes of right." That testimony is in Sahih al-Bukhari. She was the first to pray with him.

All his children except Ibrahim—who was born later to Maria al-Qibtiyya—were from Khadijah: al-Qasim, Abdullah (called al-Tayyib and al-Tahir), and the daughters Zaynab, Ruqayyah, Umm Kulthum, and Fatimah رضي الله عنهن. The boys died in childhood in Makkah. The daughters lived to see Islam; Fatimah was the youngest and the most beloved. Khadijah's house was the shelter of the earliest da'wah when Quraysh still mocked.

He ﷺ married no other woman while she lived. After her death he remembered her constantly. Aisha رضي الله عنها said she was never more jealous of any woman than of Khadijah, though she had never seen her, because he mentioned her so often. He would slaughter a sheep and send portions to Khadijah's friends. When he heard a voice that resembled hers he would grow glad. Aisha's report is in the two Sahihs and is told with respect for both Mothers.

Khadijah died in Makkah about three years before the Hijrah, around 619 CE, in the same hard season in which Abu Talib died. The year is called 'Am al-Huzn, the Year of Sorrow. She was buried at al-Hajun, in what later became Jannat al-Mu'alla. Jibril came to the Prophet ﷺ and said: "Give Khadijah greetings of peace from her Lord and from me, and give her glad tidings of a house of pearls in Paradise in which there is no noise and no toil" (Bukhari and Muslim).

Ibn Sa'd and the books of shamail gather her virtues: generosity, intellect, and a faith that did not waver when the boycott of Banu Hashim pressed the valley. She spent her fortune on the poor of the new religion. The Prophet ﷺ did not forget that debt of love. In later Madinah, when other wives entered the household, her name remained the measure of loyalty.

Sunni seerah therefore begins the list of the Mothers with her, not only because she was first in time, but because she was first in iman. To speak of the wives of the Prophet ﷺ without Khadijah is to miss the foundation on which the later household was built. May Allah be pleased with her.""",
    """خدیجہ بنت خویلد بن اسد رضی اللہ عنہا، قریش کے بنو اسد سے، نبی ﷺ کی پہلی زوجہ اور سب سے پہلے ایمان لانے والیں تھیں۔ مال اور رائے والی خاتون تھیں، مکہ کی تاجرة جن کے قافلے بازاروں میں جانے جاتے تھے۔ آپ سے پہلے دو بار بیوہ ہو چکی تھیں۔ انہوں نے محمد ﷺ کو شام کی تجارت پر مقرر کیا، پھر آپ کی امانت دیکھ کر نفسیہ کے ذریعے نکاح چاہا۔ آپ پچیس سال کے تھے؛ ابن اسحاق کی مشہور روایت میں ان کی عمر چالیس بیان ہوئی۔ نکاح نبوت سے پہلے مکہ میں ہوا اور وفات تک قائم رہا۔

انہوں نے مال اور دل سے ساتھ دیا۔ غار حرا میں پہلی وحی کے بعد آپ کانپتے ہوئے لوٹے؛ انہوں نے اوڑھایا، تسلی دی، اور چچا زاد ورقہ بن نوفل کے پاس لے گئیں جنہوں نے موسیٰ ﷺ کے ناموس کو پہچانا۔ فرمایا: «کلا والله لا يخزيك الله أبداً» — اللہ تمہیں رسوا نہ کرے گا؛ تم صلہ رحمی کرتے، سچ بولتے، بوجھ اٹھاتے، مہمان نوازی کرتے اور حق کے کاموں میں مدد کرتے ہو۔ یہ شہادت صحیح بخاری میں ہے۔ وہ پہلے آپ کے ساتھ نماز پڑھیں۔

ابراہیم کے سوا—جو بعد میں ماریہ قبطیہ سے ہوئے—تمام اولاد خدیجہ سے تھی: قاسم، عبد اللہ (طیب و طاہر)، اور بیٹیاں زینب، رقیہ، ام کلثوم اور فاطمہ رضی اللہ عنہن۔ بیٹے مکہ میں بچپن میں فوت ہوئے۔ بیٹیاں اسلام دیکھیں؛ فاطمہ سب سے چھوٹی اور محبوب ترین تھیں۔ قریش کے مذاق کے دنوں میں خدیجہ کا گھر دعوت کا پہلا پناہ گاہ تھا۔

ان کی حیات میں آپ ﷺ نے کوئی اور نکاح نہیں کیا۔ وفات کے بعد کثرت سے یاد فرماتے۔ عائشہ رضی اللہ عنہا فرماتی ہیں خدیجہ جیسی رشک کسی عورت پر نہیں آیا حالانکہ انہیں دیکھا نہیں، کیونکہ آپ ان کا ذکر بار بار کرتے تھے۔ دنبہ ذبح کر کے خدیجہ کی سہیلیوں کو بھیجتے۔ ان جیسی آواز سن کر خوش ہوتے۔ عائشہ کی یہ روایت دونوں صحیحوں میں ہے اور دونوں امهات کے ادب سے بیان ہوتی ہے۔

خدیجہ مکہ میں ہجرت سے تقریباً تین سال پہلے، لگ بھگ 619ء، اسی سخت موسم میں فوت ہوئیں جس میں ابو طالب کا انتقال ہوا۔ اسے عام الحزن کہتے ہیں۔ تدفین الحجون میں ہوئی، جو بعد میں جنت المعلیٰ کہلائی۔ جبریل نبی ﷺ کے پاس آئے اور کہا: خدیجہ کو ان کے رب اور میری طرف سے سلام کہو، اور موتیوں کے گھر کی بشارت دو جس میں نہ شور ہے نہ تکلیف (بخاری و مسلم)۔

ابن سعد اور شمائل کی کتابیں ان کے فضائل جمع کرتی ہیں: سخاوت، عقل، اور وہ ایمان جو شعب ابی طالب کے بائیکاٹ میں نہ ہلا۔ نئے دین کے غریبوں پر مال خرچ کیا۔ نبی ﷺ اس احسان کو نہ بھولے۔ بعد کے مدنی گھر میں جب اور ازواج آئیں، خدیجہ کا نام وفا کا پیمانہ رہا۔

لہٰذا اہل سنت کی سیرت امهات کی فہرست انہیں سے شروع کرتی ہے، نہ صرف اس لیے کہ وقت میں پہلی تھیں بلکہ اس لیے کہ ایمان میں پہلی تھیں۔ خدیجہ کے بغیر ازواج مطہرات کی بات بنیاد چھوڑ دینی ہے۔ اللہ ان سے راضی ہو۔""",
    """ख़दीजा बिन्त ख़ुवैलिद इब्न असद رضي الله عنها, कुरैश के बनू असद से, नबी ﷺ की पहली ज़ौजा और सबसे पहले ईमान लाने वाली थीं। माल और राय वाली ख़ातून थीं, मक्का की ताजिरा जिनके क़ाफ़िले बाज़ारों में मशहूर थे। आपसे पहले दो बार विधवा हो चुकी थीं। उन्होंने मुहम्मद ﷺ को शाम की तिजारत पर मुक़र्रर किया, फिर आपकी अमानत देखकर नफ़ीसा के ज़रिए निकाह चाहा। आप पच्चीस वर्ष के थे; इब्न इसहाक की मशहूर रिवायत में उनकी उम्र चालीस बताई गई। निकाह नुबुव्वत से पहले मक्का में हुआ और वफ़ात तक क़ायम रहा।

उन्होंने माल और दिल से साथ दिया। गार-ए-हिरा में पहली वही के बाद आप कांपते लौटे; उन्होंने ओढ़ाया, तसल्ली दी, और चचेरे वारक़ा इब्न नौफ़ल के पास ले गईं जिन्होंने मूसा ﷺ के नामूस को पहचाना। फ़रमाया: अल्लाह तुम्हें रुसवा न करेगा; तुम सिल-ए-रहमी करते, सच बोलते, बोझ उठाते, मेहमाननवाज़ी करते और हक़ के कामों में मदद करते हो। यह गवाही सही बुख़ारी में है। वे पहले आपके साथ नमाज़ पढ़ीं।

इबराहीम के सिवा—जो बाद में मारिया क़िब्तिया से हुए—तमाम औलाद ख़दीजा से थी: क़ासिम, अब्दुल्लाह (तय्यिब व ताहिर), और बेटियाँ ज़ैनब, रुक़य्या, उम्म कुलसूम और फ़ातिमा رضي الله عنهن। बेटे मक्का में बचपन में फ़ौत हुए। बेटियाँ इस्लाम देखीं; फ़ातिमा सबसे छोटी और महबूब थीं। कुरैश के मज़ाक के दिनों में ख़दीजा का घर दावत की पहली पनाहगाह था।

उनकी हयात में आप ﷺ ने कोई और निकाह नहीं किया। वफ़ात के बाद कसरत से याद फ़रमाते। आयशा رضي الله عنها फ़रमाती हैं ख़दीजा जैसी रश्क किसी औरत पर नहीं आई हालाँकि उन्हें देखा नहीं, क्योंकि आप उनका ज़िक्र बार-बार करते थे। दुम्बा ज़बह कर ख़दीजा की सहेलियों को भेजते। उनकी जैसी आवाज़ सुनकर ख़ुश होते। आयशा की यह रिवायत दोनों सहीहों में है और दोनों उम्महात के अदब से बयान होती है।

ख़दीजा मक्का में हिजरत से लगभग तीन वर्ष पहले, तकरीबन 619 ई., उसी सख़्त मौसम में फ़ौत हुईं जिसमें अबू तालिब का इंतिक़ाल हुआ। उसे आम उल-हुज़्न कहते हैं। तदफ़ीन अल-हजून में हुई, जो बाद में जन्नतुल मुअल्ला कहलाई। जिब्रील नबी ﷺ के पास आए और कहा: ख़दीजा को उनके रब और मेरी तरफ़ से सलाम कहो, और मोतियों के घर की बशारत दो जिसमें न शोर है न तकलीफ़ (बुख़ारी व मुस्लिम)।

इब्न साद और शमाइल की किताबें उनके फ़ज़ाइल जमा करती हैं: सख़ावत, अक़्ल, और वह ईमान जो शिअब-ए-अबी तालिब के बायकॉट में न हिला। नए दीन के ग़रीबों पर माल ख़र्च किया। नबी ﷺ इस एहसान को न भूले। बाद के मदनी घर में जब और अज़वाज आईं, ख़दीजा का नाम वफ़ा का पैमाना रहा।

लिहाज़ा अहले सुन्नत की सीरत उम्महात की फ़ेहरिस्त उन्हीं से शुरू करती है, न केवल इसलिए कि वक़्त में पहली थीं बल्कि इसलिए कि ईमान में पहली थीं। ख़दीजा के बिना अज़वाज-ए-मुतहहरात की बात बुनियाद छोड़ देनी है। अल्लाह उनसे राज़ी हो।""",
    """খাদিজাহ বিনত খুওয়াইলিদ ইবন আসাদ رضي الله عنها, কুরাইশের বনু আসাদ থেকে, নবী ﷺ-এর প্রথম স্ত্রী এবং সর্বপ্রথম ঈমান আনেন। তিনি ধন ও বিচারবুদ্ধির অধিকারী মক্কার ব্যবসায়ী ছিলেন, যাঁর কাফেলা বাজারে পরিচিত ছিল। তাঁর আগে দুবার বিধবা হয়েছিলেন। তিনি মুহাম্মদ ﷺ-কে সিরিয়ার বাণিজ্যে নিযুক্ত করেন, পরে সততা দেখে নফিসার মাধ্যমে বিবাহ চান। তিনি তখন পঁচিশ; ইবন ইসহাকের প্রসিদ্ধ বর্ণনায় খাদিজাহর বয়স চল্লিশ। বিবাহ নবুয়তের আগে মক্কায় হয় এবং ওফাত পর্যন্ত স্থায়ী থাকে।

তিনি সম্পদ ও হৃদয় দিয়ে সহায়তা করেন। হিরা গুহায় প্রথম ওহীর পর তিনি কাঁপতে কাঁপতে ফিরে আসেন; খাদিজাহ তাঁকে জড়িয়ে সান্ত্বনা দেন এবং চাচাতো ভাই ওয়ারাকাহ ইবন নাওফালের কাছে নিয়ে যান, যিনি মূসা ﷺ-এর নামূস চেনেন। তিনি বলেন, ‘কখনো নয়! আল্লাহ আপনাকে কখনো লাঞ্ছিত করবেন না। আপনি আত্মীয়তার সম্পর্ক রক্ষা করেন, সত্য বলেন, বোঝা বহন করেন, মেহমানের সম্মান করেন এবং ন্যায়ের কাজে সাহায্য করেন।’ এই সাক্ষ্য সহীহ বুখারিতে আছে। তিনিই প্রথম তাঁর সঙ্গে সালাত আদায় করেন।

ইবরাহিম ছাড়া—যিনি পরে মারিয়াহ আল-কিবতিয়াহর গর্ভে জন্মান—তাঁর সব সন্তান খাদিজাহ থেকে: আল-কাসিম, আব্দুল্লাহ (আত-তাইয়্যিব ও আত-তাহির), এবং কন্যা যাইনাব, রুকইয়াহ, উম্মু কুলসুম ও ফাতিমাহ رضي الله عنهن। পুত্ররা মক্কায় শৈশবে মারা যান। কন্যারা ইসলাম দেখেন; ফাতিমাহ সর্বকনিষ্ঠ ও সর্বাধিক প্রিয়। কুরাইশের উপহাসের দিনে খাদিজাহর ঘরই প্রথম দাওয়াতের আশ্রয় ছিল।

তাঁর জীবদ্দশায় তিনি ﷺ অন্য কাউকে বিয়ে করেননি। ওফাতের পর তিনি তাঁকে সর্বদা স্মরণ করতেন। আয়িশা رضي الله عنها বলেন, তিনি খাদিজাহর মতো অন্য কোনো নারীর প্রতি ঈর্ষা করেননি, যদিও তাঁকে দেখেননি, কারণ তিনি তাঁর কথা এতবার বলতেন। তিনি দুম্বা জবেহ করে খাদিজাহর সখীদের পাঠাতেন। তাঁর মতো কণ্ঠ শুনলে আনন্দিত হতেন। আয়িশার এই বর্ণনা দুই সহীহতে আছে এবং উভয় উম্মুল মুমিনীনের আদব রেখে বলা হয়।

খাদিজাহ মক্কায় হিজরতের প্রায় তিন বছর আগে, প্রায় ৬১৯ খ্রিস্টাব্দে, সেই কঠিন মৌসুমে ইন্তেকাল করেন যে মৌসুমে আবু তালিবও মারা যান। বছরটিকে আমুল হুজন, দুঃখের বছর বলা হয়। তাঁকে আল-হাজুনে দাফন করা হয়, যা পরে জান্নাতুল মুআল্লা নামে পরিচিত। জিবরীল নবী ﷺ-এর কাছে এসে বলেন, ‘খাদিজাহকে তাঁর রব ও আমার পক্ষ থেকে সালাম বলুন, এবং জান্নাতে মুক্তার একটি ঘরের সুসংবাদ দিন যেখানে শোরগোল নেই, কষ্ট নেই’ (বুখারি ও মুসলিম)।

ইবন সাদ ও শামাইল গ্রন্থ তাঁর ফযীলত সংগ্রহ করে: দানশীলতা, বুদ্ধি, এবং সেই ঈমান যা বনু হাশিমের বয়কটে টলেনি। তিনি নতুন দ্বীনের দরিদ্রদের ওপর সম্পদ ব্যয় করেন। নবী ﷺ সেই ইহসান ভোলেননি। পরে মদিনার ঘরে অন্য স্ত্রীগণ আসলেও খাদিজাহর নামই আনুগত্যের মাপকাঠি থাকে।

সুতরাং সুন্নি সিরাত উম্মাহাতের তালিকা তাঁ দিয়েই শুরু করে, কেবল সময়ের দিক থেকে প্রথম বলে নয়, ঈমানে প্রথম বলে। খাদিজাহ ছাড়া নবীর স্ত্রীগণের আলোচনা ভিত্তি ছাড়াই হয়। আল্লাহ তাঁর প্রতি সন্তুষ্ট হোন।""",
    """Khadijah binti Khuwailid bin Asad radhiyallahu anha, dari Bani Asad Quraisy, adalah istri pertama Nabi ﷺ dan orang pertama yang beriman kepada beliau. Ia wanita berharta dan berpandangan tajam, pedagang Makkah yang kafilahnya dikenal di pasar. Dua kali menjanda sebelum beliau, ia mempekerjakan Muhammad ﷺ berdagang ke Syam, lalu karena kejujurannya meminta pernikahan melalui sahabatnya Nafisah. Beliau berusia dua puluh lima; riwayat terkenal Ibnu Ishaq menyebut usia Khadijah empat puluh. Pernikahan terjadi di Makkah sebelum kenabian dan berlangsung hingga ia wafat.

Ia menopang beliau dengan harta dan dengan hati. Ketika wahyu pertama turun di Gua Hira, beliau pulang gemetar; Khadijah menyelimuti, menenangkan, dan membawanya kepada sepupunya Waraqah bin Naufal, yang mengenali Namus Musa ﷺ. Ia berkata: "Tidak! Demi Allah, Allah tidak akan menghinakanmu. Engkau menyambung silaturahmi, berkata benar, memikul beban, memuliakan tamu, dan menolong perkara yang hak." Kesaksian itu ada dalam Sahih al-Bukhari. Ia orang pertama yang salat bersama beliau.

Semua anak beliau kecuali Ibrahim—yang kemudian lahir dari Maria al-Qibtiyah—berasal dari Khadijah: al-Qasim, Abdullah (dipanggil al-Thayyib dan al-Tahir), serta putri Zainab, Ruqayyah, Ummu Kultsum, dan Fatimah radhiyallahu anhunna. Putra-putra meninggal kecil di Makkah. Putri-putri sempat melihat Islam; Fatimah yang bungsu dan paling dicintai. Rumah Khadijah adalah naungan dakwah paling awal ketika Quraisy masih mencemooh.

Beliau ﷺ tidak menikah dengan wanita lain semasa Khadijah hidup. Setelah ia wafat, beliau senantiasa mengingatnya. Aisyah radhiyallahu anha berkata ia tidak pernah lebih cemburu kepada wanita mana pun melebihi Khadijah, padahal ia tidak pernah melihatnya, karena beliau begitu sering menyebutnya. Beliau menyembelih kambing dan mengirim bagian kepada sahabat Khadijah. Ketika mendengar suara yang menyerupainya, beliau gembira. Riwayat Aisyah ada dalam dua sahih dan diceritakan dengan adab bagi kedua ibu kaum mukmin.

Khadijah wafat di Makkah sekitar tiga tahun sebelum Hijrah, sekitar 619 M, pada musim yang sama ketika Abu Thalib meninggal. Tahun itu disebut 'Am al-Huzn, Tahun Kesedihan. Ia dimakamkan di al-Hajun, yang kemudian menjadi Jannatul Mu'alla. Jibril datang kepada Nabi ﷺ dan berkata: "Sampaikan kepada Khadijah salam dari Tuhannya dan dariku, dan berilah kabar gembira berupa rumah dari mutiara di surga yang tiada kegaduhan dan tiada letih" (Bukhari dan Muslim).

Ibnu Sa'd dan kitab syamail menghimpun keutamaannya: kedermawanan, kecerdasan, dan iman yang tidak goyah ketika pemboikotan Bani Hasyim menekan lembah. Ia membelanjakan hartanya untuk orang miskin agama yang baru. Nabi ﷺ tidak melupakan utang cinta itu. Di Madinah kemudian, ketika istri lain masuk rumah tangga, namanya tetap ukuran kesetiaan.

Sirah Ahlus Sunnah karena itu memulai daftar para ibu dengan Khadijah, bukan hanya karena ia pertama dalam waktu, tetapi karena ia pertama dalam iman. Membicarakan istri Nabi ﷺ tanpa Khadijah berarti kehilangan fondasi rumah tangga yang kemudian dibangun. Semoga Allah meridainya.""",
)

c["items"][1]["details"] = D(
    """Sawdah bint Zam'ah ibn Qays رضي الله عنها was of Banu Amir ibn Lu'ayy of Quraysh. She accepted Islam early, together with her husband al-Sakran ibn Amr, and they were among those who migrated to Abyssinia when Quraysh persecuted the weak. After returning to Makkah, Sakran died, and she remained a widow of mature years, known for a large, kind presence and a ready humour.

After Khadijah's death the household of the Prophet ﷺ was empty of a wife's companionship. Khawlah bint Hakim suggested two names: the young Aisha, daughter of his closest friend, and Sawdah, a believing widow who had already borne the cost of hijrah. He ﷺ married Sawdah in Makkah, before the Hijrah, so that a believing woman of experience would keep the house. She later migrated to Madinah and lived in one of the chambers beside the mosque.

Classical reports remember her laughter. The Prophet ﷺ smiled at her jokes; Ibn Sa'd preserves glimpses of a household that was not only solemn. She was older than several of the later wives and treated the younger ones with a sister's ease. Her Islam was not a late convenience: it had already been tested in the crossing to the Negus and in the return to a hostile Makkah.

In Madinah, as other marriages followed, turns were divided among the wives. When Sawdah grew older she feared that he ﷺ might divorce her, and she preferred to remain his wife on the Day of Resurrection. She therefore gifted her night to Aisha رضي الله عنها out of love for the Messenger ﷺ. The commentators of 4:128 mention this as an instance of a wife who yields a right in peace. He accepted the gift and she kept her rank as Mother of the Believers.

She transmitted a number of hadith and remained in Madinah after his wafat. Reports of her death vary; a well-known statement places it in Madinah around 54 AH, in the caliphate of Mu'awiyah, and her burial in al-Baqi'. Other early notices put her passing earlier. What is agreed is that she died a widow of the Prophet ﷺ and did not remarry.

Sunni seerah does not treat her as a footnote between Khadijah and Aisha. She was the woman who stood in the house in the last Makkan years and the first Madinan years, when the community was still small and grief for Khadijah was fresh. Her gift of her night is remembered as generosity, not as humiliation.

Thus the second Mother in the customary list is a widow of Abyssinia, married in Makkah after the Year of Sorrow, remembered for humour, and honoured for preferring the prophetic household to her own turn. May Allah be pleased with her.""",
    """سودہ بنت زمعہ بن قیس رضی اللہ عنہا قریش کے بنو عامر بن لوی سے تھیں۔ جلد اسلام لائیں، شوہر سکران بن عمرو کے ساتھ، اور کمزوروں پر قریش کے ظلم کے وقت حبشہ ہجرت کرنے والوں میں سے تھیں۔ مکہ واپسی کے بعد سکران فوت ہوئے؛ وہ پختہ عمر کی بیوہ رہیں، بڑی نرم طبیعت اور حاضر جواب مزاح کے ساتھ پہچانی گئیں۔

خدیجہ کی وفات کے بعد نبی ﷺ کے گھر میں زوجہ کی رفاقت نہ رہی۔ خولہ بنت حکیم نے دو نام تجویز کیے: جوان عائشہ، قریبی ترین دوست کی بیٹی، اور سودہ، ایمان والی بیوہ جنہوں نے ہجرت کی قیمت ادا کی تھی۔ آپ ﷺ نے ہجرت سے پہلے مکہ میں سودہ سے نکاح کیا تاکہ تجربہ کار مؤمنہ گھر سنبھالے۔ بعد میں مدینہ ہجرت کیں اور مسجد سے ملے حجرے میں رہیں۔

کلاسیکی روایات ان کے ہنسنے کو یاد کرتی ہیں۔ نبی ﷺ ان کے لطیفوں پر مسکراتے؛ ابن سعد گھر کی جھلکیاں محفوظ کرتے ہیں جو صرف سنجیدگی نہ تھی۔ وہ کئی بعد کی ازواج سے عمر میں بڑی تھیں اور چھوٹی بہنوں سے سہولت سے پیش آتیں۔ ان کا اسلام دیر کی سہولت نہ تھا: نجاشی کی طرف سفر اور دشمن مکہ میں واپسی میں آزمایا جا چکا تھا۔

مدینہ میں جب اور نکاح ہوئے تو باریاں تقسیم ہوئیں۔ جب سودہ کی عمر زیادہ ہوئی تو اندیشہ ہوا کہ آپ ﷺ جدائی فرما دیں، حالانکہ وہ قیامت کے دن آپ کی زوجہ رہنا چاہتی تھیں۔ اس لیے رسول ﷺ کی محبت میں اپنی رات عائشہ رضی اللہ عنہا کو ہبہ کر دی۔ 4:128 کے مفسرین اسے اس مثال میں لاتے ہیں جب بیوی صلح سے حق چھوڑے۔ آپ نے ہبہ قبول کیا اور وہ ام المؤمنین کے مرتبے پر رہیں۔

کچھ احادیث روایت کیں اور وفات نبوی کے بعد مدینہ میں رہیں۔ وفات کی روایات مختلف ہیں؛ مشہور قول انہیں تقریباً 54ھ میں معاویہ کی خلافت میں مدینہ میں دفن بتاتا ہے، بقیع میں۔ کچھ اگلی خبریں پہلے کی وفات بتاتی ہیں۔ متفق علیہ یہ ہے کہ وہ نبی ﷺ کی بیوہ فوت ہوئیں اور دوبارہ نکاح نہ کیا۔

اہل سنت کی سیرت انہیں خدیجہ اور عائشہ کے درمیان حاشیہ نہیں سمجھتی۔ وہ عورت تھیں جو آخری مکی اور پہلی مدنی برسوں میں گھر میں کھڑی رہیں، جب جماعت چھوٹی تھی اور خدیجہ کا غم تازہ تھا۔ رات کا ہبہ سخاوت کے طور پر یاد ہے، رسوائی کے طور پر نہیں۔

یوں معروف فہرست کی دوسری ماں حبشہ کی مہاجر بیوہ ہیں، عام الحزن کے بعد مکہ میں نکاح، مزاح سے یاد، اور اپنی باری پر نبوی گھر کو ترجیح دینے سے عزت۔ اللہ ان سے راضی ہو۔""",
    """सौदा बिन्त ज़मआ इब्न क़ैस رضي الله عنها कुरैश के बनू आमिर इब्न लुअय्य से थीं। जल्दी इस्लाम लाईं, शौहर सक्रान इब्न अम्र के साथ, और कमज़ोरों पर कुरैश के ज़ुल्म के वक़्त हबशा हिजरत करने वालों में थीं। मक्का वापसी के बाद सक्रान फ़ौत हुए; वे परिपक्व उम्र की विधवा रहीं, बड़ी नरम तबीयत और हाज़िरजवाब मिज़ाज से पहचानी गईं।

ख़दीजा की वफ़ात के बाद नबी ﷺ के घर में ज़ौजा की रफ़ाक़त न रही। ख़ौला बिन्त हकीम ने दो नाम सुझाए: जवान आयशा, क़रीबी दोस्त की बेटी, और सौदा, ईमान वाली विधवा जिन्होंने हिजरत की क़ीमत अदा की थी। आप ﷺ ने हिजरत से पहले मक्का में सौदा से निकाह किया ताकि तजरबेकार मोमिना घर संभाले। बाद में मदीना हिजरत कीं और मस्जिद से जुड़े हुजरे में रहीं।

क्लासिकल रिवायात उनकी हँसी को याद करती हैं। नबी ﷺ उनके लतीफ़ों पर मुस्कराते; इब्न साद घर की झलकियाँ महफ़ूज़ करते हैं जो केवल संजीदगी न थी। वे कई बाद की अज़वाज से उम्र में बड़ी थीं और छोटी बहनों से सहूलत से पेश आतीं। उनका इस्लाम देर की सहूलत न था: नजाशी की तरफ़ सफ़र और दुश्मन मक्का में वापसी में आज़माया जा चुका था।

मदीना में जब और निकाह हुए तो बारियाँ बँटीं। जब सौदा की उम्र अधिक हुई तो अंदेशा हुआ कि आप ﷺ जुदाई फ़रमा दें, हालाँकि वे क़ियामत के दिन आपकी ज़ौजा रहना चाहती थीं। इसलिए रसूल ﷺ की मुहब्बत में अपनी रात आयशा رضي الله عنها को हिबा कर दी। 4:128 के मुफ़स्सिरिन इसे उस मिसाल में लाते हैं जब बीवी सुलह से हक़ छोड़ दे। आपने हिबा क़ुबूल किया और वे उम्मुल मुमिनीन के मर्तबे पर रहीं।

कुछ हदीसें रिवायत कीं और विसाल-ए-नबवी के बाद मदीना में रहीं। वफ़ात की रिवायात मुख़्तलिफ़ हैं; मशहूर क़ौल उन्हें लगभग 54 हिजरी में मुआविया की ख़िलाफ़त में मदीना, बक़ी' में दफ़न बताता है। कुछ अगेली ख़बरें पहले की वफ़ात बताती हैं। मुत्तफ़िक़ यह है कि वे नबी ﷺ की विधवा फ़ौत हुईं और दोबारा निकाह न किया।

अहले सुन्नत की सीरत उन्हें ख़दीजा और आयशा के बीच हाशिया नहीं समझती। वे औरत थीं जो आख़िरी मक्की और पहली मदनी बरसों में घर में खड़ी रहीं, जब जमाअत छोटी थी और ख़दीजा का ग़म ताज़ा था। रात का हिबा सख़ावत के तौर पर याद है, रुसवाई के तौर पर नहीं।

यूँ मा'रूफ़ फ़ेहरिस्त की दूसरी माँ हबशा की मुहाजिर विधवा हैं, आम उल-हुज़्न के बाद मक्का में निकाह, मिज़ाज से याद, और अपनी बारी पर नबवी घर को तरजीह देने से इज़्ज़त। अल्लाह उनसे राज़ी हो।""",
    """সাওদাহ বিনত যামআহ ইবন কায়স رضي الله عنها কুরাইশের বনু আমির ইবন লুআয়্য থেকে ছিলেন। তিনি স্বামী আস-সাকরান ইবন আমরের সঙ্গে আগেই ইসলাম গ্রহণ করেন এবং কুরাইশ দুর্বলদের নির্যাতন করলে হাবশায় হিজরতকারীদের অন্তর্ভুক্ত হন। মক্কায় ফেরার পর সাকরান মারা যান; তিনি পরিণত বয়সের বিধবা থাকেন, বড় সদয় উপস্থিতি ও উপস্থিত রসবোধে পরিচিত।

খাদিজাহর ওফাতের পর নবী ﷺ-এর ঘরে স্ত্রীর সঙ্গ ছিল না। খাওলাহ বিনত হাকিম দুটি নাম প্রস্তাব করেন: তরুণী আয়িশা, তাঁর ঘনিষ্ঠতম বন্ধুর কন্যা, এবং সাওদাহ, মুমিন বিধবা যিনি হিজরতের মূল্য দিয়েছেন। তিনি ﷺ হিজরতের আগে মক্কায় সাওদাহকে বিয়ে করেন, যাতে অভিজ্ঞ মুমিনা ঘর সামলান। পরে তিনি মদিনায় হিজরত করেন এবং মসজিদের পাশের হুজরায় বাস করেন।

ক্লাসিক বর্ণনা তাঁর হাসি মনে রাখে। নবী ﷺ তাঁর রসিকতায় মুচকি হাসতেন; ইবন সাদ এমন গৃহচিত্র রক্ষা করেন যা কেবল গম্ভীর নয়। তিনি পরবর্তী কয়েকজন স্ত্রীর চেয়ে বয়সে বড় ছিলেন এবং ছোটদের সঙ্গে বোনের সহজতায় চলতেন। তাঁর ইসলাম দেরিতে সুবিধা ছিল না: নাজাশির দিকে যাত্রা ও শত্রু মক্কায় প্রত্যাবর্তনে তা ইতোমধ্যে পরীক্ষিত।

মদিনায় অন্য বিবাহ হলে পালা ভাগ হয়। সাওদাহর বয়স বাড়লে তিনি আশঙ্কা করেন তিনি ﷺ তালাক দিতে পারেন, অথচ তিনি কিয়ামতের দিন তাঁর স্ত্রী থাকতে চান। তাই রাসূল ﷺ-এর ভালোবাসায় তিনি তাঁর রাত আয়িশা رضي الله عنها-কে দান করেন। ৪:১২৮-এর মুফাসসিররা একে সেই উদাহরণে আনেন যেখানে স্ত্রী শান্তিতে অধিকার ছেড়ে দেন। তিনি দান গ্রহণ করেন এবং সাওদাহ উম্মুল মুমিনীনের মর্যাদায় থাকেন।

তিনি কিছু হাদিস বর্ণনা করেন এবং নবীর ওফাতের পর মদিনায় থাকেন। ওফাতের বর্ণনা ভিন্ন; প্রসিদ্ধ মত তাঁকে প্রায় ৫৪ হিজরিতে মুআবিয়ার খিলাফতে মদিনায়, বাকীতে দাফন বলে। কিছু আগের খবর আগে মৃত্যুর কথা বলে। একমত এই যে তিনি নবী ﷺ-এর বিধবা হিসেবে ইন্তেকাল করেন এবং পুনরায় বিয়ে করেননি।

সুন্নি সিরাত তাঁকে খাদিজাহ ও আয়িশার মাঝে পাদটীকা মানে না। তিনি সেই নারী যিনি শেষ মক্কী ও প্রথম মাদানী বছরে ঘরে দাঁড়িয়েছিলেন, যখন জামাত ছোট এবং খাদিজাহর শোক তাজা। রাতের দান উদারতা হিসেবে স্মরণীয়, অপমান হিসেবে নয়।

এভাবে প্রচলিত তালিকার দ্বিতীয় মাতা হাবশার মুহাজির বিধবা, দুঃখের বছরের পর মক্কায় বিবাহিত, রসবোধে স্মরণীয়, এবং নিজ পালার ওপর নববি ঘরকে প্রাধান্য দেওয়ার সম্মানে। আল্লাহ তাঁর প্রতি সন্তুষ্ট হোন।""",
    """Saudah binti Zam'ah bin Qais radhiyallahu anha berasal dari Bani Amir bin Lu'ay Quraisy. Ia masuk Islam lebih awal bersama suaminya al-Sakran bin Amr, dan termasuk yang berhijrah ke Habasyah ketika Quraisy menganiaya yang lemah. Setelah kembali ke Makkah, Sakran meninggal, dan ia tetap janda yang sudah dewasa, dikenal karena kehadiran yang luas dan lembut serta humor yang sigap.

Setelah Khadijah wafat, rumah Nabi ﷺ kosong dari teman istri. Khawlah binti Hakim mengusulkan dua nama: Aisyah yang muda, putri sahabat terdekat, dan Saudah, janda mukminah yang sudah membayar harga hijrah. Beliau ﷺ menikahi Saudah di Makkah sebelum Hijrah, agar wanita beriman yang berpengalaman menjaga rumah. Ia kemudian berhijrah ke Madinah dan tinggal di salah satu kamar di sisi masjid.

Riwayat klasik mengingat tawanya. Nabi ﷺ tersenyum pada gurauannya; Ibnu Sa'd menyimpan cuplikan rumah tangga yang tidak hanya khidmat. Ia lebih tua daripada beberapa istri kemudian dan memperlakukan yang lebih muda dengan kelegaan seorang saudari. Islamnya bukan kemudahan belakangan: sudah diuji dalam penyeberangan kepada Najasyi dan dalam kembali ke Makkah yang memusuhi.

Di Madinah, ketika pernikahan lain menyusul, giliran dibagi di antara para istri. Ketika Saudah bertambah usia, ia khawatir beliau ﷺ menceraikannya, padahal ia ingin tetap menjadi istri beliau pada Hari Kebangkitan. Ia lalu menghibahkan malamnya kepada Aisyah radhiyallahu anha karena cinta kepada Rasulullah ﷺ. Para mufasir 4:128 menyebut ini sebagai contoh istri yang melepaskan hak dengan damai. Beliau menerima hibah itu dan ia tetap dalam martabat Ummul Mukminin.

Ia meriwayatkan sejumlah hadis dan tetap di Madinah setelah wafat beliau. Riwayat tentang kewafatannya berbeda-beda; pendapat terkenal menempatkannya di Madinah sekitar 54 H, pada khilafah Muawiyah, dimakamkan di Baqi. Catatan awal lain menyebut ia wafat lebih dulu. Yang disepakati ialah ia meninggal sebagai janda Nabi ﷺ dan tidak menikah lagi.

Sirah Ahlus Sunnah tidak memperlakukannya sebagai catatan kaki antara Khadijah dan Aisyah. Ia wanita yang berdiri di rumah pada tahun-tahun Makkah terakhir dan Madinah pertama, ketika jamaah masih kecil dan duka atas Khadijah masih baru. Hibah malamnya diingat sebagai kedermawanan, bukan kehinaan.

Dengan itu ibu kedua dalam daftar lazim adalah janda hijrah Habasyah, dinikahi di Makkah setelah Tahun Kesedihan, dikenang karena humor, dan dimuliakan karena lebih memilih rumah tangga nabi daripada gilirannya sendiri. Semoga Allah meridainya.""",
)

c["items"][2]["details"] = D(
    """Aisha bint Abi Bakr al-Siddiq رضي الله عنها was the daughter of the closest friend of the Messenger ﷺ and of Umm Ruman. She grew up in a house that had already entered Islam. After Khadijah's death the nikah was contracted in Makkah; the marriage was consummated in Madinah after the Hijrah, in Shawwal according to the well-known report. She is the only wife of the Prophet ﷺ who had not been previously married.

The chamber next to the mosque became a school. She memorised the Qur'an, observed wudu and prayer at the closest range, and asked until she understood. Senior Companions later sought her fatwa. A large portion of the hadith of the household—purity, prayer, the Prophet's manners in the home, and the events of Madinah—is narrated from her. Sunni rijal count her among the most knowledgeable of the Companions, men or women.

In 6 AH, after the expedition of Banu al-Mustaliq, the incident of Ifk took place. She lagged behind the army looking for a necklace, and Safwan ibn al-Mu'attal found her and brought her on. The hypocrites spread a slander. For about a month the household was in distress until Allah revealed verses of Surah al-Nur (24:11–20) declaring her innocence and warning those who love that indecency should spread among the believers. Abu Bakr رضي الله عنه then resumed kindness to Mistah, who had been involved in the talk, after the verse on pardon.

She was human in jealousy, eloquent in speech, and fierce in defence of the truth as she saw it. The Prophet ﷺ died in her room, his head in her lap, and was buried in her house. That chamber is now within al-Masjid al-Nabawi. After his death she taught for decades in Madinah. Young Successors sat at her door. She narrated thousands of reports; the two Sahihs and the sunan are full of "Aisha said."

The years after Uthman's murder were a trial for the whole Ummah. Sunni historians record that she went out seeking reform and later expressed regret for the fighting that followed, remaining throughout a Mother of the Believers whose honour is not to be attacked. The adab of Ahl al-Sunnah is to hold a good opinion of all the Companions in that fitnah and to leave what is beyond our knowledge to Allah.

She died on the 17th of Ramadan 58 AH in Madinah, during the caliphate of Mu'awiyah, at a little over sixty years by the common count. Abu Hurayrah رضي الله عنه is reported to have led the funeral prayer in one well-known notice; she was buried at night in al-Baqi' at her own request, so that the crowd would not become a spectacle. The Ummah has called her al-Siddiqah bint al-Siddiq.

Thus the third Mother in the list is the scholar of the household, the narrator of hadith, the woman declared innocent by the Qur'an, and the last earthly nurse of the Messenger ﷺ. May Allah be pleased with her.""",
    """عائشہ بنت ابی بکر صدیق رضی اللہ عنہا رسول ﷺ کے سب سے قریبی دوست اور ام رومان کی صاحبزادی تھیں۔ اس گھر میں پلیں جو اسلام لا چکا تھا۔ خدیجہ کی وفات کے بعد نکاح مکہ میں ہوا؛ رخصتی ہجرت کے بعد مدینہ میں ہوئی، مشہور روایت کے مطابق شوال میں۔ وہ نبی ﷺ کی واحد زوجہ ہیں جو پہلے شادی شدہ نہ تھیں۔

مسجد سے ملا حجرہ مدرسہ بن گیا۔ قرآن حفظ کیا، وضو و نماز قریب سے دیکھیں، سمجھ تک پوچھتیں۔ بعد میں بڑے صحابہ ان سے فتویٰ لیتے۔ گھر کی احادیث کا بڑا حصہ—طہارت، نماز، گھر میں نبوی اطوار، اور مدنی واقعات—انہی سے مروی ہے۔ اہل سنت کا رجال انہیں صحابہ میں سب سے زیادہ علم والوں میں شمار کرتا ہے، مرد ہوں یا عورت۔

6ھ میں غزوہ بنو مصطلق کے بعد واقعہ افک پیش آیا۔ ہار ڈھونڈتے لشکر سے پیچھے رہ گئیں، صفوان بن معطل نے پایا اور سوار کر کے لائے۔ منافقوں نے تہمت پھیلائی۔ تقریباً ایک مہینہ گھر رنج میں رہا یہاں تک کہ اللہ نے سورہ نور کی آیات (24:11–20) نازل فرمائیں جو ان کی براءت بیان کرتی ہیں اور جو چاہتے ہیں کہ فحش ایمان والوں میں پھیلے انہیں ڈراتی ہیں۔ ابو بکر رضی اللہ عنہ نے پھر مسطح سے نرمی کی جو اس بات میں شامل تھا، عفو والی آیت کے بعد۔

غیرت میں انسانی تھیں، زبان میں فصیح، اور حق کی حمایت میں تیز جیسا انہیں نظر آیا۔ نبی ﷺ ان کے حجرے میں، ان کی گود میں سر رکھ کر وفات پائے، اور انہی کے گھر دفن ہوئے۔ وہ حجرہ اب مسجد نبوی کے اندر ہے۔ وفات کے بعد دہائیوں مدینہ میں پڑھایا۔ جوان تابعین دروازے پر بیٹھے۔ ہزاروں روایات بیان کیں؛ دونوں صحیحیں اور سنن «قالت عائشة» سے بھری ہیں۔

عثمان کے قتل کے بعد کے سال پوری امت کے لیے آزمائش تھے۔ اہل سنت کے مورخ لکھتے ہیں وہ اصلاح چاہتے نکلیں اور بعد میں ہونے والی لڑائی پر ندامت ظاہر کی، اور اس دوران ام المؤمنین رہیں جن کی عزت پر حملہ نہیں کیا جاتا۔ اہل سنت کا ادب اس فتنے میں تمام صحابہ کے بارے حسن ظن رکھنا اور جو ہمارے علم سے باہر ہے اللہ پر چھوڑنا ہے۔

17 رمضان 58ھ کو مدینہ میں معاویہ کی خلافت میں وفات ہوئی، معروف شمار میں ساٹھ سے کچھ اوپر۔ ایک مشہور خبر میں ابو ہریرہ رضی اللہ عنہ نے نماز جنازہ پڑھائی؛ انہوں نے رات بقیع میں دفن کی وصیت کی تاکہ ہجوم تماشا نہ بنے۔ امت انہیں الصدیقة بنت الصدیق کہتی ہے۔

یوں فہرست کی تیسری ماں گھر کی عالمہ، حدیث کی راوی، قرآن سے بری ٹھہرائی گئی خاتون، اور رسول ﷺ کی آخری دنیاوی تیماردار ہیں۔ اللہ ان سے راضی ہو۔""",
    """आयशा बिन्त अबी बक्र सिद्दीक رضي الله عنها रसूल ﷺ के सबसे क़रीबी दोस्त और उम्म रूमान की साहिबज़ादी थीं। उस घर में पलीं जो इस्लाम ला चुका था। ख़दीजा की वफ़ात के बाद निकाह मक्का में हुआ; रुख्सती हिजरत के बाद मदीना में हुई, मशहूर रिवायत के मुताबिक शव्वाल में। वे नबी ﷺ की इकलौती ज़ौजा हैं जो पहले शादीशुदा न थीं।

मस्जिद से जुड़ा हुजरा मदरसा बन गया। कुरआन हिफ़्ज़ किया, वुज़ू व नमाज़ क़रीब से देखीं, समझ तक पूछा। बाद में बड़े सहाबा उनसे फ़तवा लेते। घर की हदीसों का बड़ा हिस्सा—तहारत, नमाज़, घर में नबवी अतवार, और मदनी वाक़ियात—उन्हीं से मरवी है। अहले सुन्नत का रिजाल उन्हें सहाबा में सबसे अधिक इल्म वालों में शुमार करता है, मर्द हों या औरत।

6 हिजरी में ग़ज़वा बनू मुस्तलिक़ के बाद वाक़िआ-ए-इफ़्क पेश आया। हार ढूँढते लश्कर से पीछे रह गईं, सफ़वान इब्न मुअत्तल ने पाया और सवार कर लाए। मुनाफ़िक़ों ने तोहमत फैलाई। लगभग एक महीना घर रंज में रहा यहाँ तक कि अल्लाह ने सूरह नूर की आयतें (24:11–20) नाज़िल फ़रमाईं जो उनकी बराअत बयान करती हैं और जो चाहते हैं कि फ़हश ईमान वालों में फैले उन्हें डराती हैं। अबू बक्र رضي الله عنه ने फिर मिस्तह से नरमी की जो उस बात में शामिल था, अफ़्व वाली आयत के बाद।

ग़ैरत में इंसानी थीं, ज़बान में फ़सीह, और हक़ की हिमायत में तेज़ जैसा उन्हें नज़र आया। नबी ﷺ उनके हुजरे में, उनकी गोद में सर रखकर वफ़ात पाए, और उन्हीं के घर दफ़न हुए। वह हुजरा अब मस्जिद-ए-नबवी के अंदर है। वफ़ात के बाद दशकों मदीना में पढ़ाया। जवान ताबिईन दरवाज़े पर बैठे। हज़ारों रिवायात बयान कीं; दोनों सहीहें और सुनन «क़ालत आयशा» से भरी हैं।

उस्मान के क़त्ल के बाद के साल पूरी उम्मत के लिए आज़माइश थे। अहले सुन्नत के मुअर्रिख लिखते हैं वे इस्लाह चाहते निकलीं और बाद में होने वाली लड़ाई पर नदामत ज़ाहिर की, और उस दौरान उम्मुल मुमिनीन रहीं जिनकी इज़्ज़त पर हमला नहीं किया जाता। अहले सुन्नत का अदब उस फ़ितने में तमाम सहाबा के बारे हुस्न-ए-ज़न्न रखना और जो हमारे इल्म से बाहर है अल्लाह पर छोड़ना है।

17 रमज़ान 58 हिजरी को मदीना में मुआविया की ख़िलाफ़त में वफ़ात हुई, मा'रूफ़ शुमार में साठ से कुछ ऊपर। एक मशहूर ख़बर में अबू हुरैरा رضي الله عنه ने नमाज़-ए-जनाज़ा पढ़ाई; उन्होंने रात बक़ी' में दफ़न की वसीयत की ताकि हुजूम तमाशा न बने। उम्मत उन्हें अस-सिद्दीक़ा बिन्त अस-सिद्दीक़ कहती है।

यूँ फ़ेहरिस्त की तीसरी माँ घर की आलिमा, हदीस की राविया, कुरआन से बरी ठहराई गई ख़ातून, और रसूल ﷺ की आख़िरी दुनियावी टीमारदार हैं। अल्लाह उनसे राज़ी हो।""",
    """আয়িশাহ বিনত আবি বকর আস-সিদ্দিক رضي الله عنها রাসূল ﷺ-এর ঘনিষ্ঠতম বন্ধু ও উম্মু রুমানের কন্যা ছিলেন। তিনি এমন ঘরে বেড়ে ওঠেন যা ইতোমধ্যে ইসলাম গ্রহণ করেছে। খাদিজাহর ওফাতের পর আকদ মক্কায় হয়; বিবাহ হিজরতের পর মদিনায় সম্পন্ন হয়, প্রসিদ্ধ বর্ণনায় শাওয়ালে। তিনি নবী ﷺ-এর একমাত্র স্ত্রী যিনি পূর্বে বিবাহিত ছিলেন না।

মসজিদের পাশের হুজরা মাদরাসা হয়ে যায়। তিনি কুরআন মুখস্থ করেন, ওযু ও সালাত নিকট থেকে দেখেন, বুঝে না নেওয়া পর্যন্ত জিজ্ঞাসা করেন। পরে প্রবীণ সাহাবিরা তাঁর ফতোয়া চান। গৃহের হাদিসের বড় অংশ—পবিত্রতা, সালাত, ঘরে নববি আদব, এবং মদিনার ঘটনাবলি—তাঁর থেকে বর্ণিত। সুন্নি রিজাল তাঁকে সাহাবিদের মধ্যে সর্বাধিক জ্ঞানীদের অন্তর্ভুক্ত করে, পুরুষ বা নারী যাই হোন।

৬ হিজরিতে বনু মুস্তালিক অভিযানের পর ইফকের ঘটনা ঘটে। হার খুঁজতে সেনাবাহিনী থেকে পিছিয়ে পড়েন, সাফওয়ান ইবন আল-মুআত্তাল তাঁকে পেয়ে আনেন। মুনাফিকরা অপবাদ ছড়ায়। প্রায় এক মাস ঘর কষ্টে থাকে, যতক্ষণ না আল্লাহ সূরা আন-নূরের আয়াত (২৪:১১–২০) নাজিল করেন যা তাঁর নির্দোষতা ঘোষণা করে এবং যারা চায় অশ্লীলতা মুমিনদের মধ্যে ছড়াক তাদের সতর্ক করে। আবু বকর رضي الله عنه তখন মিসতাহের প্রতি পুনরায় সদয় হন, যিনি সেই আলোচনায় জড়িত ছিলেন, ক্ষমার আয়াতের পর।

তিনি ঈর্ষায় মানুষ ছিলেন, বাক্যে সাবলীল, এবং যে সত্য তিনি দেখতেন তার পক্ষে তীব্র। নবী ﷺ তাঁর হুজরায়, তাঁর কোলে মাথা রেখে ওফাত পান, এবং তাঁর ঘরেই দাফন হন। সেই হুজরা এখন মসজিদে নববীর অন্তর্গত। ওফাতের পর তিনি দশকের পর দশক মদিনায় শিক্ষা দেন। তরুণ তাবেয়িরা দরজায় বসতেন। তিনি হাজার হাজার বর্ণনা করেন; দুই সহীহ ও সুনান ‘আয়িশা বলেছেন’ এ ভরা।

উসমানের শাহাদাতের পরের বছরগুলো পুরো উম্মাহর জন্য পরীক্ষা ছিল। সুন্নি ঐতিহাসিকরা লেখেন তিনি সংস্কার চেয়ে বেরিয়েছিলেন এবং পরবর্তী লড়াইয়ে অনুশোচনা প্রকাশ করেন, সর্বদা উম্মুল মুমিনীন থেকে যার সম্মান আক্রমণের বিষয় নয়। আহলুস সুন্নাহর আদব সেই ফিতনায় সব সাহাবির প্রতি সদ্বিচার রাখা এবং যা আমাদের জ্ঞানের বাইরে তা আল্লাহর ওপর ছেড়ে দেওয়া।

১৭ রমজান ৫৮ হিজরিতে মদিনায় মুআবিয়ার খিলাফতে তিনি ইন্তেকাল করেন, প্রচলিত গণনায় সাটোর কিছু ওপর। একটি প্রসিদ্ধ বর্ণনায় আবু হুরায়রা رضي الله عنه জানাজার ইমামতি করেন; তিনি রাতে বাকীতে দাফনের অসিয়ত করেন যাতে ভিড় দৃশ্য না হয়। উম্মাহ তাঁকে আস-সিদ্দীকাহ বিনত আস-সিদ্দীক বলে।

এভাবে তালিকার তৃতীয় মাতা ঘরের আলিমা, হাদিসের বর্ণনাকারী, কুরআন কর্তৃক নির্দোষ ঘোষিত নারী, এবং রাসূল ﷺ-এর শেষ পার্থিব সেবিকা। আল্লাহ তাঁর প্রতি সন্তুষ্ট হোন।""",
    """Aisyah binti Abu Bakar ash-Shiddiq radhiyallahu anha adalah putri sahabat terdekat Rasulullah ﷺ dan Ummu Ruman. Ia tumbuh di rumah yang sudah masuk Islam. Setelah Khadijah wafat, akad dilangsungkan di Makkah; pernikahan disempurnakan di Madinah setelah Hijrah, pada Syawal menurut riwayat terkenal. Ia satu-satunya istri Nabi ﷺ yang belum pernah menikah sebelumnya.

Kamar di sisi masjid menjadi sekolah. Ia menghafal Al-Qur'an, menyaksikan wudu dan salat dari jarak terdekat, dan bertanya hingga paham. Para sahabat senior kemudian meminta fatwanya. Sebagian besar hadis rumah tangga—kesucian, salat, adab nabi di rumah, dan peristiwa Madinah—diriwayatkan darinya. Ilmu rijal Ahlus Sunnah menilainya di antara sahabat yang paling berilmu, laki-laki atau perempuan.

Pada 6 H, setelah ekspedisi Bani Mustaliq, terjadi peristiwa Ifk. Ia tertinggal dari pasukan mencari kalung, dan Safwan bin al-Mu'attal menemukannya lalu membawanya. Orang munafik menebar fitnah. Sekitar satu bulan rumah tangga dalam duka hingga Allah menurunkan ayat Surah an-Nur (24:11–20) yang menyatakan kesuciannya dan memperingatkan orang yang suka kekejian tersebar di kalangan mukmin. Abu Bakar radhiyallahu anhu kemudian kembali berlemah lembut kepada Mistah, yang terlibat dalam omongan itu, setelah ayat tentang maaf.

Ia manusiawi dalam cemburu, fasih dalam bicara, dan tegas membela kebenaran sebagaimana ia melihatnya. Nabi ﷺ wafat di kamarnya, kepala di pangkuannya, dan dimakamkan di rumahnya. Kamar itu kini berada dalam Masjid Nabawi. Setelah beliau wafat ia mengajar berpuluh tahun di Madinah. Tabiin muda duduk di pintunya. Ia meriwayatkan ribuan laporan; dua sahih dan kitab sunan penuh dengan "Aisyah berkata."

Tahun-tahun setelah terbunuhnya Utsman adalah ujian bagi seluruh umat. Sejarawan Ahlus Sunnah mencatat ia keluar menuntut islah dan kemudian menyesali pertempuran yang menyusul, tetap sepanjang itu Ummul Mukminin yang kehormatannya tidak boleh diserang. Adab Ahlus Sunnah ialah berbaik sangka kepada semua sahabat dalam fitnah itu dan menyerahkan yang di luar ilmu kita kepada Allah.

Ia wafat pada 17 Ramadan 58 H di Madinah, pada khilafah Muawiyah, sedikit di atas enam puluh tahun menurut hitungan umum. Abu Hurairah radhiyallahu anhu dilaporkan mensalatkan jenazahnya dalam satu catatan terkenal; ia dimakamkan malam hari di Baqi atas wasiatnya agar kerumunan tidak menjadi tontonan. Umat memanggilnya ash-Shiddiqah binti ash-Shiddiq.

Dengan itu ibu ketiga dalam daftar adalah ulama rumah tangga, perawi hadis, wanita yang dinyatakan suci oleh Al-Qur'an, dan perawat duniawi terakhir Rasulullah ﷺ. Semoga Allah meridainya.""",
)

c["items"][3]["details"] = D(
    """Hafsah bint Umar ibn al-Khattab رضي الله عنها was the daughter of the second caliph and of Zaynab bint Maz'un. She accepted Islam with her father in Makkah and was among the early believing women. She married Khunays ibn Hudhafah al-Sahmi, who migrated to Abyssinia and then to Madinah. Khunays died in Madinah after Badr—of wounds or of illness, as the reports differ—and Hafsah was left a young widow.

Umar رضي الله عنه, concerned for her, offered her in marriage to Uthman and then to Abu Bakr; both declined. The Prophet ﷺ then married her, around 3 AH, joining the household of Umar to his own as Aisha had joined the household of Abu Bakr. The two fathers-in-law stood at the centre of the community, and the two daughters lived as sister-wives beside the mosque.

Her character was strong, like her father's: fasting, night prayer, and a frank tongue. A report in the sunan states that the Prophet ﷺ divorced her once, then took her back after Jibril said she fasted and prayed much and would be his wife in Paradise. Ahl al-Sunnah relate this as an honour, not as a stain. She remained Mother of the Believers until her death.

When Abu Bakr رضي الله عنه compiled the sheets of the Qur'an after Yamamah, they passed to Umar, and after Umar they were kept with Hafsah. In the caliphate of Uthman, those suhuf were borrowed as the basis of the official mushaf copied for the cities, then returned to her. After she died, the governor Marwan took the copy so that no variant collection would remain beside the Uthmanic standard. Her name is thus bound to the written preservation of the Book.

She narrated hadith from the Prophet ﷺ and from her father. The chamber of Hafsah was one of the houses whose doors opened toward the mosque. After the wafat she stayed in Madinah, honouring the rule that the Mothers do not remarry, and she saw the first decades of the caliphate from that blessed neighbourhood.

She died in Sha'ban 45 AH according to a well-known report, in Madinah, and was buried in al-Baqi'. Other dates are mentioned in the tabaqat; the difference does not touch her rank. Umar's daughter remained, in the memory of the Ummah, a keeper of pages and a woman of worship.

Thus the fourth Mother is the widow of Khunays, the daughter of Umar, the neighbour of Aisha, and the trustee of the compiled mushaf. May Allah be pleased with her.""",
    """حفصہ بنت عمر بن خطاب رضی اللہ عنہا دوسرے خلیفہ اور زینب بنت مظعون کی صاحبزادی تھیں۔ والد کے ساتھ مکہ میں اسلام لائیں اور اولین مؤمنات میں سے تھیں۔ خنیس بن حذافہ سهمی سے نکاح ہوا جو حبشہ پھر مدینہ ہجرت کر گئے۔ خنیس بدر کے بعد مدینہ میں فوت ہوئے—زخموں یا بیماری سے، روایات میں فرق ہے—اور حفصہ جوان بیوہ رہ گئیں۔

عمر رضی اللہ عنہ نے فکر سے عثمان پھر ابو بکر کو نکاح کی پیشکش کی؛ دونوں نے معذرت کی۔ پھر نبی ﷺ نے تقریباً 3ھ میں نکاح فرمایا، عمر کے گھر کو اپنے گھر سے جوڑ دیا جیسا عائشہ نے ابو بکر کے گھر کو جوڑا تھا۔ دونوں خسروں کا مقام جماعت کے مرکز میں تھا، اور دونوں بیٹیاں مسجد کے پاس سوکن بہنوں کی طرح رہیں۔

ان کا مزاج والد جیسا مضبوط تھا: روزہ، تہجد، اور صاف زبان۔ سنن کی روایت ہے کہ نبی ﷺ نے ایک بار طلاق دی پھر جبریل کے کہنے پر رجوع کیا کہ وہ بہت روزہ رکھتی اور نماز پڑھتی ہیں اور جنت میں آپ کی زوجہ ہوں گی۔ اہل سنت اسے عزت سمجھتے ہیں، داغ نہیں۔ وہ وفات تک ام المؤمنین رہیں۔

یمامہ کے بعد جب ابو بکر رضی اللہ عنہ نے قرآن کے اوراق جمع کیے تو وہ عمر کے پاس گئے، اور عمر کے بعد حفصہ کے پاس رہے۔ عثمان کی خلافت میں ان صحیفوں کو شہروں کے لیے سرکاری مصحف کی بنیاد بنایا گیا، پھر انہیں واپس کیے گئے۔ وفات کے بعد گورنر مروان نے وہ نسخہ لے لیا تاکہ عثمانی معیار کے ساتھ کوئی الگ مجموعہ نہ رہے۔ یوں ان کا نام کتاب کی تحریری حفاظت سے جڑا۔

نبی ﷺ اور والد سے احادیث روایت کیں۔ حفصہ کا حجرہ ان گھروں میں تھا جن کے دروازے مسجد کی طرف کھلتے تھے۔ وفات نبوی کے بعد مدینہ میں رہیں، اس حکم کی پابند کہ امهات دوبارہ نکاح نہ کریں، اور اسی مبارک پڑوس سے خلافت کی پہلی دہائیاں دیکھیں۔

مشہور روایت کے مطابق شعبان 45ھ میں مدینہ میں وفات ہوئی، بقیع میں دفن ہوئیں۔ طبقات میں اور تاریخیں بھی ہیں؛ اختلاف ان کے مرتبے کو نہیں چھوتا۔ امت کی یاد میں عمر کی بیٹی اوراق کی امانت دار اور عبادت والی رہیں۔

یوں چوتھی ماں خنیس کی بیوہ، عمر کی صاحبزادی، عائشہ کی پڑوسن، اور جمع شدہ مصحف کی امین ہیں۔ اللہ ان سے راضی ہو۔""",
    """हफ़्सा बिन्त उमर इब्न अल-ख़त्ताब رضي الله عنها दूसरे ख़लीफ़ा और ज़ैनब बिन्त मज़ऊन की साहिबज़ादी थीं। वालिद के साथ मक्का में इस्लाम लाईं और अव्वलीन मोमिनात में थीं। ख़ुनैस इब्न हुज़ाफ़ा सहमी से निकाह हुआ जो हबशा फिर मदीना हिजरत कर गए। ख़ुनैस बद्र के बाद मदीना में फ़ौत हुए—ज़ख़्मों या बीमारी से, रिवायात में फ़र्क है—और हफ़्सा जवान विधवा रह गईं।

उमर رضي الله عنه ने फ़िक्र से उस्मान फिर अबू बक्र को निकाह की पेशकश की; दोनों ने माज़रत की। फिर नबी ﷺ ने लगभग 3 हिजरी में निकाह फ़रमाया, उमर के घर को अपने घर से जोड़ दिया जैसा आयशा ने अबू बक्र के घर को जोड़ा था। दोनों ख़ुसरों का मक़ाम जमाअत के मर्कज़ में था, और दोनों बेटियाँ मस्जिद के पास सौतन बहनों की तरह रहीं।

उनका मिज़ाज वालिद जैसा मज़बूत था: रोज़ा, तहज्जुद, और साफ़ ज़बान। सुनन की रिवायत है कि नबी ﷺ ने एक बार तलाक़ दी फिर जिब्रील के कहने पर रुजू किया कि वे बहुत रोज़ा रखती और नमाज़ पढ़ती हैं और जन्नत में आपकी ज़ौजा होंगी। अहले सुन्नत इसे इज़्ज़त समझते हैं, दाग़ नहीं। वे वफ़ात तक उम्मुल मुमिनीन रहीं।

यमामा के बाद जब अबू बक्र رضي الله عنه ने कुरआन के औराक़ जमा किए तो वे उमर के पास गए, और उमर के बाद हफ़्सा के पास रहे। उस्मान की ख़िलाफ़त में उन सहीफ़ों को शहरों के लिए सरकारी मुसहफ़ की बुनियाद बनाया गया, फिर उन्हें वापस किए गए। वफ़ात के बाद गवर्नर मरवान ने वह नुस्ख़ा ले लिया ताकि उस्मानी मेयार के साथ कोई अलग मज्मुआ न रहे। यूँ उनका नाम किताब की तहरीरि हिफ़ाज़त से जुड़ा।

नबी ﷺ और वालिद से हदीसें रिवायत कीं। हफ़्सा का हुजरा उन घरों में था जिनके दरवाज़े मस्जिद की तरफ़ खुलते थे। विसाल-ए-नबवी के बाद मदीना में रहीं, इस हुक्म की पाबंद कि उम्महात दोबारा निकाह न करें, और उसी मुबारक पड़ोस से ख़िलाफ़त के पहले दशक देखीं।

मशहूर रिवायत के मुताबिक शबान 45 हिजरी में मदीना में वफ़ात हुई, बक़ी' में दफ़न हुईं। तबाक़ात में और तारीख़ें भी हैं; इख़्तिलाफ़ उनके मर्तबे को नहीं छूता। उम्मत की याद में उमर की बेटी औराक़ की अमानतदार और इबादत वाली रहीं।

यूँ चौथी माँ ख़ुनैस की विधवा, उमर की साहिबज़ादी, आयशा की पड़ोसन, और जमाशुदा मुसहफ़ की अमीन हैं। अल्लाह उनसे राज़ी हो।""",
    """হাফসাহ বিনত উমর ইবনুল খাত্তাব رضي الله عنها দ্বিতীয় খলিফা ও যাইনাব বিনত মাযউনের কন্যা ছিলেন। তিনি পিতার সঙ্গে মক্কায় ইসলাম গ্রহণ করেন এবং প্রথম যুগের মুমিনাদের অন্তর্ভুক্ত। তিনি খুনাইস ইবন হুযাফাহ আস-সাহমিকে বিয়ে করেন, যিনি হাবশা ও পরে মদিনায় হিজরত করেন। খুনাইস বদরের পর মদিনায় মারা যান—ক্ষত বা রোগে, বর্ণনা ভিন্ন—এবং হাফসাহ তরুণ বিধবা থাকেন।

উমর رضي الله عنه তাঁর চিন্তায় উসমান ও পরে আবু বকরকে বিবাহের প্রস্তাব দেন; উভয়ে ওজর করেন। তারপর নবী ﷺ প্রায় ৩ হিজরিতে তাঁকে বিয়ে করেন, উমরের ঘরকে নিজ ঘরের সঙ্গে যুক্ত করেন যেমন আয়িশা আবু বকরের ঘরকে যুক্ত করেছিলেন। দুই শ্বশুর জামাতের কেন্দ্রে ছিলেন, আর দুই কন্যা মসজিদের পাশে ভগিনী-সতীন হিসেবে বাস করেন।

তাঁর চরিত্র পিতার মতো দৃঢ় ছিল: সিয়াম, রাতের সালাত, এবং স্পষ্ট ভাষা। সুনানের একটি বর্ণনায় নবী ﷺ একবার তালাক দেন, পরে জিবরীলের কথায় ফিরিয়ে নেন যে তিনি অধিক রোজা ও সালাত করেন এবং জান্নাতে তাঁর স্ত্রী হবেন। আহলুস সুন্নাহ একে সম্মান মানে, কলঙ্ক নয়। তিনি ওফাত পর্যন্ত উম্মুল মুমিনীন থাকেন।

ইয়ামামার পর আবু বকর رضي الله عنه কুরআনের পত্রাবলি সংকলন করলে সেগুলো উমরের কাছে যায়, উমরের পর হাফসাহর কাছে থাকে। উসমানের খিলাফতে সেই সুহুফ শহরগুলোর জন্য সরকারি মুশাফের ভিত্তি হিসেবে ধার নেওয়া হয়, পরে তাঁকে ফিরিয়ে দেওয়া হয়। তাঁর ওফাতের পর গভর্নর মারওয়ান সেই নুসখা নেন যাতে উসমানি মানের পাশে অন্য সংকলন না থাকে। এভাবে তাঁর নাম কিতাবের লিখিত সংরক্ষণের সঙ্গে জড়িত।

তিনি নবী ﷺ ও পিতার থেকে হাদিস বর্ণনা করেন। হাফসাহর হুজরা সেই ঘরগুলোর একটি যাঁর দরজা মসজিদের দিকে খুলত। নবীর ওফাতের পর তিনি মদিনায় থাকেন, এই বিধান মান্য করে যে উম্মাহাত পুনরায় বিয়ে করেন না, এবং সেই বরকতময় পাড়া থেকে খিলাফতের প্রথম দশক দেখেন।

প্রসিদ্ধ বর্ণনায় শাবান ৪৫ হিজরিতে মদিনায় ইন্তেকাল করেন, বাকীতে দাফন হন। তবাকাতে অন্য তারিখও আছে; মতভেদ তাঁর মর্যাদা ছুঁয় না। উম্মাহর স্মৃতিতে উমরের কন্যা পাতার আমানতদার ও ইবাদতকারী নারী।

এভাবে চতুর্থ মাতা খুনাইসের বিধবা, উমরের কন্যা, আয়িশার প্রতিবেশী, এবং সংকলিত মুশাফের আমানতদার। আল্লাহ তাঁর প্রতি সন্তুষ্ট হোন।""",
    """Hafshah binti Umar bin al-Khaththab radhiyallahu anha adalah putri khalifah kedua dan Zainab binti Maz'un. Ia masuk Islam bersama ayahnya di Makkah dan termasuk wanita mukminah paling awal. Ia menikah dengan Khunais bin Hudzafah as-Sahmi, yang berhijrah ke Habasyah lalu ke Madinah. Khunais meninggal di Madinah setelah Badar—karena luka atau sakit, riwayat berbeda—dan Hafshah ditinggal janda muda.

Umar radhiyallahu anhu, prihatin kepadanya, menawarkannya kepada Utsman lalu kepada Abu Bakar; keduanya menolak. Nabi ﷺ kemudian menikahinya sekitar 3 H, menggabungkan rumah Umar kepada rumahnya sebagaimana Aisyah telah menggabungkan rumah Abu Bakar. Kedua mertua berdiri di pusat jamaah, dan kedua putri hidup sebagai saudara-istri di sisi masjid.

Wataknya kuat seperti ayahnya: puasa, salat malam, dan lidah yang terang. Riwayat dalam sunan menyatakan Nabi ﷺ sekali menceraikannya, lalu merujukinya setelah Jibril berkata ia banyak puasa dan salat dan akan menjadi istrinya di surga. Ahlus Sunnah menuturkan ini sebagai kehormatan, bukan noda. Ia tetap Ummul Mukminin hingga wafat.

Ketika Abu Bakar radhiyallahu anhu menghimpun lembaran Al-Qur'an setelah Yamamah, lembaran itu beralih kepada Umar, dan setelah Umar disimpan pada Hafshah. Pada khilafah Utsman, suhuf itu dipinjam sebagai dasar mushaf resmi yang disalin untuk kota-kota, lalu dikembalikan kepadanya. Setelah ia wafat, gubernur Marwan mengambil naskah itu agar tidak ada kumpulan lain di samping standar Utsmani. Namanya dengan itu terikat pada pemeliharaan tertulis Kitab.

Ia meriwayatkan hadis dari Nabi ﷺ dan dari ayahnya. Kamar Hafshah adalah salah satu rumah yang pintunya menghadap masjid. Setelah wafat beliau ia tinggal di Madinah, menaati ketentuan bahwa para ibu tidak menikah lagi, dan ia menyaksikan dasawarsa pertama khilafah dari tetangga yang diberkahi itu.

Ia wafat pada Sya'ban 45 H menurut riwayat terkenal, di Madinah, dan dimakamkan di Baqi. Tanggal lain disebut dalam thabaqat; perbedaan itu tidak menyentuh martabatnya. Putri Umar tetap, dalam ingatan umat, penjaga lembaran dan wanita ibadah.

Dengan itu ibu keempat adalah janda Khunais, putri Umar, tetangga Aisyah, dan pemegang amanah mushaf yang terhimpun. Semoga Allah meridainya.""",
)

c["items"][4]["details"] = D(
    """Zaynab bint Khuzaymah رضي الله عنها was of Banu Hilal ibn Amir. She was already known, even before Islam, as Umm al-Masakin, Mother of the Poor, because she fed the hungry and gave without counting. She entered Islam, migrated, and was widowed. Among the names given for a previous husband is Ubaydah ibn al-Harith, the cousin of the Prophet ﷺ who was martyred at Badr; the tabaqat also mention other reports. What is agreed is that she was a believing widow of generosity when the Messenger ﷺ married her in Madinah, about 3 AH.

The marriage was brief. After only a few months—two or three in some notices, eight in others—she died in Madinah, around 4 AH. She is the only wife besides Khadijah رضي الله عنها who died during the lifetime of the Prophet ﷺ. He buried her, and the Ummah learned her kunya more than a long chronicle of her days, because her days in the household were few.

That short span is itself a seerah lesson. Not every Mother is remembered for decades of hadith. Some are remembered for a quality that already had a name in the Jahiliyyah and then shone in Islam: care for the poor. Ibn Sa'd records her title with honour. The Prophet ﷺ did not marry her for tribe or treaty alone; her house was known for bread given away.

She had no surviving narrative corpus like Aisha or Umm Salamah. Students of seerah therefore speak of her with the caution of limited reports, without inventing speeches or miracles. The fact of her death in his lifetime is enough to mark her among the wives who preceded him to the grave, as Khadijah had in Makkah.

She was buried in al-Baqi'. After her, the household in Madinah continued with Sawdah, Aisha, Hafsah, and then Umm Salamah and the later Mothers. Her empty place reminded the community that even the houses beside the mosque taste death.

Umm al-Masakin remains in the list of the Mothers of the Believers. The Qur'anic honour of 33:6 covers the short marriage as it covers the long ones. The Ummah asks Allah to be pleased with her and does not measure her rank by the number of years in the chamber.

Thus the fifth Mother is the Hilali widow called Mother of the Poor, married in Madinah, deceased after a few months, the only wife besides Khadijah to die while he ﷺ still lived. May Allah be pleased with her.""",
    """زینب بنت خزیمہ رضی اللہ عنہا بنو ہلال بن عامر سے تھیں۔ اسلام سے پہلے بھی ام المساکین کہلاتی تھیں، غریبوں کی ماں، کیونکہ بھوکوں کو کھلاتی اور گنے بغیر دیتیں۔ اسلام لائیں، ہجرت کیں، بیوہ ہوئیں۔ پچھلے شوہر کے ناموں میں عبیدہ بن حارث ہیں، نبی ﷺ کے چچا زاد جو بدر میں شہید ہوئے؛ طبقات میں اور روایات بھی ہیں۔ متفق علیہ یہ ہے کہ مدینہ میں تقریباً 3ھ میں جب رسول ﷺ نے نکاح کیا تو وہ سخاوت والی مؤمنہ بیوہ تھیں۔

نکاح مختصر تھا۔ صرف چند ماہ بعد—کچھ خبروں میں دو تین، کچھ میں آٹھ—تقریباً 4ھ میں مدینہ میں وفات پا گئیں۔ خدیجہ رضی اللہ عنہا کے علاوہ وہ واحد زوجہ ہیں جو نبی ﷺ کی حیات میں فوت ہوئیں۔ آپ نے دفن فرمایا، اور امت نے ان کے دنوں کی لمبی داستان سے زیادہ کنیت یاد رکھی، کیونکہ گھر میں دن کم تھے۔

یہ مختصر مدت خود سیرت کا سبق ہے۔ ہر ماں دہائیوں حدیث کے لیے یاد نہیں ہوتیں۔ کچھ اس وصف سے یاد ہیں جس کا نام جاہلیت میں تھا پھر اسلام میں چمکا: فقیروں کی خبرگیری۔ ابن سعد ان کی کنیت عزت سے لکھتے ہیں۔ نبی ﷺ نے صرف قبیلے یا معاہدے کے لیے نکاح نہ کیا؛ ان کا گھر دیے گئے روٹی سے پہچانا جاتا تھا۔

عائشہ یا ام سلمہ جیسا روایتی ذخیرہ ان سے نہیں۔ طالب سیرت اس لیے محدود روایات کی احتیاط سے بات کرتے ہیں، تقریریں یا معجزے گھڑتے نہیں۔ حیات نبوی میں وفات کا واقعہ کافی ہے انہیں ان ازواج میں رکھنے کے لیے جو آپ سے پہلے قبر میں گئیں، جیسا مکہ میں خدیجہ گئیں تھیں۔

بقیع میں دفن ہوئیں۔ ان کے بعد مدنی گھر سودہ، عائشہ، حفصہ، پھر ام سلمہ اور بعد کی امهات کے ساتھ چلا۔ ان کی خالی جگہ نے جماعت کو یاد دلایا کہ مسجد سے ملے گھر بھی موت چکھتے ہیں۔

ام المساکین امہات المؤمنین کی فہرست میں رہیں۔ 33:6 کی قرآنی عزت مختصر نکاح کو بھی ویسے ڈھانپتی ہے جیسے لمبے نکاح کو۔ امت اللہ سے رضامندی مانگتی ہے اور حجرے کے سال گن کر مرتبہ نہیں ناپتی۔

یوں پانچویں ماں ہلالی بیوہ ہیں جنہیں غریبوں کی ماں کہا گیا، مدینہ میں نکاح، چند ماہ بعد وفات، خدیجہ کے سوا واحد زوجہ جو آپ ﷺ کی زندگی میں فوت ہوئیں۔ اللہ ان سے راضی ہو۔""",
    """ज़ैनब बिन्त ख़ुज़ैमा رضي الله عنها बनू हिलाल इब्न आमिर से थीं। इस्लाम से पहले भी उम्म उल-मसाकीन कहलाती थीं, ग़रीबों की माँ, क्योंकि भूखों को खिलाती और गिने बिना देतीं। इस्लाम लाईं, हिजरत कीं, विधवा हुईं। पिछले शौहर के नामों में उबैदा इब्न अल-हारिस हैं, नबी ﷺ के चचेरे जो बद्र में शहीद हुए; तबाक़ात में और रिवायात भी हैं। मुत्तफ़िक़ यह है कि मदीना में लगभग 3 हिजरी में जब रसूल ﷺ ने निकाह किया तो वे सख़ावत वाली मोमिना विधवा थीं।

निकाह मुख़्तसर था। केवल चंद महीने बाद—कुछ ख़बरों में दो-तीन, कुछ में आठ—लगभग 4 हिजरी में मदीना में वफ़ात पा गईं। ख़दीजा رضي الله عنها के अलावा वे इकलौती ज़ौजा हैं जो नबी ﷺ की हयात में फ़ौत हुईं। आपने दफ़न फ़रमाया, और उम्मत ने उनके दिनों की लंबी दास्तान से ज़्यादा कुन्यत याद रखी, क्योंकि घर में दिन कम थे।

यह मुख़्तसर मुद्दत ख़ुद सीरत का सबक़ है। हर माँ दशकों हदीस के लिए याद नहीं होतीं। कुछ उस वस्फ़ से याद हैं जिसका नाम जाहिलिय्यत में था फिर इस्लाम में चमका: फ़कीरों की ख़बरगीरी। इब्न साद उनकी कुन्यत इज़्ज़त से लिखते हैं। नबी ﷺ ने केवल क़बीले या मुआहदे के लिए निकाह न किया; उनका घर दी गई रोटी से पहचाना जाता था।

आयशा या उम्म सलमा जैसा रिवायती ज़ख़ीरा उनसे नहीं। तालिब-ए-सीरत इसलिए महदूद रिवायात की एहतियात से बात करते हैं, तकरीरें या मोजिज़े नहीं गढ़ते। हयात-ए-नबवी में वफ़ात का वाक़िआ काफ़ी है उन्हें उन अज़वाज में रखने के लिए जो आपसे पहले क़ब्र में गईं, जैसा मक्का में ख़दीजा गई थीं।

बक़ी' में दफ़न हुईं। उनके बाद मदनी घर सौदा, आयशा, हफ़्सा, फिर उम्म सलमा और बाद की उम्महात के साथ चला। उनकी ख़ाली जगह ने जमाअत को याद दिलाया कि मस्जिद से जुड़े घर भी मौत चखते हैं।

उम्म उल-मसाकीन उम्महातुल मुमिनीन की फ़ेहरिस्त में रहीं। 33:6 की कुरआनी इज़्ज़त मुख़्तसर निकाह को भी वैसे ढाँपती है जैसे लंबे निकाह को। उम्मत अल्लाह से रज़ामंदी माँगती है और हुजरे के साल गिनकर मर्तबा नहीं नापती।

यूँ पाँचवीं माँ हिलाली विधवा हैं जिन्हें ग़रीबों की माँ कहा गया, मदीना में निकाह, चंद महीने बाद वफ़ात, ख़दीजा के सिवा इकलौती ज़ौजा जो आप ﷺ की ज़िंदगी में फ़ौत हुईं। अल्लाह उनसे राज़ी हो।""",
    """যাইনাব বিনত খুযাইমাহ رضي الله عنها বনু হিলাল ইবন আমির থেকে ছিলেন। ইসলামের আগেও তিনি উম্মুল মাসাকীন, দরিদ্রদের মাতা নামে পরিচিত ছিলেন, কারণ তিনি ক্ষুধার্তদের খাওয়াতেন এবং গণনা ছাড়াই দিতেন। তিনি ইসলাম গ্রহণ করেন, হিজরত করেন এবং বিধবা হন। পূর্ব স্বামীর নামের মধ্যে উবাইদাহ ইবন আল-হারিস আছেন, নবী ﷺ-এর চাচাতো ভাই যিনি বদরে শহীদ হন; তবাকাতে অন্য বর্ণনাও আছে। একমত এই যে মদিনায় প্রায় ৩ হিজরিতে রাসূল ﷺ যখন বিয়ে করেন তিনি দানশীল মুমিনা বিধবা ছিলেন।

বিবাহ সংক্ষিপ্ত ছিল। মাত্র কয়েক মাস পর—কিছু খবরে দুই-তিন, কিছুতে আট—প্রায় ৪ হিজরিতে মদিনায় তিনি ইন্তেকাল করেন। খাদিজাহ رضي الله عنها ছাড়া তিনিই একমাত্র স্ত্রী যিনি নবী ﷺ-এর জীবদ্দশায় মারা যান। তিনি তাঁকে দাফন করেন, এবং উম্মাহ তাঁর দিনের দীর্ঘ কাহিনি অপেক্ষা কুনিয়া বেশি মনে রাখে, কারণ ঘরে তাঁর দিন কম ছিল।

এই সংক্ষিপ্ত সময় নিজেই সিরাতের শিক্ষা। প্রতি মাতা দশকের হাদিসের জন্য স্মরণীয় নন। কেউ এমন গুণে স্মরণীয় যা জাহিলিয়াতে নাম পেয়েছিল পরে ইসলামে জ্বলে: গরিবের খবর রাখা। ইবন সাদ তাঁর উপাধি সম্মানের সঙ্গে লেখেন। নবী ﷺ কেবল গোত্র বা সন্ধির জন্য তাঁকে বিয়ে করেননি; তাঁর ঘর দেওয়া রুটি দিয়ে চেনা যেত।

আয়িশা বা উম্মু সালামাহর মতো বর্ণনাভাণ্ডার তাঁর নেই। সিরাতের ছাত্র তাই সীমিত বর্ণনার সতর্কতায় কথা বলে, বক্তৃতা বা মুজিজা উদ্ভাবন করে না। তাঁর জীবদ্দশায় ওফাতই যথেষ্ট তাঁকে সেই স্ত্রীদের মধ্যে রাখতে যারা তাঁর আগে কবরে যান, যেমন মক্কায় খাদিজাহ গিয়েছিলেন।

তিনি বাকীতে দাফন হন। তাঁর পর মদিনার ঘর সাওদাহ, আয়িশা, হাফসাহ, তারপর উম্মু সালামাহ ও পরবর্তী উম্মাহাতের সঙ্গে চলে। তাঁর খালি স্থান জামাতকে মনে করায় মসজিদের পাশের ঘরও মৃত্যু আস্বাদন করে।

উম্মুল মাসাকীন উম্মাহাতুল মুমিনীনের তালিকায় থাকেন। ৩৩:৬-এর কুরআনি সম্মান সংক্ষিপ্ত বিবাহকেও ঢাকে যেমন দীর্ঘ বিবাহকে। উম্মাহ আল্লাহর সন্তুষ্টি চায় এবং হুজরার বছর গণনা করে মর্যাদা মাপে না।

এভাবে পঞ্চম মাতা হিলালি বিধবা যাঁকে দরিদ্রদের মাতা বলা হয়, মদিনায় বিবাহিত, কয়েক মাস পর ওফাত, খাদিজাহ ছাড়া একমাত্র স্ত্রী যিনি তাঁর ﷺ জীবদ্দশায় মারা যান। আল্লাহ তাঁর প্রতি সন্তুষ্ট হোন।""",
    """Zainab binti Khuzaimah radhiyallahu anha berasal dari Bani Hilal bin Amir. Ia sudah dikenal, bahkan sebelum Islam, sebagai Ummul Masakin, Ibu Orang Miskin, karena memberi makan orang lapar dan memberi tanpa menghitung. Ia masuk Islam, berhijrah, dan menjanda. Di antara nama suami sebelumnya ialah Ubaidah bin al-Harits, sepupu Nabi ﷺ yang syahid di Badar; thabaqat juga menyebut riwayat lain. Yang disepakati ialah ia janda mukminah yang dermawan ketika Rasulullah ﷺ menikahinya di Madinah, sekitar 3 H.

Pernikahan itu singkat. Setelah hanya beberapa bulan—dua atau tiga dalam sebagian catatan, delapan dalam yang lain—ia wafat di Madinah, sekitar 4 H. Ia satu-satunya istri selain Khadijah radhiyallahu anha yang meninggal semasa hidup Nabi ﷺ. Beliau memakamkannya, dan umat lebih mengingat kunyahnya daripada kronik panjang hari-harinya, karena hari-harinya di rumah tangga sedikit.

Jangka pendek itu sendiri pelajaran sirah. Tidak setiap ibu dikenang karena dasawarsa hadis. Sebagian dikenang karena sifat yang sudah bernama di jahiliah lalu bersinar dalam Islam: peduli kepada orang miskin. Ibnu Sa'd mencatat gelarnya dengan kehormatan. Nabi ﷺ tidak menikahinya hanya karena suku atau perjanjian; rumahnya dikenal karena roti yang diberikan.

Ia tidak memiliki korpus riwayat seperti Aisyah atau Ummu Salamah. Penuntut sirah karena itu berbicara tentangnya dengan kehati-hatian riwayat yang terbatas, tanpa mengarang pidato atau mukjizat. Fakta kewafatannya semasa hidup beliau cukup untuk menempatkannya di antara istri yang mendahului beliau ke kubur, sebagaimana Khadijah di Makkah.

Ia dimakamkan di Baqi. Setelahnya, rumah tangga di Madinah berlanjut dengan Saudah, Aisyah, Hafshah, lalu Ummu Salamah dan para ibu kemudian. Tempatnya yang kosong mengingatkan jamaah bahwa bahkan rumah di sisi masjid merasakan kematian.

Ummul Masakin tetap dalam daftar ibu kaum mukmin. Kehormatan Qurani 33:6 mencakup pernikahan singkat sebagaimana pernikahan yang panjang. Umat memohon Allah meridainya dan tidak mengukur martabatnya dengan bilangan tahun di kamar.

Dengan itu ibu kelima adalah janda Hilal yang disebut Ibu Orang Miskin, dinikahi di Madinah, wafat setelah beberapa bulan, satu-satunya istri selain Khadijah yang meninggal sementara beliau ﷺ masih hidup. Semoga Allah meridainya.""",
)

c["items"][5]["details"] = D(
    """Umm Salamah, Hind bint Abi Umayyah ibn al-Mughira رضي الله عنها, was of Banu Makhzum, among the noblest of Quraysh. She and her husband Abu Salamah Abdullah ibn Abd al-Asad were among the earliest Muslims. Abu Salamah was a foster-brother of the Prophet ﷺ, both having been nursed by Thuwaybah. They migrated to Abyssinia, returned, then were among the first to Madinah. Her hijrah is told with hardship: her clan held her, and her son Salamah was pulled between them, until Allah opened a way.

Abu Salamah fought at Uhud, was wounded, recovered for a time, then died in Madinah in Jumada al-Akhirah 4 AH from those wounds. She said the words of istirja' and the du'a taught for calamity, asking Allah for a better husband than him. Then the Messenger ﷺ proposed. She hesitated, mentioning her age, her children, and a nature that could be jealous; he ﷺ answered each concern. The marriage was in Shawwal 4 AH. Her children—Salamah, Umar, Zaynab, and Durrah—entered the prophetic household with her.

She was a woman of judgement. The most famous counsel is at al-Hudaybiyyah in 6 AH. When the Companions, grieved by the treaty, delayed slaughtering their animals and shaving, she advised him ﷺ to go out, slaughter, and shave without speaking to anyone. He did so; they followed. Ibn Ishaq and the maghazi preserve that scene as an example of a wife's wisdom in a public crisis.

After Aisha she is among the most learned of the Mothers. Many hadith of fiqh, of the hijrah, and of the Prophet's words in the home are from her. The Successors of Madinah took knowledge at her door. She lived through Badr's aftermath, Uhud, the Trench, the Conquest, and the Farewell, and she could speak of them as an eyewitness of the inner house.

She remained in Madinah after his wafat, did not remarry, and taught. Reports of her death include 59 AH and 61 or 62 AH; many scholars hold that she was among the last of the Mothers to die, in Madinah, and that she was buried in al-Baqi'. The difference of a few years does not change her place in the seerah.

Banu Makhzum had been among the fiercest opponents in Makkah; her presence in the household is part of how Allah turned old enmity into kinship. Students remember her not only as a widow of Uhud but as the counsellor of Hudaybiyyah and a pillar of female scholarship.

Thus the sixth Mother is Hind of Makhzum, early Muslim, emigrant to Abyssinia and Madinah, widow of Abu Salamah, wise wife whose word moved an army at Hudaybiyyah. May Allah be pleased with her.""",
    """ام سلمہ، ہند بنت ابی امیہ بن مغیرہ رضی اللہ عنہا، بنو مخزوم سے تھیں، قریش کے اشراف میں۔ شوہر ابو سلمہ عبد اللہ بن عبد الاسد کے ساتھ اولین مسلمانوں میں سے تھیں۔ ابو سلمہ نبی ﷺ کے رضاعی بھائی تھے، دونوں ثویبہ کا دودھ پی چکے تھے۔ حبشہ ہجرت، واپسی، پھر مدینہ کے اولین مہاجرین میں۔ ان کی ہجرت سختی سے بیان ہوتی ہے: قبیلے نے روکا، بیٹا سلمہ کھینچا گیا، یہاں تک اللہ نے راہ کھولی۔

ابو سلمہ احد میں لڑے، زخمی ہوئے، کچھ افاقہ پھر جمادی الآخرہ 4ھ میں انہی زخموں سے مدینہ میں فوت ہوئے۔ انہوں نے استرجاع اور مصیبت کی دعا پڑھی، اللہ سے ان سے بہتر شوہر مانگا۔ پھر رسول ﷺ نے پیغام دیا۔ عمر، بچوں اور غیرت کے مزاج کا ذکر کر کے ہچکچائیں؛ آپ ﷺ نے ہر فکر کا جواب دیا۔ نکاح شوال 4ھ میں ہوا۔ بچے—سلمہ، عمر، زینب، درہ—ان کے ساتھ نبوی گھر میں آئے۔

صاحب رائے تھیں۔ سب سے مشہور مشورہ 6ھ میں حدیبیہ پر ہے۔ جب صحابہ معاہدے کے غم میں قربانی اور سر منڈانے میں رکے، انہوں نے کہا آپ ﷺ بغیر کسی سے کہے نکل کر قربانی کریں اور منڈائیں۔ آپ نے ایسا کیا؛ سب نے پیروی کی۔ ابن اسحاق اور مغازی اس منظر کو عوامی بحران میں بیوی کی حکمت کی مثال رکھتے ہیں۔

عائشہ کے بعد امهات میں سب سے زیادہ عالمہ میں سے ہیں۔ فقہ، ہجرت، اور گھر میں نبوی کلام کی بہت احادیث ان سے ہیں۔ مدینہ کے تابعین دروازے پر علم لیتے۔ بدر کے بعد، احد، خندق، فتح اور وداع تک جئیں، اور اندرونی گھر کی گواہ کی طرح بیان کر سکتی تھیں۔

وفات نبوی کے بعد مدینہ میں رہیں، دوبارہ نکاح نہ کیا، پڑھایا۔ وفات کی روایات 59ھ اور 61 یا 62ھ شامل ہیں؛ بہت علما انہیں آخری امهات میں شمار کرتے ہیں جو مدینہ میں فوت ہوئیں، بقیع میں دفن۔ چند سال کا فرق سیرت میں ان کا مقام نہیں بدلتا۔

بنو مخزوم مکہ میں سخت ترین مخالفوں میں تھے؛ گھر میں ان کی موجودگی اس بات کا حصہ ہے کہ اللہ نے پرانی دشمنی کو رشتہ بنا دیا۔ طالب علم انہیں صرف احد کی بیوہ نہیں، حدیبیہ کی مشیر اور خواتین کے علم کا ستون سمجھتے ہیں۔

یوں چھٹی ماں مخزوم کی ہند ہیں، اولین مسلم، حبشہ و مدینہ کی مہاجر، ابو سلمہ کی بیوہ، دانا زوجہ جن کی بات نے حدیبیہ پر لشکر ہلایا۔ اللہ ان سے راضی ہو۔""",
    """उम्म सलमा, हिन्द बिन्त अबी उमैया इब्न अल-मुग़ीरा رضي الله عنها, बनू मख़ज़ूम से थीं, कुरैश के अशराफ़ में। शौहर अबू सलमा अब्दुल्लाह इब्न अब्दुल असद के साथ अव्वलीन मुसलमानों में थीं। अबू सलमा नबी ﷺ के रज़ाई भाई थे, दोनों सुवैबा का दूध पी चुके थे। हबशा हिजरत, वापसी, फिर मदीना के अव्वलीन मुहाजिरीन में। उनकी हिजरत सख़्ती से बयान होती है: क़बीले ने रोका, बेटा सलमा खिंचा गया, यहाँ तक अल्लाह ने राह खोली।

अबू सलमा उहुद में लड़े, ज़ख़्मी हुए, कुछ आराम फिर जमाद अल-आख़िरा 4 हिजरी में उन्हीं ज़ख़्मों से मदीना में फ़ौत हुए। उन्होंने इस्तिरजा और मुसीबत की दुआ पढ़ी, अल्लाह से उनसे बेहतर शौहर माँगा। फिर रसूल ﷺ ने पैग़ाम दिया। उम्र, बच्चों और ग़ैरत के मिज़ाज का ज़िक्र कर हिचकिचाईं; आप ﷺ ने हर फ़िक्र का जवाब दिया। निकाह शव्वाल 4 हिजरी में हुआ। बच्चे—सलमा, उमर, ज़ैनब, दुर्रा—उनके साथ नबवी घर में आए।

साहब-ए-राय थीं। सबसे मशहूर मशवरा 6 हिजरी में हुदैबिया पर है। जब सहाबा मुआहदे के ग़म में क़ुर्बानी और सर मुंडाने में रुके, उन्होंने कहा आप ﷺ बिना किसी से कहे निकलकर क़ुर्बानी करें और मुंडाएँ। आपने ऐसा किया; सब ने पैरवी की। इब्न इसहाक और मग़ाज़ी इस मंज़र को आवामी बहरान में बीवी की हिकमत की मिसाल रखते हैं।

आयशा के बाद उम्महात में सबसे अधिक आलिमा में से हैं। फ़िक़्ह, हिजरत, और घर में नबवी कलाम की बहुत हदीसें उनसे हैं। मदीना के ताबिईन दरवाज़े पर इल्म लेते। बद्र के बाद, उहुद, खंदक, फ़तह और विदा तक जीं, और अंदरूनी घर की गवाह की तरह बयान कर सकती थीं।

विसाल-ए-नबवी के बाद मदीना में रहीं, दोबारा निकाह न किया, पढ़ाया। वफ़ात की रिवायात 59 हिजरी और 61 या 62 हिजरी शामिल हैं; बहुत उलेमा उन्हें आख़िरी उम्महात में शुमार करते हैं जो मदीना में फ़ौत हुईं, बक़ी' में दफ़न। चंद साल का फ़र्क सीरत में उनका मक़ाम नहीं बदलता।

बनू मख़ज़ूम मक्का में सख़्ततरीन मुख़ालिफ़ों में थे; घर में उनकी मौजूदगी इस बात का हिस्सा है कि अल्लाह ने पुरानी दुश्मनी को रिश्ता बना दिया। तालिब-ए-इल्म उन्हें केवल उहुद की विधवा नहीं, हुदैबिया की मुशीर और ख़वातीन के इल्म का सुतून समझते हैं।

यूँ छठी माँ मख़ज़ूम की हिन्द हैं, अव्वलीन मुस्लिम, हबशा व मदीना की मुहाजिर, अबू सलमा की विधवा, दाना ज़ौजा जिनकी बात ने हुदैबिया पर लश्कर हिलाया। अल्लाह उनसे राज़ी हो।""",
    """উম্মু সালামাহ, হিন্দ বিনত আবি উমাইয়াহ ইবন আল-মুগীরাহ رضي الله عنها, বনু মাখযুম থেকে ছিলেন, কুরাইশের সম্ভ্রান্তদের মধ্যে। তিনি ও স্বামী আবু সালামাহ আব্দুল্লাহ ইবন আব্দুল আসাদ প্রথম যুগের মুসলিম। আবু সালামাহ নবী ﷺ-এর দুধভাই, উভয়ে সুওয়াইবাহর দুধ পান করেছেন। তাঁরা হাবশায় হিজরত করেন, ফিরে আসেন, পরে মদিনার প্রথম মুহাজিরদের মধ্যে। তাঁর হিজরত কষ্টের সঙ্গে বলা হয়: গোত্র তাঁকে আটকে, পুত্র সালামাহ টানাটানি হয়, যতক্ষণ আল্লাহ পথ খুলেন।

আবু সালামাহ উহুদে যুদ্ধ করেন, আহত হন, কিছুটা সেরে ওঠেন, পরে জুমাদাল আখিরাহ ৪ হিজরিতে সেই ক্ষতে মদিনায় মারা যান। তিনি ইস্তির্জা ও মুসিবতের দোয়া পড়েন, আল্লাহর কাছে তাঁর চেয়ে উত্তম স্বামী চান। তারপর রাসূল ﷺ প্রস্তাব দেন। তিনি বয়স, সন্তান ও ঈর্ষাপ্রবণ স্বভাবের কথা বলে দ্বিধা করেন; তিনি ﷺ প্রতিটি চিন্তার উত্তর দেন। বিবাহ শাওয়াল ৪ হিজরিতে হয়। তাঁর সন্তান—সালামাহ, উমর, যাইনাব, দুররাহ—তাঁর সঙ্গে নববি ঘরে আসে।

তিনি বিচারবুদ্ধির অধিকারী ছিলেন। সবচেয়ে প্রসিদ্ধ পরামর্শ ৬ হিজরিতে হুদায়বিয়ায়। সাহাবিরা সন্ধির দুঃখে কুরবানি ও মাথা মুণ্ডনে দেরি করলে তিনি পরামর্শ দেন তিনি ﷺ কারও সঙ্গে না বলে বেরিয়ে কুরবানি করুন ও মুণ্ডন করুন। তিনি তাই করেন; সবাই অনুসরণ করে। ইবন ইসহাক ও মাগাজি সেই দৃশ্যকে জনসংকটে স্ত্রীর হিকমতের উদাহরণ হিসেবে রাখে।

আয়িশার পর তিনি উম্মাহাতের মধ্যে অন্যতম শ্রেষ্ঠ আলিমা। ফিকহ, হিজরত ও ঘরে নববি বাণীর অনেক হাদিস তাঁর থেকে। মদিনার তাবেয়িরা দরজায় ইলম নেন। তিনি বদরের পর, উহুদ, খন্দক, বিজয় ও বিদায় পর্যন্ত বেঁচে থাকেন এবং অন্তর্ঘরের সাক্ষী হিসেবে বলতে পারতেন।

নবীর ওফাতের পর মদিনায় থাকেন, পুনরায় বিয়ে করেননি, শিক্ষা দেন। ওফাতের বর্ণনায় ৫৯ হিজরি এবং ৬১ বা ৬২ হিজরি আছে; অনেক আলিম তাঁকে সর্বশেষ উম্মাহাতের মধ্যে গণ্য করেন যারা মদিনায় ইন্তেকাল করেন, বাকীতে দাফন। কয়েক বছরের পার্থক্য সিরাতে তাঁর স্থান বদলায় না।

বনু মাখযুম মক্কায় কঠোরতম বিরোধীদের মধ্যে ছিল; ঘরে তাঁর উপস্থিতি সেই অধ্যায়ের অংশ যেভাবে আল্লাহ পুরনো শত্রুতাকে আত্মীয়তায় ঘোরান। ছাত্ররা তাঁকে কেবল উহুদের বিধবা নন, হুদায়বিয়ার পরামর্শদাতা ও নারী ইলমের স্তম্ভ হিসেবে মনে রাখেন।

এভাবে ষষ্ঠ মাতা মাখযুমের হিন্দ, প্রথম যুগের মুসলিম, হাবশা ও মদিনার মুহাজির, আবু সালামাহর বিধবা, জ্ঞানী স্ত্রী যাঁর কথা হুদায়বিয়ায় সেনাদল নাড়ায়। আল্লাহ তাঁর প্রতি সন্তুষ্ট হোন।""",
    """Ummu Salamah, Hind binti Abu Umayyah bin al-Mughirah radhiyallahu anha, berasal dari Bani Makhzum, termasuk bangsawan Quraisy. Ia dan suaminya Abu Salamah Abdullah bin Abd al-Asad termasuk muslim paling awal. Abu Salamah adalah saudara susuan Nabi ﷺ, keduanya disusui Tsuwaibah. Mereka berhijrah ke Habasyah, kembali, lalu termasuk yang pertama ke Madinah. Hijrahnya diceritakan dengan kesukaran: keluarganya menahannya, dan putranya Salamah ditarik di antara mereka, hingga Allah membuka jalan.

Abu Salamah berperang di Uhud, terluka, sembuh sementara, lalu meninggal di Madinah pada Jumadal Akhirah 4 H karena luka itu. Ia mengucapkan istirja dan doa musibah, memohon kepada Allah suami yang lebih baik darinya. Kemudian Rasulullah ﷺ meminang. Ia ragu, menyebut usia, anak-anak, dan watak yang bisa cemburu; beliau ﷺ menjawab setiap kekhawatiran. Pernikahan pada Syawal 4 H. Anak-anaknya—Salamah, Umar, Zainab, dan Durrah—masuk rumah tangga nabi bersamanya.

Ia wanita yang berpandangan. Nasihat paling terkenal ialah di Hudaibiyah tahun 6 H. Ketika para sahabat, sedih karena perjanjian, menunda menyembelih hewan dan mencukur, ia menasihati beliau ﷺ agar keluar, menyembelih, dan mencukur tanpa berbicara kepada siapa pun. Beliau melakukannya; mereka mengikuti. Ibnu Ishaq dan maghazi menyimpan adegan itu sebagai contoh hikmah istri dalam krisis publik.

Setelah Aisyah ia termasuk ibu yang paling berilmu. Banyak hadis fikih, hijrah, dan ucapan nabi di rumah berasal darinya. Tabiin Madinah mengambil ilmu di pintunya. Ia hidup melewati pasca-Badar, Uhud, Khandaq, Fathu Makkah, dan haji wada, dan dapat berbicara sebagai saksi mata rumah batin.

Ia tetap di Madinah setelah wafat beliau, tidak menikah lagi, dan mengajar. Riwayat kewafatannya meliputi 59 H dan 61 atau 62 H; banyak ulama menilai ia termasuk ibu terakhir yang wafat, di Madinah, dimakamkan di Baqi. Selisih beberapa tahun tidak mengubah tempatnya dalam sirah.

Bani Makhzum termasuk penentang paling keras di Makkah; kehadirannya di rumah tangga adalah bagian dari bagaimana Allah memalingkan permusuhan lama menjadi kekerabatan. Penuntut ilmu mengingatnya bukan hanya sebagai janda Uhud, tetapi sebagai penasihat Hudaibiyah dan pilar keilmuan perempuan.

Dengan itu ibu keenam adalah Hind dari Makhzum, muslim awal, muhajirah ke Habasyah dan Madinah, janda Abu Salamah, istri bijak yang katanya menggerakkan pasukan di Hudaibiyah. Semoga Allah meridainya.""",
)

c["items"][6]["details"] = D(
    """Zaynab bint Jahsh al-Asadiyyah رضي الله عنها was the daughter of Umaymah bint Abd al-Muttalib, and so a cousin of the Prophet ﷺ. Her family had entered Islam and known the pressure of Quraysh. He ﷺ married her first to Zayd ibn Harithah, his freedman and adopted son, who until then was called Zayd ibn Muhammad. She was reluctant because of lineage; then she obeyed when the command came. The intent, in the Sunni reading, was to break pride of blood by joining a Hashimi cousin to a freedman whom Allah and His Messenger loved.

The marriage with Zayd did not rest in harmony. Zayd complained more than once; he ﷺ told him to keep his wife. When the union could not continue, Zayd divorced her. After her waiting period Allah revealed: "We married her to you" (al-Ahzab 33:37). The verse names the wisdom: so that the believers would have no difficulty in the wives of their adopted sons when they have finished with them. Jahili custom had treated an adopted son as a biological son in marriage law. The Qur'an had already said "Call them by their fathers" (33:5). This nikah ended that fiction in the most public house in Madinah.

Hypocrites gossiped. The revelation answered them. Zaynab رضي الله عنها would say, with gratitude not vanity: your families married you, but Allah married me from above seven heavens. Ibn Sa'd and the hadith collections preserve that wording. Sunni seerah rejects the claim that the Prophet ﷺ acted from a hidden passion; the matter is tied in the Qur'an to legislation, and he had first insisted that Zayd keep her.

She was known for piety, night prayer, and working leather with her own hands to give in charity. The Prophet ﷺ said the one of you with the longest reach would join him first; they later understood it of charity, and Zaynab was the first of the wives to die after him, in 20 AH (641 CE) in the caliphate of Umar. Umar رضي الله عنه provided a generous shroud and prayed over her. She was buried in al-Baqi'.

Her death in 20 AH makes her the first Mother to follow him ﷺ to the grave after the wafat. The household remembered her fasting and her refusal to keep wealth overnight. Students of seerah place her marriage in 5 AH, after the legislation of hijab and the ending of the adopted-son custom had become a public lesson.

She left hadith, though fewer than Aisha or Umm Salamah. Her honour is the verse itself. To speak of her without 33:37 is to miss why this marriage stands in the Qur'an while many others do not.

Thus the seventh Mother is the Hashimi cousin, once wife of Zayd, married by revelation, breaker of a Jahili legal fiction, a woman of prayer and charity who died in 20 AH. May Allah be pleased with her.""",
    """زینب بنت جحش اسدیہ رضی اللہ عنہا امیہ بنت عبد المطلب کی بیٹی تھیں، پس نبی ﷺ کی پھوپھی زاد۔ خاندان اسلام لا چکا تھا اور قریش کا دباؤ دیکھ چکا تھا۔ آپ ﷺ نے پہلے انہیں زید بن حارثہ سے نکاح دیا، اپنے آزاد کردہ اور منہ بولے بیٹے سے، جنہیں اس وقت زید بن محمد کہا جاتا تھا۔ نسب کی وجہ سے ہچکچائیں؛ پھر حکم آنے پر اطاعت کی۔ اہل سنت کی قراءت میں مقصد خون کے غرور کو توڑنا تھا، ہاشمی پھوپھی زاد کو اس آزاد کردہ سے جوڑ کر جسے اللہ اور اس کے رسول چاہتے تھے۔

زید سے نکاح میں ہمواری نہ رہی۔ زید نے بار بار شکایت کی؛ آپ ﷺ نے بیوی رکھنے کو کہا۔ جب گھر نہ چل سکا تو زید نے طلاق دی۔ عدت کے بعد اللہ نے نازل فرمایا: «زوجناکها» (الاحزاب 33:37)۔ آیت حکمت نام لیتی ہے: تاکہ مؤمنوں پر منہ بولے بیٹوں کی بیویوں میں تنگی نہ ہو جب وہ ان سے فارغ ہو جائیں۔ جاہلی رسم منہ بولے بیٹے کو نکاح کے حکم میں سگے بیٹے کی طرح سمجھتی تھی۔ قرآن پہلے کہہ چکا تھا «ادْعُوهُمْ لِآبَائِهِمْ» (33:5)۔ اس نکاح نے مدینہ کے سب سے کھلے گھر میں وہ فرضی نسبت ختم کی۔

منافقوں نے چہ میگوئیاں کیں۔ وحی نے جواب دیا۔ زینب رضی اللہ عنہا شکر سے، نہ غرور سے، کہتیں: تمہارے خاندانوں نے تمہارا نکاح کیا، اللہ نے اوپر سات آسمانوں سے میرا نکاح کیا। ابن سعد اور حدیث کی کتابیں یہ الفاظ رکھتی ہیں۔ اہل سنت کی سیرت اس دعوے کو رد کرتی ہے کہ نبی ﷺ نے چھپی خواہش سے کام لیا؛ معاملہ قرآن میں تشریع سے بندھا ہے، اور آپ نے پہلے زید کو انہیں رکھنے پر اصرار کیا تھا۔

تقویٰ، تہجد، اور اپنے ہاتھ چمڑا کام کر کے صدقہ دینے سے مشہور ہوئیں۔ نبی ﷺ نے فرمایا تم میں لمبا ہاتھ والی پہلے ملے گی؛ بعد میں سمجھا گیا صدقے کا ہاتھ، اور زینب ازواج میں آپ کے بعد سب سے پہلے 20ھ (641ء) عمر کی خلافت میں فوت ہوئیں۔ عمر رضی اللہ عنہ نے فراخ کفن دیا اور نماز پڑھائی۔ بقیع میں دفن ہوئیں۔

20ھ کی وفات انہیں وفات نبوی کے بعد قبر میں پہلی ماں بناتی ہے۔ گھر نے ان کے روزے اور مال رات نہ رکھنے کو یاد رکھا۔ طالب سیرت نکاح 5ھ میں رکھتے ہیں، جب حجاب کا حکم اور منہ بولے بیٹے کی رسم کا خاتمہ کھلا سبق بن چکا تھا۔

احادیث چھوڑیں، عائشہ یا ام سلمہ سے کم۔ ان کی عزت خود آیت ہے۔ 33:37 کے بغیر ان کی بات اس سوال کو چھوڑتی ہے کہ یہ نکاح قرآن میں کیوں ہے اور بہت سے اور نہیں۔

یوں ساتویں ماں ہاشمی پھوپھی زاد ہیں، کبھی زید کی زوجہ، وحی سے نکاح، جاہلی قانونی فرضی نسبت توڑنے والی، نماز و صدقے کی خاتون جو 20ھ میں فوت ہوئیں۔ اللہ ان سے راضی ہو۔""",
    """ज़ैनब बिन्त जह्श असदिया رضي الله عنها उमैमा बिन्त अब्दुल मुत्तलिब की बेटी थीं, पस नबी ﷺ की फूफेरी बहन। ख़ानदान इस्लाम ला चुका था और कुरैश का दबाव देख चुका था। आप ﷺ ने पहले उन्हें ज़ैद इब्न हारिसा से निकाह दिया, अपने आज़ादशुदा और मुंहबोले बेटे से, जिन्हें तब ज़ैद इब्न मुहम्मद कहा जाता था। नसब की वजह से हिचकिचाईं; फिर हुक्म आने पर इताअत की। अहले सुन्नत की क़िराअत में मक़सद ख़ून के ग़ुरूर को तोड़ना था, हाशिमी फूफेरी को उस आज़ादशुदा से जोड़कर जिसे अल्लाह और उसके रसूल चाहते थे।

ज़ैद से निकाह में हमवारी न रही। ज़ैद ने बार-बार शिकायत की; आप ﷺ ने बीवी रखने को कहा। जब घर न चल सका तो ज़ैद ने तलाक़ दी। इद्दत के बाद अल्लाह ने नाज़िल फ़रमाया: «ज़व्वजनाकाहा» (अल-अहज़ाब 33:37)। आयत हिकमत नाम लेती है: ताकि मोमिनों पर मुंहबोले बेटों की बीवियों में तंगी न हो जब वे उनसे फ़ारिग़ हो जाएँ। जाहिली रस्म मुंहबोले बेटे को निकाह के हुक्म में सगे बेटे की तरह समझती थी। कुरआन पहले कह चुका था «उन्हें उनके बापों से पुकारो» (33:5)। इस निकाह ने मदीना के सबसे खुले घर में वह फ़र्ज़ी निस्बत ख़त्म की।

मुनाफ़िक़ों ने चह-मीगुई कीं। वही ने जवाब दिया। ज़ैनब رضي الله عنها शुक्र से, न ग़ुरूर से, कहतीं: तुम्हारे ख़ानदानों ने तुम्हारा निकाह किया, अल्लाह ने ऊपर सात आसमानों से मेरा निकाह किया। इब्न साद और हदीस की किताबें ये अल्फ़ाज़ रखती हैं। अहले सुन्नत की सीरत उस दावे को रद करती है कि नबी ﷺ ने छिपी ख़्वाहिश से काम लिया; मामला कुरआन में तशरीअ से बंधा है, और आपने पहले ज़ैद को उन्हें रखने पर इस्रार किया था।

तक़वा, तहज्जुद, और अपने हाथ चमड़ा काम कर सदक़ा देने से मशहूर हुईं। नबी ﷺ ने फ़रमाया तुम में लंबा हाथ वाली पहले मिलेगी; बाद में समझा गया सदक़े का हाथ, और ज़ैनब अज़वाज में आपके बाद सबसे पहले 20 हिजरी (641 ई.) उमर की ख़िलाफ़त में फ़ौत हुईं। उमर رضي الله عنه ने फ़राख़ कफ़न दिया और नमाज़ पढ़ाई। बक़ी' में दफ़न हुईं।

20 हिजरी की वफ़ात उन्हें विसाल-ए-नबवी के बाद क़ब्र में पहली माँ बनाती है। घर ने उनके रोज़े और माल रात न रखने को याद रखा। तालिब-ए-सीरत निकाह 5 हिजरी में रखते हैं, जब हिजाब का हुक्म और मुंहबोले बेटे की रस्म का ख़ातिमा खुला सबक़ बन चुका था।

हदीसें छोड़ीं, आयशा या उम्म सलमा से कम। उनकी इज़्ज़त ख़ुद आयत है। 33:37 के बिना उनकी बात उस सवाल को छोड़ती है कि यह निकाह कुरआन में क्यों है और बहुत से और नहीं।

यूँ सातवीं माँ हाशिमी फूफेरी हैं, कभी ज़ैद की ज़ौजा, वही से निकाह, जाहिली क़ानूनी फ़र्ज़ी निस्बत तोड़ने वाली, नमाज़ व सदक़े की ख़ातून जो 20 हिजरी में फ़ौत हुईं। अल्लाह उनसे राज़ी हो।""",
    """যাইনাব বিনত জাহশ আল-আসাদিয়্যাহ رضي الله عنها উমাইমাহ বিনত আব্দুল মুত্তালিবের কন্যা, সুতরাং নবী ﷺ-এর ফুফাতো বোন। তাঁর পরিবার ইসলাম গ্রহণ করেছে এবং কুরাইশের চাপ দেখেছে। তিনি ﷺ প্রথমে তাঁকে যায়েদ ইবন হারিসার সঙ্গে বিয়ে দেন, তাঁর মুক্ত ও পোষ্য পুত্র, যাঁকে তখন যায়েদ ইবন মুহাম্মদ বলা হত। বংশের কারণে তিনি দ্বিধা করেন; পরে নির্দেশ এলে মান্য করেন। সুন্নি পাঠে উদ্দেশ্য ছিল রক্তের অহংকার ভাঙা, এক হাশিমি ফুফাতো বোনকে সেই মুক্ত মানুষের সঙ্গে যুক্ত করে যাঁকে আল্লাহ ও তাঁর রাসূল ভালোবাসেন।

যায়েদের সঙ্গে বিবাহে সম্প্রীতি থাকেনি। যায়েদ বারবার অভিযোগ করেন; তিনি ﷺ স্ত্রী রাখতে বলেন। ঘর না চললে যায়েদ তালাক দেন। ইদ্দতের পর আল্লাহ নাজিল করেন, ‘আমি তাঁকে তোমার সঙ্গে বিবাহ দিয়েছি’ (আল-আহযাব ৩৩:৩৭)। আয়াত হিকমত নাম করে: যাতে মুমিনদের জন্য পোষ্য পুত্রদের স্ত্রী বিষয়ে সংকীর্ণতা না থাকে যখন তারা তাদের থেকে অব্যাহতি পায়। জাহিলি প্রথা পোষ্য পুত্রকে বিবাহ আইনে রক্তের পুত্রের মতো মানত। কুরআন আগেই বলেছে, ‘তাদের পিতাদের নামে ডাকো’ (৩৩:৫)। এই বিবাহ মদিনার সবচেয়ে প্রকাশ্য ঘরে সেই কল্পিত সম্পর্ক শেষ করে।

মুনাফিকরা গুজব ছড়ায়। ওহী উত্তর দেয়। যাইনাব رضي الله عنها কৃতজ্ঞতায়, অহংকারে নয়, বলতেন: তোমাদের পরিবার তোমাদের বিয়ে দিয়েছে, আল্লাহ সাত আসমানের ওপর থেকে আমার বিয়ে দিয়েছেন। ইবন সাদ ও হাদিসগ্রন্থ এই শব্দ রাখে। সুন্নি সিরাত এই দাবি প্রত্যাখ্যান করে যে নবী ﷺ গোপন আবেগ থেকে কাজ করেছেন; বিষয়টি কুরআনে আইন প্রণয়নের সঙ্গে বাঁধা, এবং তিনি আগে যায়েদকে তাঁকে রাখতে জোর দিয়েছিলেন।

তিনি তাকওয়া, রাতের সালাত, এবং নিজ হাতে চামড়ার কাজ করে দান করার জন্য পরিচিত। নবী ﷺ বলেছেন তোমাদের মধ্যে দীর্ঘহস্তা আগে মিলবে; পরে বোঝা যায় দানের হাত, এবং যাইনাব স্ত্রীদের মধ্যে তাঁর পর সর্বপ্রথম ২০ হিজরিতে (৬৪১ খ্রি.) উমরের খিলাফতে ইন্তেকাল করেন। উমর رضي الله عنه প্রশস্ত কাফন দেন ও সালাত পড়ান। তিনি বাকীতে দাফন হন।

২০ হিজরির ওফাত তাঁকে নবীর ওফাতের পর কবরে প্রথম মাতা করে। ঘর তাঁর সিয়াম ও রাতে সম্পদ না রাখাকে মনে রাখে। সিরাতের ছাত্র বিবাহ ৫ হিজরিতে রাখেন, যখন হিজাবের বিধান ও পোষ্য-পুত্র প্রথার অবসান প্রকাশ্য শিক্ষা হয়ে উঠেছে।

তিনি হাদিস রাখেন, আয়িশা বা উম্মু সালামাহর চেয়ে কম। তাঁর সম্মান আয়াতটিই। ৩৩:৩৭ ছাড়া তাঁর আলোচনা এই প্রশ্ন ছাড়ে কেন এই বিবাহ কুরআনে আছে আর অনেক অন্য বিবাহ নেই।

এভাবে সপ্তম মাতা হাশিমি ফুফাতো বোন, একদা যায়েদের স্ত্রী, ওহী দ্বারা বিবাহিত, জাহিলি আইনি কল্পনা ভাঙা নারী, সালাত ও দানের নারী যিনি ২০ হিজরিতে ইন্তেকাল করেন। আল্লাহ তাঁর প্রতি সন্তুষ্ট হোন।""",
    """Zainab binti Jahsy al-Asadiyyah radhiyallahu anha adalah putri Umaimah binti Abdul Muththalib, jadi sepupu Nabi ﷺ. Keluarganya sudah masuk Islam dan merasakan tekanan Quraisy. Beliau ﷺ menikahkannya lebih dulu dengan Zaid bin Haritsah, orang merdeka dan anak angkatnya, yang hingga itu dipanggil Zaid bin Muhammad. Ia ragu karena nasab; lalu taat ketika perintah datang. Dalam bacaan Ahlus Sunnah, tujuannya mematahkan kesombongan darah dengan menyatukan sepupu Hasyimi kepada orang merdeka yang dicintai Allah dan Rasul-Nya.

Pernikahan dengan Zaid tidak berjalan rukun. Zaid mengeluh lebih dari sekali; beliau ﷺ menyuruhnya mempertahankan istrinya. Ketika rumah tangga tidak dapat dilanjutkan, Zaid menceraikannya. Setelah idahnya, Allah menurunkan: "Kami menikahkannya denganmu" (al-Ahzab 33:37). Ayat itu menamai hikmah: agar orang beriman tidak keberatan mengenai istri anak-anak angkat mereka apabila mereka telah selesai darinya. Adat jahiliah memperlakukan anak angkat seperti anak kandung dalam hukum nikah. Al-Qur'an sudah berkata "Panggillah mereka menurut ayah-ayah mereka" (33:5). Pernikahan ini mengakhiri fiksi itu di rumah paling terbuka di Madinah.

Orang munafik bergunjing. Wahyu menjawab mereka. Zainab radhiyallahu anha berkata, dengan syukur bukan kesombongan: keluargamu yang menikahkanmu, tetapi Allah menikahkanku dari atas tujuh langit. Ibnu Sa'd dan kitab hadis menyimpan lafaz itu. Sirah Ahlus Sunnah menolak klaim bahwa Nabi ﷺ bertindak dari nafsu tersembunyi; perkara ini diikat dalam Al-Qur'an kepada pensyariatan, dan beliau lebih dulu bersikeras agar Zaid mempertahankannya.

Ia dikenal karena takwa, salat malam, dan mengerjakan kulit dengan tangannya sendiri untuk disedekahkan. Nabi ﷺ bersabda yang paling panjang jangkauannya di antara kalian akan menyusul beliau lebih dulu; kemudian dipahami sebagai sedekah, dan Zainab adalah istri pertama yang wafat setelah beliau, pada 20 H (641 M) pada khilafah Umar. Umar radhiyallahu anhu menyediakan kafan yang lapang dan mensalatkannya. Ia dimakamkan di Baqi.

Kewafatannya pada 20 H menjadikannya ibu pertama yang menyusul beliau ﷺ ke kubur setelah wafat. Rumah tangga mengingat puasanya dan keengganannya menyimpan harta semalam. Penuntut sirah menempatkan pernikahannya pada 5 H, setelah syariat hijab dan berakhirnya adat anak angkat menjadi pelajaran publik.

Ia meninggalkan hadis, walaupun lebih sedikit daripada Aisyah atau Ummu Salamah. Kehormatannya adalah ayat itu sendiri. Membicarakannya tanpa 33:37 berarti melewatkan mengapa pernikahan ini berdiri dalam Al-Qur'an sementara banyak yang lain tidak.

Dengan itu ibu ketujuh adalah sepupu Hasyimi, pernah istri Zaid, dinikahkan oleh wahyu, pematah fiksi hukum jahiliah, wanita salat dan sedekah yang wafat tahun 20 H. Semoga Allah meridainya.""",
)

c["items"][7]["details"] = D(
    """Juwayriyah bint al-Harith ibn Abi Dirar رضي الله عنها was the daughter of the chief of Banu al-Mustaliq, a branch of Khuza'ah. In Sha'ban of 5 AH, or 6 AH according to Ibn Ishaq—the sources differ by a year—the expedition of al-Muraysi' met Banu al-Mustaliq. She was among the captives and fell in the lot of Thabit ibn Qays. She sought a mukatabah, a contract to buy her freedom, then came to the Prophet ﷺ asking help with the price.

He ﷺ offered a better way: he would pay what was due and marry her. She accepted. Her name had been Barrah; he renamed her Juwayriyah. As soon as she became Mother of the Believers, the Companions said: these captives are the in-laws of the Messenger of Allah. They freed many of her people—a hundred or more in the famous count. She later said that no woman brought greater blessing to her people than she. The marriage turned a battlefield into kinship.

Islam spread in Banu al-Mustaliq after that honour. Her father al-Harith is reported to have come, received his daughter with dignity, and accepted Islam in the well-known telling. Whether every detail of that visit is equally strong, the seerah agrees that the tribe's fortune changed because one woman entered the prophetic house. Students of maghazi read al-Muraysi' together with this nikah, not as two separate stories.

She was remembered for long dhikr. Muslim and the sunan narrate from her the report of the four phrases after Fajr—"Subhan Allah wa bi-hamdihi, 'adada khalqihi..."—which the Prophet ﷺ taught her, saying they outweighed her long tasbih that morning. The Ummah learned from a Mother that remembrance has weight, not only duration.

She lived in Madinah in a chamber among the wives, narrated hadith, and remained a widow of the Prophet ﷺ after 11 AH. She died in Rabi' al-Awwal 50 AH according to a well-known report (some say 56 AH), in Madinah, and was buried in al-Baqi'. The difference of years is noted in the tabaqat without dispute of her rank.

Her story is taught as a model of how a marriage in Islam can lift a whole tribe from captivity to affinity. It is not told as a tale of humiliation. Juwayriyah رضي الله عنها is honoured as Mother of the Believers, daughter of a chieftain, and a woman of dhikr.

Thus the eighth Mother is the Mustaliqi princess of al-Muraysi', whose nikah freed captives, whose tongue remembered Allah, and who died in Madinah about 50 AH. May Allah be pleased with her.""",
    """جویریہ بنت الحارث بن ابی ضرار رضی اللہ عنہا بنو مصطلق کے سردار کی بیٹی تھیں، خزاعہ کی شاخ۔ شعبان 5ھ میں، یا ابن اسحاق کے مطابق 6ھ—مصادر ایک سال کا فرق رکھتے ہیں—غزوہ مریسیع بنو مصطلق سے ٹکرایا۔ وہ قیدیوں میں تھیں اور ثابت بن قیس کے حصے میں آئیں۔ مکاتبہ چاہی، آزادی کی قیمت، پھر نبی ﷺ کے پاس قیمت میں مدد مانگیں۔

آپ ﷺ نے بہتر بات کی: جو واجب ہے ادا کریں گے اور نکاح کریں گے۔ انہوں نے قبول کیا۔ نام برہ تھا؛ آپ نے جویریہ رکھا۔ جیسے ہی ام المؤمنین بنیں صحابہ نے کہا یہ قیدی رسول اللہ کے سسرال ہیں۔ ان کی قوم کے بہت سے—مشہور شمار میں سو یا زیادہ—آزاد کیے۔ بعد میں کہتیں کوئی عورت اپنی قوم کے لیے مجھ سے بڑی برکت نہ لائی۔ نکاح نے میدان جنگ کو رشتہ بنا دیا۔

اس عزت کے بعد بنو مصطلق میں اسلام پھیلا۔ والد حارث کے آنے، بیٹی عزت سے لینے، اور اسلام لانے کی مشہور روایت ہے۔ چاہے اس آمد کی ہر تفصیل یکساں قوی نہ ہو، سیرت اس پر متفق ہے کہ قبیلے کی قسمت اس لیے بدلی کہ ایک عورت نبوی گھر میں آئی۔ طالب مغازی مریسیع کو اس نکاح کے ساتھ پڑھتے ہیں، دو الگ کہانیاں نہیں۔

ذکر کثیر سے یاد کی گئیں۔ مسلم اور سنن ان سے فجر کے بعد چار کلمات کی روایت لاتے ہیں—«سبحان الله وبحمده عدد خلقه...»—جو نبی ﷺ نے سکھائے، فرمایا اس صبح کی لمبی تسبیح پر بھاری ہیں۔ امت نے ایک ماں سے سیکھا کہ ذکر کا وزن ہے، صرف مدت نہیں۔

مدینہ میں ازواج کے حجروں میں رہیں، حدیث روایت کیں، 11ھ کے بعد نبی ﷺ کی بیوہ رہیں۔ مشہور روایت کے مطابق ربیع الاول 50ھ میں (کچھ 56ھ کہتے ہیں) مدینہ میں وفات، بقیع میں دفن۔ طبقات سالوں کا فرق لکھتے ہیں، مرتبہ پر نزاع نہیں۔

ان کا قصہ اس نمونے کے طور پر پڑھایا جاتا ہے کہ اسلام میں نکاح پوری قوم کو قید سے رشتہ داری تک کیسے اٹھا سکتا ہے۔ ذلت کی کہانی کے طور پر نہیں بتایا جاتا۔ جویریہ رضی اللہ عنہا ام المؤمنین، سردار کی بیٹی، اور ذکر والی خاتون کے طور پر محترم ہیں۔

یوں آٹھویں ماں مریسیع کی مصطلقی سردارزادی ہیں، جن کے نکاح نے قیدی آزاد کیے، جن کی زبان نے اللہ کو یاد کیا، اور جو تقریباً 50ھ میں مدینہ میں فوت ہوئیں۔ اللہ ان سے راضی ہو۔""",
    """जुवैरिया बिन्त अल-हारिस इब्न अबी दिरार رضي الله عنها बनू मुस्तलिक़ के सरदार की बेटी थीं, ख़ुज़ाआ की शाख़। शबान 5 हिजरी में, या इब्न इसहाक के मुताबिक 6 हिजरी—मसादिर एक साल का फ़र्क रखते हैं—ग़ज़वा अल-मुरैसी बनू मुस्तलिक़ से टकराया। वे क़ैदियों में थीं और साबित इब्न क़ैस के हिस्से में आईं। मुकातबा चाही, आज़ादी की क़ीमत, फिर नबी ﷺ के पास क़ीमत में मदद माँगीं।

आप ﷺ ने बेहतर बात कही: जो वाजिब है अदा करेंगे और निकाह करेंगे। उन्होंने क़ुबूल किया। नाम बर्रह था; आपने जुवैरिया रखा। जैसे ही उम्मुल मुमिनीन बनीं सहाबा ने कहा ये क़ैदी रसूलुल्लाह के ससुराल हैं। उनकी क़ौम के बहुत से—मशहूर शुमार में सौ या ज़्यादा—आज़ाद किए। बाद में कहतीं कोई औरत अपनी क़ौम के लिए मुझसे बड़ी बरकत न लाई। निकाह ने मैदान-ए-जंग को रिश्ता बना दिया।

उस इज़्ज़त के बाद बनू मुस्तलिक़ में इस्लाम फैला। वालिद हारिस के आने, बेटी इज़्ज़त से लेने, और इस्लाम लाने की मशहूर रिवायत है। चाहे उस आमद की हर तफ़सील एक जैसी क़वी न हो, सीरत इस पर मुत्तफ़िक़ है कि क़बीले की क़िस्मत इसलिए बदली कि एक औरत नबवी घर में आई। तालिब-ए-मग़ाज़ी मुरैसी को इस निकाह के साथ पढ़ते हैं, दो अलग कहानियाँ नहीं।

ज़िक्र-ए-कसीर से याद की गईं। मुस्लिम और सुनन उनसे फ़ज्र के बाद चार कलिमात की रिवायत लाते हैं—«सुब्हानल्लाह व बिहम्दिही अदद ख़लकिही...»—जो नबी ﷺ ने सिखाए, फ़रमाया उस सुबह की लंबी तस्बीह पर भारी हैं। उम्मत ने एक माँ से सीखा कि ज़िक्र का वज़न है, सिर्फ़ मुद्दत नहीं।

मदीना में अज़वाज के हुजरों में रहीं, हदीस रिवायत कीं, 11 हिजरी के बाद नबी ﷺ की विधवा रहीं। मशहूर रिवायत के मुताबिक रबीउल अव्वल 50 हिजरी में (कुछ 56 हिजरी कहते हैं) मदीना में वफ़ात, बक़ी' में दफ़न। तबाक़ात सालों का फ़र्क लिखते हैं, मर्तबे पर निज़ा नहीं।

उनका क़िस्सा इस नमूने के तौर पर पढ़ाया जाता है कि इस्लाम में निकाह पूरी क़ौम को क़ैद से रिश्तेदारी तक कैसे उठा सकता है। ज़िल्लत की कहानी के तौर पर नहीं बताया जाता। जुवैरिया رضي الله عنها उम्मुल मुमिनीन, सरदार की बेटी, और ज़िक्र वाली ख़ातून के तौर पर मोहतरम हैं।

यूँ आठवीं माँ मुरैसी की मुस्तलिकी सरदारज़ादी हैं, जिनके निकाह ने क़ैदी आज़ाद किए, जिनकी ज़बान ने अल्लाह को याद किया, और जो लगभग 50 हिजरी में मदीना में फ़ौत हुईं। अल्लाह उनसे राज़ी हो।""",
    """জুওয়াইরিয়াহ বিনত আল-হারিস ইবন আবি দিরাহ رضي الله عنها বনু মুস্তালিকের নেতার কন্যা ছিলেন, খুযাআর শাখা। শাবান ৫ হিজরিতে, বা ইবন ইসহাক অনুসারে ৬ হিজরিতে—উৎস এক বছরের ব্যবধান রাখে—আল-মুরাইসী অভিযান বনু মুস্তালিকের মুখোমুখি হয়। তিনি বন্দিদের মধ্যে ছিলেন এবং সাবিত ইবন কায়সের ভাগে পড়েন। তিনি মুকাতাবাহ চান, মুক্তির মূল্য, পরে নবী ﷺ-এর কাছে মূল্যে সাহায্য চান।

তিনি ﷺ উত্তম পথ দেন: যা বাকি আছে আদায় করবেন এবং বিয়ে করবেন। তিনি রাজি হন। নাম ছিল বাররাহ; তিনি জুওয়াইরিয়াহ রাখেন। উম্মুল মুমিনীন হওয়ামাত্র সাহাবিরা বলেন, এই বন্দিরা রাসূলুল্লাহর শ্বশুরবাড়ি। তাঁর গোত্রের অনেককে—প্রসিদ্ধ গণনায় একশ বা তার বেশি—মুক্ত করা হয়। পরে তিনি বলতেন তাঁর গোত্রের জন্য তাঁর চেয়ে বড় বরকত আর কোনো নারী আনেননি। বিবাহ যুদ্ধক্ষেত্রকে আত্মীয়তায় ঘোরায়।

সেই সম্মানের পর বনু মুস্তালিকে ইসলাম ছড়ায়। পিতা আল-হারিসের আসা, কন্যাকে মর্যাদায় নেওয়া, এবং ইসলাম গ্রহণের প্রসিদ্ধ বর্ণনা আছে। সেই আগমনের প্রতিটি বিবরণ সমান মজবুত না হলেও সিরাত একমত যে গোত্রের ভাগ্য বদলে কারণ এক নারী নববি ঘরে ঢোকেন। মাগাজির ছাত্র মুরাইসীকে এই বিবাহের সঙ্গে পড়ে, দুটি আলাদা গল্প নয়।

দীর্ঘ জিকিরে তিনি স্মরণীয়। মুসলিম ও সুনান তাঁর থেকে ফজরের পর চার বাক্যের বর্ণনা আনে—‘সুবহানাল্লাহি ওয়া বিহামদিহি আদাদা খালকিহি...’—যা নবী ﷺ শেখান, বলেন সেই সকালের দীর্ঘ তাসবিহের চেয়ে ভারী। উম্মাহ এক মাতার কাছ থেকে শেখে জিকিরের ওজন আছে, কেবল সময় নয়।

তিনি মদিনায় স্ত্রীদের হুজরায় থাকেন, হাদিস বর্ণনা করেন, ১১ হিজরির পর নবী ﷺ-এর বিধবা থাকেন। প্রসিদ্ধ বর্ণনায় রবিউল আউয়াল ৫০ হিজরিতে (কেউ ৫৬ হিজরি বলে) মদিনায় ওফাত, বাকীতে দাফন। তবাকাত বছরের পার্থক্য লেখে, মর্যাদায় বিবাদ নেই।

তাঁর কাহিনি এমন আদর্শ হিসেবে পড়ানো হয় যে ইসলামে বিবাহ কীভাবে পুরো গোত্রকে বন্দিদশা থেকে আত্মীয়তায় তুলতে পারে। অপমানের গল্প হিসেবে বলা হয় না। জুওয়াইরিয়াহ رضي الله عنها উম্মুল মুমিনীন, সরদারের কন্যা, এবং জিকিরের নারী হিসেবে সম্মানিত।

এভাবে অষ্টম মাতা মুরাইসীর মুস্তালিকি রাজকন্যা, যাঁর বিবাহ বন্দি মুক্ত করে, যাঁর জিহ্বা আল্লাহকে স্মরণ করে, এবং যিনি প্রায় ৫০ হিজরিতে মদিনায় ইন্তেকাল করেন। আল্লাহ তাঁর প্রতি সন্তুষ্ট হোন।""",
    """Juwairiyah binti al-Harits bin Abi Dirar radhiyallahu anha adalah putri pemuka Bani Mustaliq, cabang Khuza'ah. Pada Sya'ban 5 H, atau 6 H menurut Ibnu Ishaq—sumber berbeda satu tahun—ekspedisi al-Muraisi' bertemu Bani Mustaliq. Ia termasuk tawanan dan jatuh pada undian Tsabit bin Qais. Ia meminta mukatabah, kontrak membeli kemerdekaan, lalu datang kepada Nabi ﷺ memohon bantuan membayarnya.

Beliau ﷺ menawarkan jalan yang lebih baik: beliau akan membayar yang terutang dan menikahinya. Ia menerima. Namanya Barrah; beliau menamainya Juwairiyah. Begitu ia menjadi Ummul Mukminin, para sahabat berkata: tawanan ini adalah ipar Rasulullah. Mereka membebaskan banyak kaumnya—seratus atau lebih dalam hitungan terkenal. Ia kemudian berkata tidak ada wanita yang membawa berkah lebih besar kepada kaumnya daripada dirinya. Pernikahan itu memalingkan medan perang menjadi kekerabatan.

Islam tersebar di Bani Mustaliq setelah kehormatan itu. Ayahnya al-Harits dilaporkan datang, menerima putrinya dengan martabat, dan masuk Islam dalam kisah terkenal. Entah setiap rincian kunjungan itu sama kuatnya, sirah sepakat nasib suku berubah karena seorang wanita masuk rumah nabi. Penuntut maghazi membaca al-Muraisi' bersama nikah ini, bukan dua kisah terpisah.

Ia dikenang karena zikir yang panjang. Muslim dan sunan meriwayatkan darinya empat kalimat setelah Subuh—"Subhanallah wa bihamdihi, 'adada khalqihi..."—yang diajarkan Nabi ﷺ, beliau bersabda itu lebih berat daripada tasbih panjangnya pagi itu. Umat belajar dari seorang ibu bahwa zikir punya bobot, bukan hanya durasi.

Ia tinggal di Madinah di kamar di antara para istri, meriwayatkan hadis, dan tetap janda Nabi ﷺ setelah 11 H. Ia wafat pada Rabiul Awal 50 H menurut riwayat terkenal (sebagian mengatakan 56 H), di Madinah, dimakamkan di Baqi. Selisih tahun dicatat dalam thabaqat tanpa sengketa martabatnya.

Kisahnya diajarkan sebagai teladan bagaimana pernikahan dalam Islam dapat mengangkat seluruh suku dari tawanan kepada pertalian. Ia tidak diceritakan sebagai kisah kehinaan. Juwairiyah radhiyallahu anha dimuliakan sebagai Ummul Mukminin, putri pemuka, dan wanita zikir.

Dengan itu ibu kedelapan adalah putri Mustaliq dari al-Muraisi', yang nikahnya membebaskan tawanan, yang lidahnya mengingat Allah, dan yang wafat di Madinah sekitar 50 H. Semoga Allah meridainya.""",
)

c["items"][8]["details"] = D(
    """Umm Habibah, Ramlah bint Abi Sufyan ibn Harb رضي الله عنها, was the daughter of the Qurashi leader who for years headed the opposition in Makkah. She accepted Islam early, against her father's stance, and married Ubayd Allah ibn Jahsh. They migrated to Abyssinia in the second hijrah to the Negus. There Ubayd Allah left Islam for Christianity and later died. She remained Muslim in a foreign land, a widow far from her clan.

The Prophet ﷺ sent Amr ibn Umayyah al-Damri to al-Najashi to contract marriage with her while she was still in Abyssinia, around 6–7 AH. The Negus acted in the contract, gave a mahr of four hundred dinars in the famous report, and Khalid ibn Sa'id ibn al-As stood as wali. She came to Madinah with those who returned from Abyssinia after Khaybar in 7 AH. The Messenger ﷺ had married her by proxy across the sea; she entered Madinah already Mother of the Believers.

Her father Abu Sufyan visited Madinah after Hudaybiyyah, before his own Islam. She is reported to have folded up the Prophet's mattress so that a mushrik would not sit on it. The scene, preserved in the seerah, shows a daughter's iman standing even before a powerful father. Abu Sufyan accepted Islam at the Conquest of Makkah in 8 AH. The marriage had already linked the house of Harb to the Prophet ﷺ.

She narrated hadith, lived in a chamber by the mosque, and remained in Madinah after the wafat. She was the sister of Mu'awiyah. Sunni historians mention that kinship without turning her story into later political argument. She died in Madinah around 44 AH according to the well-known report used in this chapter, and was buried in al-Baqi'. Other dates appear in some tabaqat; 44 AH is the figure commonly taught with her notice.

The wisdom of the marriage is clear in the maghazi: a believing woman stranded after her husband's apostasy was honoured by the most honourable of men, and a door was opened toward a household that had long fought the da'wah. It is told with respect for her sabr in Abyssinia, not as a worldly bargain.

She never returned to idolatry when her husband did. That steadfastness is why the Negus's court is part of her seerah and why her name is Ramlah in the genealogies and Umm Habibah in the household.

Thus the ninth Mother is the daughter of Abu Sufyan, early Muslim, emigrant to Abyssinia, widow after apostasy and death, married through the Negus, who died in Madinah about 44 AH. May Allah be pleased with her.""",
    """ام حبیبہ، رملہ بنت ابی سفیان بن حرب رضی اللہ عنہا، اس قریشی سردار کی بیٹی تھیں جو برسوں مکہ میں مخالفت کی قیادت کرتا رہا۔ والد کے موقف کے خلاف جلد اسلام لائیں اور عبید اللہ بن جحش سے نکاح ہوا۔ دوسرے حبشہ ہجرت میں نجاشی کے پاس گئیں۔ وہاں عبید اللہ نے اسلام چھوڑ کر عیسائیت اختیار کی اور بعد میں فوت ہوئے۔ وہ اجنبی ملک میں مسلمان بیوہ رہیں، اپنے قبیلے سے دور۔

نبی ﷺ نے عمرو بن امیہ ضمری کو نجاشی کے پاس بھیجا کہ ابھی حبشہ میں ہیں تو نکاح ہو جائے، تقریباً 6–7ھ۔ نجاشی نے عقد میں کام کیا، مشہور روایت میں چار سو دینار مہر دیا، خالد بن سعید بن العاص ولی رہے۔ 7ھ میں خیبر کے بعد حبشہ سے لوٹنے والوں کے ساتھ مدینہ آئیں۔ رسول ﷺ نے سمندر پار وکالت سے نکاح کیا تھا؛ مدینہ میں ام المؤمنین بن کر داخل ہوئیں۔

والد ابو سفیان حدیبیہ کے بعد، اپنے اسلام سے پہلے، مدینہ آئے۔ روایت ہے انہوں نے نبی ﷺ کی بچھاون سمیٹ لی تاکہ مشرک اس پر نہ بیٹھے۔ سیرت میں محفوظ یہ منظر دکھاتا ہے کہ بیٹی کا ایمان طاقتور باپ سے پہلے کھڑا رہا۔ ابو سفیان 8ھ میں فتح مکہ پر اسلام لائے۔ نکاح پہلے ہی حرب کے گھر کو نبی ﷺ سے جوڑ چکا تھا۔

حدیث روایت کیں، مسجد سے ملے حجرے میں رہیں، وفات کے بعد مدینہ میں ٹھہریں۔ معاویہ کی بہن تھیں۔ اہل سنت کے مورخ اس رشتے کا ذکر کرتے ہیں بغیر ان کے قصے کو بعد کی سیاست کا مقدمہ بنائے۔ اس باب کی معروف خبر کے مطابق تقریباً 44ھ میں مدینہ میں وفات، بقیع میں دفن۔ طبقات میں اور تاریخیں بھی ہیں؛ 44ھ ان کے ترجمہ کے ساتھ عام پڑھا جاتا ہے۔

نکاح کی حکمت مغازی میں صاف ہے: شوہر کی ارتداد کے بعد اٹکی مؤمنہ کو سب سے معزز انسان نے عزت دی، اور اس گھر کی طرف دروازہ کھلا جو دیر سے دعوت سے لڑتا رہا۔ حبشہ میں ان کے صبر کے ادب سے بتایا جاتا ہے، دنیاوی سودے کے طور پر نہیں۔

شوہر کے پھرنے پر وہ بت پرستی کی طرف نہ لوٹیں۔ وہی استقامت ہے جس لیے نجاشی کا دربار ان کی سیرت کا حصہ ہے اور نام نسب میں رملہ اور گھر میں ام حبیبہ ہے۔

یوں نویں ماں ابو سفیان کی صاحبزادی ہیں، اولین مسلم، حبشہ کی مہاجر، ارتداد و موت کے بعد بیوہ، نجاشی کے ذریعے نکاح، تقریباً 44ھ میں مدینہ میں وفات۔ اللہ ان سے راضی ہو۔""",
    """उम्म हबीबा, रमला बिन्त अबी सुफ़्यान इब्न हर्ब رضي الله عنها, उस कुरैशी सरदार की बेटी थीं जो बरसों मक्का में मुख़ालफ़त की क़ियादत करता रहा। वालिद के मौक़िफ़ के ख़िलाफ़ जल्दी इस्लाम लाईं और उबैदुल्लाह इब्न जह्श से निकाह हुआ। दूसरी हबशा हिजरत में नजाशी के पास गईं। वहाँ उबैदुल्लाह ने इस्लाम छोड़कर ईसाइयत इख़्तियार की और बाद में फ़ौत हुए। वे अजनबी मुल्क में मुसलमान विधवा रहीं, अपने क़बीले से दूर।

नबी ﷺ ने अम्र इब्न उमैया दमरी को नजाशी के पास भेजा कि अभी हबशा में हैं तो निकाह हो जाए, लगभग 6–7 हिजरी। नजाशी ने अक़द में काम किया, मशहूर रिवायत में चार सौ दीनार महर दिया, ख़ालिद इब्न सईद इब्न अल-आस वली रहे। 7 हिजरी में ख़ैबर के बाद हबशा से लौटने वालों के साथ मदीना आईं। रसूल ﷺ ने समुंदर पार वकालत से निकाह किया था; मदीना में उम्मुल मुमिनीन बनकर दाख़िल हुईं।

वालिद अबू सुफ़्यान हुदैबिया के बाद, अपने इस्लाम से पहले, मदीना आए। रिवायत है उन्होंने नबी ﷺ की बिछावन समेट ली ताकि मुशरिक उस पर न बैठे। सीरत में महफ़ूज़ यह मंज़र दिखाता है कि बेटी का ईमान ताक़तवर बाप से पहले खड़ा रहा। अबू सुफ़्यान 8 हिजरी में फ़त्हे मक्का पर इस्लाम लाए। निकाह पहले ही हर्ब के घर को नबी ﷺ से जोड़ चुका था।

हदीस रिवायत कीं, मस्जिद से जुड़े हुजरे में रहीं, वफ़ात के बाद मदीना में ठहरीं। मुआविया की बहन थीं। अहले सुन्नत के मुअर्रिख इस रिश्ते का ज़िक्र करते हैं बिना उनके क़िस्से को बाद की सियासत का मुक़द्दमा बनाए। इस बाब की मा'रूफ़ ख़बर के मुताबिक लगभग 44 हिजरी में मदीना में वफ़ात, बक़ी' में दफ़न। तबाक़ात में और तारीख़ें भी हैं; 44 हिजरी उनके तरजमे के साथ आम पढ़ा जाता है।

निकाह की हिकमत मग़ाज़ी में साफ़ है: शौहर की इर्तदाद के बाद अटकी मोमिना को सबसे मोअज़्ज़ज़ इंसान ने इज़्ज़त दी, और उस घर की तरफ़ दरवाज़ा खुला जो देर से दावत से लड़ता रहा। हबशा में उनके सब्र के अदब से बताया जाता है, दुनियावी सौदे के तौर पर नहीं।

शौहर के फिरने पर वे बुतपरस्ती की तरफ़ न लौटीं। वही इस्तिक़ामत है जिसकी वजह से नजाशी का दरबार उनकी सीरत का हिस्सा है और नाम नसब में रमला और घर में उम्म हबीबा है।

यूँ नौवीं माँ अबू सुफ़्यान की साहिबज़ादी हैं, अव्वलीन मुस्लिम, हबशा की मुहाजिर, इर्तदाद व मौत के बाद विधवा, नजाशी के ज़रिए निकाह, लगभग 44 हिजरी में मदीना में वफ़ात। अल्लाह उनसे राज़ी हो।""",
    """উম্মু হাবিবাহ, রামলাহ বিনত আবি সুফিয়ান ইবন হারব رضي الله عنها, সেই কুরাইশি নেতার কন্যা যাঁর নেতৃত্বে বছরের পর বছর মক্কায় বিরোধিতা চলে। পিতার অবস্থানের বিরুদ্ধে তিনি আগেই ইসলাম গ্রহণ করেন এবং উবায়দুল্লাহ ইবন জাহশকে বিয়ে করেন। তাঁরা দ্বিতীয় হিজরতে নাজাশির কাছে হাবশায় যান। সেখানে উবায়দুল্লাহ ইসলাম ছেড়ে খ্রিস্টধর্ম গ্রহণ করেন এবং পরে মারা যান। তিনি বিদেশে মুসলিম বিধবা থাকেন, গোত্র থেকে দূরে।

নবী ﷺ আমর ইবন উমাইয়াহ আদ-দামরিকে নাজাশির কাছে পাঠান যেন তিনি এখনও হাবশায় থাকতে বিবাহ সম্পন্ন হয়, প্রায় ৬–৭ হিজরি। নাজাশি আকদে কাজ করেন, প্রসিদ্ধ বর্ণনায় চারশ দিনার মোহর দেন, খালিদ ইবন সাঈদ ইবন আল-আস অভিভাবক থাকেন। ৭ হিজরিতে খাইবারের পর হাবশা থেকে ফেরাদের সঙ্গে তিনি মদিনায় আসেন। রাসূল ﷺ সমুদ্র পেরিয়ে প্রক্সি আকদ করেছিলেন; তিনি উম্মুল মুমিনীন হয়ে মদিনায় প্রবেশ করেন।

পিতা আবু সুফিয়ান হুদায়বিয়ার পর, নিজ ইসলামের আগে, মদিনায় আসেন। বর্ণনায় তিনি নবীর বিছানা গুটিয়ে নেন যাতে মুশরিক তাতে না বসে। সিরাতে রক্ষিত এই দৃশ্য দেখায় কন্যার ঈমান শক্তিশালী পিতার আগে দাঁড়ায়। আবু সুফিয়ান ৮ হিজরিতে মক্কা বিজয়ে ইসলাম গ্রহণ করেন। বিবাহ ইতোমধ্যে হারবের ঘরকে নবী ﷺ-এর সঙ্গে যুক্ত করেছে।

তিনি হাদিস বর্ণনা করেন, মসজিদের পাশের হুজরায় থাকেন, ওফাতের পর মদিনায় থাকেন। তিনি মুআবিয়ার বোন। সুন্নি ঐতিহাসিকরা সেই আত্মীয়তার উল্লেখ করেন তাঁর কাহিনিকে পরবর্তী রাজনীতির মামলা না বানিয়ে। এই অধ্যায়ে ব্যবহৃত প্রসিদ্ধ বর্ণনায় তিনি প্রায় ৪৪ হিজরিতে মদিনায় ইন্তেকাল করেন, বাকীতে দাফন। তবাকাতে অন্য তারিখও আছে; ৪৪ হিজরি তাঁর পরিচিতির সঙ্গে সাধারণত পড়ানো হয়।

বিবাহের হিকমত মাগাজিতে স্পষ্ট: স্বামীর ধর্মত্যাগের পর আটকে পড়া মুমিনাকে সর্বাধিক সম্মানিত মানুষ সম্মান দেন, এবং সেই ঘরের দিকে দরজা খোলে যা দীর্ঘকাল দাওয়াতের সঙ্গে লড়েছে। হাবশায় তাঁর সবরের আদব রেখে বলা হয়, পার্থিব চুক্তি হিসেবে নয়।

স্বামী ফিরে গেলে তিনি মূর্তিপূজায় ফিরে যাননি। সেই অটলতাই নাজাশির দরবারকে তাঁর সিরাতের অংশ করে এবং নাম বংশে রামলাহ ও ঘরে উম্মু হাবিবাহ।

এভাবে নবম মাতা আবু সুফিয়ানের কন্যা, প্রথম যুগের মুসলিম, হাবশার মুহাজির, ধর্মত্যাগ ও মৃত্যুর পর বিধবা, নাজাশির মাধ্যমে বিবাহিত, প্রায় ৪৪ হিজরিতে মদিনায় ওফাত। আল্লাহ তাঁর প্রতি সন্তুষ্ট হোন।""",
    """Ummu Habibah, Ramlah binti Abu Sufyan bin Harb radhiyallahu anha, adalah putri pemimpin Quraisy yang bertahun-tahun mengepalai penentangan di Makkah. Ia masuk Islam lebih awal, menentang sikap ayahnya, dan menikah dengan Ubaidullah bin Jahsy. Mereka berhijrah ke Habasyah pada hijrah kedua kepada Najasyi. Di sana Ubaidullah meninggalkan Islam menuju Nasrani lalu meninggal. Ia tetap muslimah di negeri asing, janda jauh dari sukunya.

Nabi ﷺ mengutus Amr bin Umayyah ad-Damri kepada Najasyi untuk mengakadkannya sementara ia masih di Habasyah, sekitar 6–7 H. Najasyi bertindak dalam akad, memberi mahar empat ratus dinar dalam riwayat terkenal, dan Khalid bin Sa'id bin al-As menjadi wali. Ia tiba di Madinah bersama yang pulang dari Habasyah setelah Khaibar tahun 7 H. Rasulullah ﷺ menikahinya secara wakil menyeberangi laut; ia memasuki Madinah sudah sebagai Ummul Mukminin.

Ayahnya Abu Sufyan mengunjungi Madinah setelah Hudaibiyah, sebelum Islamnya sendiri. Ia dilaporkan menggulung tilam Nabi agar seorang musyrik tidak duduk di atasnya. Adegan yang tersimpan dalam sirah itu menunjukkan iman seorang putri berdiri bahkan di hadapan ayah yang berkuasa. Abu Sufyan masuk Islam pada Fathu Makkah tahun 8 H. Pernikahan sudah mengikat rumah Harb kepada Nabi ﷺ.

Ia meriwayatkan hadis, tinggal di kamar di sisi masjid, dan tetap di Madinah setelah wafat. Ia saudara Muawiyah. Sejarawan Ahlus Sunnah menyebut kekerabatan itu tanpa mengubah kisahnya menjadi argumen politik belakangan. Ia wafat di Madinah sekitar 44 H menurut riwayat terkenal yang dipakai bab ini, dimakamkan di Baqi. Tanggal lain muncul dalam sebagian thabaqat; 44 H adalah angka yang umum diajarkan bersama biografnya.

Hikmah pernikahan itu jelas dalam maghazi: wanita beriman yang terdampar setelah suaminya murtad dimuliakan oleh manusia paling mulia, dan sebuah pintu terbuka menuju rumah tangga yang lama memerangi dakwah. Ia diceritakan dengan hormat kepada kesabarannya di Habasyah, bukan sebagai tawar-menawar duniawi.

Ia tidak kembali kepada berhala ketika suaminya kembali. Keteguhan itulah mengapa istana Najasyi menjadi bagian sirahnya dan mengapa namanya Ramlah dalam nasab dan Ummu Habibah dalam rumah tangga.

Dengan itu ibu kesembilan adalah putri Abu Sufyan, muslimah awal, muhajirah ke Habasyah, janda setelah kemurtadan dan kematian, dinikahi melalui Najasyi, yang wafat di Madinah sekitar 44 H. Semoga Allah meridainya.""",
)

c["items"][9]["details"] = D(
    """Safiyyah bint Huyayy ibn Akhtab رضي الله عنها was of Banu Nadir. Her father Huyayy was a chief of that tribe; her mother was of Banu Qurayza. The family traced nobility to Harun ﷺ. After Banu Nadir were expelled from Madinah in 4 AH they settled at Khaybar. She had been married, lastly to Kinana ibn al-Rabi'. In 7 AH / 628 CE the Prophet ﷺ marched on Khaybar. After the fortress fell she was among those taken; Dihyah al-Kalbi had a share, then the Messenger ﷺ took her, freed her, and married her, making her manumission her mahr.

She accepted Islam. On the return from Khaybar the marriage was established at a halt such as Sahba'. He ﷺ treated her as a wife, not as a captive kept in humiliation. When other wives, in a moment of human jealousy, alluded to her Jewish origin, he taught her to answer with dignity: her father was Harun, her uncle Musa ﷺ, and her husband Muhammad ﷺ. That lesson is in the sunan and is the Sunni way of speaking about her lineage.

He honoured her on the road and in the house. Reports of his making a knee for her to mount, and of his anger at any insult to her, belong to the adab of the Mothers. She prayed, fasted, and lived among the chambers by the mosque. The Ummah is forbidden to revive the scorn that the Prophet ﷺ himself put down.

Khaybar's aftermath included treaties, dates as tribute, and the opening of the north. Her nikah is part of that chapter of maghazi: a daughter of Huyayy ibn Akhtab entered the prophetic household after war, in peace, as Mother of the Believers. Seerah does not ask the reader to hate her father's memory as a licence to hate her; she is honoured in her own iman.

She narrated hadith and remained in Madinah after 11 AH. She died around 50 AH (some say 52 AH) in the time of Mu'awiyah, and was buried in al-Baqi'. The tabaqat record her as Safiyyah bint Huyayy, Umm al-Mu'minin.

Thus the tenth Mother is the Nadiri daughter of Huyayy, taken at Khaybar, freed and married, taught to invoke Harun and Musa ﷺ with honour, who died in Madinah about 50 AH. May Allah be pleased with her.""",
    """صفیہ بنت حیي بن اخطب رضی اللہ عنہا بنو نضیر سے تھیں۔ والد حیي اس قبیلے کے سردار تھے؛ والدہ بنو قریظہ سے۔ خاندان ہارون ﷺ کی شرافت سے جڑا تھا۔ 4ھ میں بنو نضیر مدینہ سے نکالے جانے کے بعد خیبر بसे। شادی شدہ رہ چکی تھیں، آخر میں کنانہ بن الربیع سے۔ 7ھ / 628ء میں نبی ﷺ خیبر گئے۔ قلعہ گرنے کے بعد قید ہوئیں؛ دحیہ کلبی کا حصہ تھا، پھر رسول ﷺ نے لیا، آزاد کیا، نکاح کیا، آزادی کو مہر بنایا۔

اسلام قبول کیا۔ خیبر سے واپسی پر مقام جیسے صہباء میں گھر آباد ہوا۔ آپ ﷺ نے زوجہ کی طرح رکھا، ذلیل قیدی کی طرح نہیں۔ جب اور ازواج نے انسانی غیرت میں یہودی اصل کی طرف اشارہ کیا تو سکھایا عزت سے جواب دیں: والد ہارون، چچا موسیٰ ﷺ، شوہر محمد ﷺ۔ یہ سبق سنن میں ہے اور اہل سنت ان کے نسب پر اسی ادب سے بات کرتے ہیں۔

راستے اور گھر میں عزت کی۔ سوار ہونے کے لیے گھٹنا دینے، اور کسی توہین پر ناراضگی کی روایات امهات کے ادب سے ہیں۔ نماز، روزہ، مسجد سے ملے حجروں میں زندگی۔ امت کو وہ تحقیر زندہ کرنے سے منع ہے جو نبی ﷺ نے خود دبا دی۔

خیبر کے بعد معاہدے، خراج کی کھجوریں، اور شمال کا کھلنا ہے۔ ان کا نکاح مغازی کے اسی باب کا حصہ ہے: حیي بن اخطب کی بیٹی جنگ کے بعد امن میں نبوی گھر میں ام المؤمنین بن کر آئیں۔ سیرت قاری سے نہیں کہتی کہ والد کی یاد سے نفرت ان سے نفرت کا جواز ہو؛ وہ اپنے ایمان میں محترم ہیں۔

حدیث روایت کیں، 11ھ کے بعد مدینہ میں رہیں۔ تقریباً 50ھ (کچھ 52ھ) معاویہ کے دور میں وفات، بقیع میں دفن۔ طبقات انہیں صفیہ بنت حیي، ام المؤمنین لکھتے ہیں۔

یوں دسویں ماں نضیری بیٹی حیي کی ہیں، خیبر پر قید پھر آزاد و منکوحہ، ہارون و موسیٰ ﷺ کو عزت سے یاد سکھائی گئی، تقریباً 50ھ میں مدینہ میں وفات۔ اللہ ان سے راضی ہو۔""",
    """सफ़िया बिन्त हुयय इब्न अख़्तब رضي الله عنها बनू नज़ीर से थीं। वालिद हुयय उस क़बीले के सरदार थे; वालिदा बनू क़ुराइज़ा से। ख़ानदान हारून ﷺ की शराफ़त से जुड़ा था। 4 हिजरी में बनू नज़ीर मदीना से निकाले जाने के बाद ख़ैबर बसे। शादीशुदा रह चुकी थीं, आख़िर में किनाना इब्न अल-रबीअ से। 7 हिजरी / 628 ई. में नबी ﷺ ख़ैबर गए। क़िला गिरने के बाद क़ैद हुईं; दिह्या कलबी का हिस्सा था, फिर रसूल ﷺ ने लिया, आज़ाद किया, निकाह किया, आज़ादी को महर बनाया।

इस्लाम क़ुबूल किया। ख़ैबर से वापसी पर मक़ाम जैसे सहबा में घर आबाद हुआ। आप ﷺ ने ज़ौजा की तरह रखा, ज़लील क़ैदी की तरह नहीं। जब और अज़वाज ने इंसानी ग़ैरत में यहूदी असल की तरफ़ इशारा किया तो सिखाया इज़्ज़त से जवाब दें: वालिद हारून, चाचा मूसा ﷺ, शौहर मुहम्मद ﷺ। यह सबक़ सुनन में है और अहले सुन्नत उनके नसब पर इसी अदब से बात करते हैं।

रास्ते और घर में इज़्ज़त की। सवार होने के लिए घुटना देने, और किसी तोहीन पर नाराज़गी की रिवायात उम्महात के अदब से हैं। नमाज़, रोज़ा, मस्जिद से जुड़े हुजरों में ज़िंदगी। उम्मत को वह तहक़ीर ज़िंदा करने से मना है जो नबी ﷺ ने ख़ुद दबा दी।

ख़ैबर के बाद मुआहदे, ख़िराज की खजूरें, और शिमाल का खुलना है। उनका निकाह मग़ाज़ी के उसी बाब का हिस्सा है: हुयय इब्न अख़्तब की बेटी जंग के बाद अमन में नबवी घर में उम्मुल मुमिनीन बनकर आईं। सीरत क़ारी से नहीं कहती कि वालिद की याद से नफ़रत उनसे नफ़रत का जवाज़ हो; वे अपने ईमान में मोहतरम हैं।

हदीस रिवायत कीं, 11 हिजरी के बाद मदीना में रहीं। लगभग 50 हिजरी (कुछ 52 हिजरी) मुआविया के दौर में वफ़ात, बक़ी' में दफ़न। तबाक़ात उन्हें सफ़िया बिन्त हुयय, उम्मुल मुमिनीन लिखते हैं।

यूँ दसवीं माँ नज़ीरी बेटी हुयय की हैं, ख़ैबर पर क़ैद फिर आज़ाद व मन्कूहा, हारून व मूसा ﷺ को इज़्ज़त से याद सिखाई गई, लगभग 50 हिजरी में मदीना में वफ़ात। अल्लाह उनसे राज़ी हो।""",
    """সাফিয়্যাহ বিনত হুয়াইয়্য ইবন আখতাব رضي الله عنها বনু নাদির থেকে ছিলেন। পিতা হুয়াইয়্য সেই গোত্রের নেতা; মাতা বনু কুরাইজা থেকে। পরিবার হারুন ﷺ-এর সম্ভ্রান্ত ধারায় যুক্ত। ৪ হিজরিতে বনু নাদির মদিনা থেকে বিতাড়িত হওয়ার পর খাইবারে বসতি করে। তিনি বিবাহিত ছিলেন, শেষে কিনানাহ ইবন আর-রাবির সঙ্গে। ৭ হিজরি / ৬২৮ খ্রি. নবী ﷺ খাইবার অভিযান করেন। দুর্গ পতনের পর তিনি বন্দি হন; দিহইয়াহ আল-কালবির ভাগ ছিল, পরে রাসূল ﷺ তাঁকে নেন, মুক্ত করেন, বিয়ে করেন, মুক্তিকে মোহর করেন।

তিনি ইসলাম গ্রহণ করেন। খাইবার থেকে ফেরার পথে সাহবা প্রভৃতি বিরতিতে ঘর প্রতিষ্ঠিত হয়। তিনি ﷺ তাঁকে স্ত্রী হিসেবে রাখেন, লাঞ্ছিত বন্দি হিসেবে নয়। অন্য স্ত্রীগণ মানবিক ঈর্ষায় তাঁর ইহুদি উৎসের ইঙ্গিত করলে তিনি শেখান মর্যাদায় উত্তর দিতে: পিতা হারুন, চাচা মূসা ﷺ, স্বামী মুহাম্মদ ﷺ। এই শিক্ষা সুনানে আছে এবং সুন্নি পন্থা তাঁর বংশ নিয়ে এই আদবেই কথা বলে।

পথে ও ঘরে তিনি সম্মান করেন। আরোহণের জন্য হাঁটু দেওয়া, এবং কোনো অপমানে অসন্তোষের বর্ণনা উম্মাহাতের আদবের অংশ। সালাত, সিয়াম, মসজিদের পাশের হুজরায় জীবন। উম্মাহ সেই অবজ্ঞা পুনর্জীবিত করতে নিষিদ্ধ যা নবী ﷺ নিজে দমন করেছেন।

খাইবারের পরিণতিতে সন্ধি, কর হিসেবে খেজুর, এবং উত্তরের উন্মোচন। তাঁর বিবাহ মাগাজির সেই অধ্যায়ের অংশ: হুয়াইয়্য ইবন আখতাবের কন্যা যুদ্ধের পর শান্তিতে নববি ঘরে উম্মুল মুমিনীন হয়ে আসেন। সিরাত পাঠককে বলে না পিতার স্মৃতির প্রতি ঘৃণা যেন তাঁর প্রতি ঘৃণার লাইসেন্স হয়; তিনি নিজ ঈমানে সম্মানিতা।

তিনি হাদিস বর্ণনা করেন, ১১ হিজরির পর মদিনায় থাকেন। প্রায় ৫০ হিজরিতে (কেউ ৫২ হিজরি বলে) মুআবিয়ার সময়ে ওফাত, বাকীতে দাফন। তবাকাত তাঁকে সাফিয়্যাহ বিনত হুয়াইয়্য, উম্মুল মুমিনীন লেখে।

এভাবে দশম মাতা নাদিরি কন্যা হুয়াইয়্যের, খাইবারে বন্দি পরে মুক্ত ও বিবাহিতা, হারুন ও মূসা ﷺ-কে সম্মানে স্মরণ করতে শেখানো, প্রায় ৫০ হিজরিতে মদিনায় ওফাত। আল্লাহ তাঁর প্রতি সন্তুষ্ট হোন।""",
    """Safiyyah binti Huyay bin Akhthab radhiyallahu anha berasal dari Bani Nadir. Ayahnya Huyay adalah pemuka suku itu; ibunya dari Bani Quraizah. Keluarga menelusuri kemuliaan kepada Harun ﷺ. Setelah Bani Nadir diusir dari Madinah tahun 4 H mereka menetap di Khaibar. Ia pernah menikah, terakhir dengan Kinanah bin ar-Rabi'. Pada 7 H / 628 M Nabi ﷺ berangkat ke Khaibar. Setelah benteng jatuh ia termasuk yang ditawan; Dihyah al-Kalbi mendapat bagian, lalu Rasulullah ﷺ mengambilnya, memerdekakannya, dan menikahinya, menjadikan kemerdekaan itu maharnya.

Ia masuk Islam. Dalam perjalanan pulang dari Khaibar, rumah tangga ditegakkan di persinggahan seperti Sahba'. Beliau ﷺ memperlakukannya sebagai istri, bukan tawanan yang dihinakan. Ketika istri lain, dalam cemburu manusiawi, menyinggung asal Yahudinya, beliau mengajarinya menjawab dengan martabat: ayahnya Harun, pamannya Musa ﷺ, suaminya Muhammad ﷺ. Pelajaran itu ada dalam sunan dan itulah cara Ahlus Sunnah berbicara tentang nasabnya.

Beliau memuliakannya di jalan dan di rumah. Riwayat beliau berlutut agar ia naik kendaraan, dan kemarahan beliau atas penghinaan kepadanya, termasuk adab para ibu. Ia salat, puasa, dan tinggal di antara kamar di sisi masjid. Umat dilarang menghidupkan cemooh yang telah Nabi ﷺ sendiri padamkan.

Akibat Khaibar meliputi perjanjian, kurma sebagai upeti, dan terbukanya utara. Nikahnya bagian dari bab maghazi itu: putri Huyay bin Akhthab masuk rumah nabi setelah perang, dalam damai, sebagai Ummul Mukminin. Sirah tidak meminta pembaca membenci ingatan ayahnya sebagai izin membencinya; ia dimuliakan dalam imannya sendiri.

Ia meriwayatkan hadis dan tetap di Madinah setelah 11 H. Ia wafat sekitar 50 H (sebagian mengatakan 52 H) pada masa Muawiyah, dimakamkan di Baqi. Thabaqat mencatatnya sebagai Safiyyah binti Huyay, Ummul Mukminin.

Dengan itu ibu kesepuluh adalah putri Nadir anak Huyay, ditawan di Khaibar, dimerdekakan lalu dinikahi, diajari menyebut Harun dan Musa ﷺ dengan hormat, yang wafat di Madinah sekitar 50 H. Semoga Allah meridainya.""",
)

c["items"][10]["details"] = D(
    """Maymunah bint al-Harith al-Hilaliyyah رضي الله عنها was the last woman the Prophet ﷺ married. Her name had been Barrah; he named her Maymunah, blessed. She was the sister of Umm al-Fadl Lubabah, wife of al-Abbas ibn Abd al-Muttalib, and thus maternal aunt of Abdullah ibn Abbas رضي الله عنهما. Through the sisters of that Hilali house she was also tied to other great Companions. Al-Abbas took part in arranging the marriage.

The nikah was in Dhul Qa'dah 7 AH / 629 CE at Sarif, some miles from Makkah, after umrah al-qada'—the made-up umrah of the year after Hudaybiyyah. Whether he ﷺ was in ihram at the moment of contract is a famous fiqh difference: Ibn Abbas reported that he was; others reported that he was halal. The seerah records both, without turning the Mother into a dispute. What is agreed is that this was the last marriage and that it took place on that blessed journey.

Some reports say she offered herself (in the light of 33:50); others that the proposal came through her sister and al-Abbas. Both tellings keep her dignity. She entered the household in Madinah and lived in a chamber among the wives. Ibn Abbas, her nephew, narrated much from her—ritual washing, ihram, and household sunnah—so her knowledge travelled with the tafsir of the Qur'an's most famous student among the youth of Banu Hashim.

She was known for piety and remained in Madinah after the wafat, without remarrying. Toward the end of her life she went toward Makkah. She died at Sarif around 51 AH (other notices say 49 or later), at the same halt where she had married him ﷺ, and was buried there. Ibn Abbas led the funeral. Travellers on the Makkan road still hear her name at that place.

With Maymunah the customary list of the Mothers who were wives in this chapter is complete. After 7 AH no further marriage is counted among them. The household of the Ummahat was then full: widows of Makkah and Madinah, daughters of friends and of former enemies, a cousin married by revelation, and this last Hilali aunt of Ibn Abbas.

Sunni seerah closes her notice with the tenderness of a circle: the last marriage and the last roadside grave of a Mother, both at Sarif. May Allah be pleased with her.""",
    """میمونہ بنت الحارث ہلالیہ رضی اللہ عنہا آخری خاتون ہیں جن سے نبی ﷺ نے نکاح کیا۔ نام برہ تھا؛ آپ نے میمونہ رکھا، بابرکت۔ ام الفضل لبابہ کی بہن تھیں جو عباس بن عبد المطلب کی بیوی تھیں، پس عبد اللہ بن عباس رضی اللہ عنہما کی خالہ۔ اس ہلالی گھر کی بہنوں کے ذریعے اور بڑے صحابہ سے بھی جڑیں۔ عباس نے نکاح کی ترتیب میں حصہ لیا۔

نکاح ذی القعدہ 7ھ / 629ء میں سرف پر ہوا، مکہ سے چند میل، عمرہ القضاء کے بعد—حدیبیہ کے اگلے سال کا پورا کیا گیا عمرہ۔ عقد کے وقت آپ ﷺ احرام میں تھے یا نہیں مشہور فقہی اختلاف ہے: ابن عباس نے احرام کی خبر دی؛ اوروں نے حلال ہونے کی۔ سیرت دونوں رکھتی ہے، ماں کو نزاع نہیں بناتی۔ متفق علیہ یہ ہے کہ یہ آخری نکاح تھا اور اسی مبارک سفر پر ہوا۔

کچھ روایات میں انہوں نے اپنے آپ کو پیش کیا (33:50 کی روشنی میں)؛ کچھ میں پیغام بہن اور عباس کے ذریعے آیا۔ دونوں بیان ان کی عزت رکھتے ہیں۔ مدینہ کے گھر میں آئیں اور ازواج کے حجروں میں رہیں۔ بھتیجے ابن عباس نے ان سے بہت روایت کی—غسل، احرام، گھریلو سنت—چنانچہ ان کا علم بنو ہاشم کے جوانوں میں قرآن کے سب سے مشہور شاگرد کی تفسیر کے ساتھ چلا۔

تقویٰ سے پہچانی گئیں، وفات کے بعد مدینہ میں رہیں، دوبارہ نکاح نہ کیا۔ زندگی کے آخر میں مکہ رخ کیا۔ تقریباً 51ھ میں (اور خبریں 49 یا بعد) سرف میں وفات، اسی مقام پر جہاں نکاح ہوا تھا، وہیں دفن۔ ابن عباس نے جنازہ پڑھایا۔ مکی راستے کے مسافر اب بھی وہاں ان کا نام سنتے ہیں۔

میمونہ کے ساتھ اس باب میں ازواج امہات کی معروف فہرست مکمل ہوتی ہے۔ 7ھ کے بعد ان میں مزید نکاح شمار نہیں ہوتا۔ امہات کا گھر تب بھرا تھا: مکہ و مدینہ کی بیوائیں، دوستوں اور پرانے دشمنوں کی بیٹیاں، وحی سے نکاح شدہ پھوپھی زاد، اور ابن عباس کی یہ آخری ہلالی خالہ۔

اہل سنت کی سیرت ان کے ترجمہ کو دائرے کی نرمی سے بند کرتی ہے: آخری نکاح اور ماں کی آخری راہ کنار کی قبر، دونوں سرف میں۔ اللہ ان سے راضی ہو۔""",
    """मैमूना बिन्त अल-हारिस हिलालिया رضي الله عنها आख़िरी ख़ातून हैं जिनसे नबी ﷺ ने निकाह किया। नाम बर्रह था; आपने मैमूना रखा, बाबरकत। उम्म अल-फ़ज़्ल लुबाबा की बहन थीं जो अब्बास इब्न अब्दुल मुत्तलिब की बीवी थीं, पस अब्दुल्लाह इब्न अब्बास رضي الله عنهما की ख़ाला। उस हिलाली घर की बहनों के ज़रिए और बड़े सहाबा से भी जुड़ीं। अब्बास ने निकाह की तरतीब में हिस्सा लिया।

निकाह ज़ुल क़ादा 7 हिजरी / 629 ई. में सरिफ़ पर हुआ, मक्का से चंद मील, उमरा अल-क़ज़ा के बाद—हुदैबिया के अगले साल का पूरा किया गया उमरा। अक़द के वक़्त आप ﷺ इहराम में थे या नहीं मशहूर फ़िक़्ही इख़्तिलाफ़ है: इब्न अब्बास ने इहराम की ख़बर दी; औरों ने हलाल होने की। सीरत दोनों रखती है, माँ को निज़ा नहीं बनाती। मुत्तफ़िक़ यह है कि यह आख़िरी निकाह था और इसी मुबारक सफ़र पर हुआ।

कुछ रिवायात में उन्होंने अपने आप को पेश किया (33:50 की रोशनी में); कुछ में पैग़ाम बहन और अब्बास के ज़रिए आया। दोनों बयान उनकी इज़्ज़त रखते हैं। मदीना के घर में आईं और अज़वाज के हुजरों में रहीं। भतीजे इब्न अब्बास ने उनसे बहुत रिवायत की—ग़ुस्ल, इहराम, घरेलू सुन्नत—चنانचे उनका इल्म बनू हाशिम के जवानों में कुरआन के सबसे मशहूर शागिर्द की तफ़सीर के साथ चला।

तक़वा से पहचानी गईं, वफ़ात के बाद मदीना में रहीं, दोबारा निकाह न किया। ज़िंदगी के आख़िर में मक्का रुख़ किया। लगभग 51 हिजरी में (और ख़बरें 49 या बाद) सरिफ़ में वफ़ात, उसी मक़ाम पर जहाँ निकाह हुआ था, वहीं दफ़न। इब्न अब्बास ने जनाज़ा पढ़ाया। मक्की रास्ते के मुसाफ़िर अब भी वहाँ उनका नाम सुनते हैं।

मैमूना के साथ इस बाब में अज़वाज उम्महात की मा'रूफ़ फ़ेहरिस्त मुकम्मल होती है। 7 हिजरी के बाद उनमें और निकाह शुमार नहीं होता। उम्महात का घर तब भरा था: मक्का व मदीना की विधवाएँ, दोस्तों और पुराने दुश्मनों की बेटियाँ, वही से निकाहशुदा फूफेरी, और इब्न अब्बास की यह आख़िरी हिलाली ख़ाला।

अहले सुन्नत की सीरत उनके तरजमे को दायरे की नरमी से बंद करती है: आख़िरी निकाह और माँ की आख़िरी राह किनारे की क़ब्र, दोनों सरिफ़ में। अल्लाह उनसे राज़ी हो।""",
    """মায়মুনাহ বিনত আল-হারিস আল-হিলালিয়্যাহ رضي الله عنها সর্বশেষ নারী যাঁকে নবী ﷺ বিয়ে করেন। নাম ছিল বাররাহ; তিনি মায়মুনাহ রাখেন, বরকতময়ী। তিনি উম্মুল ফাদ্ল লুবাবাহর বোন, আল-আব্বাস ইবন আব্দুল মুত্তালিবের স্ত্রী, সুতরাং আব্দুল্লাহ ইবন আব্বাস رضي الله عنهما-এর খালা। সেই হিলালি ঘরের বোনদের মাধ্যমে অন্য বড় সাহাবিদের সঙ্গেও যুক্ত। আল-আব্বাস বিবাহ সাজাতে অংশ নেন।

আকদ জিলকদ ৭ হিজরি / ৬২৯ খ্রি. সারিফে হয়, মক্কা থেকে কয়েক মাইল, উমরাতুল কাদার পর—হুদায়বিয়ার পরের বছরের পূরণ করা উমরা। আকদের মুহূর্তে তিনি ﷺ ইহরামে ছিলেন কি না প্রসিদ্ধ ফিকহি মতভেদ: ইবন আব্বাস ইহরামের খবর দেন; অন্যরা হালাল হওয়ার খবর দেন। সিরাত দুইটিই রাখে, মাতাকে বিবাদে পরিণত করে না। একমত এই যে এটি সর্বশেষ বিবাহ এবং সেই বরকতময় সফরেই হয়।

কিছু বর্ণনায় তিনি নিজেকে পেশ করেন (৩৩:৫০-এর আলোকে); কিছুতে প্রস্তাব বোন ও আল-আব্বাসের মাধ্যমে আসে। উভয় বয়ান তাঁর মর্যাদা রাখে। তিনি মদিনার ঘরে আসেন এবং স্ত্রীদের হুজরায় থাকেন। ভাইপো ইবন আব্বাস তাঁর থেকে অনেক বর্ণনা করেন—গোসল, ইহরাম, গৃহ সুন্নাহ—ফলে তাঁর ইলম বনু হাশিমের যুবকদের মধ্যে কুরআনের সবচেয়ে প্রসিদ্ধ ছাত্রের তাফসিরের সঙ্গে যায়।

তাকওয়ায় পরিচিত, ওফাতের পর মদিনায় থাকেন, পুনরায় বিয়ে করেননি। জীবনের শেষে মক্কার দিকে যান। প্রায় ৫১ হিজরিতে (অন্য খবর ৪৯ বা পরে) সারিফে ওফাত, যেখানে বিবাহ হয়েছিল সেই বিরতিতেই দাফন। ইবন আব্বাস জানাজা পড়ান। মক্কী পথের মুসাফির আজও সেখানে তাঁর নাম শোনে।

মায়মুনাহর সঙ্গে এই অধ্যায়ে স্ত্রী উম্মাহাতের প্রচলিত তালিকা সম্পূর্ণ হয়। ৭ হিজরির পর তাঁদের মধ্যে আর বিবাহ গণ্য হয় না। উম্মাহাতের ঘর তখন পূর্ণ: মক্কা ও মদিনার বিধবা, বন্ধু ও পুরনো শত্রুর কন্যা, ওহী দ্বারা বিবাহিত ফুফাতো বোন, এবং ইবন আব্বাসের এই শেষ হিলালি খালা।

সুন্নি সিরাত তাঁর পরিচিতি বৃত্তের কোমলতায় বন্ধ করে: সর্বশেষ বিবাহ এবং এক মাতার সর্বশেষ পথের কবর, দুইটিই সারিফে। আল্লাহ তাঁর প্রতি সন্তুষ্ট হোন।""",
    """Maimunah binti al-Harits al-Hilaliyyah radhiyallahu anha adalah wanita terakhir yang dinikahi Nabi ﷺ. Namanya Barrah; beliau menamainya Maimunah, yang diberkahi. Ia saudara Ummu al-Fadl Lubabah, istri al-Abbas bin Abdul Muththalib, jadi bibi Abdullah bin Abbas radhiyallahu anhuma dari pihak ibu. Melalui saudari rumah Hilal itu ia juga terikat kepada sahabat-sahabat besar lain. Al-Abbas ikut mengatur pernikahan.

Akad pada Zulkaidah 7 H / 629 M di Sarif, beberapa mil dari Makkah, setelah umrah al-qadha—umrah pengganti tahun sesudah Hudaibiyah. Apakah beliau ﷺ sedang ihram saat akad adalah perbedaan fikih terkenal: Ibnu Abbas meriwayatkan beliau ihram; yang lain meriwayatkan beliau halal. Sirah mencatat keduanya, tanpa menjadikan ibu itu sengketa. Yang disepakati ialah ini pernikahan terakhir dan terjadi pada perjalanan yang diberkahi itu.

Sebagian riwayat mengatakan ia menawarkan diri (dalam cahaya 33:50); yang lain bahwa pinangan datang melalui saudarinya dan al-Abbas. Kedua kisah menjaga martabatnya. Ia masuk rumah tangga di Madinah dan tinggal di kamar di antara para istri. Ibnu Abbas, keponakannya, meriwayatkan banyak darinya—mandi junub, ihram, dan sunnah rumah—sehingga ilmunya berjalan bersama tafsir murid Al-Qur'an paling terkenal di kalangan pemuda Bani Hasyim.

Ia dikenal karena takwa dan tetap di Madinah setelah wafat, tanpa menikah lagi. Menjelang akhir hayat ia menuju Makkah. Ia wafat di Sarif sekitar 51 H (catatan lain 49 atau kemudian), di persinggahan yang sama tempat beliau menikahinya ﷺ, dan dimakamkan di sana. Ibnu Abbas mensalatkan jenazahnya. Musafir di jalan Makkah masih mendengar namanya di tempat itu.

Dengan Maimunah, daftar lazim para ibu yang menjadi istri dalam bab ini lengkap. Setelah 7 H tidak ada pernikahan lain yang dihitung di antara mereka. Rumah tangga Ummahat ketika itu penuh: janda Makkah dan Madinah, putri sahabat dan bekas lawan, sepupu yang dinikahkan wahyu, dan bibi Hilal terakhir Ibnu Abbas ini.

Sirah Ahlus Sunnah menutup biografnya dengan kelembutan sebuah lingkaran: pernikahan terakhir dan kubur pinggir jalan terakhir seorang ibu, keduanya di Sarif. Semoga Allah meridainya.""",
)

c = chapter(5)
c["details"] = D(
    """After the Hijrah in 1 AH / 622 CE the Prophet ﷺ built the mosque in Madinah, first pausing at Quba', then raising al-Masjid al-Nabawi where his camel sat. His apartments opened onto the courtyard. The mosque was not only a place of prayer: it was the school, the council, and the shelter of the poor on the suffah. From those date-palm columns the Madinan years unfolded.

He established mu'akhat, the brotherhood between Muhajirun and Ansar, pairing emigrants who had left Makkah with helpers who offered house and date-garden. That bond taught the Ummah that faith, not clan alone, makes a family. Classical seerah names pairs such as Abd al-Rahman ibn Awf with Sa'd ibn al-Rabi'. The Ansar's generosity and the Muhajirun's dignity are both praised in the Qur'an.

A written pact, often called the Constitution of Madinah, ordered relations among the believing community and the Jewish tribes and other groups of the town. Blood-money, defence of the city, and the authority of the Messenger ﷺ in dispute were set down. Ibn Ishaq preserves the gist of that sahifah. It is the political beginning of a city that would face war and treaty under one leadership.

The arc of the Madinan decade runs through Badr, Uhud, and the Trench; then Hudaybiyyah, Khaybar, and the Conquest of Makkah; then Hunayn and Ta'if; then Tabuk and the Farewell Hajj. Battles were not the whole story: letters to kings, delegations in 9 AH, and the teaching of halal and haram filled the mosque. This chapter treats the major military and public events, then the illness and wafat.

He ﷺ died in Madinah in Rabi' al-Awwal 11 AH, June 632 CE, at sixty-three years of age, and was buried in the chamber of Aisha رضي الله عنها, now within the Prophet's Mosque. The Ummah's grief was unlike any other death, because he was the last of the messengers. Abu Bakr رضي الله عنه steadied the people with the Qur'an.

Ibn Ishaq's maghazi, Ibn Hisham's recension, Ibn Sa'd, and the Kitab al-Maghazi in Bukhari and Muslim are the backbone of what follows. Dates are given in Hijri and in the common Gregorian equivalents used by historians. Where reports differ on a day, the well-known teaching of Ahl al-Sunnah is stated first.

What follows takes four scenes: the three great defensive battles; the treaty and the openings of Khaybar and Makkah; Tabuk and the sermon of Arafah; then the fever, the last prayer, and the burial where he died. Together they close the earthly seerah.""",
    """1ھ / 622ء میں ہجرت کے بعد نبی ﷺ نے مدینہ میں مسجد بنائی، پہلے قباء ٹھہرے، پھر مسجد نبوی وہاں اٹھائی جہاں ناقہ بیٹھی۔ حجرے صحن کی طرف کھلتے۔ مسجد صرف نماز کی جگہ نہ تھی: مدرسہ، مجلس، اور صفہ پر غریبوں کی پناہ تھی۔ کھجور کے ستونوں سے مدنی سال کھلے۔

مواخات قائم کی، مہاجرین و انصار میں بھائی چارہ، مکہ چھوڑنے والوں کو انصار سے جوڑا جنہوں نے گھر اور باغ دیے۔ اس بندھن نے سکھایا کہ ایمان، نہ صرف قبیلہ، خاندان بناتا ہے۔ کلاسیکی سیرت عبد الرحمن بن عوف و سعد بن ربیع جیسے جوڑے نام لیتی ہے۔ انصار کی سخاوت اور مہاجرین کی عزت دونوں قرآن میں تعریف ہوئی۔

تحریری معاہدہ، جسے اکثر میثاق مدینہ کہتے ہیں، مؤمن جماعت اور شہر کے یہودی قبائل و دیگر گروہوں کے تعلقات مرتب کرتا تھا۔ دیت، شہر کی دفاع، اور تنازع میں رسول ﷺ کی حیثیت لکھی گئی۔ ابن اسحاق اس صحیفے کا خلاصہ رکھتے ہیں۔ یہ اس شہر کی سیاسی ابتدا ہے جو ایک قیادت تلے جنگ و صلح دیکھے گا۔

مدنی دہائی کا قوس بدر، احد، خندق سے گزرتا ہے؛ پھر حدیبیہ، خیبر، فتح مکہ؛ پھر حنین و طائف؛ پھر تبوک اور حجۃ الوداع۔ جنگیں پوری کہانی نہ تھیں: بادشاہوں کے خطوط، 9ھ کے وفود، حلال و حرام کی تعلیم مسجد بھرتی رہی۔ یہ باب بڑے عسکری و عوامی واقعات پھر مرض و وفات بیان کرتا ہے۔

آپ ﷺ ربیع الاول 11ھ، جون 632ء، تریسٹھ سال کی عمر میں مدینہ میں وفات پائے، عائشہ رضی اللہ عنہا کے حجرے میں دفن ہوئے جو اب مسجد نبوی کے اندر ہے۔ امت کا غم کسی اور موت جیسا نہ تھا، کیونکہ آپ آخری رسول تھے۔ ابو بکر رضی اللہ عنہ نے قرآن سے لوگوں کو سنجھالا۔

ابن اسحاق کی مغازی، ابن ہشام کی روایت، ابن سعد، اور بخاری و مسلم کی کتاب المغازی آگے کی ریڑھ ہیں۔ تاریخیں ہجری اور مورخوں کے عام گریگوری مماثل سے دی گئی ہیں۔ جہاں دن پر روایات چھڑتی ہیں وہاں اہل سنت کی معروف تعلیم پہلے بیان ہوئی۔

آگے چار منظر ہیں: تین بڑی دفاعی جنگیں؛ صلح پھر خیبر و مکہ کے کھلنے؛ تبوک اور عرفات کا خطبہ؛ پھر بخار، آخری نماز، اور وہیں تدفین جہاں وفات ہوئی۔ یہ سب مل کر دنیاوی سیرت بند کرتے ہیں۔""",
    """1 हिजरी / 622 ई. में हिजरत के बाद नबी ﷺ ने मदीना में मस्जिद बनाई, पहले क़ुबा ठहरे, फिर मस्जिद-ए-नबवी वहाँ उठाई जहाँ नाक़ा बैठी। हुजरे सहन की तरफ़ खुलते। मस्जिद सिर्फ़ नमाज़ की जगह न थी: मदरसा, मजलिस, और सुफ़्फ़ा पर ग़रीबों की पनाह थी। खजूर के सुतूनों से मदनी साल खुले।

मुआख़ात क़ायम की, मुहाजिरीन व अनसार में भाईचारा, मक्का छोड़ने वालों को अनसार से जोड़ा जिन्होंने घर और बाग़ दिए। उस बंधन ने सिखाया कि ईमान, न केवल क़बीला, ख़ानदान बनाता है। क्लासिकल सीरत अब्दुर्रहमान इब्न अउफ़ व सअद इब्न रबीअ जैसे जोड़े नाम लेती है। अनसार की सख़ावत और मुहाजिरीन की इज़्ज़त दोनों कुरआन में तारीफ़ हुई।

तहरीरी मुआहदा, जिसे अक्सर मीसाक़-ए-मदीना कहते हैं, मोमिन जमाअत और शहर के यहूदी क़बीलों व अन्य गिरोहों के ताल्लुक़ात मुरत्तब करता था। دियत, शहर की हिफ़ाज़त, और तनाज़ुअ में रसूल ﷺ की हैसियत लिखी गई। इब्न इसहाक उस सहीफ़े का ख़ुलासा रखते हैं। यह उस शहर की सियासी इब्तदा है जो एक क़ियादत तले जंग व सुलह देखेगा।

मदनी दहाई का क़ौस बद्र, उहुद, खंदक से गुज़रता है; फिर हुदैबिया, ख़ैबर, फ़त्हे मक्का; फिर हुनैन व ताइफ़; फिर तबूक और हज्जतुल विदा। जंगें पूरी कहानी न थीं: बादशाहों के ख़ूतूत, 9 हिजरी के वुफूद, हलाल व हराम की तालीम मस्जिद भरती रही। यह बाब बड़े अस्करी व आवामी वाक़ियात फिर मर्ज़ व विसाल बयान करता है।

आप ﷺ रबीउल अव्वल 11 हिजरी, जून 632 ई., तिरेसठ वर्ष की उम्र में मदीना में वफ़ात पाए, आयशा رضي الله عنها के हुजरे में दफ़न हुए जो अब मस्जिद-ए-नबवी के अंदर है। उम्मत का ग़म किसी और मौत जैसा न था, क्योंकि आप आख़िरी रसूल थे। अबू बक्र رضي الله عنه ने कुरआन से लोगों को संभाला।

इब्न इसहाक की मग़ाज़ी, इब्न हिशाम की रिवायत, इब्न साद, और बुख़ारी व मुस्लिम की किताब अल-मग़ाज़ी आगे की रीढ़ हैं। तारीख़ें हिजरी और मुअर्रिख़ों के आम ग्रेगरी मुमासिल से दी गई हैं। जहाँ दिन पर रिवायात छिड़ती हैं वहाँ अहले सुन्नत की मा'रूफ़ तालीम पहले बयान हुई।

आगे चार मंज़र हैं: तीन बड़ी रक्षात्मक जंगें; सुलह फिर ख़ैबर व मक्का के खुलने; तबूक और अरफ़ात का ख़ुत्बा; फिर बुख़ार, आख़िरी नमाज़, और वहीं तदफ़ीन जहाँ विसाल हुई। ये सब मिलकर दुनियावी सीरत बंद करते हैं।""",
    """১ হিজরি / ৬২২ খ্রি. হিজরতের পর নবী ﷺ মদিনায় মসজিদ নির্মাণ করেন, প্রথমে কুবায় থামেন, পরে মসজিদে নববী সেখানে তোলেন যেখানে উষ্ট্রী বসে। হুজরাগুলো প্রাঙ্গণের দিকে খুলত। মসজিদ কেবল সালাতের স্থান ছিল না: মাদরাসা, মজলিস, এবং সুফ্ফায় দরিদ্রদের আশ্রয়। খেজুরের স্তম্ভ থেকে মাদানী বছর খোলে।

তিনি মুআখাত প্রতিষ্ঠা করেন, মুহাজির ও আনসারের ভ্রাতৃত্ব, মক্কা ছাড়াদের সঙ্গে সাহায্যকারীদের জোড়া দেন যাঁরা ঘর ও খেজুরবাগান দেন। সেই বন্ধন শেখায় ঈমান, কেবল গোত্র নয়, পরিবার গড়ে। ক্লাসিক সিরাত আব্দুর রহমান ইবন আউফ ও সাদ ইবন আর-রাবির মতো জোড়ার নাম লেখে। আনসারের দান ও মুহাজিরদের মর্যাদা দুই-ই কুরআনে প্রশংসিত।

এক লিখিত চুক্তি, প্রায়ই মদিনার সনদ নামে, মুমিন জামাত ও শহরের ইহুদি গোত্র ও অন্য দলের সম্পর্ক সাজায়। দিয়ত, শহররক্ষা, এবং বিবাদে রাসূল ﷺ-এর কর্তৃত্ব লেখা হয়। ইবন ইসহাক সেই সহিফার সার রাখেন। এটি সেই শহরের রাজনৈতিক সূচনা যা এক নেতৃত্বে যুদ্ধ ও সন্ধি দেখবে।

মাদানী দশকের চাপ বদর, উহুদ ও খন্দক দিয়ে যায়; তারপর হুদায়বিয়া, খাইবার ও মক্কা বিজয়; তারপর হুনাইন ও তায়েফ; তারপর তাবুক ও বিদায় হজ। যুদ্ধই পুরো কাহিনি ছিল না: রাজাদের চিঠি, ৯ হিজরির প্রতিনিধিদল, হালাল-হারামের শিক্ষা মসজিদ ভরত। এই অধ্যায় প্রধান সামরিক ও सार्वजनिक ঘটনা, তারপর অসুস্থতা ও ওফাত বলে।

তিনি ﷺ রবিউল আউয়াল ১১ হিজরি, জুন ৬৩২ খ্রি., তেষট্টি বছর বয়সে মদিনায় ওফাত পান, আয়িশা رضي الله عنها-এর হুজরায় দাফন হন যা এখন নববি মসজিদের অন্তর্গত। উম্মাহর শোক অন্য কোনো মৃত্যুর মতো ছিল না, কারণ তিনি শেষ রাসূল। আবু বকর رضي الله عنه কুরআন দিয়ে মানুষ স্থির করেন।

ইবন ইসহাকের মাগাজি, ইবন হিশামের বর্ণনা, ইবন সাদ, এবং বুখারি ও মুসলিমের কিতাবুল মাগাজি পরের মেরুদণ্ড। তারিখ হিজরি ও ঐতিহাসিকদের প্রচলিত গ্রেগরি সমতুল্যে দেওয়া। দিন নিয়ে বর্ণনা ভিন্ন হলে আহলুস সুন্নাহর প্রসিদ্ধ শিক্ষা আগে বলা হয়েছে।

এরপর চার দৃশ্য: তিন বড় প্রতিরক্ষামূলক যুদ্ধ; সন্ধি ও খাইবার-মক্কার উন্মোচন; তাবুক ও আরাফার খুতবা; তারপর জ্বর, শেষ সালাত, এবং যেখানে ওফাত সেখানে দাফন। এগুলো মিলে পার্থিব সিরাত বন্ধ করে।""",
    """Setelah Hijrah pada 1 H / 622 M Nabi ﷺ membangun masjid di Madinah, mula-mula singgah di Quba, lalu menegakkan Masjid Nabawi di tempat untanya menderum. Kamar-kamarnya membuka ke pelataran. Masjid bukan hanya tempat salat: ia sekolah, majelis, dan naungan orang miskin di suffah. Dari tiang-tiang kurma tahun-tahun Madinah terbuka.

Beliau menegakkan muakhat, persaudaraan antara Muhajirin dan Ansar, memasangkan muhajirin yang meninggalkan Makkah dengan penolong yang menawarkan rumah dan kebun kurma. Ikatan itu mengajar umat bahwa iman, bukan suku semata, menjadikan keluarga. Sirah klasik menamai pasangan seperti Abdurrahman bin Auf dengan Sa'd bin ar-Rabi'. Kedermawanan Ansar dan martabat Muhajirin keduanya dipuji dalam Al-Qur'an.

Piagam tertulis, sering disebut Konstitusi Madinah, mengatur hubungan jamaah beriman dengan suku Yahudi dan kelompok lain di kota. Diyat, pertahanan kota, dan wewenang Rasulullah ﷺ dalam sengketa dicatat. Ibnu Ishaq menyimpan inti sahifah itu. Itulah awal politik sebuah kota yang akan menghadapi perang dan perjanjian di bawah satu kepemimpinan.

Busur dasawarsa Madinah berjalan melalui Badar, Uhud, dan Khandaq; lalu Hudaibiyah, Khaibar, dan Fathu Makkah; lalu Hunain dan Thaif; lalu Tabuk dan haji wada. Peperangan bukan seluruh cerita: surat kepada raja-raja, delegasi tahun 9 H, dan pengajaran halal-haram memenuhi masjid. Bab ini menguraikan peristiwa militer dan publik utama, kemudian sakit dan wafat.

Beliau ﷺ wafat di Madinah pada Rabiul Awal 11 H, Juni 632 M, usia enam puluh tiga tahun, dan dimakamkan di kamar Aisyah radhiyallahu anha, kini di dalam Masjid Nabawi. Duka umat tidak seperti kematian lain, karena beliau rasul terakhir. Abu Bakar radhiyallahu anhu menenangkan orang dengan Al-Qur'an.

Maghazi Ibnu Ishaq, recensi Ibnu Hisyam, Ibnu Sa'd, dan Kitab al-Maghazi dalam Bukhari dan Muslim adalah tulang punggung yang berikut. Tanggal diberi dalam Hijriah dan padanan Masehi yang dipakai sejarawan. Jika riwayat berbeda tentang suatu hari, ajaran terkenal Ahlus Sunnah dinyatakan lebih dulu.

Berikutnya empat adegan: tiga pertempuran defensif besar; perjanjian lalu terbukanya Khaibar dan Makkah; Tabuk dan khutbah Arafah; kemudian demam, salat terakhir, dan pemakaman di tempat beliau wafat. Bersama-sama itu menutup sirah duniawi.""",
)

c["items"][0]["details"] = D(
    """Badr fell on Friday 17 Ramadan 2 AH / March 624 CE. About three hundred and thirteen Muslims, lightly armed, met a Quraysh caravan's war-party of about a thousand. The Qur'an names that day Yawm al-Furqan, the Day of Criterion (8:41). Fourteen Muslims were martyred—six Muhajirun and eight Ansar in the usual count. Quraysh lost many killed and captives. The Prophet ﷺ spent the night in du'a; Allah sent angels as the Book relates. Badr taught the Ummah that victory is from Allah, not from numbers.

After Badr the captives were treated with a mix of ransom and teaching; some who could write taught Madinan children. The hypocrites in Madinah and the rage of Makkah set the stage for the next trial. The names of the martyrs of Badr are still recited with honour. Hamzah, Ali, and the young men of the Ansar fought in a way the maghazi never tired of telling.

Uhud came on 15 Shawwal 3 AH / March 625 CE. The Muslims held the advantage until archers left their post on the hill against the Prophet's order, seeking spoils. Khalid ibn al-Walid, then still with Quraysh, wheeled the cavalry. The Messenger ﷺ was wounded in the face, a helmet-ring bit his cheek, and a rumour that he had been killed spread. Hamzah ibn Abd al-Muttalib رضي الله عنه was martyred by Wahshi. About seventy Muslims fell. Surah Al Imran reads Uhud as a test after the gift of Badr.

The lesson of Uhud is obedience and patience, not despair. The Prophet ﷺ buried the martyrs on the field. He pursued the enemy toward Hamra' al-Asad so that Quraysh would not return upon Madinah. Those who had fled were not permanently shamed; the Qur'an called them to repentance. Ahl al-Sunnah tell the battle without insulting the Companions who slipped that day.

The Trench, Ghazwat al-Khandaq or al-Ahzab, was in Shawwal 5 AH / 627 CE. Confederates—Quraysh, Ghatafan, and others—besieged Madinah. Salman al-Farisi رضي الله عنه suggested a trench, a method known in Persia. The Companions dug in cold and hunger; the Prophet ﷺ tied stones to his belly and struck the rock in the trench with tidings of future openings. The siege lasted weeks. A bitter wind and the failure of the coalition are in Surah al-Ahzab (33:9). Huyayy ibn Akhtab worked to pull Banu Qurayza from their pact during the siege; that breach is treated in the seerah as treachery in war, after which judgement followed the law of their own ally Sa'd ibn Mu'adh رضي الله عنه.

When the confederates withdrew, Madinah was no longer an easy prize. The sequence Badr–Uhud–Trench is the shield of the city: a victory that named the criterion, a wound that taught discipline, and a siege that Allah broke with wind. Students of maghazi read the three together.

Thus the first item of this chapter is the triad of great battles in 2, 3, and 5 AH, from the wells of Badr to the ditch of Madinah. May Allah be pleased with the martyrs and the diggers of the trench.""",
    """بدر جمعہ 17 رمضان 2ھ / مارچ 624ء کو ہوا۔ تقریباً تین سو تیرہ ہلکے مسلح مسلمان قریش کی تقریباً ہزار نفری جنگجو فوج سے ٹکرائے۔ قرآن اس دن کو یوم الفرقان کہتا ہے (8:41)۔ چودہ مسلمان شہید ہوئے—معروف شمار میں چھ مہاجر، آٹھ انصار۔ قریش کے بہت مارے اور قیدی ہوئے۔ نبی ﷺ رات دعا میں گزارے؛ اللہ نے فرشتے بھیجے جیسا کتاب بیان کرتی ہے۔ بدر نے سکھایا فتح اللہ کی طرف سے ہے، تعداد سے نہیں۔

بدر کے بعد قیدیوں سے فدیہ اور تعلیم ملی؛ لکھنے والے مدنی بچوں کو پڑھاتے۔ مدینہ کے منافق اور مکہ کا غضب اگلی آزمائش کا میدان بنا۔ بدر کے شہدا کے نام اب بھی عزت سے پڑھے جاتے ہیں۔ حمزہ، علی، اور انصار کے جوان مغازی میں بار بار آتے ہیں۔

احد 15 شوال 3ھ / مارچ 625ء کو آیا۔ مسلمان غالب رہے یہاں تک تیراندازوں نے نبی کے حکم کے خلاف پہاڑی کا مورچہ مال غنیمت کی خاطر چھوڑا۔ خالد بن ولید، جو ابھی قریش کے ساتھ تھے، سواروں کو گھما لائے۔ رسول ﷺ چہرے سے زخمی ہوئے، خود کی کڑی گال میں چبھیں، قتل کی افواہ پھیلی۔ حمزہ بن عبد المطلب رضی اللہ عنہ وحشی کے ہاتھ شہید ہوئے۔ تقریباً ستر مسلمان گرے۔ سورہ آل عمران احد کو بدر کے انعام کے بعد آزمائش پڑھتی ہے۔

احد کا سبق اطاعت و صبر ہے، مایوسی نہیں۔ نبی ﷺ نے شہدا کو میدان میں دفن کیا۔ حمراء الاسد کی طرف پیچھا کیا تاکہ قریش مدینہ پر نہ پلٹیں۔ جو بھاگے تھے مستقل رسوا نہ کیے گئے؛ قرآن نے توبہ کی دعوت دی۔ اہل سنت اس جنگ کو اس دن پھسلنے والے صحابہ کی توہین کے بغیر بیان کرتے ہیں۔

خندق، غزوہ احزاب، شوال 5ھ / 627ء میں ہوئی۔ احزاب—قریش، غطفان وغیرہ—نے مدینہ گھیر لیا۔ سلمان فارسی رضی اللہ عنہ نے خندق تجویز کی، فارس کا طریقہ۔ صحابہ سردی و بھوک میں کھودتے رہے؛ نبی ﷺ نے پیٹ پر پتھر باندھے اور خندق کی چٹان پر مستقبل کی فتوحات کی بشارت دی۔ محاصرہ ہفتوں رہا۔ تیز ہوا اور اتحاد کا ٹوٹنا سورہ احزاب (33:9) میں ہے۔ حیي بن اخطب نے محاصرے میں بنو قریظہ کو عہد سے ہٹانے کی کوشش کی؛ سیرت اسے جنگ میں غداری سمجھتی ہے، جس کے بعد فیصلہ ان کے حلیف سعد بن معاذ رضی اللہ عنہ کے قانون پر ہوا۔

جب احزاب ہٹے تو مدینہ آسان شکار نہ رہا۔ بدر–احد–خندق شہر کی ڈھال ہے: وہ فتح جس نے فرقان نام دیا، وہ زخم جس نے ضبط سکھایا، وہ حصار جسے اللہ نے ہوا سے توڑا۔ طالب مغازی تینوں کو ساتھ پڑھتے ہیں۔

یوں اس باب کی پہلی چیز 2، 3 اور 5ھ کی تین بڑی جنگیں ہیں، بدر کے کنوؤں سے مدینہ کی خندق تک۔ اللہ شہدا اور خندق کھودنے والوں سے راضی ہو۔""",
    """बद्र जुमा 17 रमज़ान 2 हिजरी / मार्च 624 ई. को हुआ। लगभग तीन सौ तेरह हल्के मुसल्लह मुसलमान कुरैश की लगभग हज़ार नेफ़री जंगजू फ़ौज से टकराए। कुरआन उस दिन को यौम उल-फ़ुरक़ान कहता है (8:41)। चौदह मुसलमान शहीद हुए—मा'रूफ़ शुमार में छह मुहाजिर, आठ अनसार। कुरैश के बहुत मारे और क़ैदी हुए। नबी ﷺ रात दुआ में गुज़ारे; अल्लाह ने फ़रिश्ते भेजे जैसा किताब बयान करती है। बद्र ने सिखाया फ़तह अल्लाह की तरफ़ से है, तादाद से नहीं।

बद्र के बाद क़ैदियों से फ़िदया और तालीम मिली; लिखने वाले मदनी बच्चों को पढ़ाते। मदीना के मुनाफ़िक़ और मक्का का ग़ज़ब अगली आज़माइश का मैदान बना। बद्र के शुहदा के नाम अब भी इज़्ज़त से पढ़े जाते हैं। हम्ज़ा, अली, और अनसार के जवान मग़ाज़ी में बार-बार आते हैं।

उहुद 15 शव्वाल 3 हिजरी / मार्च 625 ई. को आया। मुसलमान ग़ालिब रहे यहाँ तक तीरंदाज़ों ने नबी के हुक्म के ख़िलाफ़ पहाड़ी का मोर्चा माल-ए-ग़नीमत की ख़ातिर छोड़ा। ख़ालिद इब्न वलीद, जो अभी कुरैश के साथ थे, सवारों को घुमा लाए। रसूल ﷺ चेहरे से ज़ख़्मी हुए, ख़ुद की कड़ी गाल में चुभी, क़त्ल की अफ़वाह फैली। हम्ज़ा इब्न अब्दुल मुत्तलिब رضي الله عنه वहशी के हाथ शहीद हुए। लगभग सत्तर मुसलमान गिरे। सूरह आल-ए-इमरान उहुद को बद्र के इनाम के बाद आज़माइश पढ़ती है।

उहुद का सबक़ इताअत व सब्र है, मायूसी नहीं। नबी ﷺ ने शुहदा को मैदान में दफ़न किया। हमरा अल-असद की तरफ़ पीछा किया ताकि कुरैश मदीना पर न पलटें। जो भागे थे मुस्तकिल रुसवा न किए गए; कुरआन ने तौबा की दावत दी। अहले सुन्नत इस जंग को उस दिन फिसलने वाले सहाबा की तोहीन के बिना बयान करते हैं।

खंदक, ग़ज़वा अल-अहज़ाब, शव्वाल 5 हिजरी / 627 ई. में हुई। अहज़ाब—कुरैश, ग़तफ़ान वग़ैरह—ने मदीना घेर लिया। सलमान फ़ारसी رضي الله عنه ने खंदक तजवीज़ की, फ़ारस का तरीक़ा। सहाबा सर्दी व भूख में खोदते रहे; नबी ﷺ ने पेट पर पत्थर बाँधे और खंदक की चट्टान पर मुस्तक़बिल की फ़ुतूहात की बशारत दी। मुहासरा हफ़्तों रहा। तेज़ हवा और इत्तिहाद का टूटना सूरह अहज़ाब (33:9) में है। हुयय इब्न अख़्तब ने मुहासरे में बनू क़ुराइज़ा को अहद से हटाने की कोशिश की; सीरत इसे जंग में ग़द्दारी समझती है, जिसके बाद फ़ैसला उनके हलीफ़ सअद इब्न मुआज़ رضي الله عنه के क़ानून पर हुआ।

जब अहज़ाब हटे तो मदीना आसान शिकार न रहा। बद्र–उहुद–खंदक शहर की ढाल है: वह फ़तह जिसने फ़ुरक़ान नाम दिया, वह ज़ख़्म जिसने ज़ब्त सिखाया, वह हिसार जिसे अल्लाह ने हवा से तोड़ा। तालिब-ए-मग़ाज़ी तीनों को साथ पढ़ते हैं।

यूँ इस बाब की पहली चीज़ 2, 3 और 5 हिजरी की तीन बड़ी जंगें हैं, बद्र के कुओं से मदीना की खंदक तक। अल्लाह शुहदा और खंदक खोदने वालों से राज़ी हो।""",
    """বদর জুমা ১৭ রমজান ২ হিজরি / মার্চ ৬২৪ খ্রি. ঘটে। প্রায় তিনশ তেরো হালকা সশস্ত্র মুসলিম কুরাইশের প্রায় হাজার যোদ্ধার মুখোমুখি হন। কুরআন সেই দিনকে ইয়াওমুল ফুরকান বলে (৮:৪১)। চোদ্দ মুসলিম শহীদ হন—প্রচলিত গণনায় ছয় মুহাজির, আট আনসার। কুরাইশের অনেকে নিহত ও বন্দি হয়। নবী ﷺ রাত দোয়ায় কাটান; আল্লাহ ফেরেশতা পাঠান যেমন কিতাব বলে। বদর শেখায় বিজয় আল্লাহর পক্ষ থেকে, সংখ্যা থেকে নয়।

বদরের পর বন্দিদের ফিদয়া ও শিক্ষা দেওয়া হয়; লিখতে জানা কেউ মদিনার শিশুদের পড়ান। মদিনার মুনাফিক ও মক্কার ক্রোধ পরের পরীক্ষার মঞ্চ সাজায়। বদরের শহীদদের নাম আজও সম্মানে পড়া হয়। হামজাহ, আলি, এবং আনসারের যুবকেরা মাগাজিতে বারবার আসেন।

উহুদ ১৫ শাওয়াল ৩ হিজরি / মার্চ ৬২৫ খ্রি. আসে। মুসলিমরা প্রাধান্য রাখেন যতক্ষণ তীরন্দাজরা নবীর নির্দেশের বিরুদ্ধে পাহাড়ের মোর্চা গনিমতের লোভে ছাড়েন। খালিদ ইবন আল-ওয়ালিদ, তখনও কুরাইশের সঙ্গে, অশ্বারোহী ঘুরিয়ে আনেন। রাসূল ﷺ মুখে আহত হন, শিরস্ত্রাণের কড়া গালে বিঁধে, তিনি নিহত হয়েছেন এমন গুজব ছড়ায়। হামজাহ ইবন আব্দুল মুত্তালিব رضي الله عنه ওয়াহশির হাতে শহীদ হন। প্রায় সত্তর মুসলিম পড়েন। সূরা আল ইমরান উহুদকে বদরের দানের পর পরীক্ষা হিসেবে পড়ে।

উহুদের শিক্ষা আনুগত্য ও ধৈর্য, নিরাশা নয়। নবী ﷺ শহীদদের মাঠে দাফন করেন। তিনি হামরা আল-আসাদের দিকে তাড়া করেন যাতে কুরাইশ মদিনায় না ফেরে। যাঁরা পালিয়েছিলেন তাঁদের স্থায়ীভাবে অপমান করা হয়নি; কুরআন তওবার আহ্বান করে। আহলুস সুন্নাহ সেই দিন পিছলে যাওয়া সাহাবিদের অবমাননা ছাড়া যুদ্ধ বলে।

খন্দক, গাজওয়া আল-আহযাব বা আল-খন্দক, শাওয়াল ৫ হিজরি / ৬২৭ খ্রি.। সম্মিলিত বাহিনী—কুরাইশ, গাতাফান ও অন্যরা—মদিনা অবরোধ করে। সালমান আল-ফারসি رضي الله عنه পরিখা প্রস্তাব করেন, পারস্যের পদ্ধতি। সাহাবিরা ঠান্ডা ও ক্ষুধায় খোঁড়েন; নবী ﷺ পেটে পাথর বাঁধেন এবং পরিখার পাথরে ভবিষ্যৎ বিজয়ের সুসংবাদ দেন। অবরোধ সপ্তাহব্যাপী। তীব্র বাতাস ও জোটের ব্যর্থতা সূরা আল-আহযাবে (৩৩:৯)। হুয়াইয়্য ইবন আখতাব অবরোধে বনু কুরাইজাকে চুক্তি থেকে সরাবার চেষ্টা করেন; সিরাত একে যুদ্ধে বিশ্বাসঘাতকতা মানে, যার পর রায় তাঁদের মিত্র সাদ ইবন মুআয رضي الله عنه-এর আইনে হয়।

আহযাব সরে গেলে মদিনা সহজ শিকার থাকে না। বদর–উহুদ–খন্দক শহরের ঢাল: সেই বিজয় যা ফুরকান নাম দেয়, সেই ক্ষত যা শৃঙ্খলা শেখায়, সেই অবরোধ যা আল্লাহ বাতাসে ভাঙেন। মাগাজির ছাত্র তিনটিকে একসঙ্গে পড়ে।

এভাবে এই অধ্যায়ের প্রথম বিষয় ২, ৩ ও ৫ হিজরির তিন বড় যুদ্ধ, বদরের কূপ থেকে মদিনার পরিখা পর্যন্ত। আল্লাহ শহীদ ও পরিখা খননকারীদের প্রতি সন্তুষ্ট হোন।""",
    """Badar jatuh pada Jumat 17 Ramadan 2 H / Maret 624 M. Sekitar tiga ratus tiga belas muslim, bersenjata ringan, menghadapi pasukan perang Quraisy sekitar seribu orang. Al-Qur'an menamai hari itu Yaumul Furqan, Hari Pembeda (8:41). Empat belas muslim syahid—enam Muhajirin dan delapan Ansar dalam hitungan biasa. Quraisy kehilangan banyak yang terbunuh dan tertawan. Nabi ﷺ menghabiskan malam dalam doa; Allah mengirim malaikat sebagaimana Kitab menceritakan. Badar mengajar umat bahwa kemenangan dari Allah, bukan dari bilangan.

Setelah Badar, tawanan diperlakukan dengan tebusan dan pengajaran; sebagian yang pandai menulis mengajar anak-anak Madinah. Orang munafik di Madinah dan amarah Makkah menyiapkan ujian berikutnya. Nama-nama syuhada Badar masih dibaca dengan hormat. Hamzah, Ali, dan pemuda Ansar berperang dengan cara yang tidak jemu diceritakan maghazi.

Uhud datang pada 15 Syawal 3 H / Maret 625 M. Kaum muslimin unggul hingga para pemanah meninggalkan pos di bukit menentang perintah Nabi, mengejar harta. Khalid bin al-Walid, ketika itu masih bersama Quraisy, memutar kavaleri. Rasulullah ﷺ terluka di wajah, cincin helm menusuk pipi, dan desas-desus bahwa beliau terbunuh tersebar. Hamzah bin Abdul Muththalib radhiyallahu anhu syahid di tangan Wahsyi. Sekitar tujuh puluh muslim gugur. Surah Ali Imran membaca Uhud sebagai ujian setelah anugerah Badar.

Pelajaran Uhud adalah ketaatan dan kesabaran, bukan putus asa. Nabi ﷺ memakamkan syuhada di lapangan. Beliau mengejar musuh menuju Hamra al-Asad agar Quraisy tidak kembali ke Madinah. Mereka yang lari tidak dihinakan selamanya; Al-Qur'an menyeru mereka bertobat. Ahlus Sunnah menuturkan pertempuran itu tanpa mencela sahabat yang tergelincir hari itu.

Khandaq, Ghazwatul Ahzab, pada Syawal 5 H / 627 M. Konfederasi—Quraisy, Ghatafan, dan lain-lain—mengepung Madinah. Salman al-Farisi radhiyallahu anhu mengusulkan parit, metode yang dikenal di Persia. Para sahabat menggali dalam dingin dan lapar; Nabi ﷺ mengikat batu ke perutnya dan memukul batu di parit dengan kabar pembukaan kelak. Pengepungan berlangsung berminggu-minggu. Angin kencang dan gagalnya koalisi ada dalam Surah al-Ahzab (33:9). Huyay bin Akhthab berupaya menarik Bani Quraizah dari perjanjian selama pengepungan; pelanggaran itu diperlakukan dalam sirah sebagai pengkhianatan dalam perang, setelah itu keputusan mengikuti hukum sekutu mereka Sa'd bin Muaz radhiyallahu anhu.

Ketika konfederasi mundur, Madinah bukan lagi hadiah mudah. Urutan Badar–Uhud–Khandaq adalah perisai kota: kemenangan yang menamai pembeda, luka yang mengajar disiplin, dan pengepungan yang Allah pecahkan dengan angin. Penuntut maghazi membaca ketiganya bersama.

Dengan itu butir pertama bab ini adalah tritunggal pertempuran besar tahun 2, 3, dan 5 H, dari sumur Badar hingga parit Madinah. Semoga Allah meridai para syuhada dan penggali parit.""",
)









