# Из исходного текстового файла (price.txt) выбрать все цены. Посчитать количество
# полученных элементов.
import re


def count_prices(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
        # Ищем все числа с десятичной точкой или без
        prices = re.findall(r'\b\d+\.?\d*\b', text)
        # Фильтруем, оставляя только валидные числа (исключаем случаи с точкой в конце)
        valid_prices = [price for price in prices if '.' not in price or re.match(r'^\d+\.\d+$', price)]

    return len(valid_prices)


filename = 'price.txt'
price_count = count_prices(filename)
print(f"Количество цен в файле: {price_count}")