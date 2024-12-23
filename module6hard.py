class Figure():

    def __init__(self, sides_count = 0, sides = 0, color = [0, 0, 0], filled = True):
        self.sides_count = sides_count
        self.__sides = sides
        self.__color = color
        self.filled = filled

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def __is_valid_color(self, __color):
        for i in self.__color:
            if 0 <= i <= 255 and isinstance(i, int) :
                True
            else:
                False

    def __is_valid_sides(self):# c количеством сторон не пойму
        if self.__sides > 0 and isinstance(self.__sides, int):
            return True
        else:
            return False

    def get_sides(self, sides):
        self.__is_valid_sides()
        self.__sides = sides
        return self.__sides

    def __len__(self):# не пойму, где брать длины сторон
        pass

    def set_sides(self, *new_sides):
        if self.sides_count != new_sides:
            print(self.__sides)
            print(self.sides_count)
        else:
            self.sides_count = new_sides
            print(self.sides_count)


class Circle(Figure):

    sides_count = 1

    def __radius(self):
        pass

    def get_square(self):
        pass


class Triangle(Figure):

    sides_count = 3

    def get_square(self):
        pass


class Cube(Figure):

    sides_count = 12

    def __init__(self):
        pass


f1 = Figure()

f1.set_color([125, 45, 85])
(f1.get_color())
(f1.get_sides(0))




