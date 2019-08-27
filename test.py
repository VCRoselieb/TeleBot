import telebot


bot=telebot.TeleBot('889724193:AAHtBrmAfxZZmvSICxEYI5VSoATu434JIG4')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Welcome to my bot")

@bot.message_handler(commands=['vivi','mats'])
def send_coolness(message):
	bot.reply_to(message, "This person is absolutley amazing")

@bot.message_handler(regexp="CogSci")
def trigger_input(message):
	bot.reply_to(message, "This is a trigger for me to write this sentence");


@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling();
