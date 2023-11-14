"""
У вас есть банковская карта с начальным балансом равным 0 у.е. Вы хотите управлять этой картой, 
выполняя следующие операции, для выполнения которых необходимо написать следующие функции:
check_multiplicity(amount): Проверка кратности суммы при пополнении и снятии. 
deposit(amount): Пополнение счёта. 
withdraw(amount): Снятие денег. 
exit(): Завершение работы и вывод итоговой информации о состоянии счета и проведенных операциях.

Пополнение счета:
Функция deposit(amount) позволяет клиенту пополнять свой счет на определенную сумму. 
Пополнение счета возможно только на сумму, которая кратна MULTIPLICITY. Если сумма пополнения превышает RICHNESS_SUM, 
то начисляется налог на богатство в размере RICHNESS_PERCENT процентов.

Снятие средств:
Функция withdraw(amount) позволяет клиенту снимать средства со счета. Сумма снятия также должна быть кратной MULTIPLICITY. 
При снятии средств начисляется комиссия в процентах от снимаемой суммы, которая может варьироваться от MIN_REMOVAL до MAX_REMOVAL.

Завершение работы:
Функция exit() завершает работу с банковским счетом. Перед завершением, если на счету больше RICHNESS_SUM, начисляется налог 
на богатство в размере RICHNESS_PERCENT процентов.

Проверка кратности суммы:
Функция check_multiplicity(amount) проверяет, кратна ли сумма amount заданному множителю MULTIPLICITY. 

Реализуйте программу для управления банковским счетом, используя библиотеку decimal для точных вычислений.

"""

from decimal import Decimal


MULTIPLICITY = 50
RICHNESS_SUM = 1_000_000_000_000_000
RICHNESS_PERCENT = 0.1
MIN_REMOVAL = 5_000
MAX_REMOVAL = 100_000
account = Decimal("0")
operations = []


def deposit(amount):
    global account, operations
    if check_multiplicity(amount):
        account += amount
        if amount > RICHNESS_SUM:
            account = Decimal(account * (1 - RICHNESS_PERCENT)).quantize(Decimal("1"))
        operations.append(f'Пополнение карты на {amount} у.е. Итого {account} у.е.')
    return


def withdraw(amount):
    global account, operations
    commission = 30
    if check_multiplicity(amount):
        if MIN_REMOVAL <= amount <= MAX_REMOVAL:
            account -= Decimal(amount)
        else:
            amount = True
        account -= (commission + 1)
        operations.append(f'Снятие с карты {amount} у.е. Процент за снятие {commission}. Итого {account} у.е.')
    if account == 0:
        operations.append(f'Недостаточно средств. Сумма с комиссией {commission} у.е. На карте {account} у.е.')
    return


def exit():
    global account, operations
    if account > RICHNESS_SUM:
        tax = (account * Decimal(RICHNESS_PERCENT)).quantize(Decimal("1.0"))
        account -= tax
        operations.append(f'Вычтен налог на богатство {RICHNESS_PERCENT}% в сумме {tax} у.е. Итого {account} у.е.')
    operations.append(f'Возьмите карту на которой {account} у.е.')
    return


def check_multiplicity(amount):
    if amount % MULTIPLICITY == 0:
        return True
    else:
        print(f'Сумма должна быть кратной {MULTIPLICITY} у.е.')
        return False


# deposit(1000)
# withdraw(200)

# deposit(173)
# withdraw(21)

deposit(1000000000000000)
withdraw(200)
withdraw(300)
deposit(500)
withdraw(3000)

exit()

print(operations)
