#6hard
from math import pi, sqrt

class Figure:
    sides_count = 0
    def __init__(self, color:list, *sides:int):
        self.__color = [*color] if self.__is_valid_color(*color) else[0,0,0]
        self.__sides = [*sides] if len(sides) == self.sides_count else [1] * self.sides_count
        self.filled = False
    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
       if self.__is_valid_color(r, g, b):
           self.__color = [r, g, b]

    def __is_valid_sides(self,*new_sides):
        if len(new_sides) != self.sides_count:
            return False
        for side in new_sides:
            if not isinstance(side, int or float) or side <= 0:
                return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides:int):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
#            return self.__sides

class Circle(Figure):
    sides_count = 1
    def __int__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.__sides / (2 * pi)

    def get_square(self):
       return (self.__radius**2) * pi

class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        p = len(self) / 2
        self.get_sides()
        return sqrt(p*(p - side[0])*(p - side[1])*(p - side[2]))

class Cube(Figure):
    sides_count = 12

    def __init__(self, color:list, *sides:int):
        super().__init__(color, *sides)
        self.__sides = [sides[0]] * self.sides_count
        self.set_sides(*list(sides) * self.sides_count)

    def get_volume(self, *sides:int):
        return self.__sides[0] ** 3


circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 65, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())
# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())

# # Проверка периметра (круга), это и есть длина:
print(len(circle1))                     # 15

# Проверка объёма (куба):
print(cube1.get_volume())               # 216