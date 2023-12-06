"""
Создайте класс студента.
○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
Если ФИО не соответствует условию, выведите:

ФИО должно состоять только из букв и начинаться с заглавной буквы

○ Названия предметов должны загружаться из файла CSV при создании экземпляра.
Другие предметы в экземпляре недопустимы. Если такого предмета нет, выведите:

Предмет {Название предмета} не найден

○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
В противном случае выведите:

Оценка должна быть целым числом от 2 до 5
Результат теста должен быть целым числом от 0 до 100

○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам
всех предметов вместе взятых.

Вам предоставлен файл subjects.csv, содержащий предметы, например:
Математика,Физика,История,Литература

Создайте класс Student, который будет представлять студента и его успехи по предметам.
Атрибуты класса:
name (str): ФИО студента.
subjects (dict): Словарь, который хранит предметы в качестве ключей и информацию об оценках
и результатах тестов для каждого предмета в виде словаря.
"""

import csv


class Student:
    """Класс Student, который представляет студента и его успехи по предметам."""

    def __init__(self, name, subjects_file):
        """
        Конструктор класса. Принимает имя студента и файл с предметами и их результатами.
        Инициализирует атрибуты name и subjects и вызывает метод load_subjects
        для загрузки предметов из файла.
        """
        self.name = name
        self.subjects = {}
        self.load_subjects(subjects_file)

    def __setattr__(self, name, value):
        """
        Дескриптор, который проверяет установку атрибута name.
        Убеждается, что name начинается с заглавной буквы и состоит только из букв.
        """
        alphabet = {"а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о",
                    "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"}
        if name == "name":
            if not bool(alphabet.intersection(set(value.lower()))) or value[0].islower():
                print("ФИО должно состоять только из букв и начинаться с заглавной буквы")
        else:
            self.__dict__[name] = value

    def __getattr__(self, name):    # TODO: что-то не так
        """
        Позволяет получать значения атрибутов предметов (оценок и результатов тестов) по их именам.
        """

        if name in self.subjects:
            return self.subjects[name]
        return f'Предмет {name} не найден'

    def __str__(self):
        """
        Возвращает строковое представление студента, включая имя и список предметов.
        Студент: Иван Иванов
        Предметы: Математика, История
        """
        subjects = ""
        for subj in self.subjects:
            if subjects != "":
                subjects = subjects + ", " + subj
            else:
                subjects = subj
        return f'Студент: {self.name}\nПредметы: {subjects}'

    def load_subjects(self, subjects_file):
        """
        Загружает предметы из файла CSV.
        Использует модуль csv для чтения данных из файла и добавляет предметы в атрибут subjects.
        """
        with open(subjects_file, encoding="utf-8") as csv_f:
            for subj in list(csv.reader(csv_f))[0]:
                self.subjects[subj] = {'grades': [], 'test_scores': []}

    def add_grade(self, subject, grade):
        """
        Добавляет оценку по заданному предмету.
        Убеждается, что оценка является целым числом от 2 до 5.
        """
        if 2 <= grade <= 5 and isinstance(grade, int):
            if subject in self.subjects:
                self.subjects[subject]['grades'].append(grade)
            else:
                print(f"Предмет {subject} не найден")
        else:
            print("Оценка должна быть целым числом от 2 до 5")

    def add_test_score(self, subject, test_score):
        """
        Добавляет результат теста по заданному предмету.
        Убеждается, что результат теста является целым числом от 0 до 100.
        """
        if 0 <= test_score <= 100 and isinstance(test_score, int):
            if subject in self.subjects:
                self.subjects[subject]['test_scores'].append(test_score)
            else:
                print(f"Предмет {subject} не найден")
        else:
            print("Результат теста должен быть целым числом от 0 до 100")

    def get_average_test_score(self, subject):
        """
        Возвращает средний балл по тестам для заданного предмета.
        """
        if subject in self.subjects:
            test_scores = self.subjects[subject]['test_scores']
            return sum(test_scores) / len(test_scores)
        raise ValueError(f"Предмет {subject} не найден")

    def get_average_grade(self):
        """
        Возвращает средний балл по всем предметам.
        """
        grades_count = 0
        grades_sum = 0
        for value in self.subjects.values():
            grades_count += len(value['grades'])
            grades_sum += sum(value['grades'])
        return grades_sum / grades_count


if __name__ == '__main__':
    student = Student("Иван Иванов", "subjects.csv")

    student.add_grade("Математика", 4)
    student.add_test_score("Математика", 85)

    student.add_grade("История", 5)
    student.add_test_score("История", 92)

    print(student)

    average_grade = student.get_average_grade()
    print(f"Средний балл: {average_grade}")

    average_test_score = student.get_average_test_score("Математика")
    print(f"Средний результат по тестам по математике: {average_test_score}")
