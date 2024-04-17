# A. Быстрый поиск в массиве
# Ограничение времени 3 секунды Ограничение памяти 64Mb
#
# Ввод стандартный ввод или input.txt Вывод стандартный вывод или output.txt
#
# Дан массив из N целых чисел. Все числа от −109 до 109.
#
# Нужно уметь отвечать на запросы вида “Cколько чисел имеют значения отL доR?”.
#
# Формат ввода Число N (1≤N≤105). Далее N целых чисел.
#
# Затем число запросов K (1≤K≤105).
#
# Далее K пар чисел L,R (−109≤L≤R≤109) — собственно запросы.
#
# Формат вывода Выведите K чисел — ответы на запросы.
#
# Пример Ввод Вывод
#
# 5
#
# 10 1 10 3 4
#
# 4 1 10 2 9 3 4 2 2
#
# 5 2 2 0

with open('./input.txt') as f:
    N = int(f.readline())
    numbers = [i for i in map(int, f.readline().split())]
    K = int(f.readline())
    intervals = []
    for i in range(K):
        intervals.append([i for i in map(int, f.readline().split())])

numbers.sort()


# find first instance of left or a bit more
def left_ind_finder(left, numbers, N):
    left_ind = 0
    right_ind = N - 1

    if (left <= numbers[-1]):
        while (right_ind > left_ind):
            center_ind = (right_ind + left_ind) // 2
            if numbers[center_ind] >= left:
                right_ind = center_ind
            else:
                left_ind = center_ind + 1

        return left_ind

    else:
        return -1


def right_ind_finder(right, numbers, N):
    left_ind = 0
    right_ind = N - 1

    if (right >= numbers[0]):
        while (right_ind > left_ind):
            center_ind = (right_ind + left_ind + 1) // 2
            if numbers[center_ind] <= right:
                left_ind = center_ind
            else:
                right_ind = center_ind - 1

        return right_ind

    else:
        return -1


answers = []

for interval in intervals:
    left = min(interval)
    right = max(interval)

    start_index = left_ind_finder(left, numbers, N)
    finish_index = right_ind_finder(right, numbers, N)

    if (start_index == -1) or (finish_index == -1) or (finish_index < start_index):
        answers.append(0)
    else:
        answers.append(finish_index - start_index + 1)

print(*answers)
# ok
