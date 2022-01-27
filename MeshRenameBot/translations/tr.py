class TrTrans:
    
    WRONG_VALUE_ERROR = "{} değişkeni için geçersiz değer girildi."
    
    START_MSG = """Selam, ben Telegram için yeniden dosya adlandırma botuyum. Nasıl kullanacağını öğrenmek için /help komutunu kullan.

❗ Eğer bot çalışmıyorsa @lambdarmageddonn'a bildir.
"""
     
    CANCEL_MESSAGE = "Yeniden adlandırma işlemi iptal edildi. Yakında güncellenecek."
    
    RENAME_NO_FILTER_MATCH = "EŞLEŞEN FİLTRE BULUNAMADI, YENİDEN ADLANDIRMA İPTAL EDİLİYOR. \nDosyaları yeniden adlandırmak için filtreleri kullanıyorsunuz. Ancak bir filtre belirtilmemiş. /filters komutunu kullanarak filtrelerinizi yönetin."

    RENAME_FILTER_MATCH_USED = "Dosyaları yeniden adlandırmak için filtreleri kullanıyorsunuz. Ancak bir filtre belirtilmemiş. /filters komutunu kullanarak filtrelerinizi yönetin."

    RENAME_NOFLTR_NONAME = "Dosya adını bu formatta girin:- ```/rename dosya-adı.uzantı``` ya da ```Bazı yeniden adlandırma filtrelerini ayarlamak için /filters komutunu kullanın.```"

    RENAME_CANCEL = "Yeniden adlandırmayı iptal et."

    RENAMING_FILE = "Dosya yeniden adlandırılıyor beklemede kalın."
    
    DL_RENAMING_FILE = "Dosya indiriliyor, beklemede kalın."

    RENAME_ERRORED_REPORT = "Bu indirme hata ile sonuçlandı. Hatayı bildirin."

    RENAME_CANCEL_BY_USER = "Yeniden adlandırma kullanıcı tarafından iptal edildi."

    FLTR_ADD_LEFT_STR = "Ek filtre: <code>{}</code> <code>Sola</code>"
    FLTR_ADD_RIGHT_STR = "Ek filtre: <code>{}</code> <code>Sağa</code>"
    FLTR_RM_STR = "Filtreyi kaldır: <code>{}</code>"
    FLTR_REPLACE_STR = "Filtreyi değiştir: <code>{}</code> with <code>{}</code>"

    CURRENT_FLTRS = "Mevcut filtreleriniz:-"
    ADD_FLTR = "Filtre Ekle."
    RM_FLTR = "Filtre kaldır."

    FILTERS_INTRO = """
Filtre eklemeye hoş geldiniz.
3 tip filtre vardır.

Filtre değiştirme:- Bu filtre, belirttiğin bir filtreyi verdiğin kelime ile değiştirir.

Filtre eki:- Bu filtre verilen kelimeyi sonuna veya başına ekleyecektir.

Remove Filter:- Bu filtre verilen kelimeyi dosya adından kaldırır.

"""

    ADD_REPLACE_FLTR = "Değiştirme filtresi ekle."
    ADD_ADDITION_FLTR = "Ek filtre ekle."
    ADD_REMOVE_FLTR = "Kaldırma filtresi ekle"
    BACK = "Geri."

    REPALCE_FILTER_INIT_MSG = "Mesajı bu formatta gönder. <code>değiştirilecek | değiştirilen</code> ya da geriye gitmek için /igrone komutunu kullanın. \n'|' <- Bunun öncesindeki ve sonrasındaki boşluklara dikkat edin. Bot bunları farklı algılayacak."

    NO_INPUT_FROM_USER = "Sizden herhangi bir girdi alınmadı."
    INPUT_IGNORE = "Sizden iptal etme girdisi alındı."
    WRONG_INPUT_FORMAT = "Girdi geçerli değil. Verilen formatı kontrol edin."
    REPLACE_FILTER_SUCCESS = "Değiştirme filtresi başarılı. <code>'{}'</code> , bununla değiştirilecek -> <code>'{}'</code>."

    ADDITION_FILTER_INIT_MSG = "Eklemek istediğiniz metni girin ya da geri dönmek için /igrone komutunu kullanın."

    ADDITION_FILTER_SUCCESS_LEFT = "Ek filtresi başarıyla eklendi. <code>{}</code> , <code>LEFT</code>'e eklenecek."

    ADDITION_FILTER_SUCCESS_RIGHT = "Ek filtresi başarıyla eklendi. <code>{}</code>, <code>RIGHT</code>'a eklenecek."

    ADDITION_LEFT = "Sola ek"
    ADDITION_RIGHT = "Sağa ek"

    ADDITION_POSITION_PROMPT = "Metni nereye eklemek istiyorsunuz?"

    REMOVE_FILTER_INIT_MSG = "Kaldırmak istediğiniz metni girin ya da geri dönmek için /igrone komutunu kullanın."

    REMOVE_FILTER_SUCCESS = "Kaldırma filtresi başarıyla eklendi. <code>{}</code> kaldırılacak."

    REPLY_TO_MEDIA = "Dosyayı /rename ile yanıtlayın."

    HELP_STR = """
`/start` - Botun çalıştığını kontrol eder.
`/rename` - Medyayı `/rename dosya adı.uzantı` ile yanıtlayın. Eğer sadece `/rename` kullanıldıysa filtreler kullanılacak.
`/filters` - Ekle/Kaldır filtreleri. Bunların ne olduğunu görmek için bu komutu kullanın.
`/setthumb` - Küçük resmi kalıcı olarak ayarlamak için resme yanıt verin.
`/getthumb` - Şu anda ayarlanmış olan küçük resmi alın.
`/clrthumb` - Ayarlanan küçük resmi kaldırın.
`/mode` - 3 mod arasında seçim yapın:-
    - Gönderildiği formatla aynı. [Doküman gönderilirse doküman yüklenir, video gönderilirse video yüklenir.]
    - Dökümana zorlayın. [Her doküman dosya olarak yüklenir.]
    - Genel medyayı yükleyin. [Stream olarak video/ses vb.]
`/queue` - Yeniden adlandırma durumunuzu ve bottaki yüklenmeyi verir.
    """