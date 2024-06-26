# Task1 Convertation list of integer type to float type
list = list(range(0,20,3))
print("Integer list: ",list)
for i,j in enumerate(list) :
    list[i] = float(j)
print("Float list: ",list)
print('-'*60)

# Task2 Print Fibonacci numbers up to the entered number n
fib_1 = 0
fib_2 = 1
i = 0
list = [0,1]
n = int(input("Enter n: "))
if n == 1:
    list.pop()
    print(list)
else:
    while i < n - 2:
        fib_sum = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 = fib_sum
        list.append(fib_sum)
        i += 1    
    print(list)
print('-'*60)

# Task3 Script that will calculate factorial without using recursion
n = int(input("Enter n: "))
factorial = 1
while n > 1:
    factorial *= n
    n -= 1
print(f'{n}! = {factorial}')