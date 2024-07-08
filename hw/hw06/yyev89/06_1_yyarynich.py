# Task 1
given_list = list(range(1,11))

evens = [num for num in given_list if num % 2 == 0]
odds = [num for num in given_list if num % 3 == 0]
others = [num for num in given_list if num % 2 != 0 and num % 3 != 0]

print(f'Numbers which are divisible by 2: {evens}')
print(f'Numbers which are divisible by 3: {odds}')
print(f'Numbers which are not divisible by 2 and 3: {others}')


print("="*55)


# Task 2
while True: 
    login = input("Please enter your login (q to quit): ")
    if login == "First":
        print("Welcome.")
        break
    elif login == "q":
        break
    else:
        print("Incorrect input, please try again")