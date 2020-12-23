# Задание 5:
from functools import reduce

products = reduce(lambda x, y: x * y, [number for number in range(100, 1001) if number % 2 == 0])
print(f"произведения всех четных чисел от 100 до 1000 = {products}")
