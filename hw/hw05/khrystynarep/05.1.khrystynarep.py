# 05.1 
# Task 1. Create a list that contains elements of integer type, then use 
# the loop to change the type of these elements to a floating type.
# (Hint: use the built-in float () function)

list_of_int = list(range(5, 16))
list_of_float = [float(i) for i in list_of_int]
print(f"List of integer type numbers: {list_of_int}, \nList of float type numbers: {list_of_float}")


# Task 2. Print Fibonacci numbers up to the entered number n, using cycles. 

n = int(input("\n\tEnter a number for Sequence of Fibonacci numbers: "))
def fibonacci(n):
    a, b = 0, 1
    while n >= a:
        print(a, end =", ")
        a, b = b, a + b
fibonacci(n)


# Task 3. Write a script that will calculate the factorial of the entered 
# number without using recursion.

n = int(input("\n\n\tEnter a number for factorial: "))
def factorial(n):
    result=1
    for i in range(1, n+1):
        result *= i
    print(f"{n}! =", result)
factorial(n)