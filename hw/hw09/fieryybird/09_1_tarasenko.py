import tkinter as tk
import random

# Initial variables
random_number = random.randint(1, 100)
attempts = 0


# Function with game logic
def check_number():
    global attempts, random_number
    try:
        user_number = int(number_entry.get())
        attempts += 1

        if user_number < 1 or user_number > 100:
            result = "Number out of range. Try again!\n"
        elif user_number < random_number:
            result = f"{user_number} is too low. Try again!\n"
        elif user_number > random_number:
            result = f"{user_number} is too high. Try again!\n"
        elif user_number == random_number:
            result = f"Congratulations! {user_number} is correct. You've guessed the number in {attempts} attempts.\n"
            random_number = random.randint(1, 100)  # Reset for a new game
            attempts = 0  

        if attempts >= 10 and user_number != random_number:
            result += f"You've used all 10 attempts. The number was {random_number}.\n"
            random_number = random.randint(1, 100)  
            attempts = 0  

    except ValueError:
        result = "Please enter a valid number between 1 and 100.\n"

    number_label.config(text=number_label.cget("text") + result)
    number_entry.delete(0, tk.END)


# Setup Tkinter GUI 
HEIGHT = 1500
WIDTH = 2000

root = tk.Tk()
root.title("Number Guessing Game Application")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

number_frame = tk.Frame(root, bg="deep sky blue", bd=5)
number_frame.place(relx=0.5, rely=0.3, relwidth=0.75, relheight=0.1, anchor='n')

number_entry = tk.Entry(number_frame, font=('Courier', 12))
number_entry.place(relx=0, rely=0, relwidth=0.65, relheight=1)

number_button = tk.Button(number_frame, 
                          text="Check Number", 
                          bg="gray", fg="white", 
                          font=('Courier', 8), 
                          command=check_number)
number_button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

number_result_frame = tk.Frame(root, bg='gold', bd=10)
number_result_frame.place(relx=0.5, rely=0.45, relwidth=0.75, relheight=0.4, anchor='n')

number_label = tk.Label(number_result_frame, font=('Courier', 14), anchor='nw', justify='left')
number_label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()