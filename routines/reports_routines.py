from google_sheets_parser.google_sheets_parser import GSheetsParser
import matplotlib.pyplot as plt
from io import BytesIO


class Reporter:
    def __init__(self, sheet_link):
        self.parser = GSheetsParser(sheet_link)
        self.user_timeseries = self.parser.parse()

    def validate_report(self): # Этот метод даёт сигнал, отравлять отчёт или нет
        ...

        return True

    def generate_report_text(self): # Текст отчёта
        ...

        return f'''
        Отчёт по креативу: ...
        '''

    def generate_report_images(self):
        report_images = []

        plt.plot([1, 2, 3, 4, 2, 3])
        plt.ylabel('some numbers')

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)

        report_images.append(buffer) # Сюда можно положить много фото - они отправятся по очереди

        return report_images


def send_report(bot, chat_id, sheet_link):
    reporter = Reporter(sheet_link)
    if reporter.validate_report():
        bot.send_message(chat_id, reporter.generate_report_text())
        for current_image in reporter.generate_report_images():
            bot.send_photo(chat_id, photo=current_image)
