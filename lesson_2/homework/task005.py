# E. Амбициозная улитка
# Ограничение времени 5 секунд Ограничение памяти 256Mb
#
# Ввод стандартный ввод или input.txt Вывод стандартный вывод или output.txt
#
# Домашний питомец мальчика Васи — улитка Петя. Петя обитает на бесконечном в обе стороны вертикальном столбе,
# который для удобства можно представить как числовую прямую. Изначально Петя находится в точке 0.
#
# Вася кормит Петю ягодами. У него есть n ягод, каждая в единственном экземпляре. Вася знает, что если утром он даст
# Пете ягоду с номером i, то поев и набравшись сил, за остаток дня Петя поднимется на ai единиц вверх по столбу,
# но при этом за ночь, потяжелев, съедет на bi единиц вниз. Параметры различных ягод могут совпадать.
#
# Пете стало интересно, а как оно там, наверху, и Вася взялся ему в этом помочь. Ближайшие n дней он будет кормить
# Петю ягодами из своего запаса таким образом, чтобы максимальная высота, на которой побывал Петя за эти n дней была
# максимальной. К сожалению, Вася не умеет программировать, поэтому он попросил вас о помощи. Найдите, максимальную
# высоту, на которой Петя сможет побывать за эти n дней и в каком порядке Вася должен давать Пете ягоды, чтобы Петя
# смог её достичь!
#
# Формат ввода В первой строке входных данных дано число n (1≤n≤5⋅105) — количество ягод у Васи. В последующих n строках
# описываются параметры каждой ягоды. В i+1 строке дано два числа ai и bi (0≤ai,bi≤109) — то, насколько поднимется
# улитка за день после того, как съест i ягоду и насколько опуститься за ночь.
#
# Формат вывода В первой строке выходных данных выведите единственное число — максимальную высоту, которую сможет
# достичь Петя, если Вася будет его кормить оптимальным образом. В следующей строке выведите n различных целых
# чисел от 1 до n — порядок, в котором Вася должен кормить Петю (i число в строке соответствует номеру ягоды, которую
# Вася должен дать Пете в i день чтобы Петя смог достичь максимальной высоты).
#
# Пример 1
# Ввод
# 3
# 1 5
# 8 2
# 4 4
# Вывод
# 10
# 2 3 1
# Пример 2
# Ввод
# 2
# 7 6
# 7 4
# Вывод
# 10
# 2 1
#
# Примечания
# Во втором примере изначально улитка находится на высоте 0. Пусть сначала Петя накормит её второй ягодой, а затем
# первой. После того как она съест вторую ягоду, за день она поднимется на 7 (и окажется на высоте 7),
# а за ночь опустится на 4 (и окажется на высоте 3). После того как она съест первую ягоду, за день она поднимется на
# 7 (и окажется на высоте 10), а за ночь опустится на 6 (и окажется на высоте 4).
# Таким образом, максимальная высота, на которой побывает улитка при данном порядке кормления, равна 10.
# Нетрудно видеть, что если Петя накормит улитку сначала первой ягодой, а затем второй, то максимальная высота,
# на которой побывает улитка, будет меньше.
def process_input(content):
    ai_list = []
    bi_list = []
    diff_list = []
    positive_indices_list = []
    negative_indices_list = []

    biggest_climb_from_neg_list = -1
    biggest_climb_neg_ind = None

    max_ai_from_pos_dif = -1
    max_ai_from_pos_dif_ind = None

    n = int(content[0])

    for line in range(1, len(content)):
        ai, bi = map(int, content[line].split())
        difference = ai - bi
        ai_list.append(ai)
        bi_list.append(bi)
        diff_list.append(difference)
        if difference >= 0:
            if bi > max_ai_from_pos_dif:
                max_ai_from_pos_dif = bi
                max_ai_from_pos_dif_ind = line
            positive_indices_list.append(line)
        else:
            if ai > biggest_climb_from_neg_list:
                biggest_climb_from_neg_list = ai
                biggest_climb_neg_ind = line
            negative_indices_list.append(line)

    if biggest_climb_neg_ind is not None:
        negative_indices_list.remove(biggest_climb_neg_ind)

    if max_ai_from_pos_dif_ind is not None:
        positive_indices_list.remove(max_ai_from_pos_dif_ind)

    return ai_list, bi_list, diff_list, positive_indices_list, negative_indices_list, max_ai_from_pos_dif, max_ai_from_pos_dif_ind, biggest_climb_from_neg_list, biggest_climb_neg_ind


def calculate_sum_of_climb(positive_indices_list, diff_list, ai_list, max_ai_from_pos_dif_ind, biggest_climb_neg_ind):
    sum_of_climb = 0

    for i in positive_indices_list:
        sum_of_climb += diff_list[i - 1]

    sum_of_climb_1 = sum_of_climb
    if max_ai_from_pos_dif_ind is not None:
        sum_of_climb_1 += ai_list[max_ai_from_pos_dif_ind - 1]

    sum_of_climb_2 = sum_of_climb
    if max_ai_from_pos_dif_ind is not None:
        sum_of_climb_2 += diff_list[max_ai_from_pos_dif_ind - 1]
    if biggest_climb_neg_ind is not None:
        sum_of_climb_2 += ai_list[biggest_climb_neg_ind - 1]

    return max(sum_of_climb_1, sum_of_climb_2)


def main():
    with open('./input.txt') as f:
        content = f.readlines()

    ai_list, bi_list, diff_list, positive_indices_list, negative_indices_list, max_ai_from_pos_dif, max_ai_from_pos_dif_ind, biggest_climb_from_neg_list, biggest_climb_neg_ind = process_input(
        content)
    sum_of_climb = calculate_sum_of_climb(positive_indices_list, diff_list, ai_list, max_ai_from_pos_dif_ind,
                                          biggest_climb_neg_ind)

    string_of_indices = ' '.join(map(str, positive_indices_list))

    if max_ai_from_pos_dif_ind is not None:
        string_of_indices += ' ' + str(max_ai_from_pos_dif_ind)

    if biggest_climb_neg_ind is not None:
        string_of_indices += ' ' + str(biggest_climb_neg_ind)

    string_of_indices += ' ' + ' '.join(map(str, negative_indices_list))

    print(sum_of_climb)
    print(string_of_indices)


if __name__ == "__main__":
    main()
# ok
