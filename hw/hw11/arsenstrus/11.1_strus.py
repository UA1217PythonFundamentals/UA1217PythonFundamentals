#Task1
class NegativeAge(Exception):
    pass
def Odd_or_even_age():
    age=int(input("Input your age: "))
    try:
        if age<0:
            raise NegativeAge("This is not an age")
        else:
            if age%2==0:
                print("Your age is even")
            else:
                print("Your age is odd")
    except NegativeAge as e:
        print(e)

Odd_or_even_age()

#Task2:
class IncorrectData(Exception):
    pass
def DayOfTheWeek(day_number):

    if day_number==1:
        return "Monday"
    elif day_number==2:
        return "Tuesday"
    elif day_number==3:
        return "Wednesday"
    elif day_number==4:
        return "Thursday"
    elif day_number==5:
        return "Friday"
    elif day_number==6:
        return "Saturday"
    elif day_number==7:
        return "Sunday"
    else:
        raise IncorrectData("Incorrect input")
try:
    day_number = input("Input number: ")
    DayOfTheWeek(day_number)

except IncorrectData as e:
    print(e)