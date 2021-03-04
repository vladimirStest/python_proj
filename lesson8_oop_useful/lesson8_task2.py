class ZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt


x = 100

while True:
    try:
        y = int(input(f'введите делитель для {x} : '))
        if y == 0:
            raise ZeroError("На отрицательное число делить нельзя!")
        print(f"{x} разделить на {y} = {x / y}")
        break
    except ZeroError as e:
        print(e)

