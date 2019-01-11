# -*- coding: utf-8 -*-

import telebot
from time import time


bot = telebot.TeleBot("744804002:AAFnStkdLO8lN9Qu7pXddc9N5ZTLUBUsxpU")

GROUP_ID = -1001473450441

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет, я пидарас Абрахам, я ищу парня.")

@bot.message_handler(commands=["win"])
def set_ro(message):
    bot.restrict_chat_member(message.chat.id, message.from_user.id, until_date=time()+600)
    bot.send_message(message.chat.id, strings.get(get_language(message.from_user.language_code)).get("ro_win"),
                     reply_to_message_id=message.chat.id)
strings = {
    "ru": {
        "ro_win": "Вы выйграли РО на 10 минут."
    }
}

def get_language(lang_code):
    if not lang_code:
        return "en"
    if "-" in lang_code:
        lang_code = lang_code.split("-")[0]
    if lang_code == "ru":
        return "ru"
    else:
        return "en"

@bot.message_handler(content_types=['text'])
def handler_text(message):
    if message.text == "Да":
        bot.send_message(message.chat.id, "Пизда.")
    elif message.text == "@priler":
        bot.send_message(message.chat.id, "Заебал.")
    elif message.text == "@prilerbot":
        bot.send_message(message.chat.id, "Пидоры на месте.")
    elif message.text == "@arsenibyk":
        bot.send_message(message.chat.id, "Ждём всемогущего...")
        bot.send_message(480725445, "Вас зовут!")

if __name__ == "__main__":
    bot.polling(none_stop=True)
