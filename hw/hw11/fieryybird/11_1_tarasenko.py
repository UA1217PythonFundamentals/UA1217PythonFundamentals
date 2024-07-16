#  Task 11.1

class NegativeValueError(Exception):
    def __str__(self):
        return 'Negative values are not allowed.'


def check_age(age):
    return 'Age is even.' if age % 2 == 0 else 'Age is odd.'


while True:
    user_input = input("Enter your age: ")
    try:
        age = int(user_input)
        if age > 0:
            print(check_age(age))
            break
        else:
            raise NegativeValueError()
    except NegativeValueError as e:
        print(e)
    except ValueError:
        print('Incorrect data type. Provide a numeric value.')


# Task 11.2
 
def day_of_week(day_number):
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if not 1 <= day_number <= 7:
        raise IndexError()
    return week[day_number - 1]


while True:
    user_input = input("Enter the day of the week (1-7): ")
    try:
      day_number = int(user_input)
      print(day_of_week(day_number))
      break
    except IndexError: 
         print('Provide a number between 1 and 7.')
    except ValueError:
         print('Incorrect data type. Provide a numeric value.')