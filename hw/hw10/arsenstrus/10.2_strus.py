#1
class Ball(object):
    def __init__(self,type="regular"):
        self.ball_type=type

#2
import random

class Ghost(object):
    def __init__(self):
        colors = ["white", "yellow", "purple", "red"]
        self.color = random.choice(colors)

#3
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

#4
class Person:
    def __init__(self, name, age):
        self.name = str(name)
        self.age = int(age)
        self.info = f"{self.name}s age is {self.age}"

#5
import math


class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        return round(4 / 3 * math.pi * pow(self.radius, 3), 5)

    def get_surface_area(self):
        return round(4 * math.pi * pow(self.radius, 2), 5)

    def get_density(self):
        return round(self.mass / Sphere.get_volume(self), 5)

#6
import re

def class_name_changer(cls, new_name):
    if not re.match(r'^[A-Z][a-zA-Z0-9]*$', new_name):
        raise ValueError(
            "Invalid class name. It must start with an uppercase letter and contain only alphanumeric characters.")

    cls.__name__ = new_name