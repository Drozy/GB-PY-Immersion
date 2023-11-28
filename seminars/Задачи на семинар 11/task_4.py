"""
Задание №4
Добавьте функции представления экземпляра для программиста и для пользователя
"""


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

    def __str__(self):
        return f'[num= {self.num}, text= "{self.text}"]'

    def __repr__(self):
        return f'Archive("{self.text}", {self.num})'


if __name__ == '__main__':
    f1 = Archive('Text1', 111)
    print(f1)
    print(repr(f1))
