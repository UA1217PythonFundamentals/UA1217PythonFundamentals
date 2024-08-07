from math import pi
from math import pow

def area_of_rectangle(a,b):
    S = a * b
    return S

def area_of_triangle(a,h):
    S = 0.5 * a * h
    return S

def area_of_circle(r):
    S = pi * pow(r,2)
    return S