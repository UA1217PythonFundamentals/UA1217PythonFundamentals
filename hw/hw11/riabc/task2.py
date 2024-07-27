def number_of_the_day(number):
    days_of_week = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    if number in days_of_week:
        return days_of_week[number]
    else:
        return "Invalid number. Please enter a number between 1 and 7"


def main():
    try:
        number = int(input("Please enter a number: "))
        day = number_of_the_day(number)
        print(day)
    except ValueError:
        print("Error: Please enter a number")


if __name__ == "__main__":
    main()
