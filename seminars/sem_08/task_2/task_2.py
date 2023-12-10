"""
Задание №2
Напишите функцию, которая в бесконечном цикле
запрашивает имя, личный идентификатор и уровень
доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в
JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо
от уровня доступа.
При перезапуске функции уже записанные в файл данные
должны сохраняться.

"""

import json


def dump_json(json_file):
    # name = input("введите имя:> ")
    # user_id = input("введите id:> ")
    # level = int(input('введите уровень доступа (1-7):> '))
    name = "Петя"
    user_id = "002"
    level = 4

    with open(json_file, "r", encoding='utf-8') as rf:
        res = json.load(rf)

    my_dct = {
        "level": level,
        "id": user_id,
        "name": name,
    }

    with open(json_file, "w", encoding='utf-8') as wf:
        res.append(my_dct)
        json.dump(res, wf, indent=2, separators=(',', ':'), ensure_ascii=False)


my_file = 'task8_2.json'
lst = []
with open(my_file, "w", encoding='utf-8') as js_f:
    json.dump(lst, js_f)

s = 'n'
while s != 'y':
    dump_json(my_file)
    s = input('выход y/n :>')
