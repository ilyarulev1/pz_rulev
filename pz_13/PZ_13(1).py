# В двумерном списке найти суммы элементов каждой строки и поместить их в новый
# массив. Выполнить замену элементов третьего столбца исходной матрицы на
# полученные суммы.
import random

rows = int(input("Количество строк: "))
cols = int(input("Количество столбцов: "))

matrix = []
for i in range(rows):
    row = [random.randint(1, 5) for _ in range(cols)]
    matrix.append(row)

print("\nИсходная матрица:")
for row in matrix:
    print(row)

sums = [sum(row) for row in matrix]

for i in range(rows):
    if cols >= 3:
        matrix[i][2] = sums[i]

print("\nСуммы строк:", sums)
print("Матрица после замены 3-го столбца:")
for row in matrix:
    print(row)
