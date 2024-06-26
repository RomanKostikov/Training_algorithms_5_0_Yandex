# I. Пираты Баренцева моря
# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Вася играет в настольную игру «Пираты Баренцева моря», которая посвящена морским битвам.
# Игровое поле представляет собой квадрат из N×N клеток, на котором расположено N кораблей
# (каждый корабль занимает одну клетку).
# Вася решил воспользоваться линейной тактикой, для этого ему необходимо выстроить все N
#  кораблей в одном столбце. За один ход можно передвинуть один корабль в одну из четырёх соседних по стороне клеток.
# Номер столбца, в котором будут выстроены корабли, не важен. Определите минимальное количество ходов, необходимых
# для построения кораблей в одном столбце. В начале и процессе игры никакие два корабля не могут находиться в
# одной клетке.
#
# Формат ввода
# В первой строке входных данных задаётся число
# N (1≤N≤100).
# В каждой из следующих N строк задаются координаты корабля: сначала номер строки, затем номер столбца
# (нумерация начинается с единицы).
#
# Формат вывода
# Выведите одно число — минимальное количество ходов, необходимое для построения.
# Пример
# Ввод
# 3
# 1 2
# 3 3
# 1 1
# Вывод
# 3
# Примечания
# В примере необходимо выстроить корабли в столбце номер 2. Для этого необходимо переставить корабль из
# клетки 3 3 в клетку 3 2 за один ход, а корабль из клетки 1 1 в клетку 2 2 за два хода.
# Существуют и другие варианты перестановки кораблей, однако ни в одном из них нет меньше трёх ходов.

def calculate_sum_k(coord, N):
    sum_k = 0
    for i in range(N):
        sum_k += coord[i][1]
    return sum_k // N


def calculate_steps_ships(coord, N):
    steps = 0
    ships = 0
    for j in range(1, N + 1):
        for i in range(N):
            if coord[i][0] == j:
                ships += 1
        if ships <= 0:
            steps += abs(ships) + 1
        if ships > 0:
            steps += ships - 1
        ships -= 1
    return steps


def calculate_steps_column(coord, N, sum_k):
    steps_k1 = 0
    steps_k2 = 0
    for j in range(-N // 10, N // 10 + 1):
        if (sum_k + j) < 0 or (sum_k + j) > N:
            continue
        steps_k2 = 0
        for i in range(N):
            steps_k2 += abs(coord[i][1] - (sum_k + j))
        if steps_k1 == 0:
            steps_k1 = steps_k2
        steps_k1 = min(steps_k1, steps_k2)
    return steps_k1


def main():
    N = int(input())
    coord = []
    for i in range(N):
        x, y = map(int, input().split())
        coord.append([x, y])

    sum_k = calculate_sum_k(coord, N)
    steps_ships = calculate_steps_ships(coord, N)
    steps_column = calculate_steps_column(coord, N, sum_k)
    steps = steps_ships + steps_column
    print(steps)


if __name__ == "__main__":
    main()
# ok
