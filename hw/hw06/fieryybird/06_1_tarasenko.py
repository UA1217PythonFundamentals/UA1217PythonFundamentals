#  In the range from 1 to 10 determine: even numbers that are divisible by 2, odd numbers, which are divisible by 3, numbers that are not divisible by 2 and 3.

# even_numbers = [i for i in range(1,11) if i % 2 == 0]
# odd_numbers = [i for i in range(1,11) if i % 3 == 0 and i % 2 != 0]
# not_divisible_numbers = [i for i in range(1,11) if i % 2 != 0 and i % 3 != 0]

# print(f'Even numbers: {even_numbers}\n'
#       f'Odd numbers: {odd_numbers}\n'
#       f'Not divisible by 2 and 3: {not_divisible_numbers}')

# Write a scipt that check the login that the user enters. If the logint is "First", then greet the users. If the login is different, send an error massage.

allowed_logins = {'First'}

while True:
  user_login = input("Enter your login: \n")
  if user_login in allowed_logins:
    print(f'Hello, {user_login}.')
    break
  elif user_login not in allowed_logins: 
    print(f'Invalid login. Please try again.')

