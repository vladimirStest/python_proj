# Задание 4:
numbers = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_numbers = [number for number in numbers if numbers.count(number) == 1]
print(f"элементы списка, не имеющие повторений = {new_numbers}")
