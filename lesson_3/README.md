# Занятие 3 (Множества и словари)

## Classwork

## Homework(до 27.03.24(10 задач))

### task001:

A. Плейлисты
Ограничение времени	1.5 секунд
Ограничение памяти	256Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Костя успешно прошел собеседование и попал на стажировку в отдел разработки сервиса «Музыка».
Конкретно ему поручили такое задание — научиться подбирать плейлист для группы друзей, родственников или коллег. 
При этом нужно подобрать такой плейлист, в который входят исключительно нравящиеся всем членам группы песни.
Костя очень хотел выполнить это задание быстро и качественно, но у него не получается. 
Помогите ему написать программу, которая составляет плейлист для группы людей.

Формат ввода
В первой строке расположено одно натуральное число n(1≤n≤2⋅10^5), где n – количество человек в группе.
В следующих 2⋅n строках идет описание любимых плейлистов членов группы. По 2 строки на каждого участника.
В первой из этих 2-х строк расположено число ki — количество любимых треков i-го члена группы. 
В следующей строке расположено ki строк через пробел — названия любимых треков i-го участника группы.
Каждый трек в плейлисте задан в виде строки, все строки уникальны, сумма длин строк не превосходит 2⋅106. 
Строки содержат большие и маленькие латинские буквы и цифры.

Формат вывода
Выведите количество, а затем сам список песен через пробел — список треков, которые нравятся каждому участнику группы. 
Ответ необходимо отсортировать в лексикографическом порядке!
Пример 1
Ввод	
1
2
GoGetIt Life
Вывод
2
GoGetIt Life 
Пример 2
Ввод	
2
2
Love Life
2
Life GoodDay
Вывод
1
Life 

### task002:

B. Анаграмма?
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Задано две строки, нужно проверить, является ли одна анаграммой другой. Анаграммой называется строка, полученная из 
другой перестановкой букв.

Формат ввода
Строки состоят из строчных латинских букв, их длина не превосходит 100000. Каждая записана в отдельной строке.

Формат вывода
Выведите "YES" если одна из строк является анаграммой другой и "NO" в противном случае.

Пример 1
Ввод	
dusty
study
Вывод
YES
Пример 2
Ввод	
rat
bat
Вывод
NO
### task003:

C. Удаление чисел
Ограничение времени	1 секунда
Ограничение памяти	256Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Дан массив a из n чисел. Найдите минимальное количество чисел, после удаления которых попарная разность 
оставшихся чисел по модулю не будет превышать 1, то есть после удаления ни одно число не должно отличаться от 
какого-либо другого более чем на 1.
Формат ввода
Первая строка содержит одно целое число n (1≤n≤2⋅10^5) — количество элементов массива a. Вторая строка содержит 
n целых чисел a1,a2,…,an (0≤ai≤10^5) — элементы массива a.

Формат вывода
Выведите одно число — ответ на задачу.
Пример 1
Ввод	
5
1 2 3 4 5
Вывод
3
Пример 2
Ввод	
10
1 1 2 3 5 5 2 2 1 5
Вывод
4

### task004:

D. Повторяющееся число
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Вам дана последовательность измерений некоторой величины. Требуется определить, повторялась ли какое-либо число, 
причём расстояние между повторами не превосходило k.

Формат ввода
В первой строке задаются два числа n и k (1 ≤ n, k ≤ 105).

Во второй строке задаются n чисел, по модулю не превосходящих 109.

Формат вывода
Выведите YES, если найдется повторяющееся число и расстояние между повторами не превосходит k и NO в противном случае.

Пример 1
Ввод	
4 2
1 2 3 1
Вывод
NO
Пример 2
Ввод	
4 1
1 0 1 1
Вывод
YES
Пример 3
Ввод	
6 2
1 2 3 1 2 3
Вывод
NO
### task005:

E. Два из трех
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Вам даны три списка чисел. Найдите все числа, которые встречаются хотя бы в двух из трёх списков.

Формат ввода
Во входных данных описывается три списка чисел. Первая строка каждого описания списка состоит из длины 
списка n (1 ≤ n ≤ 1000). Вторая строка описания содержит список натуральных чисел, записанных через пробел. 
Числа не превосходят 109.

Формат вывода
Выведите все числа, которые содержатся хотя бы в двух списках из трёх, в порядке возрастания. Обратите внимание, 
что каждое число необходимо выводить только один раз.

Пример 1
Ввод	
2
3 1
2
1 3
2
1 2
Вывод
1 3
Пример 2
Ввод	
3
1 2 2
3
3 4 3
1
5
Вывод
### task006:

F. Замена слов
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
С целью экономии чернил в картридже принтера было принято решение укоротить некоторые слова в тексте. 
Для этого был составлен словарь слов, до которых можно сокращать более длинные слова. Слово из текста можно 
сократить, если в словаре найдется слово, являющееся началом слова из текста. Например, если в списке есть 
слово "лом", то слова из текста "ломбард", "ломоносов" и другие слова, начинающиеся на "лом", можно сократить до "лом".

Если слово из текста можно сократить до нескольких слов из словаря, то следует сокращать его до самого короткого слова.

Формат ввода
В первой строке через пробел вводятся слова из словаря, слова состоят из маленьких латинских букв. Гарантируется, 
что словарь не пуст и количество слов в словаре не превышет 1000, а длина слов — 100 символов.

Во второй строке через пробел вводятся слова текста (они также состоят только из маленьких латинских букв). 
Количество слов в тексте не превосходит 105, а суммарное количество букв в них — 106.

Формат вывода
Выведите текст, в котором осуществлены замены.

Пример 1
Ввод	
a b
abdafb basrt casds dsasa a
Вывод
a b casds dsasa a
Пример 2
Ввод	
aa bc aaa
a aa aaa bcd abcd
Вывод
a aa aa bc abcd
### task007:

G. Построить квадрат
Ограничение времени	2 секунды
Ограничение памяти	256Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Задано множество, состоящее из N различных точек на плоскости. Координаты всех точек — целые числа. 
Определите, какое минимальное количество точек нужно добавить во множество, чтобы нашлось четыре точки, лежащие в 
вершинах квадрата.

Формат ввода
В первой строке вводится число N (1 ≤ N ≤ 2000) — количество точек.

В следующих N строках вводится по два числа xi, yi (-108 ≤ xi, yi ≤ 108) — координаты точек.

Формат вывода
В первой строке выведите число K — минимальное количество точек, которые нужно добавить во множество.

В следующих K строках выведите координаты добавленных точек xi, yi через пробел. Координаты должны быть целыми 
и не превышать 109 по модулю.

Если решений несколько — выведите любое из них.

Пример 1
Ввод	
2
0 1
1 0
Вывод
2
0 0
1 1
Пример 2
Ввод	
3
0 2
2 0
2 2
Вывод
1
0 0
Пример 3
Ввод	
4
-1 1
1 1
-1 -1
1 -1
Вывод
0  
### task008:

H. Спички детям не игрушка!
Ограничение времени	3 секунды
Ограничение памяти	256Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Вася любит решать головоломки со спичками. Чаще всего они формулируется следующим образом: дано изображение A, 
составленное из спичек; переложите в нем минимальное количество спичек так, чтобы получилось изображение B.

Например, из номера текущего командного чемпионата школьников Санкт-Петербурга по программированию, можно получить
ромб с диагональю, переложив всего три спички.


Головоломки, которые решает Вася, всегда имеют решение. Это значит, что набор спичек, используемый в изображении A, 
совпадает с набором спичек, используемым в изображении B. Кроме того, в одном изображении никогда не встречаются две 
спички, у которых есть общий участок ненулевой длины (то есть спички могут пересекаться, но не могут накладываться 
друг на друга).

Вася устал решать головоломки вручную, и теперь он просит вас написать, программу, которая будет решать 
головоломки за него. Программа будет получать описания изображений A и B и должна найти минимальное количество 
спичек, которые надо переложить в изображении A, чтобы полученная картинка получалась из B параллельным переносом.

Формат ввода
В первой строке входного файла содержится целое число n — количество спичек в каждом из изображений (1 ≤ n ≤ 1000).

В следующих n строках записаны координаты концов спичек на изображении A. Спичка номер i описывается 
целыми числами x1i, y1i, x2i, y2i — координатами ее концов. Следующие n строк содержат описание изображения 
B в таком же формате. Набор длин этих спичек совпадает с набором длин спичек с изображения A.

Все координаты по абсолютной величине не превосходят 104. Все спички имеют ненулевую длину, 
то есть x1i ≠ x2i или y1i ≠ y2i.

Формат вывода
Выведите в выходной файл минимальное количество спичек, которые следует переложить, чтобы изображение A 
совпало с изображением B, с точностью до параллельного переноса.

Пример 1
Ввод	
5
0 0 1 2
1 0 0 2
2 0 2 2
4 0 3 2
4 0 5 2
9 -1 10 1
10 1 9 3
8 1 10 1
8 1 9 -1
8 1 9 3
Вывод
3
Пример 2
Ввод	
1
3 4 7 9
-1 3 3 8
Вывод
0
Пример 3
Ввод	
1
-4 5 2 -3
-12 4 -2 4
Вывод
1
### task009:

I. Играйте в футбол!
Ограничение времени	2 секунды
Ограничение памяти	256Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Ася Вуткина — известный футбольный комментатор. Будучи профессионалом своего дела, Ася тщательно следит за 
всеми матчами всех европейских чемпионатов.

Благодаря накопленной информации, Ася может во время трансляции матча сообщить какую-нибудь интересную статистику, 
например: «Индзаги третий матч подряд забивает гол на 9-й минуте» или «Матерацци никогда не открывает счет в матче».

Но мозг Аси не безграничен, а помнить всю историю футбола просто невозможно. Поэтому Ася попросила вас написать 
программу, которая собирает статистику матчей и умеет отвечать на некоторые запросы, касающиеся истории футбола.

Информация о матче сообщается программе в следующей форме:

"<Название 1-й команды>" - "<Название 2-й команды>" <Счет 1-й команды>:<Счет 2-й команды>

<Автор 1-го забитого мяча 1-й команды> <Минута, на которой был забит мяч>'

<Автор 2-го забитого мяча 1-й команды> <Минута, на которой был забит мяч>'

...

<Автор последнего забитого мяча 1-й команды> <Минута, на которой был забит мяч>'

<Автор 1-го забитого мяча 2-й команды> <Минута, на которой был забит мяч>'

...

<Автор последнего забитого мяча 2-й команды> <Минута, на которой был забит мяч>'

Запросы к программе бывают следующих видов:

Total goals for <Название команды>

— количество голов, забитое данной командой за все матчи.

Mean goals per game for <Название команды>

— среднее количество голов, забиваемое данной командой за один матч. Гарантирутся, что к моменту подачи такого 
запроса команда уже сыграла хотя бы один матч.

Total goals by <Имя игрока>

— количество голов, забитое данным игроком за все матчи.

Mean goals per game by <Имя игрока>

— среднее количество голов, забиваемое данным игроком за один матч его команды.

Гарантирутся, что к моменту подачи такого запроса игрок уже забил хотя бы один гол.

Goals on minute <Минута> by <Имя игрока>

— количество голов, забитых данным игроком ровно на указанной минуте матча.

Goals on first <T> minutes by <Имя игрока>

— количество голов, забитых данным игроком на минутах с первой по T-ю включительно.

Goals on last <T> minutes by <Имя игрока>

— количество голов, забитых данным игроком на минутах с (91 - T)-й по 90-ю включительно.

Score opens by <Название команды>

— сколько раз данная команда открывала счет в матче.

Score opens by <Имя игрока>

— сколько раз данный игрок открывал счет в матче.

Формат ввода
Входной файл содержит информацию о матчах и запросы в том порядке, в котором они поступают в программу Аси Вуткиной.

Во входном файле содержится информация не более чем о 100 матчах, в каждом из которых забито не более 10 голов. 
Всего в чемпионате участвует не более 20 команд, в каждой команде не более 10 игроков забивают голы.

Все названия команд и имена игроков состоят только из прописных и строчных латинских букв и пробелов, а их длина не
превышает 30. Прописные и строчные буквы считаются различными. Имена и названия не начинаются и не оканчиваются 
пробелами и не содержат двух пробелов подряд. Каждое имя и название содержит хотя бы одну букву.

Минута, на которой забит гол — целое число от 1 до 90 (про голы, забитые в дополнительное время, принято говорить, 
что они забиты на 90-й минуте).

Для простоты будем считать, что голов в собственные ворота в европейских чемпионатах не забивают, и на одной 
минуте матча может быть забито не более одного гола (в том числе на 90-й). Во время чемпионата игроки не переходят 
из одного клуба в другой.

Количество запросов во входном файле не превышает 500.

Формат вывода
Для каждого запроса во входном файле выведите ответ на этот запрос в отдельной строке. Ответы на запросы, 
подразумевающие нецелочисленный ответ, должны быть верны с точностью до трех знаков после запятой.

Пример 1
Ввод	
"Juventus" - "Milan" 3:1
Inzaghi 45'
Del Piero 67'
Del Piero 90'
Shevchenko 34'
Total goals for "Juventus"
Total goals by Pagliuca
Mean goals per game by Inzaghi
"Juventus" - "Lazio" 0:0
Mean goals per game by Inzaghi
Mean goals per game by Shevchenko
Score opens by Inzaghi
Вывод
3
0
1.0
0.5
1.0
0
Пример 2
Ввод	
Total goals by Arshavin
Вывод
0
### task010:

J. P2P обновление
Ограничение времени	15 секунд
Ограничение памяти	256Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
В системе умного дома под управлением голосового помощника Лариса n устройств, соединяющихся между собой по 
сети LoRaWAN. Устройство номер 1 подключено к интернету и на него было скачано обновление, которое необходимо
передать на все устройства.

Сеть LoRaWAN очень медленная, поэтому для распространения протокола был придуман peer-to-peer (P2P) протокол. 
Файл обновления разбивается на k одинаковых по размеру частей, занумерованных от 1 до k.

Передача части обновления происходит во время таймслотов. Каждый таймслот занимает одну минуту. За один таймслот 
каждое устройство может получить и передать ровно одну часть обновления. То есть устройство во время таймслота 
может получать новую часть обновления и передавать уже имеющуюуся у него к началу таймслота часть обновления, 
или совершать только одно из этих действий, или вообще не осуществлять прием или передачу. После приема части 
обновления устройство может передавать эту часть обновления другим устройствам в следующих таймслотах.

Перед каждым таймслотом для каждой части обновления определяется, на скольких устройствах сети скачана эта часть. 
Каждое устройство выбирает отсутствующую на нем часть обновления, которая встречается в сети реже всего. 
Если таких частей несколько, то выбирается отсутствующая на устройстве часть обновления с наименьшим номером.

После этого устройство делает запрос выбранной части обновления у одного из устройств, на котором такая часть 
обновления уже скачана. Если таких устройств несколько — выбирается устройство, на котором скачано наименьшее 
количество частей обновления. Если и таких устройств оказалось несколько — выбирается устройство с минимальным номером.

После того, как все запросы отправлены, каждое устройство выбирает, чей запрос удовлетворить. Устройство A 
удовлетворяет тот запрос, который поступил от наиболее ценного для A устройства. Ценность устройства B для устройства 
A определяется как количество частей обновления, ранее полученных устройством A от устройства B. Если на устройство 
A пришло несколько запросов от одинаково ценных устройств, то удовлетворяется запрос того устройства, на котором 
меньше всего скачанных частей обновления. Если и таких запросов несколько, то среди них выбирается устройство с 
наименьшим номером.

Далее начинается новый таймслот. Устройства, чьи запросы удовлетворены, скачивают запрошенную часть обновления, 
а остальные не скачивают ничего.

Для каждого устройства определите, сколько таймслотов понадобится для скачивания всех частей обновления.

Формат ввода
Вводится два числа n и k (2 ≤ n ≤ 100, 1 ≤ k ≤ 200).

Формат вывода
Выведите n-1 число — количество таймслотов, необходимых для скачивания обновления на устройства с номерами от 2 до n.

Пример
Ввод	
3 2
Вывод
3 3
Примечания
Для удобства будем пользоваться обозначениями устройств буквами A, B, C (соответствует устройствам с 
номерами 1, 2 и 3). На устройстве A есть обе части обновления, а на устройствах B и C — ни одной.

Перед первым таймслотом для каждой части определяется количество устройств, на которых скачана каждая часть 
обновления: и 1 и 2 часть обновления присутствуют только на одном устройстве.

Устройства B и C выбирают самую редкую отсутствующую у них часть обновления с минимальным номером: самая редкая 
часть с минимальным номером — это часть 1. Она отсутствует и на устройстве B, и на устройстве С. Они запрашивают 
ее у устройства A. Ценность устройств B и C для устройства A равна нулю. Количество имеющихся у устройств B и C 
частей обновления одинакова и равно нулю. Поэтому устройство A выбирает устройство с минимальным номером (B). 
Во время первого таймслота выполняется передача части 1 с устройства A на устройство B. Ценность устройства A 
для устройства B становится равной 1.

Перед вторым таймслотом для каждой части определяется количество устройств, на которых скачана каждая часть 
обновления: самой редкой оказывается часть 2 (присутствует только на устройстве A), следующая по редкости часть 1 
(присутствует на устройствах A и B).

Устройства B и C выбирают среди отсутствующих у них частей обновления самую редкую: для обоих устройств выбирается 
часть 2. Каждое из них делает запрос части 2 у единственного обладателя этой части — устройства A. Ценность 
устройств B и C для устройства A одинакова и равна нулю. Количество имеющихся у устройства C частей (0) меньше, 
чем у устройства B (1), поэтому выбирается устройство C. Во время второго таймслота выполняется передача части 2 
с устройства A на устройство C. Ценность устройства A для устройства C становится равной 1.

Перед третьим таймслотом для каждой части определяется количество устройств, на которых скачана каждая часть 
обновления: обе части 1 и 2 присутствуют на двух устройствах (часть 1 на устройствах A и B, часть 2 — на 
устройствах A и C)

Устройство B может сделать запрос недостающей части 2 у обладающей ей устройств A и C, но выбирает устройство 
C, т.к. на устройстве C скачано меньше частей (1), чем у устройства A (2).

Устройство C может сделать запрос недостающей части 1 у обладающей ей устройств A и B, но выбирает устройство B, т.к. 
на устройстве B скачано меньше частей (1), чем у устройства A (2).

Во время третьего таймслота оба запроса оказываются единственными запросами у устройств B и C и удовлетворяются. 
Часть 2 передается с устройства C на устройство B. Часть 1 передается с устройства B на устройство C. Ценность 
устройства B для устройства C становится равной 1. Ценность устройства C для устройства B становится равной 1.

Все части обновления оказываются на всех устройствах и на этом обновление заканчивается.
