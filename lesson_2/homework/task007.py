# G. Ни больше ни меньше
# Ограничение времени 2 секунды Ограничение памяти 256Mb
#
# Ввод стандартный ввод или input.txt Вывод стандартный вывод или output.txt
#
# Дан массив целых положительных чисел a длины n. Разбейте его на минимально возможное количество отрезков,
# чтобы каждое число было не меньше длины отрезка которому оно принадлежит. Длиной отрезка считается количество чисел
# в нем.
#
# Разбиение массива на отрезки считается корректным, если каждый элемент принадлежит ровно одному отрезку.
#
# Формат ввода
#
# Первая строка содержит одно целое число t (1 ≤ t ≤ 1 000) — количество наборов тестовых данных. Затем следуют
# t наборов тестовых данных.
#
# Первая строка набора тестовых данных содержит одно целое число n (1 ≤ n ≤ 105) — длину массива.
#
# Следующая строка содержит n целых чисел a1, a2, …, an (1 ≤ ai ≤ n) — массив a.
#
# Гарантируется, что сумма n по всем наборам тестовых данных не превосходит 2 ⋅ 105.
#
# Формат вывода
#
# Для каждого набора тестовых данных в первой строке выведите число k — количество отрезков в вашем разбиении.
#
# Затем в следующей строке выведите k чисел len1, len2, …, lenk — длины отрезков в порядке слева направо.
#
# Пример
# Ввод
# 3
# 5
# 1 3 3 3 2
# 16
# 1 9 8 7 6 7 8 9 9 9 9 9 9 9 9 9
# 7
# 7 2 3 4 3 2 7
# Вывод
# 3
# 1 2 2
# 3
# 1 6 9
# 3
# 2 3 2
# Примечания
#
# Ответы в примере соответствуют разбиениям:
#
# {[1], [3, 3], [3, 2]}
#
# {[1], [9, 8, 7, 6, 7, 8], [9, 9, 9, 9, 9, 9, 9, 9, 9]}
#
# {[7, 2], [3, 4, 3], [2, 7]}
#
# В первом наборе тестовых данных набор длин {1, 3, 1}, соответствующий разбиению {[1], [3, 3, 3], [2]}, также был бы
# корректным.

def process_input():
    num_of_test_elems = []
    all_test_data = []

    tests = int(input())
    for test in range(tests):
        num_of_test_elems.append(int(input()))
        test_nums = [i for i in map(int, input().split())]
        all_test_data.append(test_nums)

    return num_of_test_elems, all_test_data, tests


def calculate_segments(num_of_test_elems, all_test_data, tests):
    all_segments = []
    for test in range(tests):
        segments = []
        max_seg_len = 0
        current_len = 0
        for elem in range(num_of_test_elems[test]):
            if current_len == 0:
                max_seg_len = all_test_data[test][elem]
                current_len = 1
            elif (current_len + 1) <= all_test_data[test][elem]:
                current_len += 1
                if all_test_data[test][elem] < max_seg_len:
                    max_seg_len = all_test_data[test][elem]
            elif (current_len + 1) > all_test_data[test][elem]:
                segments.append(current_len)
                max_seg_len = all_test_data[test][elem]
                current_len = 1
            if (max_seg_len == current_len) or (elem == (num_of_test_elems[test] - 1)):
                segments.append(current_len)
                max_seg_len = 0
                current_len = 0
        all_segments.append(segments)

    return all_segments


def output_results(all_segments, tests):
    for test in range(tests):
        print(len(all_segments[test]))
        print(' '.join(map(str, all_segments[test])))


def main():
    num_of_test_elems, all_test_data, tests = process_input()
    all_segments = calculate_segments(num_of_test_elems, all_test_data, tests)
    output_results(all_segments, tests)


if __name__ == "__main__":
    main()
# ok
