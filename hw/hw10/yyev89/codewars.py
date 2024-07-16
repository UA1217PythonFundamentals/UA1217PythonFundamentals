# Ball-super-ball
class Ball:
    def __init__(self, ball_type='regular'):
        self.ball_type = ball_type


# Color-ghost
import random
class Ghost(object):
    def __init__(self):
        colors = ['red', 'yellow', 'purple', 'white']
        self.color = random.choice(colors) 


# Basic subclasses - Adam and Eve
class Human:
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

def God():
    adam = Man()
    eve = Woman()
    return [adam, eve]


# Classy Classes
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.info=f'{name}s age is {age}'
    

# Building Spheres
import math
class Sphere:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius
    
    def get_mass(self):
        return self.mass
    
    def get_volume(self):
        volume = (4/3) * math.pi * self.radius ** 3
        return round(volume, 5)
    
    def get_surface_area(self):
        surface_area = 4 * math.pi * self.radius ** 2
        return round(surface_area, 5)
    
    def get_density(self):
        density = self.mass / self.get_volume()
        return round(density, 5)
    

# Dynamic Classes
def class_name_changer(cls, new_name):
    if new_name[0].isupper() and new_name.isalnum():
        cls.__name__ = new_name
    else:
        raise ValueError('Wrong name')