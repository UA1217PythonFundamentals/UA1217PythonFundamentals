from math import pi, pow

def area_rectangle(width: float, height: float) -> float:
    '''Returns calculated area of rectangle with width and height provided as arguments'''
    return width * height

def area_triangle(base: float, height: float) -> float:
    '''Returns calculated area of triangle with base and height provided as arguments'''
    return 1/2 * base * height

def area_circle(radius: float) -> float:
    '''Returns calculated area of circle with radius provided as argument
    Needs pi and pow() built-in functions from math module 
    '''
    return pi * pow(radius, 2)