# Task 1

def largest_number(a, b):
    """Returns the largest number of two given numbers. """
    return a if a > b else b

# Task 2

import math
def area_of_rectangle(l, w):
    return l*w
def area_of_triangle(b, h):
    return (1/2)*b*h
def area_of_circle(r): 
    return round(math.pi*(r**2),2)
def calculation_of_area()->float:
    """ Calculates the area of a rectangle, triangle, or circle. 
    The function prompts the user to input a shape and then based on the shape, 
    prompts the user to enter the parameters."""
    shape = input("Please enter the shape ('rectangle', 'triangle', or 'circle.'): ").lower()
    if shape == 'rectangle':
        l = float(input("Enter the lenght: "))
        w = float(input("Enter the width: "))
        if l <= 0 or w <= 0:
            print("Error: The length and width must be positive values.")
            return None
        print(f"The area of {shape} = {area_of_rectangle(l,w)}")
    elif shape == 'triangle':
        b = float(input("Enter the base: "))
        h = float(input("Enter the height: "))
        if b <= 0 or h <= 0:
            print("Error: The base and height must be positive values.")
            return None
        print(f"The area of {shape} = {area_of_triangle(b, h)}")
    elif shape == 'circle':
        r = float(input("Enter the radius: "))
        if r <= 0:
            print("Error: The radius must be a positive value.")
            return None
        print(f"The area of {shape} = {area_of_circle(r)}")
    else:
        print("Invalid shape. Please enter 'rectangle', 'triangle', or 'circle.'")
        return None
calculation_of_area()

# Task 3

from collections import Counter
word=input("Word for counting letter: ")
number_of_letter=lambda word: dict(Counter(word))
"""Return a dictionary with the letter and its frequence of apperance in the given word."""
print(number_of_letter(word))
    