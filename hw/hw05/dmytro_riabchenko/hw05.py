#Task1
for element in list(range(1,10)):
    element = float(element)
    print(element)


#Task2
n = int(input("Enter the number: "))
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
       return 1
   
    a, b = 0, 1
    count = 2
    while count <= n:
        a, b = b, a + b
        count += 1
    return b
print(f"Fibonacci of {n} = {fibonacci(n)}")


#Task3
n = int(input("Enter a number: "))
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
print(f"{n}!={factorial(n)}")
