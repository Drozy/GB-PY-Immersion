"""
Задание №4
Прочитайте созданный в прошлом задании csv файл без
использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка
csv файла представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы
функции.
"""

import csv
import json
import os


def csv_to_json(scv_file):
    with open(scv_file, encoding="utf-8") as f:
        f_r = csv.reader(f)
        res = list(f_r)
        for i in range(1, len(res)):
            temp = res[i][1]
            res[i][1] = f"{temp.zfill(10)}"
            res[i][2] = res[i][2].title()

    json_file = os.path.splitext(scv_file)[0] + '.json'
    with open(json_file, "w", encoding="utf-8") as j:
        json.dump(res, j, ensure_ascii=False)


csv_to_json('task8_2.csv')
