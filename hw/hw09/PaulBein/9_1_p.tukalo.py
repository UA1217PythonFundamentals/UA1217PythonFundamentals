import random

number = random.randint(1, 100)
tries = 0
attemps = 10
while True:
    if tries == 10:
        print(f"You lose. You used 10 attempts to guess, but you failed.")
        break
    choice = int(input("Enter your number:"))
    print(f'You have {attemps - 1} attemps left.')
    attemps = attemps - 1
    if choice == number:
        print(f"You won! You used {tries+1} attempts to guess the number.")
        break
    else:
        tries = tries + 1
    if choice < number:
        print("Too low.")
    else:
        print("Too high.")