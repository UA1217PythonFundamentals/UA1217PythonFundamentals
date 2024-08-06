# f = open("lessons/lesson14/in.txt")

# # open("myFoo.boo", "w")


# text = f.read()
# print(f"{text=}")
# text1 = f.read()
# print(f"{text1=}")
# f.seek(0)
# text2 = f.read()
# print(f"{text2=}")
# f.seek(10)
# text3 = f.read()
# print(f"{text3=}")
# f = open("lessons/lesson14/in.txt")
# text4 = f.read()
# print(f"{text4=}")
# ff = f
# text4 = ff.read()
# print(f"{text4=}")

# f.seek(0)
# text5 = f.readline()
# print(text5)
# text5 = f.readlines()
# print(text5)
# # f.write("text") #io.UnsupportedOperation: not writable

# f = open("lessons/lesson14/out.txt", "a+")

# print(f.read())
# f.seek(20)
# print(f.read())
# f.seek(0)
# f.write("<AAA>")

# f.close()

# with open("lessons/lesson14/out.txt", "a+") as file:
#     from datetime import datetime
#     date = datetime.now()
#     file.write(f"{str(date)}\n")

# file.write("TEXT")
# print(file)

# try:
#     file = open("lessons/lesson14/out.txt", "a+")
#     from datetime import datetime
#     date = datetime.now()
#     file.write(f"{str(date)}\n")
# finally:
#     file.close()

# with open("lessons/lesson14/out.txt", "a+") as file1:
#     with open("lessons/lesson14/out.txt", "a+") as file2:
#         with open("lessons/lesson14/out.txt", "a+") as file3:
#             from datetime import datetime
#             date = datetime.now()
#             file1.write(f"{str(date)}\n")

with (open("lessons/lesson14/out.txt", "a+") as file1,
         open("lessons/lesson14/out.txt", "a+") as file2,
           open("lessons/lesson14/out.txt", "a+") as file3):
            from datetime import datetime
            date = datetime.now()
            file1.write(f"{str(date)}\n")