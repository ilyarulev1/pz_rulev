# Постановка задачи. Дано множество А из N точек (точки заданы своими координатами
# х, у). Среди всех точек этого множества, лежащих в первой или третьей четверти, найти
# точку, наиболее #близкую к началу координат. Если таких точек нет, то вывести точку с
# нулевыми координатами. Расстояние R между точками с координатами (х1, У1) и (х2,
# У2) вычисляется по формуле: R= V(x2 -x1)=+ (y2- y1)? Для хранения данных о каждом
# наборе точек следует использовать по два списка: первый список для хранения абсцисс,
# второй — для хранения ординат.
import math

def find_closest_point(x_coords, y_coords):
    closest_point = None
    min_distance = float('inf')

    for i in range(len(x_coords)):# Цикл по индексам точек
        x = x_coords[i]
        y = y_coords[i]

        if (x > 0 and y > 0) or (x < 0 and y < 0): # Проверяем, находится ли точка в первой или третьей четверти
            distance = math.sqrt(x ** 2 + y ** 2)
            if distance < min_distance:
                min_distance = distance
                closest_point = (x, y)

    if closest_point is None:
        return (0, 0)
    else:
        return closest_point

# Ввод количества точек
N = input("Введите размер списка N: ")
while True:
    try:
        N = int(N)
        if N <= 0:
            print("Ошибка: введите положительное число.")
            N = input("Введите размер списка N: ")
            continue
        break
    except ValueError:
        print('Введите ЧИСЛО!')
        N = input('Введи число: ')

# Создаем списки для координат (абсцисс и ординат)
x_coords = []
y_coords = []
print("Введите", N, "точек (каждую координату по отдельности):")
for i in range(N):
    while True:
        try:
            x = float(input(f"Введите абсциссу для точки {i + 1}: "))
            y = float(input(f"Введите ординату для точки {i + 1}: "))
            x_coords.append(x)
            y_coords.append(y)
            break  # Выходим из цикла, если ввод успешен
        except ValueError:
            print("Ошибка: введите числовые координаты.")

# Нахождение ближайшей точки
closest = find_closest_point(x_coords, y_coords)
print("Ближайшая точка:", closest)