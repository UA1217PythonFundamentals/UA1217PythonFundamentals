#Task1
integer_list = [1,2,3,4,5]
float_list = []
for item in integer_list:
    float_list.append(float(item))
print(float_list)    

#Task2
n = int(input("Введіть число n: "))

fibonacci_sequence = [0, 1]

for i in range(2, n):
    next_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    fibonacci_sequence.append(next_value)

print(fibonacci_sequence)
#Task3
n = int(input("Enter a number: " ))
factorial = 1
for i in range(1,n+1):
    factorial *= i
print(f"Factorial of a number {n} = {factorial}")   