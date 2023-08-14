from google_sheets_parser.google_sheets_parser import GSheetsParser


class Reporter:
    def __init__(self, sheet_link):
        self.parser = GSheetsParser(sheet_link)

    def validate_report(self):
        ...

        return True

    def generate_report_text(self):
        ...

        return f'''
        Отчёт по креативу: ...
        '''

    def generate_report_images(self):
        ...

        return []


def send_report(bot, chat_id, sheet_link):
    reporter = Reporter(sheet_link)
    if reporter.validate_report():
        bot.send_message(chat_id, reporter.generate_report_text())
        for current_image in reporter.generate_report_images():
            bot.send_photo(chat_id, photo=current_image)
