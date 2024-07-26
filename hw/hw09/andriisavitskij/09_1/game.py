import random

number = random.randint(1, 100)
tries = 0
while True:
    if tries == 10:
        print(f"You lose. You used {tries} attempts to guess, but you failed.")
        break
    choice = int(input("Enter your number:"))
    if choice == number:
        print(f"You won! You used {tries} attempts to guess the number.")
        break
    else:
        print("Please,try again:")
        tries = tries + 1
    if choice < number:
        print("The number should be greater.")
    else:
        print("The number should be less.")
