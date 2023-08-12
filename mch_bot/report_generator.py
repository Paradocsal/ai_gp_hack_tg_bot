import pandas as pd

import sys

sys.path.insert(0, '../')

from google_sheets_parser.google_sheets_parser import GSheetsParser


# noinspection SpellCheckingInspection
def pretty_timeseria(timeseria):
    timeseria.columns = timeseria.iloc[0]
    timeseria = timeseria.drop(timeseria.index[0])

    timeseria['campaign_name'] = timeseria['campaign_name'].str.lower()
    timeseria.loc[:, 'date'] = pd.to_datetime(timeseria['date'], format='%m/%d/%Y')
    timeseria['impressions'] = pd.to_numeric(timeseria['impressions'], errors='coerce').fillna(0)
    timeseria['clicks'] = pd.to_numeric(timeseria['clicks'], errors='coerce').fillna(0)

    # Не уверен, что это нужно:
    # timeseria = timeseria.drop('campaign_id', axis=1)
    # timeseria = timeseria[(timeseria['clicks'] > 0) | (timeseria['impressions'] > 100)]
    # timeseria = timeseria.drop(timeseria.loc[timeseria['impressions'] < timeseria['clicks']].index)

    timeseria['click_rate'] = timeseria['clicks'] / timeseria['impressions']

    timeseria.loc[(timeseria.campaign_name.str.contains('dexonal')) | (
        timeseria.campaign_name.str.contains('дексонал')), 'drug_name'] = 'dexonal'
    timeseria.loc[(timeseria.campaign_name.str.contains('диклофенак')) | (
        timeseria.campaign_name.str.contains('diclofenac')), 'drug_name'] = 'diclofenac_akos'
    timeseria.loc[(timeseria.campaign_name.str.contains('maxilac')) | (
        timeseria.campaign_name.str.contains('максилак')), 'drug_name'] = 'maxilac'
    timeseria.loc[(timeseria.campaign_name.str.contains('кагоцел')) | (
        timeseria.campaign_name.str.contains('kagocel')), 'drug_name'] = 'kagocel'
    timeseria.loc[(timeseria.campaign_name.str.contains('венарус')) | (
        timeseria.campaign_name.str.contains('venarus')), 'drug_name'] = 'venarus'
    timeseria.loc[(timeseria.campaign_name.str.contains('необутин')) | (
        timeseria.campaign_name.str.contains('neobutin')), 'drug_name'] = 'neobutin'
    timeseria.loc[(timeseria.campaign_name.str.contains('эльмуцин')) | (
        timeseria.campaign_name.str.contains('elmucin')), 'drug_name'] = 'elmucin'
    timeseria.loc[(timeseria.campaign_name.str.contains('парацитолгин')) | (
        timeseria.campaign_name.str.contains('paracitolgin')), 'drug_name'] = 'paracitolgin'
    timeseria.loc[(timeseria.campaign_name.str.contains('акнауцер')) | (
        timeseria.campaign_name.str.contains('aknaucer')), 'drug_name'] = 'aknaucer'
    timeseria.loc[timeseria['drug_name'].isna(), 'drug_name'] = 'none'

    timeseria.loc[(timeseria.campaign_name.str.contains('carousel')) | (
        timeseria.campaign_name.str.contains('carusel')), 'adv_format'] = 'carousel'
    timeseria.loc[
        (timeseria.campaign_name.str.contains('баннеры')) | (
            timeseria.campaign_name.str.contains('banner')), 'adv_format'] = 'banner'
    timeseria.loc[(timeseria.campaign_name.str.contains('video')) | (
        timeseria.campaign_name.str.contains('видео')), 'adv_format'] = 'video'
    timeseria.loc[(timeseria.campaign_name.str.contains('multiformat')), 'adv_format'] = 'multiformat'
    timeseria.loc[
        ~((timeseria.campaign_name.str.contains('carousel')) | (timeseria.campaign_name.str.contains('carusel')) |
          (timeseria.campaign_name.str.contains('баннеры')) | (timeseria.campaign_name.str.contains('banner')) |
          (timeseria.campaign_name.str.contains('video')) | (timeseria.campaign_name.str.contains('видео')) |
          (timeseria.campaign_name.str.contains('multiformat'))), 'adv_format'] = 'others'

    # TODO - Добавить тип ЦА

    timeseria = timeseria.drop('campaign_id', axis=1)
    timeseria = timeseria.drop('campaign_name', axis=1)
    timeseria = timeseria.drop('platform', axis=1)

    timeseria = timeseria.sort_values('date')

    return timeseria


def generate_report(google_sheet_link):
    parser = GSheetsParser('''
        https://docs.google.com/spreadsheets/d/1AcAuR951KcHvMK1JIJJ_BThaO1r1PtkiBJBsRGYTlSw/edit#gid=0
    ''')

    user_timeseria = pretty_timeseria(pd.DataFrame(parser.parse()))

    return f'Размер ваших данных: {user_timeseria.shape}'
