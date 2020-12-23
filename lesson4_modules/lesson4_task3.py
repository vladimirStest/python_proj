# Задание 3:
new_numbers = [number for number in range(20, 241) if (number % 20 == 0) | (number % 21 == 0)]
print(f"Для чисел в пределах от 20 до 240 числа, кратные 20 или 21 = {new_numbers}")
