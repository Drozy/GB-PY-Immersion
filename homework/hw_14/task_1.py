"""
Возьмите задачу Rectangle с прошлых семинаров. Напишите тесты для этой задачи.
Используйте модуль doctest.

Тесты:
test_width: Тестирование инициализации ширины. Созданы прямоугольники r1 с шириной 5
и r4 с отрицательной шириной (-2). Убедимся, что r1.width корректно установлен на 5,
а создание r4 вызывает исключение NegativeValueError.

test_height: Тестирование инициализации ширины и высоты. Созданы прямоугольники r2
с шириной 3 и высотой 4. Проверяем, что r2.width равно 3 и r2.height равно 4.

test_perimeter: Тестирование вычисления периметра. Создан прямоугольник r1 с шириной 5
и проверяем, что r1.perimeter() возвращает 20. Также создан прямоугольник r2 с шириной
3 и высотой 4 и проверяем, что r2.perimeter() возвращает 14.

test_area: Тестирование вычисления площади. Создан прямоугольник r1 с шириной 5
и проверяем, что r1.area() возвращает 25. Также создан прямоугольник r2 с шириной 3
и высотой 4 и проверяем, что r2.area() возвращает 12.

test_addition: Тестирование операции сложения. Созданы прямоугольники r1 с шириной 5
и r2 с шириной 3 и высотой 4. Выполняем операцию сложения r1 + r2 и проверяем, что
полученный прямоугольник r3 имеет правильные значения ширины и высоты (8 и 6.0 соответственно).

test_subtraction: Тестирование операции вычитания. Созданы прямоугольники r1 с шириной
5 и r2 с шириной 3 и высотой 4. Выполняем операцию вычитания r1 - r2 и проверяем,
что полученный прямоугольник r3 имеет правильные значения ширины и высоты (2 и 2.0 соответственно).
"""
import doctest


class NegativeValueError(Exception):
    pass


class Rectangle:
    """
    Класс, представляющий прямоугольник.

    Атрибуты:
    - width (int): ширина прямоугольника
    - height (int): высота прямоугольника

    Методы:
    - perimeter(): вычисляет периметр прямоугольника
    - area(): вычисляет площадь прямоугольника
    - __add__(other): определяет операцию сложения двух прямоугольников
    - __sub__(other): определяет операцию вычитания одного прямоугольника из другого
    - __lt__(other): определяет операцию "меньше" для двух прямоугольников
    - __eq__(other): определяет операцию "равно" для двух прямоугольников
    - __le__(other): определяет операцию "меньше или равно" для двух прямоугольников
    - __str__(): возвращает строковое представление прямоугольника
    - __repr__(): возвращает строковое представление прямоугольника, которое может быть
    использовано для создания нового объекта
    """

    def __init__(self, width, height=None):
        """
        test_width
        >> > r1 = Rectangle(5)
        >> > print(r1.width)
        5
        >> > r4 = Rectangle(-2)
        Traceback(most recent call last):
        ...
        NegativeValueError: Ширина должна быть положительной, а не - 2

        test_height
        >>> r2 = Rectangle(3, 4)
        >>> r2.width
        3
        >>> r2.height
        4
        """
        if not isinstance(width, (int, float)):
            raise NegativeValueError(f"Ширина должна быть числом, а не {width}")
        elif width < 0:
            raise NegativeValueError(f"Ширина должна быть положительной, а не {width}")
        else:
            self.width = width
        if height is None:
            self.height = width
        else:
            if not isinstance(height, (int, float)):
                raise NegativeValueError(f"Высота должна быть числом, а не {height}")
            elif height < 0:
                raise NegativeValueError(f"Высота должна быть положительной, а не {height}")
            self.height = height

    def perimeter(self):
        """
        Вычисляет периметр прямоугольника.

        Возвращает:
        - int: периметр прямоугольника

        test_perimeter
        >>> r1 = Rectangle(5)
        >>> r1.perimeter()
        20
        >>> r2 = Rectangle(3, 4)
        >>> r2.perimeter()
        14
        """
        return 2 * (self.width + self.height)

    def area(self):
        """
        Вычисляет площадь прямоугольника.

        Возвращает:
        - int: площадь прямоугольника

        test_area
        >>> r1 = Rectangle(5)
        >>> r1.area()
        25
        >>> r2 = Rectangle(3, 4)
        >>> r2.area()
        12
        """
        return self.width * self.height

    def __add__(self, other):
        """
        Определяет операцию сложения двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем сложения двух исходных прямоугольников

        test_addition
        >>> r1 = Rectangle(5)
        >>> r2 = Rectangle(3, 4)
        >>> r3 = r1 + r2
        >>> r3.width
        8
        >>> r3.height
        9
        """
        width = self.width + other.width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter // 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        """
        Определяет операцию вычитания одного прямоугольника из другого.

        Аргументы:
        - other (Rectangle): вычитаемый прямоугольник

        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем вычитания вычитаемого прямоугольника из исходного

        test_subtraction
        >>> r1 = Rectangle(5)
        >>> r2 = Rectangle(3, 4)
        >>> r3 = r1 - r2
        >>> r3.width
        2
        >>> r3.height
        1
        """
        width = abs(self.width - other.width)
        perimeter = abs(self.perimeter() - other.perimeter())
        height = perimeter // 2 - width
        return Rectangle(width, height)

    def __lt__(self, other):
        """
        Определяет операцию "меньше" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площадь первого прямоугольника меньше площади второго, иначе False
        """
        return self.area() < other.area()

    def __eq__(self, other):
        """
        Определяет операцию "равно" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площади равны, иначе False
        """
        return self.area() == other.area()

    def __le__(self, other):
        """
        Определяет операцию "меньше или равно" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площадь первого прямоугольника меньше или равна площади второго, иначе False
        """
        return self.area() <= other.area()

    def __str__(self):
        """
        Возвращает строковое представление прямоугольника.

        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        """
        Возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта.

        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Rectangle({self.width}, {self.height})"


if __name__ == '__main__':
    doctest.testmod(verbose=True)
