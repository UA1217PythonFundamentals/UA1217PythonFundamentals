class Polygon:
    def __init__(self, sides):
        self.sides = sides

# Define the Rectangle class that inherits from Polygon
class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__(sides=4)  # Rectangle has 4 sides
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Example usage
rectangle = Rectangle(5, 10)
print(f"Area of the rectangle: {rectangle.area()}")