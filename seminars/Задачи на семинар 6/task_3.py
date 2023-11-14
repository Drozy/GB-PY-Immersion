"""
Задание №3

Улучшаем задачу 2.
Добавьте возможность запуска функции “угадайки”
из модуля в командной строке терминала.
Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
Для преобразования строковых аргументов командной строки в
числовые параметры используйте генераторное выражение.
"""

from random import randint
from sys import argv

args = [int(el) for el in argv[1:]]

def guess_num(args):
    num = randint(args[0], args[1])
    i = 0
    while args[2] > i:
        u_num = int(input(
            f"введите число в диапазоне от {args[0]} до {args[1]}: "))
        if u_num > num:
            print('меньше!')
        elif u_num < num:
            print('больше!')
        else:
            print('Угадал!')
            return True
        i += 1
    return False


args = [int(el) for el in argv[1:]]
    
if __name__ == '__main__':    
    print(guess_num(args))
