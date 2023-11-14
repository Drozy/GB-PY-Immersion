"""
Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.
Создайте файл __init__.py и запишите в него функцию rename_files
"""

import warnings

warnings.filterwarnings('ignore')

func_str = ("import os\n"
            "\n"
            "\n"
            "def rename_files(*, name_range=None, desired_name=\"new_file_\", "
            "num_digits=3, source_ext=\"txt\", target_ext=\"doc\"):\n"
            "    if name_range is None:\n"
            "        name_range = [0, 0]\n"
            "    index = 1\n"
            "    for file in os.listdir(folder):\n"
            "        if file.endswith(source_ext):\n"
            "            serial_number = ''\n"
            "            for i in range(num_digits):\n"
            "                if index % pow(10, num_digits - i) > 0:\n"
            "                    serial_number = '0' * i + f'{index}'\n"
            "                old_filename = str(os.path.splitext(file)[0])[name_range[0]:name_range[1]]\n"
            "                new_filename = f'{old_filename}{desired_name}{serial_number}.{target_ext}'\n"
            "                os.rename(os.path.join(folder, file), os.path.join(folder, new_filename))\n"
            "                index += 1")

with open("__init__.py", "w", encoding='utf-8') as file:
    file.write(func_str)
    file.close()

with open("__init__.py", "r") as init_file:
    code = init_file.read()

function_names = [
    "def rename_files"
]

for func_name in function_names:
    if func_name not in code:
        print(f"Функция {func_name} не найдена в файле __init__.py")
    else:
        print(f"Функция {func_name} найдена в файле __init__.py")
