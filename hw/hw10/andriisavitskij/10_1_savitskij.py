# #Task 1: Create a polygon class and a rectangle class that inherits from the polygon class and finds the square of rectangle
# class Polygon:
#     def __init__(self, *args):
#         self.a=args

# class Rectangle(Polygon):
#     def __init__(self, l, h):
#         super().__init__(l,h)

#     def rec_square(self):
#         h, l = self.a
#         return l*h
    
# test = Rectangle(7,8)
# r = test.rec_square()
# print(f'Area of rectangle is: {r}')


#Task 2: Class Human
# class Person:
#     species = "Homosapiens"
#     def __init__(self, name):
#         self.name = name

#     def display_info(self):
#         print("Hello, my name is ", self.name)

#     def display_species(self):
#         print(f"{self.name} is",Person.species)

#     def arb_message():
#         return "Person class"

        
# person1 = Person("Jackob")
# person1.display_info() # Hello, my name is Jackob

# person2 = Person("Andrzej")
# person2.display_info() # Hello, my name is Andrzej

# person1.display_species()
# person2.display_species()
# print(Person.arb_message())


# Task 3: Employee class
class Employee:
    """An employee class"""
    employees = 0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        employees += 1
    
    @classmethod
    def number_of_employees(cls):
        """Print a total number of employees"""
        print(f"Total Employees: {cls.total_employees}")        

    def display_info(self):
        """Name and salary of each employee"""
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")


person1=Employee("Andrii", 3400)
person2=Employee("Nazar", 200)
Employee.display_total_number() # 2
person1.display_info()
person2.display_info()

#Addition
print(Employee.__base__, Employee.__dict__,
        Employee.__name__, Employee.__module__,
        Employee.__doc__)