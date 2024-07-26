# Task1

even_div_by_2, odd_div_by_3, not_div_by_2_and_3 = [], [], []

for num in range(1, 11):
    if num % 2 == 0:
        even_div_by_2.append(num)
    elif num % 3 == 0:
        odd_div_by_3.append(num)
    else:
        not_div_by_2_and_3.append(num)

print("Even numbers that are divisible by 2:", even_div_by_2)
print("Odd numbers, which are divisible by 3:", odd_div_by_3)
print("Numbers that are not divisible by 2 and 3:", not_div_by_2_and_3)

# Task2
user_login = ""

while user_login != "First":
    
    user_login = input("Please enter your login: ")

    if user_login == "First":
        print("Welcome!")
    else:
        print("Error: Incorrect login. Please try again.")