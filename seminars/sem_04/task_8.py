"""
Задание №8
✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
✔ Напишите функцию, которая при запуске заменяет содержимое переменных
оканчивающихся на s (кроме переменной из одной буквы s) на None.
✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
"""
names = ['Alex', 'Nick', 'Michael']
count = 1
tapes = 1500
txt = 'Test'
rows = 'first'
s = -15
sym_calls = True

my_vars = globals().copy()

def rename_vars(vars):
    my_var_name = {}
    for item in vars.keys():
        if not item.startswith('__'):
            my_var_name[item] = vars[item]

    for el in my_var_name.copy():
        if el.endswith("s") and len(el) != 1:
            my_var_name[el[:-1]] = my_var_name[el]
            my_var_name[el] = None
    return my_var_name

# print(rename_vars(globals().copy()))
print(rename_vars(my_vars))
