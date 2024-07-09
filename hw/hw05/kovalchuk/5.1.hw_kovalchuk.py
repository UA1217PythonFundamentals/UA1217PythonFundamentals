# HOMEWORK

# Task1. Create a list that contains elements of integer type, then use the loop to change the type of these elements to a floating type. (Hint: use the built-in float() function).

for i in list(range(99)):
    i = float(i)
    print(i)



# # Task2. Print Fibonacci numbers up to the entered number n, using cycles. (Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.)

number = int(input("Enter number: "))

num1, num2 = 0, 1

while num1 <= number:
    print(num1, end=" ")
    num1, num2 = num2, num1+num2


# Task3. Write a script that will calculate the factorial of the entered number without using recursion. Example: 0!=1, 1!=1, 2!=2, 3!= 123=6, ....

n = int(input("Enter number to calculate the factorial: "))

factorial = 1

for i in range(1, n+1):
    factorial *= i
print(f"Factorial of the {n}: {factorial}")