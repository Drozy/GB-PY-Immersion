"""
Задание №7
Погружение в Python | Коллекции
✔ Пользователь вводит строку текста.
✔ Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним.
✔ Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке.
✔ Обратите внимание на порядок ключей. Объясните почему они совпадают или не совпадают в ваших решениях.
"""

text = "Apuleius Florida. Gaius Iulius Caesar De Bello Gallico. Cicero Pro "\
"Quincto. De Lege Agraria Contra Rullum!"

my_dict = {}

for item in text.lower():
    if item.isalpha():
        my_dict[item] = my_dict.get(item, 0) + 1

print(my_dict)