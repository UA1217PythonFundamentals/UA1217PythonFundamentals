# Task 9.1 Guessing number game
from random import randint

secret_num = randint(1, 100)
print('Secret number is chosen between 1 and 100, try to guess it in 10 attempts')

for guess_attempt in range(1, 11):
    print('Guess the number: ')
    try:
        guess = int(input())
    except ValueError:
        print('Please enter a numeric value')
        continue

    if guess < secret_num:
        print('Too low')
    elif guess > secret_num:
        print('Too high')
    else:
        break

if guess == secret_num:
    print(f'Good job, you guessed the number in {guess_attempt} tries')
else:
    print(f'Sorry, try one more time. Secret number was {secret_num}')