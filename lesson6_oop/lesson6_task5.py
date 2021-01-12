class Stationery:

    def draw(self):
        return "Запуск отрисовки"


class Pen(Stationery):
    title = "ручка"

    def draw(self):
        print(f"{super().draw()} для {self.title}")


class Pencil(Stationery):
    title = "карандаш"

    def draw(self):
        print(f"{super().draw()} для {self.title}")


class Handle(Stationery):
    title = "маркер"

    def draw(self):
        print(f"{super().draw()} для {self.title}")


Pen().draw()
Pencil().draw()
Handle().draw()
