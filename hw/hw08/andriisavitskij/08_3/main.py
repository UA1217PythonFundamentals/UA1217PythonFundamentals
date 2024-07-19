from modules import *
option=int(input("Choose an option: \n1. Calculate the area of rectangle. \n2. Calculate the area of Triangle.\n3. Calculate the area of circle.\n"))
if option == 1:
    rectangle_calc()
elif option == 2: 
    triangle_calc()
elif option == 3:
    circle_calc()
else:
    print("Error, unknown choice. Exiting the program..")
   