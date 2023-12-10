"""
Задание №1
📌 Создайте класс Моя Строка, где:
📌 будут доступны все возможности str
📌 дополнительно хранятся имя автора строки и время создания
(time.time)
"""
import time


class MyString(str):
    """
    Класс наследник класса str
    """

    def __new__(cls, text, author):
        """
        При создании экземпляра класса добавляются имя автора и время создания
        :param text: Any text
        :param author: Author's name
        """
        instance = super().__new__(cls, text)
        instance.author = author
        instance.init_time = time.strftime('%H:%M:%S')
        return instance


if __name__ == '__main__':
    my_str = MyString("My text", "me")
    print(f'{my_str=}\n{my_str.author=}\n{my_str.init_time=}')

    help(MyString)
