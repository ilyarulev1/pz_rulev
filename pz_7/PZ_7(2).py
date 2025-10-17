#Дана строка-предложение на рускком языке. Преобразовать строку так, чтобы каждое слово начиналось с заглавной буквы.
#Словом считать набор символов, не содержащий пробелов и ограниченный пробелами или началом/концом строки
#Слова, не начинающиеся с буквы, не изменять.

def possitive(box):

    words = box.split()
    possitivest = []

    for word in words:
        if word and word[0].isalpha():
            possitivest.append(word.capitalize())
        else:
            possitivest.append(word)
    return ' '.join(possitivest)
try:
    box = input("Введите предложение: ")
    if not box.strip():
        print("Ошибка: Ввод не должен быть пустым.")
    else:
        result = possitive(box)
        print("Результат:", result)
except ValueError:
    print(f"Произошла ошибка: ")