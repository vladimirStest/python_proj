# Задание 6:
from itertools import count
from itertools import cycle

start_for_count = int(input("Введите стартовое число: "))
finish_for_count = int(input("Введите последнее число: "))
print(f"Ниже представлены целые числа, начиная с {start_for_count} и до {finish_for_count} :")
for el in count(start_for_count):
    if el > finish_for_count:
        break
    else:
        print(el)

count_of_elements_in_cycle = 10
string_for_cycle = input(f"Введите строчку для демонстрации функции cycle на {count_of_elements_in_cycle} элементах: ")
с = 0
for el in cycle(string_for_cycle):
    if с > 10:
        break
    print(el)
    с += 1
