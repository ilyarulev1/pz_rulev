n = int(input('Введите количество элементов в последовательности A: '))
A = [random.randint(-100, 100) for _ in range(n)]

B = [x for x in A if x % 2 == 0]
C = [x for x in A if x % 2 != 0]

od_len = min(len(B), len(C))
sum_od = [B[i] + C[i] for i in range(od_len)]

print('Последовательность A:', A)
print('Четные элементы (B):', B)
print('Нечетные элементы (C):', C)
print('Сумма соответствующих элементов B и C:', sum_od)

if sum_od:
    min_element = min(sum_od)
    print('Минимальный элемент полученной последовательности:', min_element)
else:
    print('Суммировать не удалось — одна из последовательностей пустая.')