class Fruit:
    def __init__(self, name, weight):
        self.name = name  # Наименование фрукта
        self.weight = weight  # Вес фрукта (в граммах)

    def __str__(self):
        return f"{self.name} ({self.weight} г)"


class Apple(Fruit):
    def __init__(self, name, weight, color):
        super().__init__(name, weight)
        self.color = color  # Цвет яблока

    def __str__(self):
        return f"{super().__str__()}, цвет: {self.color}"


class Orange(Fruit):
    def __init__(self, name, weight, color):
        super().__init__(name, weight)
        self.color = color  # Цвет апельсина

    def __str__(self):
        return f"{super().__str__()}, цвет: {self.color}"


apple = Apple("Яблоко", 150, "красный")
orange = Orange("Апельсин", 200, "оранжевый")

print(apple)

print(orange)