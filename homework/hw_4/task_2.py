"""
Напишите функцию key_params, принимающую на вход только ключевые параметры и возвращающую 
словарь, где ключ - значение переданного аргумента, а значение - имя аргумента.
Если ключ не хешируем, используйте его строковое представление. 
"""

def key_params(**kwargs):
    result_dict = {}
    for k, v in kwargs.items():
        if isinstance(v, list) or isinstance(v, dict) or v == None:
            result_dict[str(v)] = k
        else:
            result_dict[v] = k
    return result_dict

# params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
# print(params)

print(key_params(a = None, b = '', c = [], d = {}))