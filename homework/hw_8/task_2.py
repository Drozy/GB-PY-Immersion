"""
Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.

Создайте файл __init__.py и запишите в него все функции:
get_dir_size,
save_results_to_json,
save_results_to_csv,
save_results_to_pickle,
traverse_directory.
"""


func_str = ("import os\n"
            "import csv\n"
            "import pickle\n"
            "\n"
            "def get_dir_size():\n"
            "    pass\n"
            "\n"
            "\n"
            "def save_results_to_json():\n"
            "    pass\n"
            "\n"
            "\n"
            "def save_results_to_csv():\n"
            "    pass\n"
            "\n"
            "\n"
            "def save_results_to_pickle():\n"
            "    pass\n"
            "\n"
            "\n"
            "def traverse_directory():\n"
            "    pass\n")

with open("__init__.py", "w", encoding='utf-8') as file:
    file.write(func_str)
