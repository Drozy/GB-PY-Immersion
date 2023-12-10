"""
Задание №3
Напишите функцию, которая сохраняет созданный в
прошлом задании файл в формате CSV.
"""
import json
import csv
import os


def json_to_csv(json_file):
    with open(json_file, "r", encoding='utf-8') as js_f:
        res = json.load(js_f)
        lst = []
        keys = res[0].keys()
        lst.append(keys)
        for el in res:
            vals = el.values()
            lst.append(vals)

    csv_file = os.path.splitext(json_file)[0] + '.csv'
    with open(csv_file, "w", newline='', encoding='utf-8') as cs_f:
        writer = csv.writer(cs_f)
        for el in lst:
            writer.writerow(el)


json_to_csv('task8_2.json')
