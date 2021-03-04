# Задание 2:
from abc import ABC, abstractmethod
from decimal import Decimal, getcontext

getcontext().prec = 3


class Clothes(ABC):

    @abstractmethod
    def tissue_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def tissue_consumption(self):
        return Decimal(self.size) / Decimal(6.5) + Decimal(0.5)


class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def tissue_consumption(self):
        return 2 * Decimal(self.height) + Decimal(0.3)


size = height = 25
print(f"Расход ткани на пальто = {Coat(size).tissue_consumption} м")
print(f"Расход ткани на костюм = {Suit(height).tissue_consumption} м")
