# E. Два из трех
# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Вам даны три списка чисел. Найдите все числа, которые встречаются хотя бы в двух из трёх списков.
#
# Формат ввода
# Во входных данных описывается три списка чисел. Первая строка каждого описания списка состоит из длины
# списка n (1 ≤ n ≤ 1000). Вторая строка описания содержит список натуральных чисел, записанных через пробел.
# Числа не превосходят 109.
#
# Формат вывода
# Выведите все числа, которые содержатся хотя бы в двух списках из трёх, в порядке возрастания. Обратите внимание,
# что каждое число необходимо выводить только один раз.
#
# Пример 1
# Ввод
# 2
# 3 1
# 2
# 1 3
# 2
# 1 2
# Вывод
# 1 3
# Пример 2
# Ввод
# 3
# 1 2 2
# 3
# 3 4 3
# 1
# 5
# Вывод
with open('./input.txt') as f:
    n1 = int(f.readline())
    nums_1 = {i for i in map(int, f.readline().split())}
    n2 = int(f.readline())
    nums_2 = {i for i in map(int, f.readline().split())}
    n3 = int(f.readline())
    nums_3 = {i for i in map(int, f.readline().split())}

count_dict = {}

for num in nums_1:
    if num in count_dict:
        count_dict[num] = count_dict[num] + 1
    else:
        count_dict[num] = 1

for num in nums_2:
    if num in count_dict:
        count_dict[num] = count_dict[num] + 1
    else:
        count_dict[num] = 1

for num in nums_3:
    if num in count_dict:
        count_dict[num] = count_dict[num] + 1
    else:
        count_dict[num] = 1

at_least_two = []

for key, value in count_dict.items():
    if value > 1:
        at_least_two.append(int(key))

at_least_two.sort()
at_least_two = list(map(str, at_least_two))

print(' '.join(at_least_two))
# python- ok, C++ - ok
