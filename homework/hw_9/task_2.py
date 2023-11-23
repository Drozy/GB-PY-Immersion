"""
Из созданных на уроке и в рамках домашнего задания функций,
соберите пакет для работы с файлами.

Создайте файл __init__.py и запишите в него все функции:
save_to_json,
find_roots,
generate_csv_file.
"""

func_str = ("import csv\n"
            "import json\n"
            "from random import randint\n"
            "\n"
            "def save_to_json():\n"
            "    pass\n"
            "\n"
            "\n"
            "def find_roots():\n"
            "    pass\n"
            "\n"
            "\n"
            "def generate_csv_file():\n"
            "    pass\n")

with open("__init__.py", "w", encoding='utf-8') as file:
    file.write(func_str)
