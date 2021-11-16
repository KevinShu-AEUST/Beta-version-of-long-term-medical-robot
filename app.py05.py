from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


#======這裡是呼叫的檔案內容=====
from message import *
from new import *
from Function import *
from yiy import *
#======這裡是呼叫的檔案內容=====
import requests
from bs4 import BeautifulSoup
import re
import configparser
#======python的函數庫==========
import tempfile, os
import datetime
import time
#======python的函數庫==========

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('qGoQrowCYO+4kXJQvVjlfnvrZchKiWQ4wGu5LwD20ldIaZ5gptBjSllBLI7f0plCeEO7y6VeC+R2YbgZNaaCY7SyBL4Xa0jYwY7s0nu4ggwEGOyD0Fbk4/hAKo0yJudDR2i9DMPEvdmGGZKVaXKuSwdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('32a3ef582ed90a1a1738f4cefdd39385')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'
#案1開始

# 處理訊息1
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    if '最新合作廠商' in msg:
        message = imagemap_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '台灣目前確診人數' in msg :#查看台灣確診數
        message = TextSendMessage(text=insect4()+insect3())
        line_bot_api.reply_message(event.reply_token, message)
    elif '台灣新增確診數' in msg :#查看台灣新增確診數
        message = TextSendMessage(text=insect5()+insect6())
        line_bot_api.reply_message(event.reply_token, message)
    elif '最新活動訊息' in msg:
        message = buttons_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '1' in msg:
        message = LocationSendMessage(
            title = "亞東醫院附近",
            address = "亞東醫院附近",
            latitude =  24.99732,
            longitude = 121.45302
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif '2' in msg:
        message = Confirm_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '3' in msg:
        message = ttt()
        line_bot_api.reply_message(event.reply_token, message)
    elif '4' in msg :
        message = [
        TextSendMessage(
        #type= 'text',
        text= '這功能是讓病人看看可愛圖片，以達到心靈療癒的效果'
      ),
        Confirmloli_Template(
        #type= TextSendMessage,
        #text= 'reply message 3'
      )]
        line_bot_api.reply_message(event.reply_token, message)
    elif '比起真鼠，我更喜歡卡哇伊的天竺鼠車車' in msg :
        message = [
        ImageSendMessage(
        original_content_url='https://www.niusnews.com/upload/imgs/default/2021Feb_CHOU/0224LINE/batch_sticker-7.jpg',
        preview_image_url='https://www.niusnews.com/upload/imgs/default/2021Feb_CHOU/0224LINE/batch_sticker-7.jpg'
        ),
        ImageSendMessage(
        original_content_url='https://i.ytimg.com/vi/_6TtTRrno3E/maxresdefault.jpg',
        preview_image_url='https://i.ytimg.com/vi/_6TtTRrno3E/maxresdefault.jpg'
        ),
        ImageSendMessage(
        original_content_url='https://static.popdaily.com.tw/u/202101/e638ed95-069a-4123-843a-9165971741c4.jpg',
        preview_image_url='https://static.popdaily.com.tw/u/202101/e638ed95-069a-4123-843a-9165971741c4.jpg'   
        )]
        line_bot_api.reply_message(event.reply_token, message)
        ####
    elif '當然是真鼠賽高啊!' in msg :
        message = [
        ImageSendMessage(
        original_content_url='https://s.newtalk.tw/album/news/525/6005167706521.jpg',
        preview_image_url='https://s.newtalk.tw/album/news/525/6005167706521.jpg'
        ),
        ImageSendMessage(
        original_content_url='https://www.hikari-tw.com/image/catalog/article/5.small/shutterstock_694688611-s.jpg',
        preview_image_url='https://www.hikari-tw.com/image/catalog/article/5.small/shutterstock_694688611-s.jpg'
        ),
        ImageSendMessage(
        original_content_url='https://attach.setn.com/newsimages/2019/12/26/2324167-PH.jpg',
        preview_image_url='https://attach.setn.com/newsimages/2019/12/26/2324167-PH.jpg'
        ),
        ImageSendMessage(
        original_content_url='https://imgs.gvm.com.tw/upload/gallery/20210126/77453_01.jpg',
        preview_image_url='https://imgs.gvm.com.tw/upload/gallery/20210126/77453_01.jpg'
        )
        ]
        line_bot_api.reply_message(event.reply_token, message)
    elif '讓我看看附近的藥局吧!' in msg :
        message = Carousel_Template()
        line_bot_api.reply_message(event.reply_token, message)
        ####
    elif '讓我看看附近的醫療器材店吧!' in msg :
        message = Confirm22_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '快帶我去!!!' in msg :
        message = Carouse2_Template()
        line_bot_api.reply_message(event.reply_token, message)
    
        #呼較旋轉木馬的文字
    
        #呼較旋轉木馬的文字
    elif '我想看亞東醫院附近有哪些藥局' in msg :
        message = Carousel_Template()
        line_bot_api.reply_message(event.reply_token, message)
        #維康藥局的旋轉木馬
    elif '我想看維康藥局的客服電話' in msg :
        message = TextSendMessage(text="0289669912")
        line_bot_api.reply_message(event.reply_token, message)
        #維康藥局的旋轉木馬
    elif '我想看維康藥局在哪' in msg:
        message = LocationSendMessage(
            title = "維康醫療用品店",
            address = "220新北市板橋區南雅南路二段21號亞東新院區B1樓",
            latitude =  24.99733,
            longitude = 121.45284
        )
        line_bot_api.reply_message(event.reply_token, message)
        #利安社區藥局旋轉木馬
    elif '我想看利安社區藥局的客服電話' in msg :
        message = TextSendMessage(text="0289671551")
        line_bot_api.reply_message(event.reply_token, message)###
    elif '我想看利安社區藥局在哪' in msg:
        message = LocationSendMessage(
            title = "利安社區藥局",
            address = "220新北市板橋區德興街37巷14號",
            latitude = 24.99409,
            longitude = 121.45416
        )
        line_bot_api.reply_message(event.reply_token, message)
     ###########亞季藥局旋轉木馬
    elif '我想看亞季藥局的客服電話' in msg :
        message = TextSendMessage(text="0289671131")
        line_bot_api.reply_message(event.reply_token, message)###
    elif '我想看亞季藥局在哪' in msg:
        message = LocationSendMessage(
            title = "亞季藥局",
            address = "220新北市板橋區南雅南路二段142巷11號",
            latitude = 24.99717,
            longitude = 121.45178
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif '圖片畫廊' in msg:
        message = test()
        line_bot_api.reply_message(event.reply_token, message)
    elif '功能列表' in msg:
        message = function_list()
        line_bot_api.reply_message(event.reply_token, message)
    elif '我想看杏一醫療器材店的客服電話' in msg :
        message = TextSendMessage(text=insect2())
        line_bot_api.reply_message(event.reply_token, message)
        #維康藥局的旋轉木馬
    elif '我想看杏一醫療器材店在哪' in msg:
        message = LocationSendMessage(
            title = "杏一醫療用品 亞東院前店",
            address = "22060新北市板橋區南雅南路二段21號",
            latitude =  24.99747,
            longitude = 121.45307
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif '我想看宏宇醫療器材店的客服電話' in msg :
        message = TextSendMessage(text=insect1())
        line_bot_api.reply_message(event.reply_token, message)
        #維康藥局的旋轉木馬
    elif '我想看宏宇醫療器材行在哪' in msg:
        message = LocationSendMessage(
            title = "宏宇醫療器材行",
            address = "220新北市板橋區南雅南路二段134號1樓",
            latitude =  24.99688,
            longitude = 121.45236
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif '我想看康適美健康實業的客服電話' in msg :
        message = TextSendMessage(text="0289668080")
        line_bot_api.reply_message(event.reply_token, message)
    elif '我想看康適美健康實業在哪' in msg:
        message = LocationSendMessage(
            title = "康適美健康實業",
            address = "220新北市板橋區南雅南路二段144巷6號",
            latitude =  24.99629, 
            longitude = 121.45118
        )
        line_bot_api.reply_message(event.reply_token, message)    
    elif '我想看大瀚醫療儀器有限公司的客服電話' in msg :
        message = TextSendMessage(text="0229539781")
        line_bot_api.reply_message(event.reply_token, message)
    elif '我想看大瀚醫療儀器有限公司在哪' in msg:
        message = LocationSendMessage(
            title = "大瀚醫療儀器有限公司",
            address = "新北市板橋區校前街28號",
            latitude =   25.00329,
            longitude =  121.46068
        )
        line_bot_api.reply_message(event.reply_token, message)   
    elif '什麼是長期照顧服務？' in msg :
        message = TextSendMessage(text='''長期照顧是針對身體功能缺損或因衰老或無法自我照顧的民眾，提供一
        系列持續性的服務。
        以恢復、維護或改善他們日常生活功能為目的，包括：
        1、身體照顧：如協助沐浴、換穿衣服、進食、翻身與使用輔具等。
        2、日常生活照顧：包括換洗衣物之洗滌或修補、文書服務、餐飲服務
        與陪同服務、居家環境整理（針對獨居或家人無能力處理之民眾）等。
        3、特殊照護（如居家護理）、身體功能缺損需要他人協助之民眾提供
        減輕功能障礙（如居家/社區復健、老人居家無障礙環境等）及家庭照
        顧者喘息服務（依服務模式及場所，可區分為居家式及機構式二類）。
        ''')
        line_bot_api.reply_message(event.reply_token, message)
    elif '請問長期照顧服務補助對象?' in msg :
        message = TextSendMessage(text='''1、65 歲以上之失能老人
        2、55 歲以上之失能原住民
        3、失能之身心障礙者
        4、僅工具性日常生活活動功能失能且獨居之老人
        5、50 歲以上之失智症患者
        6、65 歲以上之衰弱老人
        ''')
        line_bot_api.reply_message(event.reply_token, message)
    elif '請問長期照顧服務有沒有補助?' in msg :
        message = TextSendMessage(text='''1、以服務提供為主
        2、經評估失能程度不同，給予不同服務補助額度
        3、依據家庭經濟狀況，提供不同補助額度
        4、超過政府補助額度部分，由使用者全額自費使用服務
        ''')
        line_bot_api.reply_message(event.reply_token, message)
    elif '如何申請長期照顧服務?' in msg :
        message = TextSendMessage(text='''親洽：
        1、長期照顧管理中心（諮詢電話：049-2209595）
        2、各鄉鎮市衛生所（室）
        3、各鄉鎮市公所
        傳真申請：
        1、索取或網路下載申請單填寫後傳真，並電洽確認
        2、傳真電話：049-2247343
        ''')
        line_bot_api.reply_message(event.reply_token, message)
    elif '申請長期照顧服務流程為何?' in msg :
        message = TextSendMessage(text='''民眾可利用長期照顧服務申請管道提出服務之申請
        進行電話初步篩選，以了解其是否符合收案條件（如：年齡、福利身分
        別、失能狀況…等）
        符合收案條件者，安排時間進行家庭訪視評估，以了解是否符合開案條
        件並依民眾需求及意願，擬定照顧計畫並核定補助額度
        與服務提供單位聯繫，並安排民眾所需之各類照顧服務
        各類服務提供期間，持續追蹤及監督服務品質
        ''')
        line_bot_api.reply_message(event.reply_token, message)
    elif '長期照顧服務項目有哪些?' in msg :
        message = TextSendMessage(text='''1、居家護理
        2、居家（社區）復健
        3、喘息服務
        4、照顧服務（居家服務、日間照顧、家庭托顧）
        5、輔具購買、租借及居家無障礙環境改善
        6、老人營養餐飲服務
        7、交通接送服務
        8、長期照顧機構服務
        9、小規模多能服務
        10、失智症照顧服務
        11、家庭照顧者支持服務
        12、社區預防性照顧
        13、預防失能或延緩失能與失智之服務
        14、銜接出院準備服務
        15、銜接居家醫療
        16、原住民族地區整合型服務
        17、社區整體照顧模式
        ''')
        line_bot_api.reply_message(event.reply_token, message)
    elif '身心障礙證明/手冊障礙等級為輕度，等於長照中心的輕度失能？' in msg :
        message = TextSendMessage(text='''不是，身心障礙證明/手冊註記的輕度、中度、重度、極重度障礙等級
        並不等同長期照顧管理中心評估的輕度、中度、重度失能重度。
        ''')
        line_bot_api.reply_message(event.reply_token, message)
    elif '被照顧者有家屬同住可以請居家服務的照顧服務員協助環境管理嗎？' in msg :
        message = TextSendMessage(text='''長期照顧居家服務個案，如無特殊情形與子女共同居住者，其服務
        內容不提供家事服務。
        ''')
        line_bot_api.reply_message(event.reply_token, message)
    elif '居家服務中的環境整理項目是否包含與家人同住的公共區域清潔服務?' in msg :
        message = TextSendMessage(text='''沒有。
        居家環境整理服務內容僅限失能者日常生活起居空間範圍協助簡易環
        境維護，不包含擦拭天花板、洗抽油煙機、清洗流理台、清洗窗戶、打
        掃戶外、全家大掃除及爬高、搬動傢俱等過重物品，並非專業清潔工作
        內容。
        ''')
        line_bot_api.reply_message(event.reply_token, message)
    elif '照顧服務員可以每天都來家裡協助嗎？' in msg :
        message = TextSendMessage(text='''視實際情況而定。
        居家服務補助服務時間要視長期照顧管理中心評估個案失能程度及實
        際需求且經審查通過而定。若有額外需求、建議可自費方式使用。
        ''')
        line_bot_api.reply_message(event.reply_token, message)
    elif '什麼是喘息服務？' in msg :
        message = TextSendMessage(text='''家庭照顧者長期照顧失能的親屬導致身心疲憊，為了給予家庭照顧者更
        多的支持與關懷，予協助安排被照顧者入住機構接受照顧，或安排居家
        服務員至家中照顧被照顧者，讓家庭照顧者得以從持續照顧職責中獲得
        暫時休息的機會。
        依服務模式及場所，可分為居家式、機構式、社區式等三類
        ''')
        line_bot_api.reply_message(event.reply_token, message)
    elif '可以去醫院幫忙照顧嗎？' in msg :
        message = TextSendMessage(text='''目前長期照顧服務大致可分為居家式、社區式及機構式服務，倘民眾住
        院期間，須暫停服務，出院後可視情況恢復及調整服務內容。
        ''')
        line_bot_api.reply_message(event.reply_token, message)
    elif '自己的家附近有哪些長照資源？' in msg :
        message = TextSendMessage(text='''機構類資源的評鑑等級，可以幫助大家知道資源要在哪邊找。
        長期照顧管理中心亦提供長期照顧相關服務資源，連絡電話：
        049-2209595
        ''')
        line_bot_api.reply_message(event.reply_token, message)
    elif '想要知道什麼是照顧服務員' in msg :
        message = TextSendMessage(text='''照顧服務員（照服員），簡單來說就是受過專業訓練的長期照顧專家
        可以在機構裡或是到被照顧者家中提供服務。至於服務費用，目前是以稅收支應，具備申請資格者，
        依失能程度可分別核定每月約二十五至九十小時的居家服務。
        ''')
        line_bot_api.reply_message(event.reply_token, message)
    elif '請問照顧服務員資格' in msg :
        message = TextSendMessage(text='''第一方式 : 完成各縣市辦理的90小時以上照服班培訓課程，取得結訓證明
        第二方式 : 考取單一級照顧服務員證照，取得證照
        單一級照顧服務員證照檢定考試。
        ''')
        line_bot_api.reply_message(event.reply_token, message)  
    elif '請問照顧服務員考證照需要注意什麼事項' in msg :
        message = TextSendMessage(text='''通過照顧服務員訓練後，領取照顧服務員結業證書即可正式踏上照服員行列。
        但若想再進一步取得由勞動部核發的『照顧服務員單一級技術士技能證照』，只需要跟隨以下準備，並加上認真練習，
        證照即能輕鬆到手，提升照顧專業。

        一、考前準備
       【報名條件】
        1.    年滿16歲
        2.    取得『照顧服務員結業證明書』或『相關科系畢業證書』

       【最新】2021(110)全台照顧服務員訓練單位
       【報名費用】
        ▲ 一般報檢費用：2,600 元
        ▲ 免試學科費用：2,410 元
        ▲ 免試術科費用：340 元
        ''')  
        line_bot_api.reply_message(event.reply_token, message)  
    elif '想要瞭解鼻胃管' in msg :
        message = TextSendMessage(text='''在狀況不嚴重的病患，如因身體狀況無法直接進食、
        食用固體食物，鼻胃管(Nasogastric,英文縮寫 NG)可以當作暫時或長久的病患進食選擇，
        可以將食物打碎、牛奶等液體食物進行灌食來維持病人的體力。
        ''')  
        line_bot_api.reply_message(event.reply_token, message)  
    elif '請問鼻胃管灌食注意事項' in msg :
        message = TextSendMessage(text='''灌食前準備洗手。
        協助病人採坐姿或半坐臥或抬高床頭 30 ~60 度。
        食物溫度保持在約 37.7 ~ 40 度左右（以不燙手為主）。
        注意事項
        灌食後繼續採坐姿或半坐臥至少 30 分，以避免有嘔吐的情形。
        灌食後一小時內避免激烈活動如抽痰、拍背、翻身、復健、化痰等。
        固定胃管的紙膠布，應每天更換，保持部位乾淨，並黏貼在不同之部位，以避免黏貼處出現潰爛，
        注意不可移動胃管所插的深度。
        胃灌食患者應每日做多次口腔清潔（可用鹽水、薄檸檬水）及鼻腔護理。
        食物應保持新鮮，請於 2 小時內灌完，以防食物變壞，放置室溫太久的管灌食物應予以丟棄。
        食物與藥物必須分開灌。
        管子應避免受壓、扭曲或灌食時被拉出，尤其是躁動的病人。
        ''')  
        line_bot_api.reply_message(event.reply_token, message)  
    elif '想要瞭解鼻胃管灌食步驟' in msg :
        message = TextSendMessage(text='''灌食步驟
        打開鼻胃管的蓋子前，先用一手反摺鼻胃管，防空氣進入胃內。
        檢查鼻胃管位置，若有以下情形請暫停灌食並告知醫護人員：
        鼻胃管固定膠布標記有滑脫現象。
        檢查病人口中有鼻胃管脫出或纏繞在嘴巴的情形。
        先用灌食空針反抽，以確定胃管是否在胃內。
        評估胃消化情形，觀察胃內容物及顏色與量，如少於 60 ml  則可進行灌食；若是大於上一餐灌食量的一半以上，
        先暫不灌食，等 1 個小時後再評估，且須將反抽物再灌回胃內，以助消化。
        反抽物若呈墨綠色、暗紅色、血色或咖啡色時，請通知醫護人員。
        灌食前用 20 ~ 30 ml 溫開水潤濕管壁。
        灌食空針液面高度距離鼻子約 30 ~ 45 公分，利用重力使食物緩緩流入胃內，灌食時間不可少於 15 分鐘。
        灌食時避免空氣進入胃中引起腹脹。
        灌食中詢問病人感受，若病人感到腹脹不適、疼痛、嘔吐、咳嗽、呼吸困難等立刻停止灌食，
        安撫病人，視情況緊急送醫，如有嘔吐情形發生，需先將病患頭部側向一邊。
        灌完後再用 20 ~ 30 ml 溫開水沖洗管路，避免胃管阻塞或食物殘留在管內。
        胃管開口處用胃反摺塞入或用栓子塞住，以防止空氣的進入而產生腹脹及食物流出。
        ''') 
        line_bot_api.reply_message(event.reply_token, message)     
        #1111111111111111111111111111111111234
    
    
    elif '請問板橋還有護理之家嗎' in msg :
        message = TextSendMessage(text="有，不過我們建議是去長照中心問會比較清楚")
        line_bot_api.reply_message(event.reply_token, message)
    elif '7777' in msg :
        message = zoo()
        line_bot_api.reply_message(event.reply_token, message)
    elif '我可以問你問題嗎' in msg :
        message = TextSendMessage(text="可以啊，不過我是專門服務長照的機器人喔，超出能力範圍的可能聽不懂")
        line_bot_api.reply_message(event.reply_token, message)
    elif '服務項目' in msg or '費用' in msg :
        message = [
        ImageSendMessage(
        original_content_url='https://www.pidi.com.tw/archive/image/edcontent3/6c77383a05fd96b5.png',
        preview_image_url='https://www.pidi.com.tw/archive/image/edcontent3/6c77383a05fd96b5.png'
        ),
        TextSendMessage(text= '''依失能程度二至八級補助約每月1萬元至3萬6千元，以自負額最高16%計算，
        等於花1千6至6千元間，即可使用居家服務、日間照顧等「照顧服務」，或居家復健、居家營養等「專業服務」項目。
        失能第四級以上者，依交通遠近補助每月1,680元至2,400元（自負額最高30%）。 每三年最高4萬元（自負額最高30%）。
        ''')
        ]
        line_bot_api.reply_message(event.reply_token, message)
    #1114445566
    elif '照服員' in msg or '考試' in msg :
        message = [
        ImageSendMessage(
        original_content_url='https://www.ilong-termcare.com/UserFiles/Articles/f1d1e138-d4da-4501-a43b-cc2c83c4e189/%E8%80%83%E7%85%A7%E7%B6%93%E9%A9%97-1.png',
        preview_image_url='https://www.ilong-termcare.com/UserFiles/Articles/f1d1e138-d4da-4501-a43b-cc2c83c4e189/%E8%80%83%E7%85%A7%E7%B6%93%E9%A9%97-1.png'
        ),
        TextSendMessage(text= '''承上圖學科會考的有這些項目
        '''),
        ImageSendMessage(
        original_content_url='https://www.ilong-termcare.com/UserFiles/Articles/f1d1e138-d4da-4501-a43b-cc2c83c4e189/%E8%80%83%E7%85%A7%E7%B6%93%E9%A9%97-2.png',
        preview_image_url='https://www.ilong-termcare.com/UserFiles/Articles/f1d1e138-d4da-4501-a43b-cc2c83c4e189/%E8%80%83%E7%85%A7%E7%B6%93%E9%A9%97-2.png'
        ),
        TextSendMessage(text= '''承上圖術科會考的有這些項目
        ''')
        ]
        line_bot_api.reply_message(event.reply_token, message)
    elif '影片' in msg :
        message = TextSendMessage(text="https://www.youtube.com/watch?v=lOAMLaQlna8")
        line_bot_api.reply_message(event.reply_token, message)
    elif '照顧' in msg or '照護' in msg :
        message = [
        TextSendMessage(text= '''元氣居家照顧
        地址： 236新北市土城區南天母路27號
        電話： 0222680930
        網址: wecs.com.tw
        '''),
        TextSendMessage(text= '''慈馨護理之家
        地址： 220新北市板橋區館前東路96號
        電話：  02 2952 4388
        網址: http://www.cihsin.com.tw/
        '''),
        TextSendMessage(text= '''廣福老人長期照顧中心
        地址： 220新北市板橋區廣權路6號
        電話：  02 8951 4435
        '''),
        TextSendMessage(text= '''或撥打申請電話：1966
        '''),
        TextSendMessage(text= '''其他更詳細的長照服務資訊請進入此網站
        https://health.gov.taipei/Content_List.aspx?n=4406ED28437FBC4E
        ''')
        ]
        line_bot_api.reply_message(event.reply_token, message)
    elif '吃' in msg or '午餐' in msg or '晚餐' in msg:
        message = [
        TextSendMessage(text= '''歐義式 ALL 14 WELL
        地址： 220新北市板橋區南雅南路二段106號
        星期一	11:00–15:00, 17:00–21:00
        星期二	11:00–15:00, 17:00–21:00        
        星期三	11:00–15:00, 17:00–21:00
        星期四	11:00–15:00, 17:00–21:00
        星期五	11:00–15:00, 17:00–21:00
        星期六	11:00–15:00, 17:00–21:00
        星期日	11:00–15:00, 17:00–21:00
        '''),
        TextSendMessage(text= '''亞東汕頭意麵
        地址： 220新北市板橋區四川路二段47巷8弄8號
        星期一	11:00–19:30
        星期二	11:00–19:30
        星期三	11:00–19:30
        星期四	11:00–19:30
        星期五	11:00–19:30
        星期六	休息
        星期日	休息
        '''),
        TextSendMessage(text= '''食月午日 Brunch & Cafe 板橋店
        地址： 220新北市板橋區四川路二段99巷4弄3號
        星期一	07:00–14:30
        星期二	07:00–14:30
        星期三	07:00–14:30
        星期四	07:00–14:30
        星期五	07:00–14:30
        星期六	08:30–14:30
        星期日	08:30–14:30
        '''),
        TextSendMessage(text= '''薩莉亞 亞東醫院店
        地址： 220新北市板橋區南雅南路二段122-23號B1
        星期一	11:00–22:00
        星期二	11:00–22:00
        星期三	11:00–22:00
        星期四	11:00–22:00
        星期五	11:00–22:00
        星期六	11:00–22:00
        星期日	11:00–22:00
        '''),
        TextSendMessage(text= '''Ethan's Italian(義式料理)
        地址： 220新北市板橋區南雅南路二段144巷8號
        星期一	休息
        星期二	11:00–14:30, 17:15–21:30
        星期三	11:00–14:30, 17:15–21:30
        星期四	11:00–14:30, 17:15–21:30
        星期五	11:00–14:30, 17:15–21:30
        星期六	11:00–14:30, 17:15–21:30
        星期日	11:00–14:30, 17:15–21:30
        ''')
        ]
        line_bot_api.reply_message(event.reply_token, message)
    elif '翻譯機器人' in msg :
        message = [
        TextSendMessage(text= "請點擊此網址加入翻譯機器人"),
        TextSendMessage(text= "https://line.me/R/ti/p/%40826qrthc")
        ]
        line_bot_api.reply_message(event.reply_token, message)
    else:
        message = TextSendMessage(text= '''對不起，我聽不懂，建議問看看附近有什麼吃的或是長照相關的問題       
        ''')
          #按4:開啟療癒時間1111
        line_bot_api.reply_message(event.reply_token, message)
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
