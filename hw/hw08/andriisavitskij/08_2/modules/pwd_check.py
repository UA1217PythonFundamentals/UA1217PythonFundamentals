import re
test = True
def password_check(password):
    global test
    if not re.search(r"[a-z]", password):
        print("You password should have at least one small letter.")
        test=False
    
    if not re.search(r"[A-Z]", password):
        print("You password should have at least one big letter.")
        test=False
    
    if not re.search(r'[0-9]', password):
        print("Your password should have at least one number.")
        test=False

    if not re.search(r"[$#@]", password):
        print("Your password should have at least one symbol.")
        test=False
    
    if len(password) < 6:
        print("Your password should have minimum 6 characters.")
        test=False
    
    if len(password) > 16:
        print("Your password`s length should be up to 16 characters")
    
    if test == False:
        print("try again.")
    else:
        print("nice one!")
