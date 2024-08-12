import funtions
print("For what type of figure you want to calculate area: Rectangle, Triangle, Circle")
figure=input()
figure=figure.lower()
match figure:

   case "circle":
       R =float(input("Input radius of the circle:"))
       print(f"The area of figure:{funtions.area_of_circle(R)}")
   case "triangle":
       a=input("Input  side a length:")
       h=input("Input height:")
       print(f"The area of figure:{funtions.area_of_triangle(a,h)}")
   case "rectangle":
       a = input("Input  side a length:")
       b = input("Input  side b length:")
       print(f"The area of figure:{funtions.area_of_rectangle(a, b)}")
   case _:
       print("ERROR")