# G. Построить квадрат
# Ограничение времени	2 секунды
# Ограничение памяти	256Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Задано множество, состоящее из N различных точек на плоскости. Координаты всех точек — целые числа.
# Определите, какое минимальное количество точек нужно добавить во множество, чтобы нашлось четыре точки, лежащие в
# вершинах квадрата.
#
# Формат ввода
# В первой строке вводится число N (1 ≤ N ≤ 2000) — количество точек.
#
# В следующих N строках вводится по два числа xi, yi (-108 ≤ xi, yi ≤ 108) — координаты точек.
#
# Формат вывода
# В первой строке выведите число K — минимальное количество точек, которые нужно добавить во множество.
#
# В следующих K строках выведите координаты добавленных точек xi, yi через пробел. Координаты должны быть целыми
# и не превышать 109 по модулю.
#
# Если решений несколько — выведите любое из них.
#
# Пример 1
# Ввод
# 2
# 0 1
# 1 0
# Вывод
# 2
# 0 0
# 1 1
# Пример 2
# Ввод
# 3
# 0 2
# 2 0
# 2 2
# Вывод
# 1
# 0 0
# Пример 3
# Ввод
# 4
# -1 1
# 1 1
# -1 -1
# 1 -1
# Вывод
# 0
list_of_coords = set()
with open('./input.txt') as f:  # 1
    N = int(f.readline())
    for i in range(N):
        x, y = map(int, f.readline().split())
        list_of_coords.add((x, y))

least_dots_to_full_square = 2
least_dots = []
list_of_coords_copy = list_of_coords.copy()  # a copy of original set to look up in later

if N == 1:
    print('3')
    print(x + 1, y)
    print(x + 1, y + 1)
    print(x, y + 1)

else:
    for i in range(len(list_of_coords) - 1):

        if least_dots_to_full_square == 0:
            break

        dot_1 = list_of_coords.pop()

        for dot_2 in list_of_coords:

            dots_to_full_square = 2

            # get delta to center, and dx, dy - distances to center of square from each coord
            if dot_1[0] >= dot_2[0]:
                dx = (dot_1[0] - dot_2[0]) / 2
                cent_x = dot_1[0] - dx
            else:
                dx = (dot_2[0] - dot_1[0]) / 2
                cent_x = dot_2[0] - dx

            if dot_1[1] >= dot_2[1]:
                dy = (dot_1[1] - dot_2[1]) / 2
                cent_y = dot_1[1] - dy
            else:
                dy = (dot_2[1] - dot_1[1]) / 2
                cent_y = dot_2[1] - dy
            # positive slope case
            if ((dot_1[0] >= dot_2[0]) and (dot_1[1] >= dot_2[1])) or \
                    ((dot_1[0] <= dot_2[0]) and (dot_1[1] <= dot_2[1])):
                possible_coord_1 = (cent_x - dy, cent_y + dx)
                possible_coord_2 = (cent_x + dy, cent_y - dx)
            # negative slope case
            else:
                possible_coord_1 = (cent_x + dy, cent_y + dx)
                possible_coord_2 = (cent_x - dy, cent_y - dx)

            dots_to_add = [possible_coord_1, possible_coord_2]

            if possible_coord_1 in list_of_coords_copy:
                dots_to_full_square -= 1
                dots_to_add.remove(possible_coord_1)
            if possible_coord_2 in list_of_coords_copy:
                dots_to_full_square -= 1
                dots_to_add.remove(possible_coord_2)

            if dots_to_full_square < least_dots_to_full_square:
                least_dots_to_full_square = dots_to_full_square
                least_dots = dots_to_add.copy()

                if dots_to_full_square == 0:
                    least_dots.clear()
                    break

            if not least_dots:
                least_dots = dots_to_add.copy()

# calculate not diagonally for experiment
if least_dots_to_full_square == 2:
    least_dots.clear()
    dot_1 = list_of_coords_copy.pop()
    dot_2 = list_of_coords_copy.pop()

    if dot_1[0] >= dot_2[0]:
        dx = (dot_1[0] - dot_2[0])
    else:
        dx = (dot_2[0] - dot_1[0])

    if dot_1[1] >= dot_2[1]:
        dy = (dot_1[1] - dot_2[1])
    else:
        dy = (dot_2[1] - dot_1[1])

    if ((dot_1[0] >= dot_2[0]) and (dot_1[1] >= dot_2[1])) or \
            ((dot_1[0] <= dot_2[0]) and (dot_1[1] <= dot_2[1])):
        possible_coord_1 = (dot_1[0] + dy, dot_1[1] - dx)
        possible_coord_2 = (dot_2[0] + dy, dot_2[1] - dx)
    else:
        possible_coord_1 = (dot_1[0] + dy, dot_1[1] + dx)
        possible_coord_2 = (dot_2[0] + dy, dot_2[1] + dx)

    least_dots = [possible_coord_1, possible_coord_2]

print(least_dots_to_full_square)
for i in least_dots:
    print(int(i[0]), int(i[1]))
# python- TL, C++ - ok
