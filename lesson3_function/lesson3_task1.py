# Задание 1
def get_quotient(dividend, divisor):
    quotient = None
    while quotient is None:
        try:
            quotient = dividend / divisor
        except ZeroDivisionError:
            print("На ноль делить нельзя!")
            divisor = int(input(f"Введите другой делитель: "))
    if dividend % divisor != 0:
        quotient = round(quotient, 3)
    else:
        quotient = int(quotient)
    return f"{dividend}/{divisor} = {quotient}"


print(get_quotient(int(input(f"Введите делимое: ")), int(input(f"Введите делитель: "))))
