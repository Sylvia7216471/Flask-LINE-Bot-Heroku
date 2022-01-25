import os
from datetime import datetime

from flask import Flask, abort, request

# https://github.com/line/line-bot-sdk-python
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ.get("sPu7l9y6nRIkxnS0vMDvnyUHulFQRlVejLSoRk4IVa7DjVSVGlq1J3doI2T3n7MkZWInliPTPxvBQRylNqg0179vUA6rWZOgEypkzc1OBfpuDwx/cdtesVRsWE92T+s0vWknma7IIeADQNgozuRZBgdB04t89/1O/w1cDnyilFU="))
handler = WebhookHandler(os.environ.get("8cf00b16dc9113809456c406569bd0d4"))


@app.route("/", methods=["GET", "POST"])
def callback():

    if request.method == "GET":
        return "Hello Heroku"
    if request.method == "POST":
        signature = request.headers["X-Line-Signature"]
        body = request.get_data(as_text=True)

        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)

        return "OK"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    get_message = event.message.text

    # Send To Line
    reply = TextSendMessage(text=f"{get_message}")
    line_bot_api.reply_message(event.reply_token, reply)
    if event.message.text == "Sylvia":
    line_bot_api.reply_message(event.reply_token, reply)
    if event.message.text == "貼圖":
        line_bot_api.reply_message(event.reply_token,StickerSendMessage(package_id=1, sticker_id=2))
