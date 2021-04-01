"""
Bot to answer all leftist words in chat
"""

import telebot
import datetime

bot_token = "1703408507:AAHKvrd5l3Y94R0Gt3JoNgfKOrrne-kslVg"
bot = telebot.TeleBot(bot_token)
bot_name = '@antifaActionBot'

bot.can_join_groups = True
bot.can_read_all_group_message = True

@bot.message_handler(commands=['start'])
def send_start(message):
    bot.reply_to(message,"Hallo!")

@bot.message_handler(func=lambda message: True)
def say_something(message):
    chat = message.chat.id
    text = message.text.lower()
    if "antifa" in text:
        bot.send_message(chat,"Antifaaaaaaaaaa <3")
    elif "left unity" in text or "kommunismus" in text or "luxemburg" in text or "anarchismus" in text or "anarchie" in text or "engels" in text or "manifest" in text or "trotzki" in text or "kropotkin" in text or "bakunin" in text or "il" in text or "pkk" in text or "kpd" in text:
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
    elif "nazi" in text or "fascho" in text:
        bot.send_message(chat, "Nazis Töten. 🤬😡")
    elif "spd" in text or "grüne" in text:
        bot.send_message(chat,"Wer hat uns verraten? 😤😡")
    elif "links" in text:
        bot.send_message(chat,"Revolution?")
    elif "rechts" in text:
        bot.send_message(chat,"Keinen Millimeter nach rechts!")
    elif "marx" in text:
        bot.send_message(chat,"Karl Marx <3")
    elif "revolution" in text:
        bot.send_message(chat,"What solution? Reeeevoluution ✊")

while True:
    try:
        bot.polling()
        print(f"Start Polling ...      {datetime.datetime.now()}")
    except Exception as e:
        print(f"{e}      {datetime.datetime.now()}")
