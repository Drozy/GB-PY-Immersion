"""
Вы работаете над разработкой программы для проверки корректности даты, введенной пользователем. 
На вход будет подаваться дата в формате "день.месяц.год". 
Ваша задача - создать программу, которая проверяет, является ли введенная дата корректной или нет.
Ваша программа должна предоставить ответ "True" (дата корректна) или "False" (дата некорректна)
в зависимости от результата проверки.
"""


def func(date: str):
    day, month, year = map(int, date.split('.'))
    if year in range(1, 10_000) and month in range(1, 13) and day in range(1, 32):
        if _is_leap(month, year):
            if day in range(1, 30):
                return True
            else:
                return False
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return True
        elif month == 2:
            if day in range(1, 29):
                return True
            else:
                return False
        else:
            if day in range(1, 31):
                return True
            else:
                return False
    else:
        return False


def _is_leap(m, y):
    if y % 400 == 0 and m == 2 or y % 4 == 0 and y % 100 != 0 and m == 2:
        return True
    return False


# date_to_prove = "15.4.2023"   #True
date_to_prove = "31.6.2022"  # False

print(func(date_to_prove))
