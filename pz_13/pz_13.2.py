# 2. В двумерном списке отрицательные элементы возвести в квадрат.

import random

rows = int(input('Введите количество строк: '))
cols = int(input('Введите количество столбцов: '))

matr = [[random.randint(-10, 10) for i in range(cols)] for i in range(rows)]
print('Исходная матрица:')
for row in matr:
    print(row)

matr = [[x ** 2 if x < 0 else x for x in row] for row in matr]

print('Итоговая матрица:')
for row in matr:
    print(row)