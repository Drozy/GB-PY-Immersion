"""
Ваша задача - написать программу, которая принимает на вход директорию и рекурсивно обходит эту директорию и все
вложенные директории. Результаты обхода должны быть сохранены в нескольких форматах: JSON, CSV и Pickle.
Каждый результат должен содержать следующую информацию:
Путь к файлу или директории: Абсолютный путь к файлу или директории.
Тип объекта: Это файл или директория.
Размер: Для файлов - размер в байтах, для директорий - размер, учитывая все вложенные файлы и директории в байтах.
Важные детали:
Для дочерних объектов (как файлов, так и директорий) укажите родительскую директорию.
Для файлов сохраните их размер в байтах.
Для директорий, помимо их размера, учтите размер всех файлов и директорий, находящихся внутри данной директории,
и вложенных директорий.
Программа должна использовать рекурсивный обход директорий, чтобы учесть все вложенные объекты.
Результаты должны быть сохранены в трех форматах: JSON, CSV и Pickle. Форматы файлов должны быть выбираемыми.
Для обхода файловой системы вы можете использовать модуль os.
Вам необходимо написать функцию traverse_directory(directory), которая будет выполнять обход директории
и возвращать результаты в виде списка словарей. После этого результаты должны быть сохранены в трех различных файлах
(JSON, CSV и Pickle) с помощью функций save_results_to_json, save_results_to_csv и save_results_to_pickle.
"""

import os
import csv
import json
import pickle


def traverse_directory(directory):
    results = []
    for obj in os.listdir(directory):
        path = os.path.join(directory, obj)
        if os.path.isfile(path):
            results.append({'Path': path, 'Type': 'File', 'Size': os.path.getsize(path)})
    for obj in os.listdir(directory):
        path = os.path.join(directory, obj)
        if not os.path.isfile(path):
            object_info = {'Path': path, 'Type': 'Directory', 'Size': 0}
            dir_content = traverse_directory(path)
            for el in dir_content:
                if el['Type'] == 'File':
                    object_info['Size'] += el['Size']
            results.append(object_info)
            results.extend(dir_content)
    return results


def save_results_to_json(dir_info, filename):
    with open(filename, "w", encoding='utf-8') as js_f:
        json.dump(dir_info, js_f, separators=(', ', ': '), ensure_ascii=False)


def save_results_to_csv(dir_info, filename):
    lst = []
    keys = dir_info[0].keys()
    lst.append(keys)
    for el in dir_info:
        vals = el.values()
        lst.append(vals)
    with open(filename, "w", newline='', encoding='utf-8') as cs_f:
        writer = csv.writer(cs_f)
        for el in lst:
            writer.writerow(el)


def save_results_to_pickle(dir_info, filename):
    with open(filename, "wb") as p:
        pickle.dump(dir_info, p)


# TESTS
if __name__ == '__main__':
    dir_data = traverse_directory('dir1')
    print(*dir_data, sep='\n')

    save_results_to_json(dir_data, 'dir_info.json')
    save_results_to_csv(dir_data, 'dir_info.csv')
    save_results_to_pickle(dir_data, 'dir_info.pkl')

    with open('dir_info.json', 'r') as f:
        data = json.load(f)
    print('JSON')
    print(data)

    with open('dir_info.csv', 'r', newline='') as f:
        reader = csv.reader(f)
        data = [row for row in reader]
    print('CSV')
    print(data)

    with open('dir_info.pkl', 'rb') as f:
        data = pickle.load(f)
    print('PICKLE')
    print(data)
