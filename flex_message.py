line_bot_api.reply_message(
    event.reply_token,
    FlexSendMessage(
        alt_text = '全台水庫資訊',
        contents = json.load(open('reservoir.json', 'r', encoding='utf-8'))
    )
)