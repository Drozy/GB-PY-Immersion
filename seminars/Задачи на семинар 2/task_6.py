"""
Задание №6
Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег
"""

summ = 0
count_add = 0
count_out = 0

while True:
    if summ > 5_000_000:
        print("С вас сняли налог на богатство", summ * 0.1)
        summ -= summ * 0.1

    action = input("Действие: ")

    if action == "q":
        print("Выходим из банкомата")
        print("Сумма:", summ)
        break
    elif action == "a":
        summ_add = int(input("Сумма: "))
        if summ_add % 50 == 0:
            summ += summ_add
            count_add += 1
            if count_add % 3 == 0:
                summ *= 1.03
        else:
            print("Введена некорректная сумма (не кратна 50)")
    elif action == "o":
        summ_out = int(input("Сумма: "))
        comission = summ_out * 0.015
        if comission < 30:
            comission = 30
        elif comission > 600:
            comission = 600
        if summ_out + comission > summ:
            print("Недостаточно средств")
        else:
            if summ_out % 50 == 0:
                summ -= summ_out + comission
                count_out += 1
                if count_out % 3 == 0:
                    summ *= 1.03
            else:
                print("Введена некорректная сумма")
    print("Сумма:", summ)
