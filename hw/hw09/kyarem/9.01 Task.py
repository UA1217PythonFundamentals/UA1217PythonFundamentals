import random
from random import randint
random_number = random.randint(0, 100)
def guess_the_number(random_number):
    max_attempts = 10
    for x in range(1, 11):
        entered_number = int(input("Guess the number: "))
        if entered_number < random_number:
            print("Your number is less than target number!")
        elif entered_number > random_number:
            print("Your number is higher than target number!")
        elif entered_number == random_number:
            print("Congratulations! You guessed the number!")
            return
    print("You have exceed max attempts!")

guess_the_number(random_number)