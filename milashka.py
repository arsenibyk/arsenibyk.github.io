import telebot

token = "766110394:AAEFuInaTgZAzXh52xdKqm8rVLiPfdVSFrY"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Я ТРАХАЮСЬ С " + message.chat.first_name)

if __name__ == "__main__":
    bot.polling(none_stop=True)
