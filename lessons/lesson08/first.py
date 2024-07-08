# print(__name__)

# import math

# print(math.pi)

# import second

# print(second.TEXT)
# second.print_name()


# print(">>>1")
# import second as S
# print("<<<1")
# print(S.TEXT)
# S.print_name()
# print(">>>2")
# from second import TEXT, print_name
# print("<<<2")
# print(TEXT)
# print_name()
# print(dir())

# from second import *

# print(dir())
# import math

# # math.sin()
# # math.cos()

# from math import *

# print(dir())

# sin
# cos
# start = {str(name) for name in dir()}
# from second import *
# # from second import a, _a, __a
# end = {str(name) for name in dir()}
# # print(start)
# # print(end)
# print(end-start)

# from math import sin as si, cos, tan as t

# from second import ( 
#     print_name as pn1, 
#     print_name2 as pn2
# ) 

# pn2()

from second import print_name
print_name()

if __name__ == "__main__":
    print("first.py", __name__)