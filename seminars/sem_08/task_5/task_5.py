"""
Задание №5
Напишите функцию, которая ищет json файлы в указанной
директории и сохраняет их содержимое в виде
одноимённых pickle файлов.
"""
import json
import os
import pickle


def json_to_pickle(path='.'):
    for el in os.listdir(path):
        if el.endswith(".json"):
            with open(el, "r", encoding="utf-8") as j:
                res = json.load(j)
            new_filename = path.join(el.split(".")[:-1]) + ".pickle"
            with open(new_filename, "wb") as p:
                pickle.dump(res, p)


json_to_pickle()
