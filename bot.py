import telebot; bot
telebot.TeleBot('9186711841:AAHvpp8SV_1Yfwxf3y_PLTvOmd7EPdHI-jw');
@bot.message_handler(commands=['start'])
def send_welcome(message):
bot.reply_to(message, 'Hello!');
bot.infinity_polling
