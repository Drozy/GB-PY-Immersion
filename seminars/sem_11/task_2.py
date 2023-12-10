"""
Задание №2
Создайте класс Архив, который хранит пару свойств. Например, число и строку.
При создании нового экземпляра класса старые данные из ранее созданных экземпляров
сохраняются в пару списков-архивов.
Списки-архивы также являются свойствами экземпляра.
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


if __name__ == '__main__':
    f1 = Archive('Text1', 111)
    print(f1.arch)
    f2 = Archive('Text2', 222)
    print(f2.arch)
