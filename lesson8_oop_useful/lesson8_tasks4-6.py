from abc import ABC, abstractmethod

import lesson8_task3


class OfficeEquipment(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def ability(self, txt):
        pass

    def __str__(self):
        return self.name


class Storage:
    color = "black"
    info = {"подразделение": {"Название оргтехники": "Количество"}}
    given_away = {"подразделение": {"Название оргтехники": "Количество"}}
    equipments = set("оргтехника")

    def __init__(self):
        self.info.clear()
        self.given_away.clear()
        self.equipments.clear()

    def add_equipment(self, subdivision, eq: OfficeEquipment, count):
        if not isinstance(eq, OfficeEquipment):
            raise lesson8_task3.AddError("На склад нельзя добавлять ничего кроме оргтехники")
        if subdivision in self.info.keys():
            self.add_equipment_old_subdivision(subdivision, eq, count)
        else:
            self.info[subdivision] = {eq.name: count}
        self.equipments.add(eq)

    def pick_up_equipment(self, subdivision, eq: OfficeEquipment, count):
        self.add_equipment_old_subdivision(subdivision, eq, -count)

    def add_equipment_old_subdivision(self, subdivision, eq: OfficeEquipment, count):
        new_count = count
        old_count = 0
        dicts = self.info.get(subdivision)
        if eq.name in self.get_equipments(subdivision):
            old_count = list(self.info.get(subdivision).values())[0]
            new_count = old_count + count
            del (dicts[eq.name])
        if new_count < 0:
            print(
                f"Для вашего подразделения {subdivision} на складе нет {abs(count)} {eq.name}, в наличии {old_count} штуки")
            return
        dicts[eq.name] = new_count
        self.info[subdivision] = dicts
        if count < 0:
            self.pick_up(subdivision, eq, count)

    def pick_up(self, subdivision, eq: OfficeEquipment, count):
        pick_up_dicts = {}
        if eq.name in self.get_pick_up_equipments(subdivision):
            pick_up_dicts = self.given_away.get(subdivision)
            old_count = list(self.given_away.get(subdivision).values())[0]
            new_count = old_count + abs(count)
            del (pick_up_dicts[eq.name])
        else:
            new_count = abs(count)
        pick_up_dicts[eq.name] = new_count
        self.given_away[subdivision] = pick_up_dicts

    def print_equipments(self):
        x = set([t.name for t in self.equipments])
        s = "на складе представлена оргтехника:\n"
        while len(x) > 0:
            for el in self.equipments:
                if el.name in x:
                    s += f"{str(el)}\n"
                    x.remove(el.name)
        print(s)

    def get_equipments(self, subdivision):
        if self.info.get(subdivision) is None:
            return []
        return [k for (k, v) in self.info.get(subdivision).items()]

    def get_pick_up_equipments(self, subdivision):
        if self.given_away.get(subdivision) is None:
            return []
        return [k for (k, v) in self.given_away.get(subdivision).items()]

    def __str__(self):
        s1 = ""
        for k, v in self.info.items():
            s1 += f"\nдля подразделения {k}:\n"
            for key, value in v.items():
                s1 += f"на складе есть {value} {key}\n"
        s2 = ""
        for k, v in self.given_away.items():
            s2 += f"\nдля подразделения {k}:\n"
            for key, value in v.items():
                s2 += f"выдано {value} {key}\n"
        return s1 + s2


class Printer(OfficeEquipment):
    def ability(self, txt):
        print(f"{self.name} напечатал {txt}")

    name = "printer"

    def __init__(self, price):
        self.price = price

    def __str__(self):
        return f"{super().__str__()} стоимостью {self.price}"


class Scanner(OfficeEquipment):
    name = "scanner"

    def ability(self, txt):
        print(f"{self.name} отсканировал {txt}")

    def __init__(self, color):
        self.color = color

    def __str__(self):
        return f"{super().__str__()} цветом {self.color}"


class Xerox(OfficeEquipment):
    name = "xerox"

    def ability(self, txt):
        print(f"{self.name} скопировал {txt}")

    def __init__(self, velocity):
        self.velocity = velocity

    def __str__(self):
        return f"{super().__str__()} со скоростью копирования {self.velocity}"


x = Storage()
x.add_equipment("example", Printer(1000), 2)
x.pick_up_equipment("example", Printer(1000), 3)
x.add_equipment("example", Printer(1000), 4)
x.pick_up_equipment("example", Printer(1000), 3)
x.add_equipment("example", Scanner("red"), 1)

x.pick_up_equipment("example4", Printer(1000), 3)

x.add_equipment("example2", Scanner("red"), 1)
x.add_equipment("example3", Xerox(100), 3)
print(f"Для подразделения example на складе представлены {x.get_equipments('example')}")
print(x.info)
print(x)

x.print_equipments()

x.add_equipment("example", "корова", 1)
