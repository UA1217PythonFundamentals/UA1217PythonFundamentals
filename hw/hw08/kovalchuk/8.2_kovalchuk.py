import re

def validate_password(password):

    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])[A-Za-z\d$#@]{6,16}$'
    
    if re.match(pattern, password):
        return True
    else:
        return False


password = input("Enter password: ")


if validate_password(password):
    print("Valid Password")
else:
    print("Not a Valid Password")
