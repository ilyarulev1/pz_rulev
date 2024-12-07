# Постановка задачи. Дано множество А из N точек (точки заданы своими координатами
# х, у). Среди всех точек этого множества, лежащих в первой или третьей четверти, найти
# точку, наиболее #близкую к началу координат. Если таких точек нет, то вывести точку с
# нулевыми координатами. Расстояние R между точками с координатами (х1, У1) и (х2,
# У2) вычисляется по формуле: R= V(x2 -x1)=+ (y2- y1)? Для хранения данных о каждом
# наборе точек следует использовать по два списка: первый список для хранения абсцисс,
# второй — для хранения ординат.
import math


def find_closest_point(points):
    x_coords = []
    y_coords = []

    for point in points:
        x, y = point
        x_coords.append(x)
        y_coords.append(y)
    closest_point = None
    min_distance = float('inf')

    for i in range(len(points)):
        x = x_coords[i]
        y = y_coords[i]

        if (x > 0 and y > 0) or (x < 0 and y < 0):
            distance = math.sqrt(x ** 2 + y ** 2)
            if distance < min_distance:
                min_distance = distance
                closest_point = (x, y)

    if closest_point is None:
        return (0, 0)
    else:
        return closest_point


points = [(1, 2), (-1, -2), (3, 4), (-3, -4), (0, 1)]
closest = find_closest_point(points)
print("Ближайшая точка:", closest)
