#Homework 5.1

i = [23, 44, 67, 77, 91]
for element in i:
    if type(element) is int:
        j = float(element)
        print(j)


#Homework 5.2

f1 = 0
f2 = 1
n = int(input("Enter n: "))
while f1 <= n:
        print(f1, end=' ')
        f1, f2 = f2, f1 + f2



#Homework 5.3

n = int(input("Enter n: "))
j = 1
for i in range(1, n+1):
    j *= i
print(j, end=' ')