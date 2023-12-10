"""
Задание №2.
Напишите для задачи 1 тесты doctest. Проверьте
следующие варианты:
- возврат строки без изменений
- возврат строки с преобразованием регистра без потери
- символов
- возврат строки с удалением знаков пунктуации
- возврат строки с удалением букв других алфавитов
- возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)
"""
import re
from doctest import testmod


def filter_text(text: str) -> str:
    """
    Удаление из текста всех символов кроме букв латиницы и пробелов
    :param text: Исходный текст.
    :return: Текст в нижнем регистре.
    >>> filter_text("hello world")
    'hello world'
    >>> filter_text("UpperCase")
    'uppercase'
    >>> filter_text("Characters: !@#$%^&*()_+")
    'characters '
    >>> filter_text("ЯкобсCafé")
    'caf'
    >>> filter_text("Привет, MixEdCaSeS!@#")
    ' mixedcases'
    """
    text_out = re.sub(r'[^a-zA-Z\s]', '', text)
    return text_out.lower()


if __name__ == '__main__':
    testmod(verbose=True)
