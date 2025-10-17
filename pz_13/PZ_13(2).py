#В двумерном списке найти сумму элементов второй половины матрицы.
import random


rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

matrix = [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]
print("\nСгенерированная матрица:")

for row in matrix:
    print(row)

half = len(matrix) // 2
second_half = matrix[half:]
total = sum(map(sum, second_half))
print(f"\nСумма элементов второй половины матрицы: {total}")