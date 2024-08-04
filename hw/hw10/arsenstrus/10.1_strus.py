#Task1
class Polygon:
    pass
class Rectangle(Polygon):
    def __init__(self,x,y):
        self.side_a=x
        self.side_b=y

    def square(self):
        return (f"Rectangle square: {self.side_b * self.side_a}")
#Task2
class Human:
    def __init__(self,name):
        self.name=name
    def greeting(self):
        print(f"Hello {self.name}")
    @classmethod
    def information(cls):
        print("This is a Homosapiens")
    @staticmethod
    def Helloword():
        print("Hello word")

#Task3
class Employee:
    """"Saves information about employees"""
    counter=0
    def __init__(self,name,salary):
        Employee.counter+=1
        self.name=str(name)
        self.salary=int(salary)
    @classmethod
    def total_employees(cls):
        print(f"Total number of employees: {Employee.counter}")
    def info(self):
        return f'Employee {self.name} has a salary of {self.salary}$'

print("Base classes:", Employee.__base__)
print("Class namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Documentation:", Employee.__doc__)