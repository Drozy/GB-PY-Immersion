"""
Задание №6
📌 Доработайте прошлую задачу.
📌 Добавьте сравнение прямоугольников по площади
📌 Должны работать все шесть операций сравнения
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

    def __eq__(self, other):
        """равны"""
        return self.get_perimeter() == other.get_perimeter()

    def __ne__(self, other):
        """не равны"""
        return self.get_perimeter() != other.get_perimeter()

    def __gt__(self, other):
        """больше"""
        return self.get_perimeter() > other.get_perimeter()

    def __lt__(self, other):
        """меньше"""
        return self.get_perimeter() < other.get_perimeter()

    def __ge__(self, other):
        """больше или равно"""
        return self.get_perimeter() >= other.get_perimeter()

    def __le__(self, other):
        """меньше или равно"""
        return self.get_perimeter() <= other.get_perimeter()


if __name__ == '__main__':
    rectangle1 = Rectangle(7.3)
    rectangle2 = Rectangle(5.6, 10.2)

    print(f'Равны: {rectangle1 == rectangle2}')
    print(f'Не равны: {rectangle1 != rectangle2}')
    print(f'Больше: {rectangle1 > rectangle2}')
    print(f'Меньше: {rectangle1 < rectangle2}')
