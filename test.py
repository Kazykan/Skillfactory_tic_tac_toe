import random

temp_list = [0, 2, 6, 8]  # Заводим временные координаты для выбора места установки нолика
temp_r = random.choices(temp_list)  # Рандомно выбираем кординаты из списка
print(int(list((temp_r))))