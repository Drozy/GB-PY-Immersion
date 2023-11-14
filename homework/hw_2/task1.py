"""
Напишите программу, которая получает целое число num и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата. 
"""

num = int(input("введите число: "))
decimal_number = num
hexadecimal_digits = "0123456789ABCDEF"  # Строка с шестнадцатеричными цифрами
hexadecimal_number = ""

while decimal_number > 0:
    remainder = decimal_number % 16  # Получаем остаток от деления на 16
    # Получаем шестнадцатеричную цифру
    hexadecimal_digit = hexadecimal_digits[remainder]
    # Добавляем цифру в начало шестнадцатеричного числа
    hexadecimal_number = hexadecimal_digit + hexadecimal_number
    decimal_number //= 16  # Выполняем целочисленное деление на 16
print("Шестнадцатеричное представление числа:", hexadecimal_number)
print("Проверка результата:", hex(num))
