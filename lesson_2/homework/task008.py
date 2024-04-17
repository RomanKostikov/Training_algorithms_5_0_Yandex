# H. Наилучший запрет
# Ограничение времени	3 секунды
# Ограничение памяти	256Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Константин и Михаил играют в настольную игру «Ярость Эльфов». В игре есть n рас и m классов персонажей.
# Каждый персонаж характеризуется своими расой и классом. Для каждой расы и каждого класса существует ровно один
# персонаж такой расы и такого класса. Сила персонажа i-й расы и j-го класса равна ai j, и обоим игрокам это
# прекрасно известно.
#
# Сейчас Константин будет выбирать себе персонажа. Перед этим Михаил может запретить одну расу и один класс,
# чтобы Константин не мог выбирать персонажей, у которых такая раса или такой класс. Конечно же, Михаил старается,
# чтобы Константину достался как можно более слабый персонаж, а Константин, напротив, выбирает персонажа посильнее.
# Какие расу и класс следует запретить Михаилу?
#
# Формат ввода
# Первая строка содержит два целых числа n и m (2 ≤ n,m ≤ 1000) через пробел — количество рас и классов в игре
# «Ярость Эльфов», соответственно.
# В следующих n строках содержится по m целых чисел через пробел. j-е число i-й из этих строк — это ai j (1 ≤ ai j ≤ 109).
# Формат вывода
# В единственной строке выведите два целых числа через пробел — номер расы и номер класса, которые следует запретить
# Михаилу. Расы и классы нумеруются с единицы. Если есть несколько возможных ответов, выведите любой из них.
#
# Пример 1
# Ввод
# 2 2
# 1 2
# 3 4
# Вывод
# 2 2
# Пример 2
# Ввод
# 3 4
# 1 3 5 7
# 9 11 2 4
# 6 8 10 12
# Вывод
# 3 2

class Spisok:
    def __init__(self, val, row, col):
        self.val = val
        self.row = row
        self.col = col


N, M = map(int, input().split())  # ширина символа

vec = []
for i in range(N):
    vec.append(list(map(int, input().split())))  # ширина символа

maximum = 0
imaximum = 0
jmaximum = 0

for i in range(N):
    for j in range(M):
        if vec[i][j] > maximum:
            maximum = vec[i][j]
            imaximum = i
            jmaximum = j

maxi = 0
imaxi = 0
jmaxi = 0

for i in range(N):  # нашли максимум если выбили столбец
    for j in range(M):
        if j != jmaximum:
            if vec[i][j] > maxi:
                maxi = vec[i][j]
                imaxi = i
                jmaxi = j

maxi2 = 0
imaxi2 = 0
jmaxi2 = 0

for i in range(N):  # нашли максимум если выбили строчку
    for j in range(M):
        if i != imaximum:
            if vec[i][j] > maxi2:
                maxi2 = vec[i][j]
                imaxi2 = i
                jmaxi2 = j

maxi = 0

for i in range(N):
    for j in range(M):
        if not (i == imaxi or j == jmaximum):
            if vec[i][j] > maxi:
                maxi = vec[i][j]

res = 2000000000
ires = 0
jres = 0

if res > maxi:
    res = maxi
    ires = imaxi
    jres = jmaximum

maxi = 0

for i in range(N):
    for j in range(M):
        if not (i == imaximum or j == jmaxi2):
            if vec[i][j] > maxi:
                maxi = vec[i][j]

if res > maxi:
    res = maxi
    ires = imaximum
    jres = jmaxi2

print(ires + 1, jres + 1)
# ok
