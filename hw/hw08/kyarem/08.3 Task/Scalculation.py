import math

def KY_rectangle(a, b):
    area_rectangle = a * b
    return area_rectangle

def KY_triangle(a, h):
    area_triangle = (0.5 * a * h)
    round_triangle = round(area_triangle,3)
    return round_triangle

def KY_circle(r):
    area_circle = math.pi * math.pow(r, 2)
    return area_circle

