import re

def check_pass(password: str):
    """
    Password requirements:
    - At least 1 letter between [a-z]
    - At least 1 letter between [A-Z]
    - At least 1 number between [0-9]
    - At least 1 character from [$#@]
    - Minimum length 6 characters
    - Maximum length 16 characters
    """
    if len(password) < 6 or len(password) > 16:
        print(f"Doesn't match the requirements. Please choose different password.")
        return(check_pass.__doc__)
    validation = [r'[a-z]', r'[A-Z]', r'\d', r'[$#@]']
    for pattern in validation:
        if not re.search(pattern, password):
            print(f"Doesn't match the requirements. Please choose different password.")
            return (check_pass.__doc__)
    return ("The password is valid")


password = input("Enter your password: ")
result = check_pass(password)
print(result)