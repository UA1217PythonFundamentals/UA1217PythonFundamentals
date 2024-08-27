# Task 1
for i in list(range(99)):
    i = float(i)
    print(i)

# Task 2 The Fibonacci sequence can be defined as:F(n) = F(n-1) + F(n-2)
# При вивченні Java свого часу, мене це завдання зламало( відверто погуглила

n = 10
num1 = 0
num2 = 1
next_number = num2  
count = 1
 
while count <= n:
    print(next_number, end=" ")
    count += 1
    num1, num2 = num2, next_number
    next_number = num1 + num2
print()

