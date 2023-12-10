"""
Задание №6
Напишите функцию, которая преобразует pickle файл
хранящий список словарей в табличный csv файл.
Для тестированию возьмите pickle версию файла из задачи
4 этого семинара.
Функция должна извлекать ключи словаря для заголовков
столбца из переданного файла.
"""

import os
import pickle
import csv


def pickle_to_csv(pickle_file):
    with open(pickle_file, 'rb') as f:
        data = pickle.load(f)
    new_filename = os.path.splitext(pickle_file)[0] + ".csv"
    with open(new_filename, "w", encoding="utf-8", newline='') as c:
        writer = csv.writer(c)
        for row in data:
            writer.writerow(row)


pickle_to_csv('new_json.pickle')
