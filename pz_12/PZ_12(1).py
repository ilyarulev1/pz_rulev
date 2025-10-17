#В последовательности на n целых чисел умножить все элементы на первый элемент


def multiply_elements_by_first(lst):
    if not lst:  # если список пустой
        return []

    first_element = lst[0]
    return [x * first_element for x in lst]


numbers = [2, 3, 4, 5]
result = multiply_elements_by_first(numbers)
print(result)