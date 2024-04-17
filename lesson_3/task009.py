# I. Играйте в футбол!
# Ограничение времени	2 секунды
# Ограничение памяти	256Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Ася Вуткина — известный футбольный комментатор. Будучи профессионалом своего дела, Ася тщательно следит за
# всеми матчами всех европейских чемпионатов.
#
# Благодаря накопленной информации, Ася может во время трансляции матча сообщить какую-нибудь интересную статистику,
# например: «Индзаги третий матч подряд забивает гол на 9-й минуте» или «Матерацци никогда не открывает счет в матче».
#
# Но мозг Аси не безграничен, а помнить всю историю футбола просто невозможно. Поэтому Ася попросила вас написать
# программу, которая собирает статистику матчей и умеет отвечать на некоторые запросы, касающиеся истории футбола.
#
# Информация о матче сообщается программе в следующей форме:
#
# "<Название 1-й команды>" - "<Название 2-й команды>" <Счет 1-й команды>:<Счет 2-й команды>
#
# <Автор 1-го забитого мяча 1-й команды> <Минута, на которой был забит мяч>'
#
# <Автор 2-го забитого мяча 1-й команды> <Минута, на которой был забит мяч>'
#
# ...
#
# <Автор последнего забитого мяча 1-й команды> <Минута, на которой был забит мяч>'
#
# <Автор 1-го забитого мяча 2-й команды> <Минута, на которой был забит мяч>'
#
# ...
#
# <Автор последнего забитого мяча 2-й команды> <Минута, на которой был забит мяч>'
#
# Запросы к программе бывают следующих видов:
#
# Total goals for <Название команды>
#
# — количество голов, забитое данной командой за все матчи.
#
# Mean goals per game for <Название команды>
#
# — среднее количество голов, забиваемое данной командой за один матч. Гарантирутся, что к моменту подачи такого
# запроса команда уже сыграла хотя бы один матч.
#
# Total goals by <Имя игрока>
#
# — количество голов, забитое данным игроком за все матчи.
#
# Mean goals per game by <Имя игрока>
#
# — среднее количество голов, забиваемое данным игроком за один матч его команды.
#
# Гарантирутся, что к моменту подачи такого запроса игрок уже забил хотя бы один гол.
#
# Goals on minute <Минута> by <Имя игрока>
#
# — количество голов, забитых данным игроком ровно на указанной минуте матча.
#
# Goals on first <T> minutes by <Имя игрока>
#
# — количество голов, забитых данным игроком на минутах с первой по T-ю включительно.
#
# Goals on last <T> minutes by <Имя игрока>
#
# — количество голов, забитых данным игроком на минутах с (91 - T)-й по 90-ю включительно.
#
# Score opens by <Название команды>
#
# — сколько раз данная команда открывала счет в матче.
#
# Score opens by <Имя игрока>
#
# — сколько раз данный игрок открывал счет в матче.
#
# Формат ввода
# Входной файл содержит информацию о матчах и запросы в том порядке, в котором они поступают в программу Аси Вуткиной.
#
# Во входном файле содержится информация не более чем о 100 матчах, в каждом из которых забито не более 10 голов.
# Всего в чемпионате участвует не более 20 команд, в каждой команде не более 10 игроков забивают голы.
#
# Все названия команд и имена игроков состоят только из прописных и строчных латинских букв и пробелов, а их длина не
# превышает 30. Прописные и строчные буквы считаются различными. Имена и названия не начинаются и не оканчиваются
# пробелами и не содержат двух пробелов подряд. Каждое имя и название содержит хотя бы одну букву.
#
# Минута, на которой забит гол — целое число от 1 до 90 (про голы, забитые в дополнительное время, принято говорить,
# что они забиты на 90-й минуте).
#
# Для простоты будем считать, что голов в собственные ворота в европейских чемпионатах не забивают, и на одной
# минуте матча может быть забито не более одного гола (в том числе на 90-й). Во время чемпионата игроки не переходят
# из одного клуба в другой.
#
# Количество запросов во входном файле не превышает 500.
#
# Формат вывода
# Для каждого запроса во входном файле выведите ответ на этот запрос в отдельной строке. Ответы на запросы,
# подразумевающие нецелочисленный ответ, должны быть верны с точностью до трех знаков после запятой.
#
# Пример 1
# Ввод
# "Juventus" - "Milan" 3:1
# Inzaghi 45'
# Del Piero 67'
# Del Piero 90'
# Shevchenko 34'
# Total goals for "Juventus"
# Total goals by Pagliuca
# Mean goals per game by Inzaghi
# "Juventus" - "Lazio" 0:0
# Mean goals per game by Inzaghi
# Mean goals per game by Shevchenko
# Score opens by Inzaghi
# Вывод
# 3
# 0
# 1.0
# 0.5
# 1.0
# 0
# Пример 2
# Ввод
# Total goals by Arshavin
# Вывод
# 0
from collections import defaultdict


class Gamer:
    def __init__(self):
        self.name = ""
        self.total_goal = 0
        self.time = []
        self.firstly = 0


class Command:
    def __init__(self):
        self.name = ""
        self.total_goal = 0
        self.total_matches = 0
        self.firstly = 0


def split(s, delim):
    return s.split(delim)


def parce_match(line):
    tmp = split(line, '-')
    name1 = tmp[0][:-1]
    tmp1 = split(tmp[1], ' ')
    name2 = ' '.join(tmp1[1:-2])
    goal1, goal2 = map(int, tmp1[-1].split(':'))
    return name1, name2, goal1, goal2


def parce_goal(line):
    tmp = split(line, ' ')
    minute = tmp[-1].strip("'\n")
    if minute.isdigit():
        minute = int(minute)
    else:
        minute = 0  # or handle the case differently if needed
    name = '"' + ' '.join(tmp[:-2]) + '"'
    return name, minute


commands = defaultdict(Command)
gamers = defaultdict(Gamer)
gamer_from_command = {}

count = 0

with open("./input.txt") as in_file:
    for line in in_file:
        tmp = split(line, ' ')

        if tmp[0][0] == '"':
            name1, name2, goal1, goal2 = parce_match(line)
            commands[name1]
            commands[name2]

            for _ in range(goal1 + goal2):
                line = next(in_file)
                name, minute = parce_goal(line)
                gamers[name]

                if _ < goal1:
                    gamer_from_command[name] = name1
                else:
                    gamer_from_command[name] = name2

            goals = [(None, None)] * (goal1 + goal2)
            for i in range(goal1 + goal2):
                line = next(in_file)
                name, minute = parce_goal(line)
                goals[i] = (name, minute)

            first_comm = goal1 > 0
            first_name, min_time = goals[0]
            for i in range(1, goal1 + goal2):
                if min_time > goals[i][1]:
                    min_time = goals[i][1]
                    first_name = goals[i][0]
                    first_comm = i < goal1

            commands[name1].total_goal += goal1
            commands[name1].total_matches += 1
            if not first_comm:
                commands[name1].firstly += 1

            commands[name2].total_goal += goal2
            commands[name2].total_matches += 1
            if first_comm:
                commands[name2].firstly += 1

            for goal in goals:
                name, minute = goal
                gamers[name].total_goal += 1
                gamers[name].time.append(minute)

            gamers[first_name].firstly += 1

        if tmp[0] == "Total":
            if tmp[2] == "for":
                name_tmp = ' '.join(tmp[3:])
                print(commands[name_tmp].total_goal)

            if tmp[2] == "by":
                name_tmp = '"' + ' '.join(tmp[3:]) + '"'
                print(gamers[name_tmp].total_goal)

        if tmp[0] == "Mean":
            if tmp[4] == "for":
                name_tmp = ' '.join(tmp[5:])
                print(f"{(commands[name_tmp].total_goal / commands[name_tmp].total_matches):.3f}")

            if tmp[4] == "by":
                name_tmp = '"' + ' '.join(tmp[5:]) + '"'
                print(f"{(gamers[name_tmp].total_goal / commands[gamer_from_command[name_tmp]].total_matches):.3f}")

        if tmp[0] == "Goals":
            if tmp[2] == "minute":
                minute = int(tmp[3])
                name_tmp = '"' + ' '.join(tmp[5:]) + '"'
                print(gamers[name_tmp].time.count(minute))

            if tmp[2] == "first":
                minute = int(tmp[3])
                name_tmp = '"' + ' '.join(tmp[6:]) + '"'
                counter = sum(gamers[name_tmp].time.count(i) for i in range(minute + 1))
                print(counter)

            if tmp[2] == "last":
                minute = 91 - int(tmp[3])
                name_tmp = '"' + ' '.join(tmp[6:]) + '"'
                counter = sum(gamers[name_tmp].time.count(i) for i in range(minute, 91))
                print(counter)

        if tmp[0] == "Score":
            if tmp[3][0] == '"':
                name_tmp = ' '.join(tmp[3:])
                print(commands[name_tmp].firstly)
# python- WA, C++ - ok
