#Составить генератор (yield), который переведет символы строки из верхнего регистра в нижний


def to_generator(input_string):
    yield from map(lambda char: char.lower(), input_string)


input_str = "HeLLo WoRLD"
result = ''.join(to_generator(input_str))
print(result)