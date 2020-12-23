# Задание 7:
from math import factorial


def fact(numbers):
    for el in numbers:
        yield factorial(el)


number = int(input("Факториал какого числа вы хотите узнать? "))
n = [el for el in range(1, number + 1)]
x = 1
for el in fact(n):
    response = input(f"Посчитать факториал {x} да/нет? ")
    if response.lower() == "да":
        print(f"{x}! = {el}")
    elif x == number:
        print(f"{number}! = {el}")
    x += 1
