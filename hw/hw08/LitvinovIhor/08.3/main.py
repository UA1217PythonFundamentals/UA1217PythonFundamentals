from area import area_of_circle, area_of_rectangle, area_of_triangle

def calculation_of_area()->float:
    """The function prompts the user to input a shape and then based on the shape, 
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
    
if __name__ == "__main__":
    calculation_of_area()
