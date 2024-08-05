class Polygon:
    def __init__(self, sides):
        self.sides = sides
    

class Rectangle(Polygon):
    def __init__(self):
        self.width = float(input("Enter the width of the rectangle: "))
        self.height = float(input("Enter the height of the rectangle: "))
        super().__init__([self.width, self.height, self.width, self.height])
    

    def area(self):
        return self.width * self.height


rect = Rectangle()
print(f"Area of rectangle: {rect.area()}")
