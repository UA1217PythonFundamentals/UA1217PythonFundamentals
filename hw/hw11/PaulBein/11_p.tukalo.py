#Task 1
def age(value):
    if value % 2 == 0:
        print("Age is even")
    else:
        print("Age is odd")

while True:
    try:
        value = int(input("Enter an age:"))
        if value > 0:
            age(value)
            break
        else:
            print("Age must be greater 0!")
    except:
        print("You must enter integer value!")

print("-"*20)

#Task 2
def day_of_week(day):
    week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    print(week[day - 1])
    

while True:
    try:
        day = int(input("Enter value of day of week:"))
        if day > 0 and day < 8:
            day_of_week(day)
            break
        else:
            print("Day must be between 1 and 7!")
    except:
        print("You must enter integer value!")