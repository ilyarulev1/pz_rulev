# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Положительные числа:
# Количество положительных чисел:
# Отрицательные числа:
# Количество отрицательных чисел:
import random

numbers = [random.randint(-20, 20) for _ in range(10)]

with open('numbers.txt', 'w', encoding='utf-8') as f:
    f.write(' '.join(map(str, numbers)))

with open('numbers.txt', 'r', encoding='utf-8') as f:
    numbers = list(map(int, f.read().split()))

positive = [num for num in numbers if num > 0]
negative = [num for num in numbers if num < 0]

with open('numbers_result.txt', 'w', encoding='utf-8') as f:
    f.write(f"Исходные данные: {' '.join(map(str, numbers))}\n")
    f.write(f"Количество элементов: {len(numbers)}\n")
    f.write(f"Положительные числа: {' '.join(map(str, positive))}\n")
    f.write(f"Количество положительных чисел: {len(positive)}\n")
    f.write(f"Отрицательные числа: {' '.join(map(str, negative))}\n")
    f.write(f"Количество отрицательных чисел: {len(negative)}\n")
