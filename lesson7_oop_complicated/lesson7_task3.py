# Задание 3:
class Cell:

    def __init__(self, count):
        self.count = count

    def __str__(self):
        return self.count

    def __add__(self, added):
        self.count = self.count + added.count
        return self.count

    def __sub__(self, subtrahend):
        if self.count - subtrahend.count > 0:
            self.count = self.count - subtrahend.count
            return self.count
        else:
            print("Невозможно получить клетку с отрицательным или нулевым количеством клеток")

    def __mul__(self, multiplied):
        self.count = self.count * multiplied.count
        return self.count

    def __truediv__(self, divider):
        self.count = int(round(self.count / divider.count, 0))
        return self.count

    def make_order(self, number_in_row):
        x = ""
        number_of_disordered_cells = self.count
        while number_of_disordered_cells > 0:
            for i in range(number_in_row):
                x += "*"
                number_of_disordered_cells -= 1
                if number_of_disordered_cells == 0:
                    break
            x += "\n"
        return x


mc1 = Cell(11)
mc2 = Cell(3)
print(f"Сумма = {mc1 + mc2} м")
print(f"Разность = {mc1 - mc2} м")
print(f"Умножение = {mc1 * mc2} м")
print(f"Деление = {mc1 / mc2} м")
print(f"Упорядоченные клетки :\n{mc1.make_order(3)}")
