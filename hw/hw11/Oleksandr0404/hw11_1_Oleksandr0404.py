def process_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age % 2 == 0:
        return f"The age {age} is even."
    else:
        return f"The age {age} is odd."

def main():
    while True:
        user_input = input("Please enter your age: ")
        
        try:
            age = int(user_input)
            message = process_age(age)
            print(message)
            break
        except ValueError as e:
            print(e)
            continue

if __name__ == "__main__":
    main()
