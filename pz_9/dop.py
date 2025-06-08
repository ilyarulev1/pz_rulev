a = [1, 12, 32, 44, 36, 45, 78, 2, 3, 10]
c = []
for i in a:
    if i % 4 == 0 and i % 10 == 2:
        c.append(i)

s = len(c)
print(s)