# #Task 1: Create a list that contains elements of integer type,
# # then use the loop to change the type of these elements to a floating type.

int_list=list(range(8,21))
float_list=[float(i) for i in int_list]
print(f'Int list:{int_list}')
print(f'Float list:{float_list}')

# #Task 2: Print Fibonacci numbers up to the entered number n, using cycles. 

n = int(input("Enter the number:"))

def print_fibonacci(n):
    num1, num2 = 0, 1
    while num1 <=n:
        print(f"{num1}" )
        num1,num2= num2, num2+num1
print_fibonacci(n)

#Task 3: Write a script that will calculate the factorial of the entered number without using recursion

i = int(input("Enter the number: "))
result = 1
for n in range(1, i+1):
    result*=n
print(result)