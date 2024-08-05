import random

number_to_guess = random.randint(1, 100)
attempts = 0
max_attempts = 10

while attempts < max_attempts:
    try:
        user_guess = int(input("Enter your guess (1-100): "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        continue

    if user_guess < number_to_guess:
        print("Too low!")
    elif user_guess > number_to_guess:
        print("Too high!")
    else:
        print("Congratulations! You've guessed the number!")
        break

    attempts += 1

if attempts == max_attempts and user_guess != number_to_guess:
    print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
