# Задание 5
def my_func():
    result = 0
    condition = True
    while condition:
        numbers = input("Введите строку чисел, разделенных пробелом: ").split(" ")
        for number in numbers:
            if not number.isdigit():
                condition = False
                break
            result += int(number)
        print(f"Сумма всех чисел, введённых до специального знака, = {result}")


my_func()
