# Создайте класс «Книга», который имеет атрибуты название, автор и количество страниц.
# Добавьте методы для чтения и записи книги.
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def read(self):
        print(f"Вы читаете книгу: '{self.title}' автора {self.author} ({self.pages} стр.).")

    def write(self):
        print(f"Книга {self.title} была написана автором {self.author}.")

if __name__ == "__main__":
    book = Book("Властелин колец", "Дж. Р. Р. Толкин", 771)
    book.write()
    book.read()