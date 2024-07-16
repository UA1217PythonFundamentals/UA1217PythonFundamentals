##################################################
# Task 1
class Polygon:
    """Base class for all polygon shapes."""
    
    def __init__(self, num_sides):
        """Initialize with the number of sides."""
        self.num_sides = num_sides


class Rectangle(Polygon):
    """Class representing a rectangle, derived from Polygon."""
    
    def __init__(self, length, width):
        """Initialize with length and width."""
        super().__init__(4)
        self.length = length
        self.width = width

    def calc_area(self):
        """Calculate the area of the rectangle."""
        return self.length * self.width

rec = Rectangle(3, 5)
print(f'Area of rectangle: {rec.calc_area()}')


##################################################
# Task 2
class Human:
    """Class representing a human being."""
    species = 'Homosapiens'

    def __init__(self, name):
        """Initialize with the human's name."""
        self.name = name
        
    def greet(self):
        """Greet the human by name."""
        print(f'Hello, {self.name}!')

    @classmethod
    def get_species(cls):
        """Return the species of the human."""
        return f'Species = {cls.species}'

    @staticmethod
    def normality():
        """Return a description of normality."""
        return 'Nerd' 

dude = Human('Bill Gates')
dude.greet()
print(Human.get_species())
print(Human.normality())


##################################################
# Task 3
class Employee:
    """Class representing an employee."""
    counter = 0

    def __init__(self, name, salary):
        """Initialize with the employee's name and salary."""
        self.name = name
        self.salary = salary
        Employee.counter += 1
    
    def get_info(self):
        """Print the employee's information."""
        print(f'Name: {self.name}, salary: {self.salary}$')

    @classmethod
    def count_employees(cls):
        """Print the total number of employees."""
        print(f'Number of all employees: {cls.counter}')

data = f'''
Base: {Employee.__base__}
Namespace: {Employee.__dict__}
Name: {Employee.__name__}
Module: {Employee.__module__}
Documentation: {Employee.__doc__}
'''

dude01 = Employee('Steve Jobs', 1_000_000)
dude02 = Employee('Steve Wozniak', 500_000)
dude01.get_info()
dude02.get_info()
Employee.count_employees()
print(data)