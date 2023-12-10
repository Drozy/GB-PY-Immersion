"""
Задание №3
✔ Напишите программу, которая получает целое число и возвращает
его двоичное, восьмеричное строковое представление.
✔ Функции bin и oct используйте для проверки своего
результата, а не для решения.
Дополнительно:
✔ Попробуйте избежать дублирования кода
в преобразованиях к разным системам счисления
✔ Избегайте магических чисел
✔ Добавьте аннотацию типов где это возможно
"""
# https://calcus.ru/perevod-sistem-schisleniya/iz-desyatichnoy-v-vosmerichnuyu
# перевод числа из десятичного в двоичное

num_dec = int(input("введите число: "))
res = ''
DIVIDER = 2
print(bin(num_dec))
while num_dec > 0:
    res = str(num_dec % DIVIDER) + res
    num_dec //= DIVIDER
print(res)


num_dec = int(input("введите число: "))
res = ''
DIVIDER = 8
print(oct(num_dec))
while num_dec > 0:
    res = str(num_dec % DIVIDER) + res
    num_dec //= DIVIDER
print(res)
