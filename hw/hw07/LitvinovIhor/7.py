# task 1

def return_bigger(a, b):
    if a>b:
        return a
    else: 
        return b
    

# task 2

def area_of_rectangle(length, width):
    """
    Calculates the area of a rectangle.

    Parameters:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.

    Returns:
    float: The area of the rectangle.
    """
    return length * width

def area_of_triangle(base, height):
    """
    Calculates the area of a triangle.

    Parameters:
    base (float): The base of the triangle.
    height (float): The height of the triangle.

    Returns:
    float: The area of the triangle.
    """
    return 0.5 * base * height

def area_of_circle(radius):
    """
    Calculates the area of a circle.

    Parameters:
    radius (float): The radius of the circle.

    Returns:
    float: The area of the circle.
    """
    import math
    return math.pi * radius ** 2


def main():
    print("Choose the shape to calculate the area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        print(f"The area of the rectangle is {area_of_rectangle(length, width)}")
    elif choice == '2':
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        print(f"The area of the triangle is {area_of_triangle(base, height)}")
    elif choice == '3':
        radius = float(input("Enter the radius of the circle: "))
        print(f"The area of the circle is {area_of_circle(radius)}")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()

# task 3

def character_count(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

# Example usage:
input_string = "hello"
print(character_count(input_string))