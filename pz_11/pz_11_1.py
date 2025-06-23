# 1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Среднее арифметическое элементов:
# Последовательность, в которой каждый последующий элемент равен квадрату суммы двух
# соседних элементов:
with open('numbers.txt', 'w', encoding="utf-8") as f:
    f.write("1 -2 2 3 0 4")

with open('numbers.txt', 'r') as f:
    numbers = list(map(int, f.read().split()))

count = len(numbers)
average = sum(numbers) / count

num = []
for i in range(count):
    if i == 0:
        new_num = (numbers[i+1])**2
    elif i == count-1:
        new_num = (numbers[i-1])**2
    else:
        new_num = (numbers[i-1] + numbers[i+1])**2
    num.append(new_num)

with open('result.txt', 'w',encoding="utf-8") as f:
    f.write(f"Исходные данные: {' '.join(map(str, numbers))}\n")
    f.write(f"Количество элементов: {count}\n")
    f.write(f"Среднее арифметическое элементов: {average}\n")
    f.write(f"Новая последовательность: {' '.join(map(str, num))}\n")
print("Файл result.txt создан")