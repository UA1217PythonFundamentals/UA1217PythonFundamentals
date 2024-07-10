import re

print("""Password requirements:
At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.""")
password = input("Enter password: ")

# password = "Enswod"


pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])[A-Za-z\d$#@]{6,16}$'

result = re.findall(pattern, password)

def passchecker(result):
    if password in result:
        return("Welcome")
    else:
        return("The password does not meet the requirements")


print(passchecker(result))