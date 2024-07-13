import random

def guess_number():

    random_number = random.randint(1,100)

    attempts = 10
    attempt = 0

    while attempt < attempts:
        guess = int(input("Guess number: "))
        attempt += 1

        if  guess < random_number:
            print("Try a bigger number: ")   
        elif guess > random_number:
            print("Try a smaller number: ")
        else:
            print("You Win")
            break
    else:
        print("Game over")

guess_number()
