#Task 1-st
#Create a list that contains elements of integer type
integer_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
size = len(integer_list)
#Convert integer type into float:
for i in range(size):
    integer_list[i] = float(integer_list[i])

print(integer_list)


#Task 2. Print Fibonacci numbers up to the entered number n, using cycles.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610
entered_value = int(input("Enter a number: "))
if entered_value >= 1:
    print("0", end=' ')
if entered_value >= 2:
    print("1", end=' ')
    a = 0
    b = 1
    for x in range(2, entered_value):
        b = a + b
        a = b
        print(b, end=' ')



#Task3.  Write a script that will calculate the factorial of the entered
#number without using recursion.
entered_value1 = int(input("Enter a number to be calculated: "))
factorial = 1
for i in range(1, entered_value1 + 1):
    factorial *= i
print(f"{factorial} is the factorial of {entered_value1} ")