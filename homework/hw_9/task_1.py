"""
Создайте функцию generate_csv_file(file_name, rows), которая будет генерировать
по три случайных числа в каждой строке, от 100-1000 строк, и записывать их в CSV-файл.
Функция принимает два аргумента:
file_name (строка) - имя файла, в который будут записаны данные.
rows(целое число) - количество строк (записей) данных, которые нужно сгенерировать.

Создайте функцию find_roots(a, b, c), которая будет находить корни квадратного
уравнения вида ax^2 + bx + c = 0. Функция принимает три аргумента:
a, b, c (целые числа) - коэффициенты квадратного уравнения.
Функция возвращает:
None, если уравнение не имеет корней (дискриминант отрицателен).
Одно число, если уравнение имеет один корень (дискриминант равен нулю).
Два числа (корни), если уравнение имеет два корня (дискриминант положителен).

Создайте декоратор save_to_json(func), который будет оборачивать функцию find_roots.
Декоратор выполняет следующие действия:
Читает данные из CSV-файла, переданного в аргументе функции, исходя из аргумента args[0].
Для каждой строки данных вычисляет корни квадратного уравнения с помощью функции find_roots.
Сохраняет результаты в формате JSON в файл results.json.
Каждая запись JSON содержит параметры a, b, c и результаты вычислений.

Таким образом, после выполнения функций generate_csv_file и find_roots в файле results.json
будет сохранена информация о параметрах и результатах вычислений для каждой строки данных
из CSV-файла.
"""
import csv
import json
from random import randint


def generate_csv_file(file_name, rows):
    with open(file_name, "w", newline='', encoding='utf-8') as cs_f:
        writer = csv.writer(cs_f)
        for _ in range(0, rows):
            writer.writerow([randint(1, 100), randint(1, 100), randint(1, 100)])


def save_to_json(func):
    data = []

    def wrapper(csv_file):
        with open(csv_file, 'r', encoding='utf-8') as cf:
            contents = cf.readlines()
            for row in contents:
                args = [int(el) for el in row.split(',')]
                result = func(args[0], args[1], args[2])
                data.append({'a': args[0], 'b': args[1], 'c': args[2], 'result': result})
            with open("results.json", "w", encoding='utf-8') as wf:
                json.dump(data, wf, indent=2, separators=(',', ':'), ensure_ascii=False)
        return data

    return wrapper


@save_to_json
def find_roots(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        return [(-b + (d ** 0.5)) / (2 * a), (-b - (d ** 0.5)) / (2 * a)]
    if d == 0:
        return [-b / (2 * a)]
    return None


# Test
generate_csv_file("input_data.csv", 101)
find_roots("input_data.csv")

with open("results.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

if 100 <= len(data) <= 1000:
    print(True)
else:
    print("Количество строк в файле не находится в диапазоне от 100 до 1000.")

print(len(data) == 101)
