# D. Шахматная доска
# Ограничение времени 1 секунда Ограничение памяти 64Mb
#
# Ввод стандартный ввод или input.txt Вывод стандартный вывод или output.txt
#
# Из шахматной доски по границам клеток выпилили связную (не распадающуюся на части) фигуру без дыр.
# Требуется определить ее периметр.
#
# Формат ввода
#
# Сначала вводится число N (1 ≤ N ≤ 64) – количество выпиленных клеток. В следующих N строках вводятся координаты
# выпиленных клеток, разделенные пробелом (номер строки и столбца – числа от 1 до 8). Каждая выпиленная клетка
# указывается один раз.
#
# Формат вывода
#
# Выведите одно число – периметр выпиленной фигуры (сторона клетки равна единице).
#
# Пример 1
# Ввод
# 3
# 1 1
# 1 2
# 2 1
# Вывод
# 8
# Пример 2
# Ввод
# 1
# 8 8
# Вывод
# 4
#
# Примечания
#
# Вырезан уголок из трех клеток. Сумма длин его сторон равна 8.
#
# Вырезана одна клетка. Ее периметр равен 4.

def calculate_total_sides(N, squares_set):
    x_set = set()
    y_set = set()

    for x, y in squares_set:
        x_set.add(x)
        y_set.add(y)

    x_list = list(x_set)
    x_list.sort()

    previous_Ys = set()
    current_Ys = set()
    total_sides = 0

    for x_coord in range(1, 9):
        for y_coord in range(1, 9):
            if (x_coord, y_coord) in squares_set:
                current_Ys.add(y_coord)
        left_sides = abs(len(current_Ys) - len(current_Ys.intersection(previous_Ys)))
        previous_Ys = current_Ys.copy()
        current_Ys.clear()
        total_sides += left_sides

    previous_Ys.clear()
    current_Ys.clear()

    for x_coord in range(8, 0, -1):
        for y_coord in range(1, 9):
            if (x_coord, y_coord) in squares_set:
                current_Ys.add(y_coord)
        right_sides = abs(len(current_Ys) - len(current_Ys.intersection(previous_Ys)))
        previous_Ys = current_Ys.copy()
        current_Ys.clear()
        total_sides += right_sides

    previous_Xs = set()
    current_Xs = set()

    for y_coord in range(1, 9):
        for x_coord in range(1, 9):
            if (x_coord, y_coord) in squares_set:
                current_Xs.add(x_coord)
        bottom_sides = abs(len(current_Xs) - len(current_Xs.intersection(previous_Xs)))
        previous_Xs = current_Xs.copy()
        current_Xs.clear()
        total_sides += bottom_sides

    previous_Xs.clear()
    current_Xs.clear()

    for y_coord in range(8, 0, -1):
        for x_coord in range(1, 9):
            if (x_coord, y_coord) in squares_set:
                current_Xs.add(x_coord)
        top_sides = abs(len(current_Xs) - len(current_Xs.intersection(previous_Xs)))
        previous_Xs = current_Xs.copy()
        current_Xs.clear()
        total_sides += top_sides

    return total_sides


def main():
    N = int(input())
    squares_set = set()
    for i in range(N):
        x, y = map(int, input().split())
        squares_set.add((x, y))
    result = calculate_total_sides(N, squares_set)
    print(result)


if __name__ == "__main__":
    main()
# ok
