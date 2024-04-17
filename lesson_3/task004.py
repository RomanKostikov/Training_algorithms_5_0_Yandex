# D. Повторяющееся число
# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Вам дана последовательность измерений некоторой величины. Требуется определить, повторялась ли какое-либо число,
# причём расстояние между повторами не превосходило k.
#
# Формат ввода
# В первой строке задаются два числа n и k (1 ≤ n, k ≤ 105).
#
# Во второй строке задаются n чисел, по модулю не превосходящих 109.
#
# Формат вывода
# Выведите YES, если найдется повторяющееся число и расстояние между повторами не превосходит k и NO в противном случае.
#
# Пример 1
# Ввод
# 4 2
# 1 2 3 1
# Вывод
# NO
# Пример 2
# Ввод
# 4 1
# 1 0 1 1
# Вывод
# YES
# Пример 3
# Ввод
# 6 2
# 1 2 3 1 2 3
# Вывод
# NO
with open('./input.txt') as f:
    n, k = map(int, f.readline().split())
    numbers = list(f.readline().split())

answer = 'NO'
index_dict = {}

for ind, num in enumerate(numbers):
    if num in index_dict:
        index_dict[num].append(ind)
    else:
        index_dict[num] = [ind]

for key, value in index_dict.items():
    if len(value) > 1:
        for v in range(1, len(value)):
            if (value[v] - value[v - 1]) <= k:
                answer = 'YES'
                break

print(answer)
# python- ok, C++ - ok
