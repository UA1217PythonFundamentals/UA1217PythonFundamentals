import re

def validate_password():
    pattern = '^(?=.*[A-Z])(?=.*[a-z])(?=.*[$#@])(?=.*\\d)[A-Za-z0-9$#@]{6,16}$'
    entered_password = input("Specify password: ")
    starget = re.match(pattern, entered_password)
    if starget:
        print("Password is valid")

    else:
        print("Password is not valid")

validate_password()
