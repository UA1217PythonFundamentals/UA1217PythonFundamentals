import random
instruction = "Please enter a number from 1 to 100. You have 10 attempts. After each attempt, you will get a hint."
random_number = random.randint(1, 100)
tries = 9

# print(f"Random number {random_number}")
print(instruction)

while tries >= 0:
    answer = int(input("Enter a number: "))
    if random_number > answer:
        print("Hint! Correct number is greater.")
        print(f"You have attempts left: {tries}")
        tries -= 1
    elif random_number < answer:
        print("Hint! Correct number is less.")
        print(f"You have attempts left: {tries}")
        tries -= 1
    elif random_number == answer:
        print("You are winner!")
        break

    if tries == -1:
        print(f"You are loser! Right answer is {random_number}")