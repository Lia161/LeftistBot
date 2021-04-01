"""
Bot to answer all leftist words in chat
"""

import telebot
import datetime

bot_token = "<TOKEN>"
bot = telebot.TeleBot(bot_token)
bot_name = '@antifaActionBot'

bot.can_join_groups = True
bot.can_read_all_group_message = True

@bot.message_handler(commands=['start'])
def send_start(message):
    bot.reply_to(message,"Hallo!")

@bot.message_handler(func=lambda message: True)
def say_something(message):
    text = message.text.split()
    chat = message.chat.id
    for i in text:
        i = i.lower()
        if i[-1] == "." or i[-1] == "!" or i[-1] == "?" or i[-1] == " ":
            i = i[:-2]
        if i == "antifa":
            bot.send_message(chat,"Antifaaaaaaaaaa <3")
        elif i == "kommunismus":
            bot.send_message(chat,"<3")
        elif i == "anarchismus":
            bot.send_message(chat,"<3")
        elif i == "anarchie":
            bot.send_message(chat,"<3")
        elif i == "marx":
            bot.send_message(chat,"Karl Marx <3")
        elif i == "engels":
            bot.send_message(chat,"<3")
        elif i == "stalin":
            bot.send_message(chat,"Verräter! 😤😡")
        elif i == "manifest":
            bot.send_message(chat,"<3")
        elif i == "trotzki":
            bot.send_message(chat,"<3")
        elif i == "kropotkin":
            bot.send_message(chat,"<3")
        elif i == "bakunin":
            bot.send_message(chat,"<3")
        elif i == "rechts":
            bot.send_message(chat,"Keinen Millimeter nach rechts!")
        elif i == "links":
            bot.send_message(chat,"Revolution?")
        elif i == "spd" or i == "grüne":
            bot.send_message(chat,"Wer hat uns verraten? 😤😡")
        elif i == "il":
            bot.send_message(chat,"<3")
        elif i == "fascho" or i == "faschos":
            bot.send_message(chat,"Nazis Töten. 🤬😡")
        elif i == "nazi" or i == "nazis":
            bot.send_message(chat, "Nazis Töten. 🤬😡")
        elif i == "acab":
            bot.send_message(chat,"HASS, HASS, HASS WIE NOCH NIE! ALL COPS ARE TARGETS ACAT 🤬😡")
        elif i == "acat":
            bot.send_message(chat, "HASS, HASS, HASS WIE NOCH NIE! ALL COPS ARE TARGETS ACAT 🤬😡")
        elif i == "1312":
            bot.send_message(chat, "HASS, HASS, HASS WIE NOCH NIE! ALL COPS ARE TARGETS ACAT 🤬😡")
        elif i == "13120":
            bot.send_message(chat, "HASS, HASS, HASS WIE NOCH NIE! ALL COPS ARE TARGETS ACAT 🤬😡")
        elif i == "cops" or i == "cop":
            bot.send_message(chat,"FCKCPS! 🤬😡")
        elif i == "kapitalismus":
            bot.send_message(chat,"Fight Capitalism!")
        elif i == "lenin":
            bot.send_message(chat,"Daddy <3")
        elif i == "afd":
            bot.send_message(chat,"FCKAFD!!")

while True:
    try:
        bot.polling()
        print(f"Start Polling ...      {datetime.datetime.now()}")
    except Exception as e:
        print(f"{e}      {datetime.datetime.now()}")
