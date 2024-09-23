#6hard
from math import pi, sqrt

class Figure:
    sides_count = 0
    filled = False
    def __init__(self, color, *sides):
        self.__color = color if self.__is_valid_color(*color) else [0, 0, 0]
        self.__sides = [*sides]

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
 #       r,g,b = abs(r), abs(g), abs(b)
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
            if not isinstance(side, int) or side <= 0:
                return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.get_sides())

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = [*new_sides]

    def __is_valid_sides_count(self, args):
        if len(args) != self.sides_count:
            args = (1,) * self.sides_count
        return args


class Circle(Figure):
    sides_count = 1
    def __int__(self, color, *sides):
        super().__init__(*sides)
        self.__radius = self.get_sides() / (2 * pi)
#        len =  sides[0]

    def get_square(self):
        # if (len[self.sides] + 1) != self.sides_count and (len[self.sides] + 1) > 1:
        #     self.__get_sides == [0]
        return pi * (self.radius**2)

class Triangle(Figure):
    __sides_count = 3


    def __init__(self, color, __sides):
        self.__sides = __sides
        if (len(self.__sides) + 1) != self.sides_count:
            self.__sides = [1, 1, 1]
            return color, __sides
    def get_square(self):
        p = len(self) / 2
        side = self.get_sides()
        return sqrt(p*(p - side[0])*(p - side[1])*(p - side[2]))
  #      return s

class Cube(Figure):
    __sides_count = 12
    def __init__(self, color:list, *sides:int):
        super().__init__(color, *sides)
#       self.set_sides(*list(sides)*12)
        sides = sides * self.__sides_count
        super().__init__(color, *sides)
# #       return self.set_sides(*list(sides)*12)

    def get_volume(self, color:list, *sides:int):
        super().__init__(*sides)
 #       self.__sides = __sides
        return sides ** 3

 #       self.set_sides(*list(sides)*12)
#         return self.set_sides(*list(sides) ** 3)


        #
#        return self.set_side ** 3
#        super().__init__(self)

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
