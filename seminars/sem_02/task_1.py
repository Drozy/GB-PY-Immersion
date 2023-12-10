"""
Задание №1
Создайте несколько переменных разных типов.
Проверьте к какому типу относятся созданные переменные.
"""

data = [5, "string", 0.15, True, None]
for el in data:
    print(type(el))

for i in range(len(data)):
    print(type(data[i]))

# срез
for el in data[1:]:
    print(type(el))