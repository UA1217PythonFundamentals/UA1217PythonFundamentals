class Polygon:
    def __init__(self, sides):
        self.side_lengths = sides 
        self.number_of_sides = len(sides)

class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__([width, height])
        self.width, self.height = self.side_lengths

    def area(self):
        return round(float(self.width * self.height),2)


rect = Rectangle(5.5, 11)

print(rect.number_of_sides)
print(rect.area())