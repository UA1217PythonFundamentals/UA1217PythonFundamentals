# Task1. In the range from 1 to 10 determine
# 	even numbers that are divisible by 2,
# 	odd numbers, which are divisible by 3,
# 	numbers that are not divisible by 2 and 3.


even_numbers = []
odd_numbers = []
numbers_not_d_2_3 = []

for i in range(1, 10):
    if i % 2 == 0:
        even_numbers.append(i)
    elif i % 3 == 0:
        odd_numbers.append(i)
    elif i % 2 != 0 or i % 3 != 0:
        numbers_not_d_2_3.append(i)

print(f"Even numbers that are divisible by 2: {even_numbers}")
print(f"Odd numbers, which are divisible by 3: {odd_numbers}")
print(f"Numbers that are not divisible by 2 and 3: {numbers_not_d_2_3}")




# Task2. Write a script that checks the login that the user enters. 
# If the login is "First", then greet the users. If the login is different, 
# send an error message. (need to use loop while)

while True: 
    login = input("Enter login: ")
    if login == "First":
        print("Hello, Welcome")
        break
    else:
        print("Incorrect login")