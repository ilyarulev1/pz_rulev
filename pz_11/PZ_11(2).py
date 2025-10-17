# Из предложенного текстового файла (text18-16.txt) вывести на экран его содержимое,
# количество букв в верхнем регистре. Сформировать новый файл, в который поместить текст
# в стихотворной форме предварительно заменив все знаки пунктуации на знак «!».
import string

try:
    with open('text18-16.txt', 'r', encoding='utf-16') as f:
        poem = f.read()

    print("Содержимое файла:")
    print(poem)

    uppercase_count = sum(1 for char in poem if char.isupper())
    print(f"\nКоличество букв в верхнем регистре: {uppercase_count}")

    punctuation = string.punctuation.replace('!', '')
    modified_poem = poem
    for p in punctuation:
        modified_poem = modified_poem.replace(p, '!')

    with open('poem_modified.txt', 'w', encoding='utf-8') as f:
        f.write(modified_poem)

    print("\nФайл 'poem_modified.txt' успешно создан с замененными знаками пунктуации.")

except FileNotFoundError:
    print("Ошибка: файл 'text18-16.txt' не найден в текущей директории.")
    print("Пожалуйста, убедитесь, что файл существует и имеет правильное имя.")
