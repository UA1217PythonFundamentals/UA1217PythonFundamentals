from areas import triangle_area, rectangle_area, circle_area

def main():
    

    while True:
        enter_condition = input("What do u want calculate?: \n 1. Rectangle\n 2. Triangle\n 3. Circle\n 4. Exit\n")
        if enter_condition =="1" :
            a = float(input("Enter rectangle length: "))
            b = float(input("Enter rectangle width: "))
            print(f"The area of the rectangle is: {rectangle_area(a,b)}")

        elif enter_condition=="2":
            a = float(input("Enter base of triangle : "))
            h = float(input("Enter triangle height: "))
            print(f"The area of the triangle is: {triangle_area(a, h)}")

        elif enter_condition=="3":
            r = float(input("Enter radius of circle: "))
            print(f"The area of the circle is: {circle_area(r)}")
        elif enter_condition=="4":
            print("Exit")
            break
        else:
            print("Wrong number, try again: ")

if __name__ == "__main__":
    main()
