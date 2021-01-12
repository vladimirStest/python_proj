class Road:
    weight_normal = 25
    height_normal = 5

    def __init__(self, length, width):
        self.__width = width
        self.__length = length

    def calculate(self, weight=weight_normal):
        return self.__length * self.__width * weight * self.height_normal


width = 10
length = 1
example = Road(length, width)
print(f"Масса асфальта для покрытия дорожного полотна длиной {length} м и шириной {width} м = {example.calculate()} кг")
