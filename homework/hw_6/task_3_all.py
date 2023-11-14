from time import perf_counter


def queens(n, cur_column=None, all_positions=None, pos_in_prev_columns=None, used_rows=None, used_diags1=None,
           used_diags2=None):
    # При стартовом вызове заполняем все необходимые массивы
    if cur_column is None:
        cur_column = 0
        all_positions = []  # Список всех найденных позиций
        pos_in_prev_columns = []
        used_rows = [False] * n  # Список ферзей в предыдущих столбцах (True=занято)
        used_diags1 = [False] * (2 * n - 1)  # Список занятых диагоналей первого типа
        used_diags2 = [False] * (2 * n - 1)  # Список занятых диагоналей второго типа
    # В первом столбце перебираем только верхнюю половину доски, дальше по симметрии. Ускоряет в 2 раза
    if cur_column == 0:
        check_rows_in_this_column = (n + 1) // 2
    else:
        check_rows_in_this_column = n
    for row_num in range(check_rows_in_this_column):
        # Если горизонталь или диагональ заняты, идём дальше
        if used_rows[row_num] or used_diags1[row_num + cur_column] or used_diags2[row_num - cur_column]:
            continue
        # Если дошли до конца, то это победа!
        elif cur_column == n - 1:
            all_positions.append(pos_in_prev_columns + [row_num])
            # При необходимости добавляем симметричный вариант
            if pos_in_prev_columns[0] < n // 2:
                all_positions.append([n - 1 - x for x in all_positions[-1]])
        else:
            # Стандартный перебор с возвратом. Ставим нового ферзя, запускаем рекурсию, откатываемся
            used_rows[row_num] = used_diags1[row_num + cur_column] = used_diags2[row_num - cur_column] = True
            pos_in_prev_columns.append(row_num)
            queens(n, cur_column + 1, all_positions, pos_in_prev_columns, used_rows, used_diags1, used_diags2)
            pos_in_prev_columns.pop()
            used_rows[row_num] = used_diags1[row_num + cur_column] = used_diags2[row_num - cur_column] = False
    return all_positions


n = 8
st = perf_counter()
all_pos = queens(n)
en = perf_counter()
print(f'Всего {len(all_pos)} позиций для доски {n}×{n}')
print('time:', '{:.3}'.format(en - st))
for pos in sorted(all_pos):
    print(', '.join('ABCDEFGHIJKLMNOP'[col_n] + str(row_n + 1) for col_n, row_n in enumerate(pos)))
