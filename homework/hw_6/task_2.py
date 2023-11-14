"""
Добавьте в пакет, созданный на семинаре шахматный модуль.
Внутри него напишите код, решающий задачу о 8 ферзях, включающий в себя
функцию is_attacking(q1,q2), проверяющую, бьют ли ферзи друг друга и heck_queens(queens),
которая проверяет все возможные пары ферзей.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь. Не забудьте напечатать результат.
"""


# queens = []
# for _ in range(8):
#     queen = list(map(int, input().split()))
#     queens.append(queen)

# queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]


def is_attacking(q1, q2):
    if q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1]):
        return True
    return False


def check_queens(queens):
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            q1 = queens[i]
            q2 = queens[j]
            if is_attacking(q1, q2):
                return False
    return True


# if check_queens(queens):
#     print(True)
# else:
#     print(False)

print(check_queens(queens=[(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]))
