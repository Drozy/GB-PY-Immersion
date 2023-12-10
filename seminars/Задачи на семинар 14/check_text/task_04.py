"""
Задание №4
    Напишите для задачи 1 тесты pytest. Проверьте следующие
варианты:
- возврат строки без изменений
- возврат строки с преобразованием регистра без потери
символов
- возврат строки с удалением знаков пунктуации
- возврат строки с удалением букв других алфавитов
- возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)
"""
import pytest
from task_01 import filter_text


@pytest.fixture
def unchanged_text():
    return "hello world"


@pytest.fixture
def conversion_text():
    return "UpperCase"


@pytest.fixture
def remove_punctuation():
    return "Characters: !@#,$%^&*()_+."


@pytest.fixture
def remove_non_latin_letters():
    return "ЯкобсCafé"


@pytest.fixture
def mixed_cases():
    return "Привет, MixEdCaSeS!@#"


@pytest.fixture
def input_number():
    return 123


@pytest.fixture
def input_float():
    return 123.45


@pytest.fixture
def input_list():
    return [1, 2, 3]


@pytest.fixture
def input_tuple():
    return 4, 5, 6


@pytest.fixture
def input_none():
    return None


def test_unchanged_text(unchanged_text):
    assert filter_text(unchanged_text) == 'hello world'


def test_case_conversion(conversion_text):
    assert filter_text(conversion_text) == 'uppercase'


def test_remove_punctuation(remove_punctuation):
    assert filter_text(remove_punctuation) == 'characters '


def test_remove_non_latin_letters(remove_non_latin_letters):
    assert filter_text(remove_non_latin_letters) == 'caf'


def test_mixed_filters(mixed_cases):
    assert filter_text(mixed_cases) == ' mixedcases'


def test_input_number(input_number):
    with pytest.raises(TypeError):
        filter_text(input_number)


def test_input_float(input_float):
    with pytest.raises(TypeError):
        filter_text(input_float)


def test_input_list(input_list):
    with pytest.raises(TypeError):
        filter_text(input_list)


def test_input_tuple(input_tuple):
    with pytest.raises(TypeError):
        filter_text(input_tuple)


def test_input_none(input_none):
    with pytest.raises(TypeError):
        filter_text(input_none)


if __name__ == '__main__':
    pytest.main(['-v'])
