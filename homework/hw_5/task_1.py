"""
Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""


# def get_file_info(file_path):
#     # Находим индекс последнего вхождения символа /
#     last_slash = file_path.rfind('/')
#     # Получаем путь до файла
#     if last_slash == -1:
#         path = ""
#     else:
#         path = file_path[:last_slash] + "/"
#     # Находим индекс последнего вхождения символа .
#     last_dot = file_path.rfind('.')
#     # Если символ . не найден, возвращаем пустую строку вместо расширения
#     if last_dot == -1:
#         file_name = file_path[last_slash + 1:]
#         extension = ''
#     else:
#         file_name = file_path[last_slash + 1:last_dot]
#         extension = '.' + file_path[last_dot + 1:]
#     # Возвращаем кортеж из трёх элементов
#     return path, file_name, extension


# Эталонное решение
def get_file_info(file_path):
    file_name = file_path.split("/")[-1]
    file_extension = file_name.split(".")[-1]
    path = file_path[:-len(file_name)]
    return (path, file_name[:-len(file_extension)-1], "." + file_extension)


# print(get_file_info(file_path = "C:/Users/User/Documents/example.txt"))
print(get_file_info(file_path = 'file_in_current_directory.txt'))



