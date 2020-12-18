# Задание 4
def my_func(number, degree):
    # return number ** degree
    pre_result = number
    for i in range(abs(degree) - 1):
        pre_result *= number
    return 1 / pre_result


number = 2
degree = -3
print(f"{number} в степени {degree} = {my_func(number, degree)}")
