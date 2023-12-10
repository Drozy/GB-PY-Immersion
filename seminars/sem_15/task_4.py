"""
Задание №4
📌 Функция получает на вход текст вида: “1-й четверг ноября”, “3-
я среда мая” и т.п.
📌 Преобразуйте его в дату в текущем году.
📌 Логируйте ошибки, если текст не соответсвует формату.
"""

import logging
from datetime import datetime, date

logging.basicConfig(filename='Log/log_4.log',
                    filemode='w',
                    encoding='utf-8',
                    format='{levelname} - {asctime} функция "{funcName}()"'
                           ' строка {lineno} : {msg}',
                    style='{',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def text_to_date(text):
    months = {'янв': 1, 'фев': 2, 'мар': 3, 'апр': 4, 'май': 5, 'июн': 6,
              'июл': 7, 'авг': 8, 'сен': 9, 'окт': 10,
              'ноя': 11, 'дек': 12}
    weekdays = {'пон': 0, 'вто': 1, 'сре': 2, 'чет': 3, 'пят': 4, 'суб': 5,
                'вос': 6}

    '''Перевод текста в дату'''
    try:
        count, weekday_, month_, *other = text.split()  # 3-я среда мая
        count = int(count[0])
        if count > 5:
            raise Exception('Некорректная неделя')
        weekday = weekdays[weekday_[:3]]
        m = month_[:3]
        if m == "мая":
            month_ = "май"
        month = months[month_[:3]]  # 5 - число
    except Exception as exc:
        logger.error(
            f'Переданные данные: {count}-й , день недели"{weekday_}",'
            f' месяц:"{month_}" =  ошибочные данные: {exc}')
        count = 0

    if count:
        count_week = 0
        year = datetime.now().year  # 2023
        for day in range(1, 32):
            try:
                result = date(year=year, month=month, day=day)
                if result.weekday() == weekday:
                    count_week += 1
                    if count_week == count:
                        logger.info(
                            f'{count}-й {weekday_} {month_} {year} = {result} ')
                        return result
            except ValueError as e:
                logger.error(
                    f'Переданные данные: {count}-й, день недели: "{weekday_}",'
                    f' месяц: "{month_}", ошибочные данные: {e}')
        print('Преобразование невозможно.')
        logger.info(
            f'Переданные данные: {count}-й, день недели: "{weekday_}",'
            f' месяц: "{month_}". Преобразование невозможно.')

    else:
        print('Преобразование невозможно.')
        return None


if __name__ == '__main__':
    # print(text_to_date('3-й вто мая'))
    # print(text_to_date('3-й вторник марта'))
    print(text_to_date('5-й понедельник сентября'))
    # print(text_to_date('5-й четверг августа'))
