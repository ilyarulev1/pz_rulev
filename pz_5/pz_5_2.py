#Описать функцию TrianglePS(a, P, S), вычисляющую по стороне а
#равностороннего треугольника его периметр Р = 3*а и площадь S = a2 V3/4 (а —
#входной, Р и S — выходные параметры; все параметры являются вещественными).
#С помощью этой функции найти периметры и площади трех равносторонних
#треугольников с данными сторонами.
def TrianglePS(a):
 # Вычисляем периметр треугольника
 P = 3 * a

 # Вычисляем площадь треугольника
 S = (a ** 2) * (3 ** 0.5) / 4

 # Возвращаем периметр и площадь
 return P, S
# Стороны трех равносторонних треугольников
sides = [6.5, 5.1, 7.02]
# Вычисляем и выводим периметры и площади для каждого треугольника
for side in sides:
 P, S = TrianglePS(side)
 print(f"Для стороны a = {side}: Периметр P = {P:.2f}, Площадь S = {S:.2f}")