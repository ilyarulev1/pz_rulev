# Создайте класс "Фрукт", который содержит информацию о наименовании и весе фрукта.
# Создайте классы "Яблоко" и "Апельсин", которые наследуются от класса "Фрукт" и содержат информацию о цвете.
class fruit:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
class apple(fruit):
    def __init__(self, name, weight, color):
        super().__init__(name, weight)
        self.color = color
class orange(fruit):
    def __init__(self, name, weight, color):
        super().__init__(name, weight)
        self.color = color

if __name__ == "__main__":
    apple = apple("яблоко", 150, "красный")
    orange = orange("апельсин", 200, "оранжевый")

    print(f"{apple.name}: {apple.weight}г, цвет — {apple.color}")
    print(f"{orange.name}: {orange.weight}г, цвет — {orange.color}")