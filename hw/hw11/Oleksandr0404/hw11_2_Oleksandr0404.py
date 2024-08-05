def get_day_of_week(number):
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    return days.get(number, "Invalid number. Please enter a number between 1 and 7.")

def main():
    while True:
        user_input = input("Enter a number (1-7) to get the corresponding day of the week: ")
        
        # Check if the input is a valid integer
        try:
            number = int(user_input)
            if 1 <= number <= 7:
                print(get_day_of_week(number))
                break
            else:
                print("Number out of range. Please enter a number between 1 and 7.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
