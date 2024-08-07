import random

number = random.randint(1, 100)
attempts = 0
while True:
    if attempts==10:
        print("You loose because you run out of attempts.")
        break
    guess=int(input("Try to guess a number between 1 and 100: "))
    if guess==number:
        print(f"Congratulations, you win a game only after using {attempts+1} attempts")
        break
    else:
        attempts=attempts+1
        print(f"Wrong guess, try again .You have {10-attempts} more attempts")
    if guess<number:
        print("Number should be greater")
    else:
        print("Number should be lesser")