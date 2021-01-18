class AddError(Exception):
    def __init__(self, txt):
        self.txt = txt


class NewList:
    newList = []

    def __init__(self):
        while True:
            try:
                digit = input(f'введите число : ')
                if digit.isdigit():
                    self.newList.append(int(digit))
                elif digit == "stop":
                    break
                else:
                    raise AddError("Вводить можно только числа!")
            except AddError as e:
                print(e)
        print(f"Список вводимых пользователем чисел: {self.newList}")


NewList()
