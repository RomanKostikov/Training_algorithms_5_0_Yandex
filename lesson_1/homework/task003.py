# Петя - начинающий программист. Сегодня он написал код из n строк.
# К сожалению оказалось, что этот код трудно читать. Петя решил исправить это, добавив в различные места пробелы.
# А точнее, для i-й строки ему нужно добавить ровно a i пробелов.
# Для добавления пробелов Петя выделяет строку и нажимает на одну из трёх клавиш: Space, Tab, и Backspace. При нажатии
# на Space в строку добавляется один пробел. При нажатии на Tab в строку добавляются четыре пробела. При нажатии на
# Backspace в строке удаляется один пробел.
# Ему хочется узнать, какое наименьшее количество клавиш придётся нажать, чтобы добавить необходимое количество пробелов
# в каждую строку. Помогите ему!
#
# Формат ввода
# Первая строка входных данных содержит одно целое положительное число n(1≤n≤10^5)– количество строк в файле.
# Каждая из следующих n строк содержит одно целое неотрицательное число ai(0≤ai≤10^9)– количество пробелов,
# которые нужно добавить в i -ю строку файла.
# Формат вывода
# Выведите одно число – минимальное количество нажатий, чтобы добавить в каждой строке необходимое количество пробелов.
# Пример
# Ввод
# 5
# 1
# 4
# 12
# 9
# 0
# Вывод
# 8

n = int(input())
a = (int(input()) for _ in range(n))
print(sum(k // 4 + min(k % 4, 2) for k in a))
# ок