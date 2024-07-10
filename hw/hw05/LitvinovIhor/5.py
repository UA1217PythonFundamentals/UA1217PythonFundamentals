# Task 1
integer_list = [1, 2, 3, 4, 5]
float_list = [float(num) for num in integer_list]
print("Original list of integers:", integer_list)
print("Converted list of floats:", float_list)

print("\n")

# Task 2
n = 100  # You can change this value or use input() to take it from the user
a, b = 0, 1
print("Fibonacci sequence up to", n, "is:")
while a <= n:
    print(a, end=" ")
    a, b = b, a + b

print("\n")

# Task 3
number = 5  # You can change this value or use input() to take it from the user
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print("Factorial of", number, "is:", factorial)