# Задание 3
def my_func(number1, number2, number3):
    numbers = [number1, number2, number3]
    max1 = max(numbers)
    numbers.remove(max1)
    max2 = max(numbers)
    return max1 + max2


numbers = [1, 2, 10]
print(f"Из списка {numbers} сумма наибольших двух аргументов = " +
      f"{my_func(numbers[0], numbers[1], numbers[2])}")
