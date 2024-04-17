# E. Прибыльный стартап
#
# k друзей организовали стартап по производству укулеле для кошек. На сегодняшний день прибыль составила n рублей. Вы,
# как главный бухгалтер компании, хотите в каждый из ближайших d дней приписывать по одной цифре в конец числа,
# выражающего прибыль. При этом в каждый из дней прибыль должна делиться на k.
#
# Формат ввода
# В единственной строке входных данных через пробел записаны три числа:n, k, d — изначальная прибыль, количество
# учредителей компании и количество дней, которое вы собираетесь следить за прибылью(1≤n, k≤10^9, 1≤d≤10^5).
# НЕ гарантируется, что n делится на k.
#
# Формат вывода
# Выведите одно целое число x — прибыль компании через d дней. Первые цифры числа x должны совпадать с числом n.
# Все префиксы числа x, которые длиннее числа n на 1, 2,…, d цифр, должны делиться на k. Если возможных ответов
# несколько, выведите любой из них. Если ответа не существует, выведите − 1.
# Пример 1
# Ввод
# 21 108 1
# Вывод
# 216
# Пример 2
# Ввод
# 5 12 4
# Вывод
# -1

def find_del(num, persons):
    for i in range(10):
        # подбор делимого числа
        if (num * 10 + i) % persons == 0:
            return str(num * 10 + i)

    return "-1"


def main():
    n, k, d = map(int, input().split())

    if n < 0 or k <= 0 or d <= 0:  # крайние случаи
        print(-1)
        return
    if n == 0:
        print(0)
        return

    summary = find_del(n, k)  # первый день

    # решение в строках, тк питону так легче
    if summary != "-1":
        summary += "0" * max(0, d - 1)  # прибыль

    print(summary)


if __name__ == '__main__':
    main()

# Вердикт Ok!