# Task 2. Write a Python program to check the validity of a password (input from users).

import re

def check_password(password):
    if len(password) < 6 or len(password) > 12:
        return False
    rules_for_v = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).{6,12}$"
    pattern = re.compile(rules_for_v)
    match = re.match(pattern, password)
    if match: return bool(match)

password = input("Please, enter a password: ").strip()

if check_password(password):
    print(f"Password '{password}' is valid.")
else:
    print(f"Password '{password}' is NOT valid.")
