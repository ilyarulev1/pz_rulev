# Дан целочисленный список размера N, не содержащий одинаковых чисел. Проверить,
# образуют ли его элементы #прогрессию. Если образуют, то вывести разность
# прогрессии, сели нет — вывести 0

import random

def is_arithmetic_progression(lst):
    if len(lst) < 2:
        return 0
    lst.sort()
    difference = lst[1] - lst[0]

    for i in range(2, len(lst)):
        if lst[i] - lst[i - 1] != difference:
            return 0

    return difference


n = input('Введи число: ')
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print('Введите ЧИСЛО!')
        n = input('Введи число: ')
random_list = random.sample(range(1, 100), n)
print("Список:", random_list)
difference = is_arithmetic_progression(random_list)
print("Разность прогрессии:", difference)