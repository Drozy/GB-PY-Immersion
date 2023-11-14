"""
Напишите функцию для транспонирования матрицы transposed_matrix, 
принимает в аргументы matrix, и возвращает транспонированную матрицу. 
"""

# matrix = [[1, 2, 3],
#          [4, 5, 6], 
#          [7, 8, 9]]


def transpose(matrix):
    new_m = []
    rows = len(matrix)
    columns = len(matrix[0])
    for i in range(columns):
        tmp_m = []
        for j in range(rows):
            tmp_m.append(matrix[j][i])
        new_m.append(tmp_m)
    return new_m


# transposed_matrix = transpose(matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
transposed_matrix = transpose(matrix = [[1]])
print (transposed_matrix)
