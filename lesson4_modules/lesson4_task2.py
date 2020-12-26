# Задание 2:
numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_numbers = [number for i, number in enumerate(numbers) if numbers[i] > numbers[i-1]]
print(f"Элементы исходного списка, значения которых больше предыдущего элемента = {new_numbers}")
