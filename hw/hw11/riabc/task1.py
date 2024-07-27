def age_input(age):
    if age < 0:
        raise ValueError("Age cannot be a negative number")
    elif age % 2 == 0:
        return f"The age {age} is even"
    else:
        return f"The age {age} is odd"


def main():
    try:
        age = int(input("Please enter your age: "))
        message = age_input(age)
        print(message)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
