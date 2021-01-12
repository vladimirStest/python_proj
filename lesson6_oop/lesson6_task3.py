class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income["wage"] = wage
        self.__income["bonus"] = bonus
        # self._income["wage"] = wage
        # self._income["bonus"] = bonus

    __income = {}
    # _income = {}


class Position(Worker):

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._Worker__income.get("wage") + self._Worker__income.get("bonus")
        # return self._income.get("wage") + self._income.get("bonus")


example = Position("имя", "фамилия", "позиция", 4, 5)
print(f"{example.get_full_name()} {example.get_total_income()}")
