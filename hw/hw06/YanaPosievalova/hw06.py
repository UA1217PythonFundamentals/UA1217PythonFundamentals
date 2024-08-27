#Task 1
even_number_2 = []
odd_number_3 = []
not_divisible = []
#n = int()
#l = range(1, 11)
for x in range(1, 11):
    if x % 2 == 0:
        even_number_2.append(x)
    elif x % 3 == 0:
        odd_number_3.append(x)
    elif x % 2 != 0 and x % 3 != 0:
        not_divisible.append(x)
print("Even numbers divisible by 2:", even_number_2)
print("Odd numbers divisible by 3:", odd_number_3)
print("Numbers not divisible by 2 and 3:", not_divisible)

#Task 2

user_name = "Text"
while True:
    user_name == input("Please, enter your user name:")
    if user_name == "First":
        print("Hello, user!")
        break
    else:
        #user_name != "First":
        print("Sorry, the user name is incorrect")

#user_name = input("Please, enter your user name:")

