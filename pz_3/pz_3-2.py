# в противном случае вычесть из него 2. Вывести полученное число.
a = input('Введите число') # Ввод данных
while type(a) != int: # обработка исключений
try:
a = int(a)
except ValueError:
print("Неправильно ввели!")
a = input('Введите число')
if a > 0:
a = a + 1
else:
a = a - 2
print(a)