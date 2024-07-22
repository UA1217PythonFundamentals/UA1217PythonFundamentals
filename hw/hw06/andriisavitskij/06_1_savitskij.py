# #Task 1: In the range from 1 to 10 determine even numbers, odd ones and numbers that are not divisible by 2 and 3.
l = list(range(1,11))
even_numbers=[]
odd_numbers=[]
non_divisible=[]
for i in l:
    if i % 2 == 0:
        even_numbers.append(i)
    
for i in l:
    if i % 2 != 0 and i % 3 != 0:
        non_divisible.append(i)

for i in l:
    if i % 3 == 0:
        odd_numbers.append(i)

print(f"Even numbers,divisible by 2: {even_numbers}")
print(f"Odd numbers,divisible by 3: {odd_numbers}")
print(f"Numbers, not divisible by 2 and 3: {non_divisible}")

#Task 2: Login check

correct="First"
while True:
    login=input("Enter your login:")
    if login == correct:
        break
    else:
        print("Wrong login. Try again.")