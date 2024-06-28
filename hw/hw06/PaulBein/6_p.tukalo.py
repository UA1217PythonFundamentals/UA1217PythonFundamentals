# Task1 in the range from 1 to 10 determine
list1,list2,list3 = [],[],[]
for i in range(1,10):
    if i % 2 == 0:
        list1.append(i)
    if i % 2 != 0 and i % 3 == 0:
        list2.append(i)
    if i % 2 != 0 and i % 3 != 0:
        list3.append(i)
print("Numbers that are divisible by 2: ",list1)
print("Odd numbers that are divisible by 3: ",list2)
print("Numbers that are not divisible by 2 and 3: ",list3)
print("-"*55)

# Task2 script that checks the login that the user enters
user_login = input("Enter your login: ")
while user_login != "First":
    user_login = input("Wrong login, please, try again: ")
print("Authorization is successful :)")