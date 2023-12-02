"""
Разработать класс Matrix, представляющий матрицу и обеспечивающий базовые операции с матрицами.

Атрибуты класса:

rows (int): Количество строк в матрице.
cols (int): Количество столбцов в матрице.
data (list): Двумерный список, содержащий элементы матрицы.

Методы класса:

__init__(self, rows, cols): Конструктор класса, который инициализирует атрибуты rows и cols,
а также создает двумерный список data размером rows x cols и заполняет его нулями.

__str__(self): Метод, возвращающий строковое представление матрицы. Возвращаемая строка
представляет матрицу, где элементы разделены пробелами, а строки разделены символами новой строки.
Например:
1 2 3
4 5 6

__repr__(self): Метод, возвращающий строковое представление объекта, которое может быть использовано
для создания нового объекта того же класса с такими же размерами и данными.

__eq__(self, other): Метод, определяющий операцию "равно" для двух матриц. Сравнивает две матрицы
и возвращает True, если они имеют одинаковое количество строк и столбцов, а также все элементы равны.
Иначе возвращает False.

__add__(self, other): Метод, определяющий операцию сложения двух матриц. Проверяет, что обе матрицы
имеют одинаковые размеры (количество строк и столбцов). Если размеры совпадают, создает новую матрицу,
где каждый элемент равен сумме соответствующих элементов входных матриц.

__mul__(self, other): Метод, определяющий операцию умножения двух матриц. Проверяет, что количество
столбцов в первой матрице равно количеству строк во второй матрице. Если условие выполняется,
создает новую матрицу, где элемент на позиции [i][j] равен сумме произведений элементов соответствующей
строки из первой матрицы и столбца из второй матрицы.
"""


class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def __str__(self):
        matrix_str = ''
        for i in range(self.rows):
            for j in range(self.cols):
                matrix_str += str(self.data[i][j])
                if j != self.cols - 1:
                    matrix_str += ' '
            if i != self.rows - 1:
                matrix_str += '\n'
        return matrix_str

    def __repr__(self):
        return f'Matrix({self.rows}, {self.cols})'

    def __eq__(self, other):
        if self.rows == other.rows and self.cols == other.cols:
            for i in range(self.rows):
                for j in range(self.cols):
                    if self.data[i][j] != other.data[i][j]:
                        return False
            return True
        return False

    def __add__(self, other):
        if self.rows == other.rows and self.cols == other.cols:
            new_matrix = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    new_matrix.data[i][j] = self.data[i][j] + other.data[i][j]
            return new_matrix
        raise ValueError('Матрицы имеют разные размеры')

    def __mul__(self, other):
        if self.cols == other.rows:
            new_matrix = Matrix(self.rows, other.cols)
            for i in range(self.rows):
                for j in range(other.cols):
                    new_matrix.data[i][j] = sum(self.data[i][k] * other.data[k][j] for k in range(other.rows))
            return new_matrix
        raise ValueError('Количество столбцов в первой матрице не равно количеству строк во второй матрице')


if __name__ == '__main__':
    # Создаем матрицы
    matrix1 = Matrix(2, 3)
    matrix1.data = [[1, 2, 3], [4, 5, 6]]

    matrix2 = Matrix(2, 3)
    matrix2.data = [[7, 8, 9], [10, 11, 12]]

    # Выводим матрицы
    print(matrix1)
    print(matrix2)

    # Сравниваем матрицы
    print(matrix1 == matrix2)  # False

    # Выполняем операцию сложения матриц
    matrix_sum = matrix1 + matrix2
    print(matrix_sum)
    # 8 10 12
    # 14 16 18

    # Выполняем операцию умножения матриц
    matrix3 = Matrix(3, 2)
    matrix3.data = [[1, 2], [3, 4], [5, 6]]

    matrix4 = Matrix(2, 2)
    matrix4.data = [[7, 8], [9, 10]]

    result = matrix3 * matrix4
    print(result)
    # 25 28
    # 57 64
    # 89 100
