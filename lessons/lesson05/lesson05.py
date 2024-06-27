# i = 0
# while i < 10:
#     print(i)
#     i += 1

# for i in range(10):
#     print(i)

# l = [1,2,3]
# while l:
#     print(l)
#     l.pop()

# start = 0
# finish = 10
# while start < finish:
#     print(start)
#     start += 1
# else:
#     print (f"The end. {start}")


# l = [11,22,33]
# for element in l:
#     print(element)
# else:
#     print ("The end.")

# start = 0
# finish = 10
# for element in range(start, finish):
#     print(element)
# else:
#     print (f"The end. {element}")


# for i in 10: pass #TypeError: 'int' object is not iterable

# for j in [10, 20, 30, 40, 50]:
#     print(j)
# else:
#     print(j, "- is the last")

# l = [10, 20, 30, 40, 50, [99]]    
# for j in l:
#     print(j, end=" => ")
#     if type(j) is int:
#         j +=100
#     if type(j) is list:
#         j.append(100)
#     print(j)


# print(l)

# l = [10, 20, 30, 40, 50, [99]]    
# for j in range(len(l)):
#     print(j, end=" => ")
#     if type(l[j]) is int:
#         l[j] +=100
#     if type(l[j]) is list:
#         l[j].append(100)
#     print(j)


# # print(l)

# print(list(range(3)))
# print(list(range(-3)))
# print(list(range(-3, 5)))
# print(list(range(-3, 5, 2)))

# l = [11,22,33]
# t = (11,22,33) 
# s = {11,22,33} 
# for e in s:
#     print(e)

# d = {"key1": 11,
#      "key2": 22,
#      "key3": 22}
# for k in d:
#     print(k, d[k])


# l = [1,2,"3",4,"5",6]
# sum = 0
# for i in l:
#     print(f"type element {i} is {type(i)}")
#     if type(i) is not int:
#         continue

#     print(f"{sum}+{i}=", end="")
#     sum += i
#     print(f"{sum}")
# else:
#     print("end. sum=", sum)




# l = [1,2,"3",4,"5",6]

# for i in l:
#     if type(i) is not int:
#         break
#     print(i)
# else:
#     print("end. ")
# # print("global")

# for i in range(10):
#     #sum
#     pass

# def f():
#     pass

# class A:
#     pass


# for i in range(2):
#     s = i

# print(s)


# for i in range(2):
#     for i in range(2):
#         s = i

# s = 1



n = int(input("N: "))
m = int(input("M: "))

for i in range(n):
    for j in range(m):
        print((i, j), end="\t")
    print()