from area_functions import area_of_rectangle, area_of_circle, area_of_triangle

def area_of_figure():
    while True:
        print("Choose a figure:")
        print("""Rectangle - 1
Triangle - 2
Circle - 3""")
        choise = input("Your choise: ")
        if choise == "1":
            width = float(input("Enter width: "))
            height = float(input("Enter height: "))
            print(f"Area of rectangle is: {area_of_rectangle(width, height)}")
            break
 
        elif choise == "2":
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            print(f"Area of triangle is: {area_of_triangle(base, height)}")
            break
            
        elif choise == "3":
            radius = float(input("Enter radius: "))
            print(f"Area of circle is: {area_of_circle(radius)}")
            break
        else:
            print("Error")
            break
        

area_of_figure()