"""
Создайте модуль и напишите в нём функцию,
которая получает на вход дату в формате DD.MM.YYYY
Функция возвращает истину, если дата может
существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999].
Весь период (1 января 1 года - 31 декабря 9999 года) действует
Григорианский календарь.
Проверку года на високосность вынести в отдельную защищённую функцию.
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
            if day in range (1, 29):
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


if __name__ == '__main__':
    print(func("29.02.2025"))
