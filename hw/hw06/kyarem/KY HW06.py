range_n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Looking for even numbers:
even_numbers = []
for i in range_n:
    if i % 2 == 0:
        even_numbers.append(i)
        print(i)
print("Even numbers that are divisible by 2:", even_numbers)

#Looking for odd numbers:
odd_numbers = []
for x in range_n:
    if x % 3 == 0 and x % 2 != 0:
        odd_numbers.append(x)
        print(x)
print("Odd numbers, which are divisible by 3:", odd_numbers)

#Looking for numbers not divisible by 2 and 3
not_divisible_numbers = []
for y in range_n:
    if y % 2 != 0 and y % 3 != 0:
        print(y)
        not_divisible_numbers.append(y)
print("Numbers that are not divisible by 2 and 3:", not_divisible_numbers)


#Elegant way:
even_numbers = [i for i in range_n if i % 2 == 0]
print("Even numbers that are divisible by 2:", even_numbers)
odd_numbers = [x for x in range_n if x % 3 == 0 and x % 2 != 0]
print("Odd numbers, which are divisible by 3:", odd_numbers)
not_divisible_numbers = [y for y in range_n if y % 2 != 0 and y % 3 != 0]
print("Numbers that are not divisible by 2 and 3:", not_divisible_numbers)


#Task 2
correct_login = "First"
attempt = 0
while True:
    enter_login = input("Login: ")
    #adding possibility to specify the Login field after each attempt
    attempt += 1
    #if Login field is valid, loop circle is ended.
    if enter_login == correct_login:
        print("Login is valid. Hello, First. How are doing today?")
        break
    else:
        print("Login is invalid. Try again.")
