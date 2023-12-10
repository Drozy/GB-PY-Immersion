"""
Задание №7
✔ Создайте функцию-генератор.
✔ Функция генерирует N простых чисел,
начиная с числа 2.
✔ Для проверки числа на простоту используйте
правило: «число является простым, если делится
нацело только на единицу и на себя».
"""

from math import sqrt


def generate_prime(n):
    count = 0
    num = 1
    is_prime = True
    while count < n:
        num += 1
        for j in range(2, int(sqrt(num) + 1)):
            if num % j == 0:
                is_prime = False
                break
            else:
                is_prime = True
        if is_prime:
            count += 1
            yield num


for item, i in enumerate(generate_prime(n=10000), start=1):
    print(f'{item}:  {i}')
