from abc import ABC, abstractmethod


class Storage:
    color = "black"


class OfficeEquipment(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def ability(self, txt):
        pass


class Printer(OfficeEquipment):
    def ability(self, txt):
        print(f"{self.name} напечатал {txt}")

    name = "printer"

    def __init__(self, price):
        self.price = price


class Scanner(OfficeEquipment):
    name = "scanner"

    def ability(self, txt):
        print(f"{self.name} отсканировал {txt}")

    def __init__(self, color):
        self.color = color


class Xerox(OfficeEquipment):
    name = "xerox"

    def ability(self, txt):
        print(f"{self.name} скопировал {txt}")

    def __init__(self, velocity):
        self.velocity = velocity
