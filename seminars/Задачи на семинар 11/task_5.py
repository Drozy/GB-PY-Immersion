"""
Задание №5
📌 Дорабатываем класс прямоугольник из прошлого семинара.
📌 Добавьте возможность сложения и вычитания.
📌 При этом должен создаваться новый экземпляр прямоугольника.
📌 Складываем и вычитаем периметры, а не длинну и ширину.
📌 При вычитании не допускайте отрицательных значений.
"""


class Rectangle:

    def __init__(self, side_a, side_b=0.0):
        self._side_a = side_a
        if side_b == 0:
            side_b = side_a
        self._side_b = side_b

    def get_perimeter(self):
        return 2 * (self._side_a + self._side_b)

    def get_area(self):
        return self._side_a * self._side_b

    def __add__(self, other):
        perimeter = self.get_perimeter() + other.get_perimeter()
        return Rectangle(perimeter / 4)

    def __sub__(self, other):
        perimeter = abs(self.get_perimeter() - other.get_perimeter())
        return Rectangle(perimeter / 4)

    def __str__(self):
        return f'[a = {self._side_a:.2f}, b = {self._side_b:.2f}]'


if __name__ == '__main__':
    rectangle1 = Rectangle(7.3)
    rectangle2 = Rectangle(5.6, 10.2)

    print(f'Сложение: {rectangle1 + rectangle2}')
    print(f'Вычитание: {rectangle1 - rectangle2}')
