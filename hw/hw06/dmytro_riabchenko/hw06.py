#1
even_divisible_by_two = set()
odd_divisible_by_three = set()
numbers_not_divisible_by_two_and_three = set()
for number in range(1, 10):
    if number %2 == 0:
        even_divisible_by_two.add(number)
    elif (number %2 != 0) and (number %3 == 0):
        odd_divisible_by_three.add(number)
    elif (number %2 != 0) and (number %3 != 0):
        numbers_not_divisible_by_two_and_three.add(number)


print(f"Even numbers that are divisible by 2: {sorted(even_divisible_by_two)}")
print(f"Odd numbers that are divisible by 3: {sorted(odd_divisible_by_three)}")
print(f"Numbers_not_divisible_by_two_and_three: {sorted(numbers_not_divisible_by_two_and_three)}")


#2
counter = 0
max_attempts = 2
while True:
    login = input("Enter your login: ")
    if login == "First":
        print("Welcome, user!")
        break
    else:
        print("Error: Incorrect login. Please try again.")
        counter += 1
        if counter > max_attempts:
            print("Too many unsuccessful attempts. Try restarting the process later.")
            break
            
