# -*- coding: UTF-8 -*- 
import jieba


# seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
# print("Full Mode: " + "/ ".join(seg_list))

# seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
# print("Default Mode: " + "/ ".join(seg_list))

# import jieba

# seg_list = jieba.cut('國民黨主席吳敦義昨接受媒體專訪時，又創新名詞，除了「徵召領表」外，又新增「特邀」一詞，希望能讓黨內最強人選參加總統初選，新北市前市長朱立倫今天受訪時依舊強調，他這幾天講得很清楚，徵召就大大方方徵召，高雄市長韓國瑜今天回國，希望吳敦義盡快跟韓國瑜見面表達主席與中央的意見，還有黨員的期待，如果韓國瑜願意接受徵召，整件事情就很單純，大大方方徵召，全黨團結一致打贏選戰。', cut_all=False)
# print(' | '.join(seg_list))


import jieba

article1 = '國民黨主席吳敦義昨接受媒體專訪時，又創新名詞，除了「徵召領表」外，又新增「特邀」一詞，希望能讓黨內最強人選參加總統初選，新北市前市長朱立倫今天受訪時依舊強調，他這幾天講得很清楚，徵召就大大方方徵召，高雄市長韓國瑜今天回國，希望吳敦義盡快跟韓國瑜見面表達主席與中央的意見，還有黨員的期待，如果韓國瑜願意接受徵召，整件事情就很單純，大大方方徵召，全黨團結一致打贏選戰。媒體詢問，立法院前院長王金平將於4月初要跟韓國瑜會面，朱立倫有沒有計畫見韓國瑜？朱立倫反問，他不是兩周前才跟韓國瑜見面嗎？他希望大家可以多見面多聊聊，全黨團結一致，大家期待的是2020年國民黨勝選、台灣贏、中華民國贏。朱立倫話鋒一轉說，大家看到總統蔡英文與前閣揆賴清德之爭，原來原因是賴清德認為蔡英文承諾的台獨與特赦阿扁沒有做到，這讓民眾看清楚，原來民進黨有這麼多交易與政治陰謀論。朱立倫表示，全黨最重要是團結一致，為什麼他說大大方方徵召，讓事情單純化，因為初選下去總是要紛爭兩、三個月，民眾也不想看到這樣的情況，所以他才希望盡快有結論。對於通訊傳播委員會（NCC）開罰特定媒體，朱立倫表示，他希望台灣不要因為政治立場不同，就對特定媒體用懷有政治目地的處法，過去國民黨執政到今天，也有很多特定媒體不斷攻擊藍軍，這是不是也要開罰。立法院前院長王金平的臉書粉絲專頁「台灣公道伯」，則po出一張陷阱卡，還說發動的效果有三，包括額外召喚一名玩家，無須準備任何資源；受召喚玩家具有口頭發動獲勝的選擇權；可讓所有參與玩家陷入困惑及憤怒狀態，卡片中還有一隻白海豚，嘲諷黨中央的意味十足。'

article2 = '韓國瑜昨晚接受廈門台商協會晚宴招，致詞時提到自己當高雄市長3個月來，最有感的就是高雄市民出現光榮感，並表示高雄人以前賺不到錢、笑不出來，「貧賤夫妻百事哀，如何笑得出來呢？」對此，民進黨議員高閔琳怒批：「高雄人貧賤？」「你才貧賤，你全家都貧賤！」韓國瑜表示，以前高雄因經濟不好、賺不到錢，他上任後庶民經濟開始活絡，各行各業都感到欣欣向榮。他說，高雄人本來就是全台最熱情，只是以前賺不到錢、笑不出來，還說「貧賤夫妻百事哀，如何笑得出來呢？」高閔琳在臉書發文，「剛剛我睡著，夢到一些人對話：『蛤，誰貧賤？』『高雄人貧賤？』『你才貧賤，你全家都貧賤！』」她說，2009年高雄主辦世界運動會的時候，全世界看到台灣、看到高雄；「我們高雄人都好光榮、為這座城市感到驕傲；不知道那個時候韓市長在哪裡？還在又老又窮？」「不知道偉哉救苦救難宇宙的救星韓國瑜市長是不是當時就是剛好在2009年的那個時候，在北京大學的光華學院讀書，然後聽說沒唸完？」高閔琳酸，不知道「眷村子弟」、「國民黨員」韓國瑜市長，是不是就是在北京的那段期間被中共吸收，吸收滿腦共產黨的思想和語言，認識了無數中共各地高幹和御用學者；所以由藍轉紅呢？「如果本身就是紅的，哪裡還需要人家抹？」她怒批，「絕口不提中華民國、滿嘴支持一國兩制，這就是中共的信徒，這就是共匪的同路人！這就是出賣中華民國和台灣！」'

article3 = '高雄市長韓國瑜率市府團隊出訪港澳大陸，還與中央駐港聯絡辦公室(中聯辦)主任王志民見面，讓前總統陳水扁大為不滿，錄製了長達25分鐘的批韓內容PO在《臉書》，痛斥「韓國瑜不要再騙了」，還說「如果韓國瑜當總統，大家一起死。」陳水扁在影片中直接表明要批判韓國瑜，「韓國瑜市長你不要再騙了，你騙高雄人不夠還要騙台灣人，要當台灣總統，我不相信高雄人這麼好騙，我更不相信，善良的台灣人有這麼好騙。」陳水扁認為，韓國瑜表態支持九二共識，就是接受一中原則、一國兩制，認為過去馬英九也不敢這麼說，「只說接受一中各表的九二共識。」陳水扁最後並說出重話：「如果讓韓國瑜明年不幸當選總統，人進來貨出去，發大財變成解放軍進來，台灣人出去，大家一起死，你要嗎？」'

jieba.load_userdict('dict.txt')
segs_gen = jieba.cut(article1, cut_all=False)
segs = ('|'.join(segs_gen)).split('|')

times1 = {}

for seg in segs:
    if seg not in times1:
        times1[seg] = 1
    else:
        times1[seg] = times1[seg] + 1

ignores = [
   '，', '。', '：', '；', '、', '！', '？', '」', '「',
   '的', '也', '與', '有', '你', '我', '你', '妳', '他', '她'
]

times1_view = [(v, k) for k, v in times1.items() if k not in ignores]
times1_view.sort(reverse=True)
times1_view = times1_view[:5]

for v, k in times1_view:
    print("%s: %d" % (k,v))
