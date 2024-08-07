#Ball-super-ball
print("-"*30)
class Ball:
    def __init__(self,ball_type = "regular"):
        self.ball_type = ball_type

ball1 = Ball()
ball2 = Ball("super")
print(ball1.ball_type)
print(ball2.ball_type)
print("-"*30)

#Color-ghost
import random
class Ghost:
    def __init__(self):
        self.color = random.choice(["white","yellow","purple","red"])

ghost = Ghost()
print(ghost.color)
print("-"*30)

#Basic-subclasses-Adam-and-Eve
class Human:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return f"{self.__class__.__name__}:{self.name}"
class Man(Human):
    def __init__(self,name = "Adam"):
        super().__init__(name)
class Woman(Human):
    def __init__(self,name = "Eve"):
        super().__init__(name)
def God():
        return [Man(),Woman()]

print(God())
print("-"*30)

#Classy-classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        return f'{self.name} age is {self.age}'
    
john = Person("John", 28)
print(john.info())
print("-"*30)

#Building Spheres
from math import pi
class Sphere:
    def __init__(self,radius,mass):
        self.radius = radius
        self.mass = mass
    def get_radius(self):
        return f'Radius of sphere is: {self.radius}'
    def get_mass(self):
        return f'Mass of sphere is: {self.mass}'
    def get_volume(self):
        volume = round((4/3) * pi * self.radius ** 3,5)
        return f'Volume of sphere is: {volume}'
    def get_surface_area(self):
        return f'Surface area of sphere is: {round(4 * pi * self.radius ** 2,5)}'
    def get_density(self):
        return f'Density of sphere is: {round(self.mass/round((4/3) * pi * self.radius ** 3,5),5)}'
    
ball = Sphere(2,50)
print(ball.get_radius())
print(ball.get_mass())
print(ball.get_volume())
print(ball.get_surface_area())
print(ball.get_density())
print("-"*30)

#Dynamic Classes
class MyClass:
    pass

def rename_class(cls,name):
    if not name[0].isupper() or not name.isalnum():
        raise ValueError("Bad name for class!")
    else:
        cls.__name__ = name

rename_class(MyClass,'123123')
rename_class(MyClass,'UsefulClass')