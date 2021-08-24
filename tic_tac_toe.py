import random  # Импортируем функцию рандома

tic = ['-', '-', '-', '-', '-', '-', '-', '-', '-']


def print_tic():  # Функция печати поля tic-tac-toe
    print(f"  0 1 2\n0 {tic[0]} {tic[1]} {tic[2]}\n1 {tic[3]} {tic[4]} {tic[5]}\n2 {tic[6]} {tic[7]} {tic[8]}\n")


def game_x(xy):  # вносим координаты в список tic
    p = list(map(int, input(f"Куда поставить {xy}?:").split()))
    if 2 >= p[0] >= 0 and 2 >= p[1] >= 0:  # Проверка выхода за диапазаон координат
        if p[0] == 0:
            if tic[p[0] + p[1]] == '-':  # Проверка свободно ли поле
                return p[0] + p[1]  # возвращаем значения
            else:
                print("Поле занято")
                return game_x(xy)
        elif p[0] == 1:
            if tic[p[0] + p[1] + 2] == '-':  # если первая координа 1 прибавляем +2 к сумме координат
                return p[0] + p[1] + 2
            else:
                print("Поле занято")
                return game_x(xy)
        else:
            if tic[p[0] + p[1] + 4] == '-':  # если 2 приб. +4 к сумме координат, чтоб попасть в диапазон tic[6,7,8]
                return p[0] + p[1] + 4  # tic[p[0] + p[1] + 4] = xy
            else:
                print("Поле занято")
                return game_x(xy)
    else:
        print("Неверные значения, введите заново")
        return game_x(xy)


def check_win(x, tic):  # проверка наличия совпадений
    b = any(list((all(item == x for item in tic[:3]), all(item == x for item in tic[3:6]),
              all(item == x for item in tic[6:]), all(item == x for item in tic[::3]),
              all(item == x for item in tic[1::3]), all(item == x for item in tic[2::3]),
              all(item == x for item in tic[0::4]), all(item == x for item in tic[2:7:2]))))
    return b


def bot_tic(xy):  # Первый бот который ходит или в цент или по краям
    s = 0
    for i in range(0, len(tic)):  # Проходимся по списку от 0 до длины списка tic
        if tic[i] == 'x':  # Преверяем, что есть только один крестик
            s += 1
    if s == 1:  # Если есть только один крестик, выполняем условие
        if tic[4] == '-' and not tic[4] == 'x' and not tic[4] == 'o':  # Проверка свободно ли поле посередине
            return 4
        else:
            temp_list = [0, 2, 6, 8]  # Заводим временные координаты для выбора места установки нолика
            temp_r = random.choices(temp_list)  # Рандомно выбираем кординаты из списка
            print(temp_r)
            if tic[temp_r[0]] == '-':  # и если оно свободно
                return temp_r[0]  # присваиваем значение
            else:
                return bot_tic(xy)  # если рандомное поле занято пробуем еще раз
    else:
        return bot_tic_win(xy)


def bot_tic_win(xy):  # Бот проделжения игры
    tic1 = tic.copy()  # Создаем временную копию
    where_x = []  # Создаем список с месторасположение х
    verif_l = []  # Создаем проверочный лист
    verif_d = {}  # Создаем пустой словарь
    for i in range(0, len(tic)):  # Проходимся по списку от 0 до длины списка tic
        if tic[i] == '-':  # Преверяем, количество свободных мест
            verif_l.append(i)  # Добавлем координаты свободных ячеек
        if tic[i] == 'x':  # Преверяем, где находится X
            where_x.append(i)  # Добавлем координаты X
    for i in verif_l:
        tic1[i] = xy  # Во временный список добавляем xy в поле i
        if check_win(xy, tic1):  # Проверяем выгрышное ли оно
            verif_d[i] = 2  # Если да, добавляем в словарь ключ=координаты, значение=уровень выйгрыша(0,1,2)
            tic1 = tic.copy()  # Обнуляем список
        else:
            verif_d[i] = 0
            tic1 = tic.copy()  # Обнуляем список
        tic1[i] = 'x'  # Во временный список добавляем xy в поле i
        if check_win('x', tic1):  # Проверяем выгрышное ли оно
            verif_d[i] = 1  # Если да, изменяем в словаре ключ=координаты, значение=уровень выгрыша на 1
            tic1 = tic.copy()  # Обнуляем список
    if max(verif_d.values()) == 0 and len(where_x) == 2:  # Обход вилки
        if where_x[0] == 1 and where_x[1] == 3:
            return 0
        if where_x[0] == 1 and where_x[1] == 5:
            return 2
        if where_x[0] == 3 and where_x[1] == 7:
            return 6
        if where_x[0] == 5 and where_x[1] == 7:
            return 8
    return max(verif_d, key=verif_d.get)  # Находим key максимального значения values возврашаем ключь (координату)


def check_x():
    if any(item == '-' for item in tic):
        tic[game_x('x')] = 'x'
        if check_win('x', tic):
            print_tic()
            print("Выйграли x")
            return ""
        else:
            if not any(item == '-' for item in tic):
                print("Ничья")
                print_tic()
                return ""
        tic[bot_tic('o')] = 'o'  # пробуем вместо game_x('o')
        print_tic()  # печатаем поле
        if check_win('o', tic):
            print_tic()
            print("Выйграли o")
            return ''
        else:
            check_x()
    else:
        print("Ничья")
        print_tic()


print_tic()  # Печатаем первую пустую сетку
check_x()
