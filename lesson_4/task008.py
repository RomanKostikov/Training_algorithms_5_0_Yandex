# H. Выборы
# Ограничение времени	3 секунды
# Ограничение памяти	256Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# В одной демократической стране приближаются парламентские выборы. Выборы проходят по следующей схеме: каждый житель
# страны, достигший восемнадцатилетнего возраста, отдает свой голос за одну из политических партий. После этого партия,
# которая набрала максимальное количество голосов, считается победившей на выборах и формирует правительство.
# Если несколько партий набрали одинаковое максимальное количество голосов, то они должны сформировать
# коалиционное правительство, что обычно приводит к длительным переговорам.
#
# Один бизнесмен решил выгодно вложить свои средства и собрался поддержать на выборах некоторые партии.
# В результате поддержки он планирует добиться победы одной из этих партий, которая затем сформирует
# правительство, которое будет действовать в его интересах. При этом возможность формирования коалиционного
# правительства его не устраивает, поэтому он планирует добиться строгой победы одной из партий.
#
# Чтобы повлиять на исход выборов, бизнесмен собирается выделить деньги на агитационную работу среди жителей страны.
# Исследование рынка показало, что для того, чтобы один житель сменил свои политические воззрения, требуется потратить
# одну условную единицу. Кроме того, чтобы i-я партия в случае победы сформировала правительство, которое
# будет действовать в интересах бизнесмена, необходимо дать лидеру этой партии взятку в размере pi условных
# единиц. При этом некоторые партии оказались идеологически устойчивыми и не согласны на сотрудничество с
# бизнесменом ни за какие деньги.
#
# По результатам последних опросов известно, сколько граждан планируют проголосовать за каждую партию перед
# началом агитационной компании. Помогите бизнесмену выбрать, какую партию следует подкупить, и какое количество
# граждан придется убедить сменить свои политические воззрения, чтобы выбранная партия победила, учитывая, что
# бизнесмен хочет потратить на всю операцию минимальное количество денег.
#
# Формат ввода
# В первой строке вводится целое число n – количество партий (1 ≤ n ≤ 105). Следующие n строк описывают партии.
# Каждая из этих строк содержит по два целых числа: vi – количество жителей, которые собираются проголосовать за
# эту партию перед началом агитационной компании, и pi – взятка, которую необходимо дать лидеру партии для того,
# чтобы сформированное ей в случае победы правительство действовало в интересах бизнесмена
# (1 ≤ vi ≤ 106, 1 ≤ pi ≤ 106 или pi = -1). Если партия является идеологически устойчивой,
# то pi равно -1. Гарантируется, что хотя бы одно pi не равно -1.
#
# Формат вывода
# В первой строке выведите минимальную сумму, которую придется потратить бизнесмену.
# Во второй строке выведите номер партии, лидеру которой следует дать взятку.
# В третьей строке выведите n целых чисел – количество голосов, которые будут отданы за каждую из
# партий после осуществления операции. Если оптимальных решений несколько, выведите любое.
#
# Пример
# Ввод	Вывод
# 3
# 7 -1
# 2 8
# 1 2
# 6
# 3
# 3 2 5
class Party:
    def __init__(self):
        self.v = 0
        self.p = 0
        self.nomer = 0


def cmp(i1, i2):
    return i1.v < i2.v


def cmp2(i1, i2):
    return i1.nomer < i2.nomer


def search(v, N, vec):
    l = -1
    r = N

    while r - l > 1:
        mid = (l + r) // 2

        if vec[mid].v >= v:
            r = mid
        else:
            l = mid

    return r


N = int(input())
vec = [Party() for _ in range(N)]

for i in range(N):
    vec[i].nomer = i
    vec[i].v, vec[i].p = map(int, input().split())

vec.sort(key=lambda x: x.v)

max_p = max(item.p for item in vec)

suff = [0] * (N + 1)
suff[N] = 0

for i in range(N - 1, -1, -1):
    suff[i] = suff[i + 1] + vec[i].v

min_p = suff[0] + max_p + 1
best_party = -1

for i in range(N):
    if vec[i].p < 0 or vec[i].p >= min_p:
        continue

    l = vec[i].v
    r = suff[0] + max_p + 1
    res = -1

    while l <= r:
        mid = (l + r) // 2
        index = search(mid, N, vec)

        if index < N and mid == vec[i].v:
            index += 1

        diff_v_best_party = mid - vec[i].v
        diff_v_prefix = suff[index] - (N - index) * (mid - 1)

        if index == N or diff_v_best_party >= diff_v_prefix:
            r = mid - 1
            res = mid
        else:
            l = mid + 1

    p = res - vec[i].v + vec[i].p

    if p < min_p:
        best_party = i
        min_p = p

vote = min_p - vec[best_party].p
index = search(vec[best_party].v + vote, N, vec)
vec[best_party].v += vote

for i in range(index, N):
    if best_party == i:
        continue
    vv = vec[i].v - vec[best_party].v + 1
    vec[i].v = vec[best_party].v - 1
    vote -= vv

ind = N

while vote > 0:
    ind -= 1

    if ind == best_party:
        continue

    if vec[ind].v > vote:
        vec[ind].v -= vote
        vote = 0
    else:
        vote -= vec[ind].v
        vec[ind].v = 0

print(min_p)
print(vec[best_party].nomer + 1)

vec.sort(key=lambda x: x.nomer)
for item in vec:
    print(item.v, end=" ")
print()
# python TL, C++ ok
