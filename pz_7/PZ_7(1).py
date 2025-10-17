#Дана строка. Преобразовать в ней все прописные латинские буквы в строчные.

def convert_case(input_string):
    return input_string.lower()

try:
    user_input = input("Введите строку: ")
    if user_input == "":
        print("Ошибка: Ввод не должен быть пустым.")
    else:
        converted_string = convert_case(user_input)
        print("Преобразованная строка:", converted_string)
except ValueError:
    print("Ошибка: Неверный ввод.")