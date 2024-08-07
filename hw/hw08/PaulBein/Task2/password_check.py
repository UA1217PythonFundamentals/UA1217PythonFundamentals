import re
msg = '''Password required:
- min 6 and max 17 characters;
- at least 1 letter from [a-z] and 1 letter from [A-Z];
- at least 1 number from [0-9];
- at least 1 symbol from [$#@].'''
print(msg)
pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@])"
result = 0
while result == 0:
    password = input('Create a password:')
    if len(password) < 6:
        print('Password is too short (min 6 characters)!')
    if len(password) > 17:
        print('Password is too long (max 17 characters)!')
    if re.search(r'[a-z]',password) == None:
        print('Password must include at least 1 letter from [a-z]!')
    if re.search(r'[A-Z]',password) == None:
        print('Password must include at least 1 letter from [A-Z]!')
    if re.search(r'[0-9]',password) == None:
        print('Password must include at least 1 number from [0-9]!')
    if re.search(r'[$#@]',password) == None:
        print('Password must include at least 1 symbol from [$#@]!')
    if re.match(pattern,password):
        print('Password is valid!')
        result = 1

