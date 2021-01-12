sides = ("лево", "право")


class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"{self.color} {self.name} начало движение"

    def stop(self):
        return f"{self.color} {self.name} остановка"

    def turn(self, direction):
        return f"{self.color} {self.name} поворот на{direction}"

    def show_speed(self):
        return f"{self.color} {self.name} едет со скоростью {self.speed} км/ч"


class TownCar(Car):
    name = "TownCar"
    max_speed = 60

    def __init__(self, speed, color):
        super().__init__(speed, color, self.name)

    def show_speed(self):
        if self.speed > self.max_speed:
            return f"{self.color} {self.name} нарушает правила!!! едет со скоростью {self.speed} км/ч"
        return super().show_speed()


class WorkCar(Car):
    name = "WorkCar"
    max_speed = 40

    def __init__(self, speed, color):
        super().__init__(speed, color, self.name)

    def show_speed(self):
        if self.speed > self.max_speed:
            return f"{self.color} {self.name} нарушает правила!!! едет со скоростью {self.speed} км/ч"
        return super().show_speed()


class SportCar(Car):
    name = "SportCar"
    color = "yellow"

    def __init__(self, speed):
        super().__init__(speed, self.color, self.name)


class PoliceCar(Car):
    name = "PoliceCar"
    color = "black"

    def __init__(self, speed):
        super().__init__(speed, self.color, self.name, True)


example_without_violation = TownCar(60, "green")
example_with_violation = WorkCar(41, "green")
example_sport_car = SportCar(130)
example_police_car = PoliceCar(90)

print(f"{example_without_violation.go()}")
print(f"{example_without_violation.show_speed()}")
print(f"{example_without_violation.turn(sides[0])}")
print(f"{example_sport_car.go()}")
print(f"{example_without_violation.stop()}")

print(f"{example_with_violation.go()}")
print(f"{example_with_violation.show_speed()}")
print(f"{example_police_car.go()}")
print(f"{example_with_violation.stop()}")
