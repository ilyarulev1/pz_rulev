 # Дан список А размера N. Сформировать новый список В того же размера, элементы
#которого определяются следующим образом: Вк = 2* Ак, если Ак < 5, Ак/2 в противном
#случае.
A = [1, 4, 6, 8, 3]  # Пример списка A
B = []
for x in A:
    if x < 5:
        B.append(2 * x)
    else:
        B.append(x / 2)

 print("Исходный список A:", A)
 print("Новый список B:", B)