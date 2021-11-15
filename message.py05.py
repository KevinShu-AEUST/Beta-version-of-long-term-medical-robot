#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

#ImagemapSendMessage(組圖訊息)
def imagemap_message():
    message = ImagemapSendMessage(
        base_url="https://i.imgur.com/BfTFVDN.jpg",
        alt_text='最新的合作廠商有誰呢？',
        base_size=BaseSize(height=2000, width=2000),
        actions=[
            URIImagemapAction(
                #家樂福
                link_uri="https://tw.shop.com/search/%E5%AE%B6%E6%A8%82%E7%A6%8F",
                area=ImagemapArea(
                    x=0, y=0, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                #生活市集
                link_uri="https://tw.shop.com/search/%E7%94%9F%E6%B4%BB%E5%B8%82%E9%9B%86",
                area=ImagemapArea(
                    x=1000, y=0, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                #阿瘦皮鞋
                link_uri="https://tw.shop.com/search/%E9%98%BF%E7%98%A6%E7%9A%AE%E9%9E%8B",
                area=ImagemapArea(
                    x=0, y=1000, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                #塔吉特千層蛋糕
                link_uri="https://tw.shop.com/search/%E5%A1%94%E5%90%89%E7%89%B9",
                area=ImagemapArea(
                    x=1000, y=1000, width=1000, height=500
                )
            ),
            URIImagemapAction(
                #亞尼克生乳捲
                link_uri="https://tw.shop.com/search/%E4%BA%9E%E5%B0%BC%E5%85%8B",
                area=ImagemapArea(
                    x=1000, y=1500, width=1000, height=500
                )
            )
        ]
    )
    return message

#TemplateSendMessage - ButtonsTemplate (按鈕介面訊息)
def buttons_message():
    message = TemplateSendMessage(
        alt_text='好消息來囉～',
        template=ButtonsTemplate(
            thumbnail_image_url="https://images.goodsmile.info/cgm/images/product/20190426/8309/60001/large/a8bfd57f527dd83d47f3c383390b8ee3.jpg",
            #thumbnail_image_url="https://pic2.zhimg.com/v2-de4b8114e8408d5265503c8b41f59f85_b.jpg",
            title="是否要進行抽獎活動？",
            text="輸入生日後即獲得抽獎機會",
            actions=[
                DatetimePickerTemplateAction(
                    label="請選擇生日",
                    data="input_birthday",
                    mode='date',
                    initial='1990-01-01',
                    max='2019-03-10',
                    min='1930-01-01'
                ),
                MessageTemplateAction(
                    label="看抽獎品項",
                    text="有哪些抽獎品項呢？"
                ),
                URITemplateAction(
                    label="免費註冊享回饋",
                    uri="https://tw.shop.com/nbts/create-myaccount.xhtml?returnurl=https%3A%2F%2Ftw.shop.com%2F"
                )
            ]
        )
    )
    return message

#TemplateSendMessage - ConfirmTemplate(確認介面訊息)
def Confirmloli_Template():

    message = TemplateSendMessage(
        alt_text='請選擇療癒方式',
        template=ConfirmTemplate(
            text="請選擇療癒方式",
            actions=[
                PostbackTemplateAction(
                    label="天竺鼠車車",
                    text="比起真鼠，我更喜歡卡哇伊的天竺鼠車車",
                    data="會員註冊"
                ),
                MessageTemplateAction(
                    label="真實天竺鼠",
                    text="當然是真鼠賽高啊!"
                )
            ]
        )
    )
    return message
def Confirm_Template():

    message = TemplateSendMessage(
        alt_text='請問您要尋找亞東醫院附近的藥局還是醫療器材店?',
        template=ConfirmTemplate(
            text="請問您要尋找亞東醫院附近的藥局還是醫療器材店?",
            actions=[
                PostbackTemplateAction(
                    label="藥局",
                    text="讓我看看附近的藥局吧!",
                    data="會員註冊"
                ),
                MessageTemplateAction(
                    label="醫療器材店",
                    text="讓我看看附近的醫療器材店吧!"
                )
            ]
        )
    )
    return message
###########################111111111111111111111111111111
def Confirm22_Template():

    message = TemplateSendMessage(
        alt_text='醫療器材店不只賣醫療器材，還有賣相關商品，能接受嗎?',
        template=ConfirmTemplate(
            text="醫療器材店不只賣醫療器材，還有賣相關商品，能接受嗎?",
            actions=[
                PostbackTemplateAction(
                    label="能",
                    text="快帶我去!!!",
                    data="會員註冊"
                ),
                MessageTemplateAction(
                    label="不能",
                    text="我才不去!!!"
                )
            ]
        )
    )
    return message

#旋轉木馬按鈕訊息介面

def Carousel_Template():
    message = TemplateSendMessage(
        alt_text='一則旋轉木馬按鈕訊息',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://medlight.com.tw/upload/2019_06_111/20190611180511g1p8l9B7516.png',              
                    title='維康醫療用品店',
                    text='離亞東醫院最近的藥局',
                    actions=[
                         MessageTemplateAction(
                            label='客服電話',
                            text='我想看維康藥局的客服電話'
                        ),
                        MessageTemplateAction(
                            label='藥局地點',
                            text='我想看維康藥局在哪'
                        ),
                        URITemplateAction(
                            label='官方網站',
                            uri='http://www.wellcare.com.tw/wellindex/new-map/page/if-2/2-newtaipei-2.htm'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://twypage.com/company-picture-%E5%88%A9%E5%AE%89%E7%A4%BE%E5%8D%80%E8%97%A5%E5%B1%80.jpg',
                    title='利安社區藥局',
                    text='猜您喜歡的藥局',
                    actions=[
                       MessageTemplateAction(
                            label='客服電話',
                            text='我想看利安社區藥局的客服電話'
                        ),
                        MessageTemplateAction(
                            label='藥局地點',
                            text='我想看利安社區藥局在哪'
                        ),
                        URITemplateAction(
                            label='更多關於此店資訊',
                            uri='https://twhi.iwiki.tw/tag/%E5%88%A9%E5%AE%89%E7%A4%BE%E5%8D%80%E8%97%A5%E5%B1%80%E7%87%9F%E6%A5%AD%E6%99%82%E9%96%93/'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://alltwcompany.com/comapny-image-%E4%BA%9E%E5%AD%A3%E8%97%A5%E5%B1%80.jpg',
                    title='亞季藥局',
                    text='猜您喜歡的藥局',
                    actions=[
                        MessageTemplateAction(
                            label='客服電話',
                            text='我想看亞季藥局的客服電話'
                        ),
                        MessageTemplateAction(
                            label='藥局地點',
                            text='我想看亞季藥局在哪'
                        ),
                        URITemplateAction(
                            label='更多資訊',
                            uri='https://drug.lifego.tw/%E8%97%A5%E5%B1%80-%E4%BA%9E%E5%AD%A3%E8%97%A5%E5%B1%80-44701'
                        )
                    ]
                )
            ]
        )
    )
    return message

#TemplateSendMessage - ImageCarouselTemplate(圖片旋轉木馬)
def image_carousel_message1():
    message = TemplateSendMessage(
        alt_text='圖片旋轉木馬',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/uKYgfVs.jpg",
                    action=URITemplateAction(
                        label="新鮮水果",
                        uri="http://img.juimg.com/tuku/yulantu/110709/222-110F91G31375.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/QOcAvjt.jpg",
                    action=URITemplateAction(
                        label="新鮮蔬菜",
                        uri="https://cdn.101mediaimage.com/img/file/1410464751urhp5.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/Np7eFyj.jpg",
                    action=URITemplateAction(
                        label="可愛狗狗",
                        uri="http://imgm.cnmo-img.com.cn/appimg/screenpic/big/674/673928.JPG"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/QRIa5Dz.jpg",
                    action=URITemplateAction(
                        label="可愛貓咪",
                        uri="https://m-miya.net/wp-content/uploads/2014/07/0-065-1.min_.jpg"
                    )
                )
            ]
        )
    )
    return message
##############
##############
############
################
def Carouse2_Template():
    message = TemplateSendMessage(
        alt_text='一則旋轉木馬按鈕訊息',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://cf.shopee.tw/file/b239b14b64f6bdcce091acddb2071ac5',
                    title='杏一醫療器材店',
                    text='猜您喜歡',
                    actions=[
                        MessageTemplateAction(
                            label='客服電話',
                            text='我想看杏一醫療器材店的客服電話'
                        ),
                        MessageTemplateAction(
                            label='藥局地點',
                            text='我想看杏一醫療器材店在哪'
                        ),
                        URITemplateAction(
                            label='官方網站',
                            uri='http://www.medfirst.com.tw/'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://data.zhupiter.com/img-%E5%AE%8F%E5%AE%87%E9%86%AB%E7%99%82%E5%99%A8%E6%9D%90%E8%A1%8C.png',
                    title='宏宇醫療器材行',
                    text='猜您喜歡',
                    actions=[
                        MessageTemplateAction(
                            label='客服電話',
                            text='我想看宏宇醫療器材店的客服電話'#'0289677211'
                        ),
                        MessageTemplateAction(
                            label='藥局地點',
                            text='我想看宏宇醫療器材行在哪'
                        ),
                        URITemplateAction(
                            label='更多資訊',
                            uri='https://www.facebook.com/pages/category/Shopping---Retail/%E5%AE%8F%E5%AE%87%E9%86%AB%E7%99%82%E5%99%A8%E6%9D%90%E8%A1%8C-161378012291159/'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://alltwcompany.com/comapny-image-%E5%BA%B7%E9%81%A9%E7%BE%8E%E5%81%A5%E5%BA%B7%E5%AF%A6%E6%A5%AD.jpg',
                    title='康適美健康實業',
                    text='猜您喜歡',
                    actions=[
                        MessageTemplateAction(
                            label='客服電話',
                            text='我想看康適美健康實業的客服電話'#'0289677211'
                        ),
                        MessageTemplateAction(
                            label='藥局地點',
                            text='我想看康適美健康實業在哪'
                        ),
                        URITemplateAction(
                            label='更多資訊',
                            uri='http://comesmile.com.tw/'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://lh3.googleusercontent.com/proxy/CcBQxaXBuCfxfvyH6gT9waSgKvujSYS-l42_jJ8VPVd5lAjRHqC87w4Jw2Z_xaUW4Y_fK6ITdloLOP5SS91vFNHTYaS97hOLAgU2x2zNn-5OxxfEBmJ7',
                    title='大瀚醫療儀器有限公司',
                    text='猜您喜歡',
                    actions=[
                        MessageTemplateAction(
                            label='客服電話',
                            text='我想看大瀚醫療儀器有限公司的客服電話'
                        ),
                        MessageTemplateAction(
                            label='藥局地點',
                            text='我想看大瀚醫療儀器有限公司在哪'
                        ),
                        URITemplateAction(
                            label='更多資訊',
                            uri='http://gogodh.com.tw/'
                        )
                    ]
                )
            ]
        )
    )
    return message
def zoo():
    message = TemplateSendMessage(
        alt_text='一則旋轉木馬按鈕訊息',
        template=CarouselTemplate(
        columns=[
                CarouselColumn(
                    thumbnail_image_url='https://acadm.cycu.edu.tw/wp-content/uploads/QA.png',
                    title='Q&A',
                    text='猜您喜歡',
                    actions=[
                        MessageTemplateAction(
                            label='什麼是長照服務？',
                            text='什麼是長期照顧服務？'
                        ),
                        MessageTemplateAction(
                            label='長照服務補助對象?',
                            text='請問長期照顧服務補助對象?'
                        ),
                        MessageTemplateAction(
                            label='長照有補助?',
                            text='請問長期照顧服務有沒有補助?'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://acadm.cycu.edu.tw/wp-content/uploads/QA.png',
                    title='Q&A',
                    text='猜您喜歡',
                    actions=[
                        MessageTemplateAction(
                            label='如何申請長照服務?',
                            text='如何申請長期照顧服務?'
                        ),
                        MessageTemplateAction(
                            label='申請長照服務流程為?',
                            text='申請長期照顧服務流程為何?'
                        ),
                        MessageTemplateAction(
                            label='長照服務項目有哪些?',
                            text='長期照顧服務項目有哪些?'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://acadm.cycu.edu.tw/wp-content/uploads/QA.png',
                    title='Q&A',
                    text='猜您喜歡',
                    actions=[
                        MessageTemplateAction(
                            label='什麼是喘息服務？',
                            text='什麼是喘息服務？'
                        ),
                        MessageTemplateAction(
                            label='可以去醫院照顧嗎？',
                            text='可以去醫院幫忙照顧嗎？'
                        ),
                        MessageTemplateAction(
                            label='家附近有哪些長照資源？',
                            text='自己的家附近有哪些長照資源？'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://acadm.cycu.edu.tw/wp-content/uploads/QA.png',
                    title='Q&A',
                    text='猜您喜歡',
                    actions=[
                        MessageTemplateAction(
                            label='關於身障等級Q&A',
                            text='身心障礙證明/手冊障礙等級為輕度，等於長照中心的輕度失能？'
                        ),
                        MessageTemplateAction(
                            label='關於環境整理Q&A',
                            text='被照顧者有家屬同住可以請居家服務的照顧服務員協助環境管理嗎？'
                        ),
                        MessageTemplateAction(
                            label='關於環境整理Q&A',
                            text='居家服務中的環境整理項目是否包含與家人同住的公共區域清潔服務?'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://acadm.cycu.edu.tw/wp-content/uploads/QA.png',
                    title='Q&A',
                    text='猜您喜歡',
                    actions=[
                        MessageTemplateAction(
                            label='什麼是照顧服務員Q&A',
                            text='想要知道什麼是照顧服務員'
                        ),
                        MessageTemplateAction(
                            label='關於照顧服務員資格Q&A',
                            text='請問照顧服務員資格'
                        ),
                        MessageTemplateAction(
                            label='關於照顧服務員考證照Q&A',
                            text='請問照顧服務員考證照需要注意什麼事項'
                        )   
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://acadm.cycu.edu.tw/wp-content/uploads/QA.png',
                    title='Q&A',
                    text='猜您喜歡',
                    actions=[
                        MessageTemplateAction(
                            label='關於鼻胃管Q&A',
                            text='想要瞭解鼻胃管灌食步驟'
                        ),
                        MessageTemplateAction(
                            label='關於鼻胃管的注意事項Q&A',
                            text='請問鼻胃管灌食注意事項'
                        ),
                        MessageTemplateAction(
                            label='關於鼻胃管灌食步驟Q&A',
                            text='想要瞭解鼻胃管灌食步驟'
                        ) 
                    ]
                )
            ]
        )
    )
    return message
#12345678
def ttt():
    message = TemplateSendMessage(
        alt_text='一則旋轉木馬按鈕訊息',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://cw1.tw/CW/images/article/C1432694965358.jpg',
                    title='其他實用功能',
                    text='猜您喜歡',
                    actions=[
                        MessageTemplateAction(
                            label='亞東附近吃的',
                            text='亞東附近吃的'#'0289677211'
                        ),
                        MessageTemplateAction(
                            label='其他長期照顧資訊',
                            text='其他長期照顧資訊'
                        ),
                        MessageTemplateAction(
                            label='長照影片',
                            text='長照影片'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://cw1.tw/CW/images/article/C1432694965358.jpg',
                    title='其他實用功能',
                    text='猜您喜歡',
                    actions=[
                        MessageTemplateAction(
                            label='照服員考試資訊',
                            text='照服員考試資訊'#'0289677211'1111111111
                        ),
                        MessageTemplateAction(
                            label='其他長照服務項目',
                            text='其他長照服務項目'
                        ),
                        MessageTemplateAction(
                            label='翻譯機器人',
                            text='翻譯機器人'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://cw1.tw/CW/images/article/C1432694965358.jpg',
                    title='其他實用功能',
                    text='猜您喜歡',
                    actions=[
                        MessageTemplateAction(
                            label='台灣確診人數',
                            text='台灣目前確診人數'#'0289677211'
                        ),
                        MessageTemplateAction(
                            label='台灣新增確診數',
                            text='台灣新增確診數'
                        ),
                        URITemplateAction(
                            label='更多疫情資訊',
                            uri='https://covid-19.nchc.org.tw/'
                        )
                    ]
                )
            ]
        )
    )
    return message



    














#關於LINEBOT聊天內容範例