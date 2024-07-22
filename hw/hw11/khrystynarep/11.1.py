# Task 1.

class NotAge(Exception):
    pass

def your_age():
    age = int(input("Please, enter your age: "))       
    if age < 0:
        raise NotAge("Age must greater than 0")     
    try:   
        if age % 2 != 0 :
            return "your age is odd" 
        else:
            return "your age is even" 
    except ValueError:
        raise NotAge("Invalid input: please enter a valid integer age")
try:
    print(your_age())
except NotAge as e:
    print(f"Error: {e}")


# Task 2.

import datetime

def get_day_of_week():
    week=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    try:
        entered_number = int(input("Enter a number in range from 1 to 7 to get the day of week: "))
        if entered_number < 1 or entered_number > 7:
            raise ValueError("Please enter a number between 1 and 7")
        else:
            return week[entered_number-1]   
    except ValueError as err:
        return f"Error: {err}"
    
print(get_day_of_week())
