# 06.1 Task
# Task1.

def categorized_numbers(lst):
    """Even, odd, and not divisible by 2 and 3 numbers in range from 1 to 10"""
    even=[i for i in lst if i % 2 == 0]
    odd=[i for i in lst if i % 3 == 0]
    not_divisible=[i for i in lst if i % 2 != 0 and i % 3 != 0]
    (print(f"\nEven numbers of this range: {even},\nodd numbers of this range: {odd},\nnumbers not divisible by 2 and 3: {not_divisible} .\n"))
#usage:
lst=list(range(1, 11))
categorized_numbers(lst)


#Task2.

def greet():
    """Taking a input from the terminal and gives an error 
    until the right login is entered. Five attemps is given """
    attemps = 5
    while attemps >= 1:
        m=input("\nPlease, enter your login: ")
        if m == 'First':
            print(f"\nWelcome, {m} !\n")
            break
        else:
            print("\n  Error")
            attemps -= 1
    else:
        print("\n  Sorry, unsuccessful sign-in.\n")
       
greet()



