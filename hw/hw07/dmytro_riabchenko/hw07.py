#Task1
def largest_number(num1, num2):
    """
    Returns the largest of two numbers.
    Args:
    num1: first number
    num2: second number
    Returns:
    int or float: The largest number between num1 and num2.
    """
    if num1 == num2:
        return("The numbers are equal")
    else:
        return max(num1, num2)
print(largest_number(5, 8))
print(largest_number(2, 2))
print(largest_number(4.5, 6.3))
print(largest_number(-3, -8))


#Task2
import math

def rectangle_area(length, width):
    """
    calculates the area of the rectangle
    """
    return length * width

def triangle_area(base, height):
    """
    calculates the area of the triangle
    """
    return 0.5 * base * height

def circle_area(radius):
    """
    calculates the area of the circle
    """   
    return math.pi * radius ** 2


print("Choose a shape to calculate its area:")
print("1. Rectangle")
print("2. Triangle")
print("3. Circle")
    
choice = input("Enter the number corresponding to the shape: ")

if choice == '1':
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = rectangle_area(length, width)
    print(f"The area of the rectangle is: {area}")
elif choice == '2':
    base = float(input("Enter the base length of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = triangle_area(base, height)
    print(f"The area of the triangle is: {area}")
elif choice == '3':
    radius = float(input("Enter the radius of the circle: "))
    area = circle_area(radius)
    print(f"The area of the circle is: {area:.2f}")
else:
    print("Invalid choice. Please enter 1, 2, or 3.")


#Task3
def calculate_characters():
    char_count = {}
    input_string = input("Enter the string: ")
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    print(f"Input: '{input_string}'")
    print("Output:", char_count)

calculate_characters()