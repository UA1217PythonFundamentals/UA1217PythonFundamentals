# I. Ball-super-ball

class Ball(object):

    def __init__(self, ball_type="regular"):
        self.ball_type=ball_type

# ball1 = Ball()
# ball2 = Ball("super")
# print(ball1.ball_type)  #=> "regular"
# print(ball2.ball_type)  #=> "super"


# II. Color-ghost


import random
class Ghost(object):
    def __init__(self):
        self.colors = ["white", "yellow", "purple", "red"]
        self.color = random.choice(self.colors)


# III. Basic-subclasses-Adam-and-Eve


class Human:
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

def God():
    return [Man(), Woman()]


# IV. Classy-classes


class Person():
    def __init__(self, name,age):
        self.name, self.age = name, age
        self.info=f"{self.name}s age is {self.age}"


# V. Building Spheres

import math
class Sphere(object):
    def __init__(self, radius, mass):
        self.radius, self.mass = radius, mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass
    
    def get_volume(self):
        self.volume = (4/3) * math.pi * (self.radius ** 3)
        return round(self.volume, 5)
    
    def get_surface_area(self):
        """rounded to 5 place after the decimal"""
        self.surface= 4* math.pi * (self.radius ** 2)
        return round(self.surface, 5)
    
    def get_density(self):
        self.density = self.mass/self.volume
        return round(self.density, 5)
    
# VI. Dynamic Classes

def change_class_name(cls, new_name):
    """Check the class name and rename class name"""
    if not new_name[0].isupper():
        raise ValueError("Class name must start with an uppercase letter")

    if not new_name.isalnum():
        raise ValueError("Class name must contain only alphanumeric characters")

    cls.__name__ = new_name


