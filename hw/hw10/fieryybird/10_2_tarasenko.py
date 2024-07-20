## 1) Ball-super-ball
class Ball:
  def __init__ (self,ballType='regular'):
    self.ballType = ballType

# 2) Color-ghost
import random

class Ghost:
  def __init__ (self):
    self.color = random.choice(["white", "yellow", "purple", "red"])

## 3) Basic-subclasses-Adam-and-Eve
class Human():
    pass
class Man(Human):
    pass
class Woman(Human):
    pass

def God():
    adam = Man()
    eve = Woman()
    return [adam, eve]

## 4) Classy-classes
class Person:
  def __init__(self, name, age):
      self.name, self.age = name, age
    
  def info(self):
      return f'{self.name}s age is {self.age}'


## 5) Building Spheres
class Sphere:
    PI = 3.14159265358979
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius
    def get_mass(self):
        return self.mass
    def get_volume(self):
        return round((4/3) * self.PI * (self.radius ** 3), 5)
    def get_surface_area(self):
        return round((4 * self.PI * (self.radius ** 2)), 5)
    def get_density(self):
        volume = self.get_volume()
        return round((self.mass / volume), 5)

## 6) Dynamic Classes
def class_name_changer(cls, new_name):
  if not new_name[0].isupper() or not new_name.isalnum():
    raise ValueError()
  else:
    cls.__name__ = new_name