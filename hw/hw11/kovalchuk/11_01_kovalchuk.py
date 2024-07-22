# Task 1
def process_age(age):
    if age < 0:
        raise ValueError("Negative numbers")
    elif (age % 2) == 0:
        return "Even"
    else:
        return "Odd"
    


def main():
    try:
        age = int(input("Enter your age: "))
        result = process_age(age)
        print(f"Your age is {result}.")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()



# Task 2
def days(number):
    if number == 1:
        return "Monday"
    elif number == 2:
        return "Tuesday"
    elif number == 3:
        return "Wednesday"
    elif number == 4:
        return "Thursday"
    elif number == 5:
        return "Friday"
    elif number == 6:
        return "Saturday "
    elif number == 7:
        return "Sunday"
    else:
        raise ValueError("Number must be between 1 and 7.")

def main():
    try:
        user_input = input("Enter number: ")
        entered = int(user_input)
        result = days(entered)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()