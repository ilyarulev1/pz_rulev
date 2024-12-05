#С помощью функций получить вертикальную и горизонтальную линии. Линия
#проводится многократной печатью символа. Заключить слово в рамку из
#полученных линий.
def g_line(lenght, simbol='-'):
 return simbol * lenght
def w_line(high, simbol='|'):
 return [simbol for _ in range(high)]
def word_in_a_frame(word):
 lenght_word = len(word)
 high_frame = g_line(lenght_word + 2)
 lower_frame = high_frame
 side_frame = w_line(3)

 print(high_frame)
 print(f"{side_frame[0]}{word}{side_frame[0]}")
 print(lower_frame)
# Использование
word = input("Введите слово")
word_in_a_frame(word)