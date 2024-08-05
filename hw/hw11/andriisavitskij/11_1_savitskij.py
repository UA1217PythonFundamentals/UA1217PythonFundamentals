# #Task 1: Negative age exception 
# class WrongAge(Exception):
#     pass

# def age_checker(age):
#     return "Your age is even" if age % 2 == 0 else "Your age is odd"

# age = int(input("Enter your age: "))
# try:
#     if age > 0:
#         print(age_checker(age))
#     else:
#         raise WrongAge("Your age is wrong.")
# except WrongAge as e:
#     print("Your age is wrong.")
# except ValueError:
#     print("You should enter a number.")

#Task 2
def print_day(num):
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if not 1 <= num <= 7:
        raise IndexError()
    return week[num-1]

day = int(input("Enter the day of the week (numeric):"))
try:
    print(print_day(day))
except IndexError:
    print("You should enter a number between 1 and 7")
except ValueError:
    print("You should enter a number.")