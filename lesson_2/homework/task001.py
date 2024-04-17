# A. Минимальный прямоугольник
# Ограничение времени 1 секунда Ограничение памяти 64Mb
#
# Ввод стандартный ввод или input.txt Вывод стандартный вывод или output.txt
#
# На клетчатой плоскости закрашено K клеток. Требуется найти минимальный по площади прямоугольник, со сторонами,
# параллельными линиям сетки, покрывающий все закрашенные клетки.
#
# Формат ввода
#
# Во входном файле, на первой строке, находится число K (1 ≤ K ≤ 100). На следующих K строках находятся пары
# чисел Xi и Yi — координаты закрашенных клеток (|Xi|, |Yi| ≤ 109).
#
# Формат вывода
#
# Выведите в выходной файл координаты левого нижнего и правого верхнего углов прямоугольника.
#
# Пример
# Ввод
# 4 1 3 3 1 3 5 6 3
# Вывод
# 1 1 6 5
def find_min_max_coordinates(K, coords):
    Xmin, Ymin, Xmax, Ymax = coords[0][0], coords[0][1], coords[0][0], coords[0][1]

    for i in range(K):
        if coords[i][0] < Xmin:
            Xmin = coords[i][0]
        if coords[i][0] > Xmax:
            Xmax = coords[i][0]
        if coords[i][1] < Ymin:
            Ymin = coords[i][1]
        if coords[i][1] > Ymax:
            Ymax = coords[i][1]

    return Xmin, Ymin, Xmax, Ymax


def main():
    K = int(input())
    coords = []

    for i in range(K):
        x, y = map(int, input().split())
        coords.append((x, y))

    Xmin, Ymin, Xmax, Ymax = find_min_max_coordinates(K, coords)
    print(Xmin, Ymin, Xmax, Ymax)


if __name__ == "__main__":
    main()
# ok
