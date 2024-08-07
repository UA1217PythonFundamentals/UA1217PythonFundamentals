#Task1
List_Int=[4,5,7,9,3,5,1,6]
List_Float=[]
for element in List_Int:
    element=float(element)
    List_Float.append(element)

List_Int = List_Float
print(List_Int)
#Task2
n=int(input("Enter the number:"))
if n<=0:
    print(n)
elif n==1:
    print(n)
elif n>1:
    x=0
    y=1

    while x<=n:
        print(x)
        x,y=y,x+y
#Task3
n=int(input("Enter the number:"))
if n==0:
    print("1")
else:
    i=1
    result=1
    while i<=n:
        result*=i
        i+=1
    print(result)