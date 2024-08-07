#Task1
even_divisible_by_2=list()
odd_divisible_by_3=list()
not_divisible_by_2_and_3=list()
for i in range(1,10):
    if i%2==0:
        even_divisible_by_2.append(i)
    elif i%3==0:
        if i%2!=0:
            odd_divisible_by_3.append(i)
    else:not_divisible_by_2_and_3.append(i)

print(f"Even numbers divisible by 2: {even_divisible_by_2}")
print(f"Odd numbers divisible by 3: {odd_divisible_by_3}")
print(f"Numbers that are not divisible by 2 and 3: {not_divisible_by_2_and_3}")

#Task2
attempts=int(3)
login="First"
while True:
    try_login=str(input("Enter your login:"))
    if try_login==login:
        print("Login successful")
        break
    else:
        print("Login failed")
        if attempts>1:
            attempts -= 1
        else:
            print("You run out of attempts ;(")
            break
