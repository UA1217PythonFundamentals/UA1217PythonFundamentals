#Task1 In the range from 1 to 10 determine
#• even numbers that are divisible by 2,
#• odd numbers, which are divisible by 3,
#• numbers that are not divisible by 2 and 3
even_div_by_2 = []
odd_div_by_3 = []
not_div_by_2_and_3 = []

for num in range(1, 10):
    if num % 2 == 0:
        even_div_by_2.append(num)
    elif num % 3 == 0:
        odd_div_by_3.append(num)
    else:
        not_div_by_2_and_3.append(num)

print("Even numbers that are divisible by 2:", even_div_by_2)
print("Odd numbers that are divisible by 3:", odd_div_by_3)
print("Numbers that are not divisible by 2 and 3:", not_div_by_2_and_3)

#Task 2
while True:
    login = input("Enter your login: ")
    if login == "First":
        print("Welcome, First!")
        break
    else:
        print("Error: Incorrect login. Please try again.")
        