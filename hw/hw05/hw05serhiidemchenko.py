
# task 5.1

l = []
for i in range(10):
    if type(i) is int:
        l.append(float(i))

print(l)

# task 5.2

num = int(input("Enter number: "))
list_fibo = []

def fibonacci(num):
    a, b = 0, 1
    while a <= num:
        # print(a, end=' ')
        list_fibo.append(a)
        # print(list_fibo)
        a, b = b, a + b
    return list_fibo

print(fibonacci(num))

# task 5.3

num = int(input("Enter number: "))

def factorial(num):
    if num == 0:
        return 1
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

print(f'Factorial of {num} is: {factorial(num)}')