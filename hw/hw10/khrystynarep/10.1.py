# Task 1
class Polygon():
    """A polygon class for calculation the area of rectangle"""
    def __init__(self, *args):
        self.a=args

class Rectangle(Polygon):
    def __init__(self, l, h):
        super().__init__(l,h)

    def square_of_rectangle(self):
        h, l = self.a
        return l*h
    
cd = Rectangle(4,4)
area = cd.square_of_rectangle()
print(f"Area of the rectangle: {area}")

# Task 1. Another way

# class Polygon:
#     def __init__(self, no_of_sides):
#         self.n = no_of_sides
#         self.sides = [0 for i in range(no_of_sides)]
    
#     def inputSides(self):
#         self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]
    
#     def dispSides(self):
#         for i in range(self.n):
#             print("Side",i+1,"is",self.sides[i])

# class RectangleQ(Polygon):
#     def __init__(self):
#         Polygon.__init__(self,2) #super().__init__(3)
    
#     def findArea(self):
#         a, b = self.sides
#         area = (a*b)
#         print('The area of the rectangle is %0.2f' %area)
# t=RectangleQ()
# t.inputSides()
# t.findArea()

# Task 2
class Person:
    """Create a class Human"""
    species = "Homosapiens"
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print("Hello, my name is ", self.name)

    def display_species(self):
        print(f"{self.name} is",Person.species)

    def arbitrary_message():
        return "Person class"

        
person1 = Person("Tom")
person1.display_info() # Hello, my name is Tom
person2 = Person("Sam")
person2.display_info() # Hello, my name is Sam
person1.display_species()
print(Person.arbitrary_message())

#Task 3
class Employee:
    """A class of an employee."""
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1 

    @classmethod
    def display_total_number(cls):
        """Calculates the total number of employee"""
        print(f"Total Employees: {cls.total_employees}")        

    def display_info(self):
        """Name and salary of each employee"""
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")

#Addition
print(Employee.__base__, Employee.__dict__,
        Employee.__name__, Employee.__module__,
        Employee.__doc__)

personid1=Employee("Alla", 3400)
personid2=Employee("Yaroslav", 2200)
Employee.display_total_number()

personid1.display_info()
