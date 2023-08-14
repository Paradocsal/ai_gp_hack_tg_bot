
import telebot
import schedule
import time

from db_routines import get_unique_links_with_chat_ids
from report_generator import generate_report


def get_bot_token():
    token_file = open('../tokens/mch_bot_token', 'r')
    token = token_file.read()
    token_file.close()
    return token


bot = telebot.TeleBot(get_bot_token())


def send_report(chat_id, report):
    bot.send_message(chat_id, report)


def send_all_reports():
    unique_links_with_chat_ids = get_unique_links_with_chat_ids()
    for current_link_and_chat_id in unique_links_with_chat_ids:
        send_report(current_link_and_chat_id[0], generate_report(current_link_and_chat_id[1]))


send_all_reports()


# schedule.every(24).hours.do(send_all_reports())
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)
