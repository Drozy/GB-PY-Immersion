"""
Задание №3.
    Напишите для задачи 1 тесты unittest. Проверьте
следующие варианты:
    возврат строки без изменений
    возврат строки с преобразованием регистра без потери
символов
    возврат строки с удалением знаков пунктуации
    возврат строки с удалением букв других алфавитов
    возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)
"""
import unittest
from task_01 import filter_text


class TestFilter(unittest.TestCase):

    def setUp(self):
        self.unchanged_string = "hello world"
        self.case_conversion = "UpperCase"
        self.remove_punctuation = "Characters: !@#,$%^&*()_+."
        self.remove_non_latin_letters = "ЯкобсCafé"
        self.mixed_cases = "Привет, MixEdCaSeS!@#"

        self.input_number = 123
        self.input_float = 123.45
        self.input_list = [1, 2, 3]
        self.input_tuple = (4, 5, 6)
        self.input_none = None

    def test_unchanged_text(self):
        self.assertEqual(filter_text(self.unchanged_string), 'hello world')

    def test_conversion_text(self):
        self.assertEqual(filter_text(self.case_conversion), 'uppercase')

    def test_remove_punctuation(self):
        self.assertEqual(filter_text("Characters: !@#,$%^&*()_+."), 'characters ')

    def test_remove_non_latin_letters(self):
        self.assertEqual(filter_text("ЯкобсCafé"), 'caf')

    def test_mixed_filters(self):
        self.assertEqual(filter_text("Привет, MixEdCaSeS!@#"), ' mixedcases')

    def test_input_number(self):
        with self.assertRaises(TypeError):
            filter_text(self.input_number)

    def test_input_float(self):
        with self.assertRaises(TypeError):
            filter_text(self.input_float)

    def test_input_list(self):
        with self.assertRaises(TypeError):
            filter_text(self.input_list)

    def test_input_tuple(self):
        with self.assertRaises(TypeError):
            filter_text(self.input_tuple)

    def test_input_none(self):
        with self.assertRaises(TypeError):
            filter_text(self.input_none)


if __name__ == '__main__':
    unittest.main(verbosity=2)
