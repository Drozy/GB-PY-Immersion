"""
Напишите функцию группового переименования файлов в папке test_folder под названием rename_files.
Она должна:
a. принимать параметр желаемое конечное имя файлов. При переименовании
в конце имени добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла. Переименование должно работать только
для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6]
берутся буквы с 3 по 6 из исходного имени файла.
К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
f. Папка test_folder доступна из текущей директории

На входе:
rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")

На выводе:
new_file_008.doc, test.doc, new_file_004.doc, new_file_005.doc, new_file_007.doc, new_file_001.doc,
new_file_006.doc, new_file_003.doc, new_file_002.doc, new_file_009.doc, new_file_010.doc
"""

import os
import shutil

# # 1
# # Создать тестовую папку
# folder_name = "test_folder"
# folder_path = os.path.join(os.getcwd(), folder_name)
# if os.path.exists(folder_path):
#     shutil.rmtree(folder_path)
# os.makedirs(folder_path)
#
# # Заполнить тестовую папку
# file_name = "test1.txt"
# file_path = os.path.join(folder_path, file_name)
# with open(file_path, "w") as file:
#     file.write("This is a test file.\n")
#     file.close()

# # 3
# Создать тестовую папку
folder_name = "test_folder"
folder_path = os.path.join(os.getcwd(), folder_name)
if os.path.exists(folder_path):
    shutil.rmtree(folder_path)
os.makedirs(folder_path)

# Заполнить тестовую папку
for i in range(10):
    file_name = f"test{i}.txt"
    file_path = os.path.join(folder_path, file_name)

    with open(file_path, "w") as file:
        file.write("This is a test file.\n")
        file.close()

file_name = "test.doc"
file_path = os.path.join(folder_path, file_name)

with open(file_path, "w") as file:
    file.write("This is a test file.\n")
    file.close()


def rename_files(*, name_range=[0, 0], desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc"):
    """Переименование файлов в папке"""
    if name_range is None:
        name_range = []
    folder = 'test_folder'
    index = 1
    for file in os.listdir(folder):
        if file.endswith(source_ext):
            serial_number = ''
            for i in range(num_digits):
                if index % pow(10, num_digits - i) > 0:
                    serial_number = '0' * i + f'{index}'
            old_filename = str(os.path.splitext(file)[0])[name_range[0]:name_range[1]]
            new_filename = f'{old_filename}{desired_name}{serial_number}.{target_ext}'
            os.rename(os.path.join(folder, file), os.path.join(folder, new_filename))
            index += 1


# rename_files()

# 0
# rename_files(name_range=[3, 7], desired_name="new_file_", num_digits=3,
#              source_ext="txt", target_ext="doc")

# 1
# rename_files(desired_name="file_", num_digits=4, source_ext="txt", target_ext="txt")

# 3
rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")

folder_content = ""
files = os.listdir(folder_path)
separator = ", "
files_as_string = separator.join(files)
print(files_as_string)

shutil.rmtree(folder_path)
