import telebot
from db_routines import initialize_db, add_user, add_timeseries_source_table
from google_sheets_parser import GSheetsParser

initialize_db()


def get_bot_token():
    token_file = open('C://Users/Adminn/Documents/GitHub/ai_gp_hack_tg_bot/tokens/mch_bot_token', 'r')
    token = token_file.read()
    token_file.close()
    return token


bot = telebot.TeleBot(get_bot_token())


@bot.message_handler(commands=['start'])
def handle_start(message):
    add_user(message.chat.id)
    bot.reply_to(message, 'Welcome! Your chat ID has been saved.')


@bot.message_handler(commands=['save_link'])
def handle_save_link(message):
    add_timeseries_source_table(message.chat.id, message.text.split('/save_link')[1])
    bot.reply_to(message, 'Link has been saved.')

@bot.message_handler(commands=['get_report'])
def handle_save_link(message):
    add_timeseries_source_table(message.chat.id, message.text.split('/get_report ')[1])
    bot.reply_to(message, 'Forming report...')


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.reply_to(message, 'I can only respond to the /start command.')


bot.polling(none_stop=True)
