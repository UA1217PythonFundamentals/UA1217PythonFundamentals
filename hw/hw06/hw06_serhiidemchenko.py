
#task 1

t = [i for i in range(10) if not i % 2]
print(t)

t = [i for i in range(10) if not i % 3 if i % 2]
print(t)

t = [i for i in range(10) if not i % 3 if i % 2]
print(t)

# task 2

login = input("Login: ")

d = {"login":login}
while True:
    if d["login"] == "First":
        print("Greed!")
        break
    else:
        print("Error. Try another login")
        break

