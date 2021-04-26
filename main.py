"""
Bot to answer all leftist words in chat
"""

import telebot
from datetime import datetime

bot_token = "<TOKEN>"
bot = telebot.TeleBot(bot_token)
bot_name = '@antifaActionBot'

bot.can_join_groups = True
bot.can_read_all_group_message = True

def replace_all(text):
    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.replace(";", "")
    text = text.replace(":", "")
    text = text.replace("-", "")
    text = text.replace(")", "")
    text = text.replace("*", "")
    text = text.replace("*", "")
    text = text.replace("!","")
    return text

@bot.message_handler(commands=['start'])
def send_start(message):
    bot.reply_to(message,"Hallo!")

@bot.message_handler(func=lambda message: True)
def say_something(message):
    chat = message.chat.id
    text = message.text.lower()
    text = replace_all(text)
    date = str(datetime.now())[5:10]
    if "antifa" in text:
        bot.send_message(chat,"Antifaaaaaaaaaa <3")
    elif "theorie" in text:
        bot.send_message(chat,"Theorie und Praxis ...")
    elif "left unity" in text or "enteignen" in text or "enteignung" in text or "kommunismus" in text or "luxemburg" in text or "anarchismus" in text or "anarchie" in text or "engels" in text or "manifest" in text or "trotzki" in text or "kropotkin" in text or "bakunin" in text or "pkk" in text or "kpd" in text:
        bot.send_message(chat, "<3")
    elif "kapitalismus" in text or "capitalism" in text:
        bot.send_message(chat,"Fight Capitalism!")
    elif "acab" in text or "acat" in text or "1312" in text:
        bot.send_message(chat,"HASS, HASS, HASS WIE NOCH NIE! ALL COPS ARE TARGETS ACAT 🤬😡")
    elif "cop" in text:
        bot.send_message(chat,"FCKCPS! 🤬😡")
    elif "afd" in text:
        bot.send_message(chat,"FCKAFD!!")
    elif "lenin" in text:
        bot.send_message(chat,"Daddy <3")
    elif "stalin" in text:
        bot.send_message(chat,"Verräter! 😤😡")
    elif "nazi" in text or "fascho" in text or "die rechte" in text:
        bot.send_message(chat, "Nazis Töten. 🤬😡")
    elif "spd" in text or "grüne" in text:
        bot.send_message(chat,"Wer hat uns verraten? 😤😡")
    elif "links" in text:
        bot.send_message(chat,"Revolution?")
    elif "rechts" in text:
        bot.send_message(chat,"Keinen Millimeter nach rechts!")
    elif "marx" in text:
        if date != "05-05":
            bot.send_message(chat,"Karl Marx <3")
        else:
            bot.send_message(chat,"HAPPY BIRTHDAY MARX <3")
    elif "revolution" in text:
        bot.send_message(chat,"What solution? Reeeevoluution ✊")
    elif "patriot" in text:
        bot.send_message(chat,"Patridiot*innen!")
    else:
        for i in text.split():
            if i == "il":
                bot.send_message(chat, "<3")
                break

while True:
    try:
        bot.polling()
        print(f"Start Polling ...      {datetime.now()}")
    except Exception as e:
        print(f"{e}      {datetime.now()}")
