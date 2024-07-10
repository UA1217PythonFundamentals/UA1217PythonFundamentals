from re import search,match,compile

password = input('Enter your password, please: \n')

def validation(password):
  '''Password validation with error type checking.'''
  error_list = []
  if not (6 <= len(password) <= 16):
    error_list.append('length_error')
  if search(r'[a-z]', password) is None:
    error_list.append('lower_case_error')
  if search(r'[A-Z]', password) is None:
    error_list.append('upper_case_error')
  if search(r'[0-9]', password) is None:
    error_list.append('num_error')
  if search(r'[$#@]', password) is None:
    error_list.append('special_character_error')
  return(error_list)


def password_check(password):
  errors = validation(password)
  if not errors:
    return('Your password is valid. Welcome.')
  else: 
    return 'Invalid Password: ' + ', '.join(errors)


# Option 2. 
    
def simple_check(password):
    '''Simple password validation by one reg-exp pattern.'''
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])[A-Za-z\d$#@]{6,16}$'
    return 'Your password is valid. Welcome.' if match(pattern, password) else 'Invalid Password!'


print(password_check(password))



