# print("hi) #SyntaxError: unterminated string literal (detected at line 1)

# a = 10
# b = 0
# a/b #ZeroDivisionError: division by zero

# a = int(input("a: "))
# b = int(input("b: "))
# a/b #?ZeroDivisionError: division by zero

# a = input("a: ")
# b = input("b: ")

# if a.isnumeric():
#     a = int(a)
# else:
#     print("a is not number")

# if b.isnumeric():
#     b = int(b)
# else:
#     print("b is not number")

# if type(a) is int and type(b) is int:
#     print(a/b)
# else:
#     print("error")


# print("Start")
# try:
#     a = int(input("a: ")) #ValueError: invalid literal for int() with base 10:
#     b = int(input("b: ")) #ValueError: invalid literal for int() with base 10:
#     c = a/b #ZeroDivisionError: division by zero
#     print(c)
# except Exception as err:
#     print("error", type(err), err)

# print("End")


# Program to handle multiple errors with one except statement
# try:
#     a = int(input("Enter your number: "))
#     if a < 4:
#         b = a/(a-3) # throws ZeroDivisionError for a = 3
#     if a >= 4:
#         print("Value of b = ", b) # throws NameError
#         # note that braces () are necessary here for multiple exceptions

# except ValueError:
#     print("Value Error!")
# except NameError:
#     print("NameError!")
# except ZeroDivisionError:
#     print("ZeroDivisionError!")
# except ArithmeticError as err:
#     print("ArithmeticError", type(err), err)
# except :
#     print("Error!")
# else:
#     print(b)

# print("END")

# def sum(a, b): 
#     try:
#         c =  a * b
#     except:
#         print("error")
#     else:
#         return c
    
#     finally:
#         print("end try")
#         return "88"


# print('sum(1, 5)', sum(1, 5))
# print('sum(1, "5")', sum(1, "5"))
# print('sum("1", "5")', sum("1", "5"))


# def pars_str_to_int(text:str):
#     if text.isdecimal():
#         return int(text)
#     raise MemoryError("my error")
#     print("end")

# pars_str_to_int("gfsdj")


# class MyError(Exception):
#     pass

# def pars_str_to_int(text:str):
#     if text.isdecimal():
#         return int(text)
#     raise MyError("err")

# try:
#     pars_str_to_int("gfsdj")
# except MyError as err:
#     print(err)


from func.funks import fibo
from func.number import parse_to_int

fibo(-10)
fibo(10)
parse_to_int("sdfvds")
parse_to_int("15")
parse_to_int("19.99")