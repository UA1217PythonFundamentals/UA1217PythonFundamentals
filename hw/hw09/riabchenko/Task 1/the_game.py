import random


def guesser_game():
    the_number = random.randint(1, 100)
    max_attempts = 10
    
    
    print("Guess the number between 1 and 100. You have 10 attempts.")
    
    
    for attempt in range(1, max_attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}/{max_attempts}: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue    
        if guess < the_number:
            print("Too low!")
        elif guess > the_number:
            print("Too high!")
        else:
            print(f"Congratulations! You have guessed the number {the_number} correctly!")
            break
    else:
        print(f"Sorry, you have used all {max_attempts} attempts. The number was {the_number}.")

        
guesser_game()
