

# a = 1

# b = 2
# c = 2

# print(a == b)
# print(c == b)
# print(a != b)

# a = 1
# b = 2
# print(a > b and a<b)
# print(a > b or a<b)
# is_false = [False, 0, "", [], (), {}, None]
# print(10 and 20)
# print(10 and 20 and 0 and 30)
# print(10 or [] or "" or {})
# print(0 or [] or "" or {})
# print((0 or 10) and "foo" or {}) # 0 or "foo" or {} => "foo"

# a = [1,2,3]

# b = [1,2,3]
# c = a
# print(id(a), a)
# print(id(b), b)
# print(a == b)
# print(a is b)
# print(a is not b)
# print(a is c)

# class A():pass
# a = A()
# print(a)
# print(id(a))

# for i in range(1000):
#     c = i+1
#     print(i, id(i)== id(c-1))


# a = "aaaaaaaaaa"
# b = "aaaaaaaaaa"
# print(id(a)==id(b))
# a += "a"
# b += "a"
# print(id(a)==id(b))
# print(a == b)


# 5 in 10 #TypeError: argument of type 'int' is not iterable

# a = "abababsbdbfhxnjcvbsnvkjc"
# print("bdb" in a)
# print("bdb1" in a)
# a = [1,2, "test", None, (3,4 ,[5,6])]
# print(1 in a)
# print("test" in a)
# print(3 in a) #false
# print((3,4) in a)
# print([5,6] in a)
# for element in a:
#     if type(element) in (list, tuple):
#         if 3 in element:
#             print("3 in element", True)

# print(3 in a[4])
# print(a)
# print(a[4])
# print(a[4][2])
# print(a[4][2][1])
# a.append(a)
# print(a[5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5])
#score = int(input("score: "))
# 
# score = int(input("score: "))
# if score > 8:
#     print("\tYou have passed the exam")
#     print("\tUra!!!!")


# print("Exam was finished.")


# if score > 8:
#     print("\tYou have passed the exam")
#     print("\tUra!!!!")
# else:
#     print("\tYou have not passed the exam")
#     print("\t:(")    

# print("Exam was finished.")





# age = int(input("my age: "))
# name = input("my name: ")
# print(age, name)
# age = int(input("my age: "))
# if age < 12:
#     print('kid')
# elif age < 18:
#     print('teenager')
# elif age < 50:
#     print('adult')
# else:
#     print('you are not old')


# if age < 12:
#     print('kid')
# else:
#     if age < 18:
#         print('teenager')
#     else:
#         if age < 50:
#             print('adult')
#         else:
#             print('you are not old')

# go to l1
# weather = "raining"
# # text = ""
# b = None
# if weather == "raining":
#     text = "Open Your umbrella"
#     a = 1
# else:
#     text = "Wear your cap"
#     b = 1
# print(text)
# print(a)
# print(b)

# text = "Open Your umbrella" if weather == "raining" else "Wear your cap"
# # weather == "raining" ? "Open Your umbrella" : "Wear your cap"

# # module .py
# # def 
# # class

# status = int(input("status code: "))

# match status:
#     case 200 | 201 as code:
#         print(f"Ok {code}")
#     case 400:
#         print("Bad request")
#     case 401:
#         print("Unauthorized")
#     case 403:
#         print("Forbidden")
#     case 404:
#         print("Not found")
#     case _:
#         print("Other error")


# values = input("valeus: ")
# sep = input("sep: ")
# print(values)
# values = values.split(sep)

# match values:
#     case "load", link:
#         print("load", link)
#     case "save", link, filename:
#         print("save", link, filename)
#     case "save", link, *filenames:
#         print("save")
#         for filename in filenames:
#             print("\t", link, filename)
#     case _:
#         print("default", values)
# valeus: gdsbvkjdbsjhsbc h hjb hb jhb j 
# valeus: save google2.com f1.txt f2.txt f3.txt
# valeus: save google2.com f1.txt

# item = ['evening', "run"]
# item = ['a', "run"]
# item = ['a', "run",1]

# match item:
#     case ['evening', action]:
#         print(f'You almost finished the day! Now {action}!')
#     case [time, action]:
#         print(f'Good {time}! It is time to {action}!')
#     case _:
#         print('The time is invalid.')


# item = ['evening', "run"]
# item = ['evening', "work"]
# item = ['evening2', "work"]
# item = ['evening2', "work", 1]
# match item:
#     case ['evening', action] if action not in ['work', 'study']:
#         print(f'You almost finished the day! Now {action}!')
#     case ['evening', _]:
#         print('Come on, you deserve some rest!')
#     case [time, action]:
#         print(f'Good {time}! It is time to {action}!')
#     case _:
#         print('The time is invalid.')



# statuses = input("status code: ").split()
# if len(statuses) > 0:
#     print(statuses)
# else:
#     print("is empty")

# if statuses:
#     print(statuses)
# else:
#     print("is empty")

def string_int(str1):
string_int(str1) = int(input("Value:"))
if str1 > 0:
     print(str1)
else:
     print("NaN")
    