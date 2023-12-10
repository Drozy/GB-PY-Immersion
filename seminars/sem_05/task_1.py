"""
Задание №1
✔ Пользователь вводит строку из четырёх
или более целых чисел, разделённых символом “/”.
Сформируйте словарь, где:
✔второе и третье число являются ключами.
✔первое число является значением для первого ключа.
✔четвертое и все возможные последующие числа
 хранятся в кортеже как значения второго ключа.
"""

# вариант 1
data = "1/2/3/4/5/6".split('/')
dct = {}
for i in range(len(data)):
    if i == 1:
        dct[data[1]] = data[i - 1]

    elif i == 2:
        tuple_obj = set()
        for j in range(3, len(data)):
            tuple_obj.add(data[j])
        dct[data[2]] = tuple_obj

print(dct)

# вариант 2
a, b, c, *d = "1/2/3/4/5/6".split('/')
print({b: a, c: tuple(d)})