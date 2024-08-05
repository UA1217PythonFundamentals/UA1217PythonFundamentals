#Task 1: Regular Ball Super Ball
# class Ball(object):
#     def __init__(self, type="regular"):
#         self.ball_type = type

#Task 2: Color-ghost
# from random import choice
# class Ghost(object):
#     colors = ["red", "yellow", "white", "purple"] 
#     def __init__(self):
#         self.color = choice(self.colors)


# #Task 3: Adam and Eve
# def God():
#     return [Man(), Woman()]
# class Human():
#     pass
# class Man(Human):
#     pass
# class Woman(Human):
#     pass


#Task 4: Classy classes
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         self.info = f"{self.name}s age is {self.age}"


#Task 5:Building Spheres
# import math
# class Sphere(object):
#     def __init__(self,radius,mass):
#         self.radius = radius
#         self.mass = mass
#     def get_radius(self):
#         return self.radius
#     def get_mass(self):
#         return self.mass
    
#     def get_volume(self):
#         res = (4/3 * math.pi * self.radius**3)
#         return round(res,5)
    
#     def get_surface_area(self):
#         res = (4 * math.pi * self.radius ** 2)
#         return round(res,5)
    
#     def get_density(self):
#         res = self.mass / (4/3 * math.pi * self.radius**3)
#         return round(res,5)


# #Task 6: Dynamic Classes
# def class_name_changer(cls, new_name):
#     cls.__name__ = new_name