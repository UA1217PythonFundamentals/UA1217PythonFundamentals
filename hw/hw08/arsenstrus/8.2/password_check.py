import re
check=True
def password_check(password):
    global check
    if len(password)<6:
        print("Your password should have minimum 6 characters.")
        check = False
    if len(password) > 16:
        print("Your password`s length should be up to 16 characters")
        check=False
    if not re.search(r"[a-z]", password):
        print("Your password must contain at least 1 letter between [a-z]")
        check=False
    if not re.search(r"[A-Z]", password):
        print("Your password must contain at least 1 letter between [A-Z]")
        check=False
    if not re.search(r"[$#@]", password):
        print("Your password must contain at least 1 character from [$#@]")
        check=False
    if check == False:
        print("Password is incorrect, try again")
    else:
        print("Password is correct!")