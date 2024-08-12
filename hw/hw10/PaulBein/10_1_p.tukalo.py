#Task1
class Polygon:
    def __init__(self,a,b):
        self.a = a
        self.b = b

class Rectangle(Polygon):
    def square(self):
        return f"Square of rectangle: {round(self.a * self.b,2)}"

result = Rectangle(8.3,6.5)
print(result.square())
print("-"*35)
#Task2
class Human:
    species = "Homosapiens"
    def __init__(self,name):
        self.name = name
    def welc_msg(self):
        return f"Welcome, {self.name}"
    @classmethod
    def homo_msg(cls):
        return f"You're a {cls.species}"
    @staticmethod
    def msg():
        return f"Big power is a big responsibility!"
    
peter = Human('Peter Parker')
print(peter.welc_msg())
print(peter.homo_msg())
print(peter.msg())
print("-"*35)

#Task3
class Employee:
    empl_count = 0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empl_count += 1
    @classmethod
    def number_of_empl(cls):
        return f'Number of employee is: {cls.empl_count}'
    def empl_info(self):
        return f'''Name: {self.name}
Salary: {self.salary}
-------------------------'''

first = Employee("Paul","10000")
second = Employee("Julia","12000")
third = Employee("William", "8500")
print(first.empl_info())
print(second.empl_info())
print(third.empl_info())
print(Employee.number_of_empl())
print("-"*25)

print(f"Base classes: {Employee.__base__}")
print(f"Class namespace: {Employee.__dict__}")
print(f"Class name: {Employee.__name__}")
print(f"Module name: {Employee.__module__}")
print(f"Documentation bar: {Employee.__doc__}")    