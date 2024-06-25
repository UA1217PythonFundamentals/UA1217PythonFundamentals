# Changes the type of list elements from integer to float using loop:
some_list = list(range(1,11)) 
print(some_list)
for index, value in enumerate(some_list):
    some_list[index] = float(value)
print(some_list)


# Prints Fibonacci numbers up to the entered number n:
def fibo_print(n):
    a, b = 0, 1
    counter = 0
    while counter < n:
        if counter == (n-1):
            print(a, end='')
        else:
            print(a, end=', ')
        a, b = b, a + b
        counter += 1
    print()

n = int(input("Please enter n (Fibonacci): "))
fibo_print(n)


# Calculates the factorial of the entered number n: 
def factorial(n):
    result = 1
    for i in range(n,0,-1):
        result *= i
    return result

n = int(input("Please enter n (factorial): "))
print(factorial(n))