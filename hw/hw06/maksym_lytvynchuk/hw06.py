# homework 6.1

divisible_by_2 = []
divisible_by_3 = []
not_divisible_by_2_3 = []
for i in range(1, 11):
    if i % 2 == 0:
        divisible_by_2.append(i)
    elif i % 3 == 0:
        divisible_by_3.append(i)
    elif i % 2 != 0 and i % 3 != 0:
        not_divisible_by_2_3.append(i)
print("Divisible by 2:", divisible_by_2)
print("Divisible by 3:", divisible_by_3)
print("Not divisible by 2 and 3:", not_divisible_by_2_3)

# homework 6.2

login_true = "First"
while True:
    user_login = input("Enter the login :")
    if login_true == user_login:
        print("Congratulation")
        break
    else:
        print("Invalid login. Try again")


