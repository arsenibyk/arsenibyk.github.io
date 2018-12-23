import telebot

token = "677024223:AAHxSjrhwoUgGO-bj1FTQSVjzIaHSIe3nvs"

bot=telebot.Telebot(token)

@bot.message_handler(commands=[start])
def start(message):
	bot.send_message(message.chat.id, "Здравствуйте," + message.chat.fist_name)

if __name__ == "__main__":
	bot.polling(none_stop=True)