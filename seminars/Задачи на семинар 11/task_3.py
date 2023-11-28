"""
Задание №3
Добавьте к задачам 1 и 2 строки документации для классов
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


class Archive:
    """
    Класс Архив хранит пару число-строка.
    В свойстве arch хранятся значения всех экземпляров класса.
    """
    arch = []

    def __init__(self, text: str, num: int):
        """
        При инициализации экземпляра класса входные значения сохраняются в список-архив
        :param text: any text
        :param num: any integer number
        """
        self.num = num
        self.text = text
        self.save_to_archive(self.arch)

    def save_to_archive(self, arch):
        """Сохранение значений текущего экземпляра в список-архив"""
        arch.append([self.num, self.text])


if __name__ == '__main__':
    print(MyString.__doc__)
    print(Archive.__doc__)
