# B. Продавец рыбы
# Ограничение времени 1 секунда Ограничение памяти 64Mb
#
# Ввод стандартный ввод или input.txt Вывод стандартный вывод или output.txt
#
# Вася решил заняться торговлей рыбой. С помощью методов машинного обучения он предсказал цены на рыбу на N дней вперёд.
# Он решил, что в один день он купит рыбу, а в один из следующих дней — продаст
# (то есть совершит или ровно одну покупку и продажу или вообще не совершит покупок и продаж, если это не принесёт ему
# прибыли). К сожалению, рыба — товар скоропортящийся и разница между номером дня продажи и номером дня покупки не
# должна превышать K.
#
# Определите, какую максимальную прибыль получит Вася.
#
# Формат ввода
#
# В первой строке входных данных задаются числа N и K (1 ≤ N ≤ 10000, 1 ≤ K ≤ 100).
#
# Во второй строке задаются цены на рыбу в каждый из N дней. Цена — целое число, которое может находится в
# пределах от 1 до 109.
#
# Формат вывода
#
# Выведите одно число — максимальную прибыль, которую получит Вася.
#
# Пример 1
# Ввод
# 5 2 1 2 3 4 5
# Вывод
# 2
#
# Пример 2
# Ввод
# 5 2 5 4 3 2 1
# Вывод
# 0

def calculate_best_profit(N, K, prices):
    best_profit = 0

    for i in range(N - 1):
        for j in range(1, min(K + 1, N - i)):
            difference = prices[i + j] - prices[i]
            if difference > best_profit:
                best_profit = difference

    return best_profit


def main():
    N, K = map(int, input().split())
    prices = [i for i in map(int, input().split())]
    result = calculate_best_profit(N, K, prices)
    print(result)


if __name__ == "__main__":
    main()
# ok