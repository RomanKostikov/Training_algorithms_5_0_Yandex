# J. Форматирование документа
# Вася пишет новую версию своего офисного пакета "Closed Office". Недавно он начал работу над редактором "Dword",
# входящим в состав пакета.
# Последняя проблема, с которой столкнулся Вася — размещение рисунков в документе. Он никак не может добиться
# стабильного отображения рисунков в тех местах, в которые он их помещает. Окончательно отчаявшись написать
# соответствующий модуль самостоятельно, Вася решил обратиться за помощью к вам. Напишите программу, которая будет
# осуществлять размещение документа на странице.
# Документ в формате редактора "Dword" представляет собой последовательность абзацев. Каждый абзац представляет собой
# последовательность элементов – слов и рисунков. Элементы одного абзаца разделены пробелами и/или переводом строки.
# Абзацы разделены пустой строкой. Строка, состоящая только из пробелов, считается пустой.
# Слово — это последовательность символов, состоящая из букв латинского алфавита, цифр, и знаков препинания:
# ".", ",", ":", ";", "!", "?", "-", "'".
# Рисунок описывается следующим образом: "(image image parameters)". Каждый параметр рисунка имеет вид "имя=значение".
# Параметры рисунка разделены пробелами и/или переводом строки. У каждого рисунка обязательно есть следующие параметры:
# width — целое положительное число, ширина рисунка в пикселях height — целое положительное число, высота рисунка
# в пикселях layout — одно из следующих значений: embedded (в тексте), surrounded (обтекание текстом),
# floating (свободное), описывает расположение рисунка относительно текста
# Документ размещается на бесконечной вверх и вниз странице шириной w пикселей (разбиение на конечные по высоте
# страницы планируется в следующей версии редактора). Одна из точек на левой границе страницы условно считается точкой
# с ординатой равной нулю. Ордината увеличивается вниз.
# Размещение документа происходит следующим образом. Абзацы размещаются по очереди. Первый абзац размещается так,
# что его верхняя граница имеет ординату 0.
# Абзац размещается следующим образом. Элементы располагаются по строкам. Каждая строка исходно имеет высоту h пикселей.
# В процессе размещения рисунков высота строк может увеличиваться, и строки могут разбиваться рисунками на фрагменты.
# Слова размещаются следующим образом. Считается, что каждый символ имеет ширину c пикселей. Перед каждым словом,
# кроме первого во фрагменте, ставится пробел шириной также в c пикселей. Если слово помещается в текущем фрагменте,
# то оно размещается на нем. Если слово не помещается в текущем фрагменте, то оно размещается в первом фрагменте текущей
# строки, расположенном правее текущего, в котором оно помещается. Если такого фрагмента нет, то начинается новая строка,
# и поиск подходящего фрагмента продолжается в ней. Слово всегда "прижимается" к верхней границе строки.
# Размещение рисунка зависит от его расположения относительно текста.
# Если расположение рисунка относительно текста установлено в "embedded", то он располагается так же, как слово,
# за тем исключением, что его ширина равна ширине, указанной в параметрах рисунка. Кроме того, если высота рисунка
# больше текущей высоты строки, то она увеличивается до высоты рисунка (при этом верхняя граница строки не перемещается,
# а смещается вниз нижняя граница). Если рисунок типа "embedded" не первый элемент во фрагменте, то перед ним ставится
# пробел шириной c пикселей. Рисунки типа "embedded" также прижимаются к верхней границе строки.
# Если расположение рисунка относительно текста установлено в "surrounded", то рисунок размещается следующим образом.
# Сначала аналогично находится первый фрагмент, в котором рисунок помещается по ширине. При этом перед рисунком этого
# типа не ставится пробел, даже если это не первый элемент во фрагменте.
# После этого рисунок размещается следующим образом: верхний край рисунка совпадает с верхней границей строки, в которой
# находится найденный фрагмент, а сам рисунок продолжается вниз. При этом строки, через которые он проходит, разбиваются
# им на фрагменты.
# Если расположение рисунка относительно текста установлено в "floating", то рисунок размещается поверх текста и других
# рисунков и никак с ними не взаимодействует. В этом случае у рисунка есть два дополнительных параметра: "dx" и "dy" —
# целые числа, задающие смещение в пикселях верхнего левого угла рисунка вправо и вниз, соответственно, относительно
# позиции, где находится верхний правый угол предыдущего слова или рисунка (или самой левой верхней точки первой строки
# абзаца, если рисунок — первый элемент абзаца).
# Если при размещении рисунка таким образом он выходит за левую границу страницы, то он смещается вправо, так, чтобы его
# левый край совпадал с левой границей страницы. Аналогично, если рисунок выходит за правую границу страницы, то он
# смещается влево, чтобы его правый край совпадал с правой границей страницы.
# Верхняя граница следующего абзаца совпадает с более низкой точкой из нижней границы последней строки и самой нижней
# границы рисунков типа "surrounded" предыдущего абзаца.
# По заданным w, h, c и документу найдите координаты верхних левых углов всех рисунков в документе.
# Формат ввода
# Первая строка входного файла содержит три целых числа: w, h и c (1 ≤ w ≤ 1000, 1 ≤ h ≤ 50, 1 ≤ c ≤ w).
# Далее следует документ. Размер входного файла не превышает 1000 байт. Гарантируется, что ширина любого слова и любого
# рисунка не превышает w. Высота всех рисунков не превышает 1000. Относительное смещение всех рисунков типа «floating»
# не превышает 1000 по абсолютной величине.
# Формат вывода
# Выведите в выходной файл по два числа для каждого рисунка — координаты его верхнего левого угла. Выводите координаты
# рисунков в том порядке, в котором они встречаются во входном файле.

# Пример 1
# Ввод
# 120 10 8
# start (image layout=embedded width=12 height=5)
# (image layout=surrounded width=25 height=58)
# and word is
# (image layout=floating dx=18 dy=-15 width=25 height=20)
# here new
# (image layout=embedded width=20 height=22)
# another
# (image layout=embedded width=40 height=19)
# longword
#
# new paragraph
# (image layout=surrounded width=5 height=30)
# (image layout=floating width=20 height=35 dx=50 dy=-16)
# Вывод
# 48 0
# 60 0
# 74 -5
# 32 20
# 0 52
# 104 81
# 100 65
# Пример 2
# Ввод
# 1000 2 3
# Вывод
# Пример 3
# Ввод
# 100 2 3
# (image dx=10 dy=11 height=100 width=20 layout=floating)
# Вывод
# 10 11

# (1 ≤ w ≤ 1000, 1 ≤ h ≤ 50, 1 ≤ c ≤ w)
# w, h, c = map(int, input().split())

# w, h, c = 120, 10, 8

# text = '''start (image layout=embedded width=12 height=5)
# (image layout=surrounded width=25 height=58)
# and word is
# (image layout=floating dx=18 dy=-15 width=25 height=20)
# here new
# (image layout=embedded width=20 height=22)
# another
# (image layout=embedded width=40 height=19)
# longword

# new paragraph
# (image layout=surrounded width=5 height=30)
# (image layout=floating width=20 height=35 dx=50 dy=-16)'''

# lines = text.split('\n')
# print(lines)
# print()

lines = []
with open('./input.txt') as f:
    # with open('yandex algo tests/11.txt') as f:
    # with open('yandex algo tests/10') as f:
    # with open('yandex algo tests/input_J1_primer.txt') as f:
    # with open('yandex algo tests/input_J1_primer_2.txt') as f:
    # with open('yandex algo tests/input_J1_primer_3.txt') as f:
    w, h, c = map(int, f.readline().split())
    content = f.readlines()

for i in range(len(content)):
    line_trimmed = content[i].split('\n')
    lines.append(line_trimmed[0])

last_up_right_dot = [0, 0]
this_line_y_start = 0
current_line = 0
current_line_height = h
line_heights_list = []
blocked_x_pixels_in_lines = [0 for line in lines]  # in start, end segments
output_list = []
currently_examining_picture = False
layout, width, height, dx, dy = None, 0, 0, 0, 0
new_fragment_start_list = []
blocked_pixels = []  # elements [top, bottom, left, right]
last_element_up_right_coordinates = [0, 0]
layout, width, height, dx, dy = '', 0, 0, 0, 0


###########SEEMS OK
def calculate_line_y_start(line, line_heights_list):
    y_sum = 0
    for i in range(line):
        y_sum += line_heights_list[i]
    return y_sum


########THIS SEEMS OK
def calculate_blocked_x_pixels_for_line(line_y_start, blocked_pixels, current_line_height):
    blocked_x_pixels_set = set()
    x_ends_of_blocking_elements = []
    for element in blocked_pixels:
        if (element[0] < (line_y_start + current_line_height)) and (element[1] > line_y_start):
            blocked_x_pixels_set_el = [i for i in range(element[2], element[3])]
            blocked_x_pixels_set_el = set(blocked_x_pixels_set_el)
            blocked_x_pixels_set = blocked_x_pixels_set.union(blocked_x_pixels_set_el)
            x_ends_of_blocking_elements.append(element[3])
    x_ends_of_blocking_elements.sort()
    return blocked_x_pixels_set, x_ends_of_blocking_elements


########THIS SEEMS OK
def word_length_func(start_pos, word_len, c, new_fragment_start_list):
    word_length = c * word_len
    if start_pos[0] == 0:
        pass  # all is good
    elif start_pos[0] in new_fragment_start_list:
        pass  # all is good
    else:
        word_length = c * (word_len + 1)
    #     print(f'Word length of word is {word_length} for position {start_pos}')
    return word_length


# REMEMBER TO CHECK FOR ALL FRAGMENTS ON THE LINE!!!!
def check_fragment_placement(line, start_pos, word_length, w, blocked_x_pixels_set):
    if start_pos[0] + word_length > w:
        return False
    elif intersects_w_other_elements(line, start_pos, word_length, blocked_x_pixels_set):
        return False
    else:
        return True


###########SEEMS OK
def intersects_w_other_elements(line, start_pos, word_length, blocked_x_pixels_set):
    word_occupies_pixels = set(range(start_pos[0], start_pos[0] + word_length))

    #     print(f"""
    #     given word length {word_length}
    #     given starting position {start_pos}
    #     word_occupies_pixels {word_occupies_pixels}
    #     blocked_x_pixels_set {blocked_x_pixels_set}
    #     """)

    intersection = False
    if word_occupies_pixels.intersection(blocked_x_pixels_set):
        intersection = True
    return intersection


###########SEEMS OK
def Place_Word(word, start_pos, c, h, line, blocked_pixels, current_line_height, line_heights_list):
    while True:

        word_len = len(word)
        blocked_x_pixels_set, x_ends_of_blocking_elements = \
            calculate_blocked_x_pixels_for_line(start_pos[1], blocked_pixels, current_line_height)
        #         print(f'x_ends_of_blocking_elements {x_ends_of_blocking_elements}')
        #         print(f'blocked_x_pixels_set {blocked_x_pixels_set}')

        word_len = word_length_func(start_pos, word_len, c, x_ends_of_blocking_elements)
        #         print('word_len inside function ', word_len)
        word_fits = check_fragment_placement(line, start_pos, word_len, w, blocked_x_pixels_set)

        if word_fits:
            next_starting_position = [start_pos[0] + word_len, start_pos[1]]
            last_element_up_right_coordinates = next_starting_position.copy()
            break

        # go to next line
        if start_pos[0] + word_len > w:
            line_heights_list.append(current_line_height)
            current_line_height = h
            line += 1
            #             print(' line ', line, 'line heights', line_heights_list)
            this_line_y_start = calculate_line_y_start(line, line_heights_list)
            start_pos = [0, this_line_y_start]
        # go to next fragment on this line
        else:
            for elem in x_ends_of_blocking_elements:
                if elem > start_pos[0]:
                    start_pos[0] = elem
                    break

    #     print (f'Function Place_word is placing end of "{word}" at {next_starting_position}')
    return line, current_line_height, next_starting_position, last_element_up_right_coordinates


# NOT DOING ANY CHECKS WITH THIS FUNCTION!!!
def Place_Picture(output_list, c, w, layout, width, height, dx, dy, start_pos, \
                  current_line, current_line_height, new_fragment_start_list, \
                  blocked_pixels, last_element_up_right_coordinates, line_heights_list):
    #     print(f'''Trying to place picture with
    #     layout {layout}
    #     width {width}
    #     height {height}
    #     dx {dx}
    #     dy {dy}
    #     start_pos {start_pos}
    #     ''')

    if layout == 'embedded':  # DON'T FORGET THE CASE WHERE YOU ADD A SPACE BEFORE

        while True:
            blocked_x_pixels_set, x_ends_of_blocking_elements = \
                calculate_blocked_x_pixels_for_line(start_pos[1], blocked_pixels, current_line_height)

            word_len = width
            if start_pos[0] == 0:
                pass  # all is good
            elif start_pos[0] in x_ends_of_blocking_elements:
                #                 print('[current_line, start_pos]', [current_line, start_pos])
                #                 print('x_ends_of_blocking_elements', x_ends_of_blocking_elements)
                pass  # all is good
            else:
                word_len += c
            #                 print('embedded picture word_len ', word_len )

            word_fits = check_fragment_placement(current_line, start_pos, word_len, w, blocked_x_pixels_set)

            if word_fits:
                next_starting_position = [start_pos[0] + word_len, start_pos[1]]
                last_element_up_right_coordinates = next_starting_position.copy()
                #                 print('PLACING EMBEDDED PICTURE AT ', [next_starting_position[0]-width, next_starting_position[1]])
                break

            # go to next line
            if start_pos[0] + word_len > w:
                line_heights_list.append(current_line_height)
                current_line_height = h
                current_line += 1
                #                 print(' line ', line, 'line heights', line_heights_list)
                this_line_y_start = calculate_line_y_start(current_line, line_heights_list)
                start_pos = [0, this_line_y_start]
            # go to next fragment on this line
            else:
                for elem in x_ends_of_blocking_elements:
                    if elem > start_pos[0]:
                        start_pos[0] = elem
                        break

        if height > current_line_height:
            current_line_height = height

        output_list.append([next_starting_position[0] - width, next_starting_position[1]])

        return current_line, current_line_height, next_starting_position, last_element_up_right_coordinates

    elif layout == 'surrounded':
        while True:
            blocked_x_pixels_set, x_ends_of_blocking_elements = \
                calculate_blocked_x_pixels_for_line(start_pos[1], blocked_pixels, current_line_height)

            top = start_pos[1]
            bottom = start_pos[1] + height
            left = start_pos[0]
            right = start_pos[0] + width

            word_len = width
            word_fits = check_fragment_placement(current_line, start_pos, word_len, w, blocked_x_pixels_set)

            if word_fits:
                next_starting_position = [start_pos[0] + word_len, start_pos[1]]
                last_element_up_right_coordinates = next_starting_position.copy()
                break

            # go to next line
            if start_pos[0] + word_len > w:
                line_heights_list.append(current_line_height)
                current_line_height = h
                current_line += 1
                #                 print(' line ', line, 'line heights', line_heights_list)
                this_line_y_start = calculate_line_y_start(current_line, line_heights_list)
                start_pos = [0, this_line_y_start]
            # go to next fragment on this line
            else:
                for elem in x_ends_of_blocking_elements:
                    if elem > start_pos[0]:
                        start_pos[0] = elem
                        break

        blocked_pixels.append([top, bottom, left, right])  # I probably dont have to explicitly pass it back?
        # since list is passed in by reference?
        #         print ('blocked_pixels: ', blocked_pixels)

        output_list.append([next_starting_position[0] - width, next_starting_position[1]])

        return current_line, current_line_height, next_starting_position, last_element_up_right_coordinates


    elif layout == 'floating':
        start_x = last_element_up_right_coordinates[0]
        start_y = last_element_up_right_coordinates[1]

        start_x += dx
        start_y += dy
        end_x = start_x + width
        end_y = start_y + height

        if start_x < 0:
            shift_x = -start_x
            start_x = 0
            end_x += shift_x
        elif end_x > w:
            shift_x = end_x - w
            end_x = w
            start_x -= shift_x

        next_starting_position = start_pos
        last_element_up_right_coordinates = [end_x, start_y]

        output_list.append([start_x, start_y])

        return current_line, current_line_height, next_starting_position, last_element_up_right_coordinates


for line in range(len(lines)):
    words = lines[line].split()
    this_line_height = h

    if (lines[line] == ''):  ###########################################################
        #         print('--------THIS IS A DIVIDOR FOR NEW PARAGRAPH---------')
        #         print(f'''current_line {current_line}
        #         current_line_height {current_line_height}
        #         line_heights_list {line_heights_list}
        #         last_up_right_dot {last_up_right_dot}''')
        line_heights_list.append(current_line_height)
        current_line_height = h
        current_line += 1
        this_line_y_start = calculate_line_y_start(current_line, line_heights_list)
        last_up_right_dot = [0, this_line_y_start]
        last_element_up_right_coordinates = [0, this_line_y_start]
    #         print(f'''current_line {current_line}
    #         current_line_height {current_line_height}
    #         line_heights_list {line_heights_list}
    #         last_up_right_dot {last_up_right_dot}''')

    for word in words:
        #         word or picture?
        if ('(' in word):
            currently_examining_picture = True

        if (currently_examining_picture == True):
            if ('layout=' in word):
                layout = word[7:]
                if (')' in word):
                    layout = layout.strip(')')
                    currently_examining_picture = False
                    current_line, current_line_height, last_up_right_dot, last_element_up_right_coordinates = \
                        Place_Picture(output_list, c, w, layout, width, height, dx, dy, last_up_right_dot, \
                                      current_line, current_line_height, new_fragment_start_list, \
                                      blocked_pixels, last_element_up_right_coordinates, line_heights_list)
                    layout, width, height, dx, dy = '', 0, 0, 0, 0
            elif ('width=' in word):
                width = word[6:]
                if (')' in word):
                    width = width.strip(')')
                    width = int(width)
                    currently_examining_picture = False
                    current_line, current_line_height, last_up_right_dot, last_element_up_right_coordinates = \
                        Place_Picture(output_list, c, w, layout, width, height, dx, dy, last_up_right_dot, \
                                      current_line, current_line_height, new_fragment_start_list, \
                                      blocked_pixels, last_element_up_right_coordinates, line_heights_list)
                    layout, width, height, dx, dy = '', 0, 0, 0, 0
                width = int(width)
            elif ('height=' in word):
                height = word[7:]
                if (')' in word):
                    height = height.strip(')')
                    height = int(height)
                    currently_examining_picture = False
                    current_line, current_line_height, last_up_right_dot, last_element_up_right_coordinates = \
                        Place_Picture(output_list, c, w, layout, width, height, dx, dy, last_up_right_dot, \
                                      current_line, current_line_height, new_fragment_start_list, \
                                      blocked_pixels, last_element_up_right_coordinates, line_heights_list)
                    layout, width, height, dx, dy = '', 0, 0, 0, 0
                height = int(height)
            elif ('dx=' in word):
                dx = word[3:]
                if (')' in word):
                    dx = dx.strip(')')
                    dx = int(dx)
                    currently_examining_picture = False
                    current_line, current_line_height, last_up_right_dot, last_element_up_right_coordinates = \
                        Place_Picture(output_list, c, w, layout, width, height, dx, dy, last_up_right_dot, \
                                      current_line, current_line_height, new_fragment_start_list, \
                                      blocked_pixels, last_element_up_right_coordinates, line_heights_list)
                    layout, width, height, dx, dy = '', 0, 0, 0, 0
                dx = int(dx)
            elif ('dy=' in word):
                dy = word[3:]
                if (')' in word):
                    dy = dy.strip(')')
                    dy = int(dy)
                    currently_examining_picture = False
                    current_line, current_line_height, last_up_right_dot, last_element_up_right_coordinates = \
                        Place_Picture(output_list, c, w, layout, width, height, dx, dy, last_up_right_dot, \
                                      current_line, current_line_height, new_fragment_start_list, \
                                      blocked_pixels, last_element_up_right_coordinates, line_heights_list)
                    layout, width, height, dx, dy = '', 0, 0, 0, 0
                dy = int(dy)

        else:
            current_line, current_line_height, last_up_right_dot, last_element_up_right_coordinates = \
                Place_Word(word, last_up_right_dot, c, h, current_line, blocked_pixels, current_line_height,
                           line_heights_list)

for item in output_list:
    print(' '.join(str(x) for x in item))
# TL