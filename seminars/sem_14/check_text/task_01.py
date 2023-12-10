"""
Задание №1.
Создайте функцию, которая удаляет из текста все символы
кроме букв латинского алфавита и пробелов.
Возвращается строка в нижнем регистре.
"""
import re


def filter_text(text: str) -> str:
    text_out = re.sub(r'[^a-zA-Z\s]', '', text)
    return text_out.lower()


if __name__ == '__main__':
    original_text = "Hello Вася123! How are you?"
    print(filter_text(original_text))
