"""
На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.
Напишите программу, которая должна возвращать сумму и произведение дробей.
Для проверки своего кода используйте модуль fractions.
"""

from fractions import Fraction

frac1 = "1/2"
frac2 = "1/3"

def sum_and_product(frac1, frac2):
    # Разделение строк на числитель и знаменатель
    numer1, denom1 = map(int, frac1.split('/'))
    numer2, denom2 = map(int, frac2.split('/'))

    # Вычисление суммы дробей
    sum_numer = numer1 * denom2 + numer2 * denom1
    sum_denom = denom1 * denom2
    
    # Вычисление произведения дробей
    prod_numer = numer1 * numer2
    prod_denom = denom1 * denom2

    # Приведение дробей к несократимому виду
    gcd_sum = gcd(sum_numer, sum_denom)
    sum_numer //= gcd_sum
    sum_denom //= gcd_sum
    gcd_prod = gcd(prod_numer, prod_denom)
    prod_numer //= gcd_prod
    prod_denom //= gcd_prod

    # Возвращение результатов в виде строк
    print(f"Сумма дробей: {sum_numer}/{sum_denom}")
    print(f"Произведение дробей: {prod_numer}/{prod_denom}")
    # return f"Сумма дробей: {sum_numer}/{sum_denom}\n", \
    #     f"Произведение дробей: {prod_numer}/{prod_denom}"

# Нахождение наибольшего общего делителя
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

sum_and_product(frac1, frac2)
print("Сумма дробей:", Fraction(frac1) + Fraction(frac2))
print("Произведение дробей:", Fraction(frac1) * Fraction(frac2))
