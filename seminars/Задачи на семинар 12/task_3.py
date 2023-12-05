"""
Задание №3
Создайте класс-генератор.
Экземпляр класса должен генерировать факториал числа
в диапазоне от start до stop с шагом step.
Если переданы два параметра, считаем step=1.
Если передан один параметр, также считаем start=1.
"""


class Factorial:

    def __init__(self, *args) -> None:
        match args:
            case (stop, ):
                self.stop = stop
                self.start = 1
                self.step = 1
            case (start, stop, ):
                self.start = start
                self.stop = stop
                self.step = 1
            case (start, stop, step):
                self.start = start
                self.stop = stop
                self.step = step
        self.res = 1

    def __iter__(self):
        return self

    def __next__(self):
        while self.start <= self.stop:
            self.res *= self.start
            self.start += self.step
            return self.res
        raise StopIteration


if __name__ == '__main__':
    f = Factorial(1, 5, 1)
    print(list(f))
    f = Factorial(9)
    print(list(f))
