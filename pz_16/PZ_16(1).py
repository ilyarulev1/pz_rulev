#Создайте класс «Книга», который имеет атрибуты название, автор и количество
#страниц. Добавьте методы для чтения и записи книги.
class Book:
    def __init__(self, title="", author="", pages=0):
        self.title = title  # Название книги
        self.author = author  # Автор книги
        self.pages = pages  # Количество страниц

    def read(self, page):
        """Метод для чтения книги (имитация)"""
        if page < 1 or page > self.pages:
            print(f"Страницы {page} не существует в этой книге.")
        else:
            print(f"Читаем страницу {page} из книги '{self.title}'")

    def write(self, new_content):
        """Метод для записи/изменения книги (имитация)"""
        print(f"В книгу '{self.title}' добавлен новый контент: {new_content}")

    def __str__(self):
        return f"Книга: {self.title} (Автор: {self.author}, Страниц: {self.pages})"


if __name__ == "__main__":

    book = Book("Война и мир", "Лев Толстой", 1225)

    print(book)

    book.read(100)
    book.read(1500)

    book.write("Новая глава")