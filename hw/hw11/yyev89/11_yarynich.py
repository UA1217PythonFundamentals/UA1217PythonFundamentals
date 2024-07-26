# Task 1
def age_check(age: int) -> str:
    return 'Even' if age % 2 == 0 else 'Odd'

while True:
    try:
        age = int(input('Please enter your age: '))
        if age <= 0:
            raise ValueError('Must be greater than zero')
    except ValueError as err:
        print(f'Invalid input: {err}')
    else:
        print(age_check(age))
        break


# Task 2
def get_day_name(day_num: int) -> str:
    day_names = {
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday',
        7: 'Sunday'
    }
    return day_names.get(day_num)

while True: 
    try:
        day_num = int(input('Please enter the number of a day (1-7): '))
        if day_num not in range(1,8):
            raise ValueError('Must be 1-7')
    except ValueError as err:
        print(f'Invalid input: {err}')
    else:
        print(get_day_name(day_num))
        break