import re

def password_validation(password: str) -> bool:
    '''Checks for validity of provided password. Validation:
    - minimum length 6 symbols, maximum 16
    - at least 1 lowercase letter and 1 uppercase
    - at least 1 number 0-9
    - at least 1 character among $, #, @
    '''
    if len(password) not in range(6,17):
        return False
    patterns = [r'[a-z]', r'[A-Z]', r'\d', r'[$#@]']
    for pattern in patterns:
        if not re.search(pattern, password):
            return False
    return True 


password = input('Enter password: ')
if password_validation(password):
    print('Valid')
else:
    print('Not valid')