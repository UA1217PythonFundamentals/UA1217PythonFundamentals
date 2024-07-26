#Task1. Create a polygon class and a rectangle class
#that inherits from the polygon class and finds the square
#of rectangle.
from abc import ABC, abstractmethod

class Polygon:
    sides = None
    sides_count = None

    def __init__(self, sides, sides_count):
        self.sides = sides
        self.sides_count = sides_count

    @abstractmethod
    def calc_square(self):
        pass

class Rectangle(Polygon):

    def __init__(self, a_side, b_side):
        super().__init__([a_side, b_side, a_side, b_side], 4)

    def calc_square(self):
        return self.sides[0] * self.sides[1]


a_side = int(input("Please, enter the length of rectangle to be calculate: "))
b_side = int(input("Please, enter the width of rectangle to be calculate: "))
rectangle = Rectangle(a_side, b_side)
print(f"Area of rectangle:  {rectangle.calc_square()}")
