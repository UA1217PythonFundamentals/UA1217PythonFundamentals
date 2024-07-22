import pygame
import random
import sys

pygame.init()

FPS = 30
gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption(' Guess Game')

clock = pygame.time.Clock()

first = 1
last = 100
attempts = 10
number_for_g = random.randint(first, last)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize font
pygame.font.init()
font = pygame.font.Font(None, 36)

def draw_text(text, x, y, color=BLACK):
    text_surface = font.render(text, True, color)
    gameDisplay.blit(text_surface, (x, y))

def main():
    global attempts, number_for_g


    draw_text(f"Guess the number! You have {attempts} attempts.", 50, 50, GREEN)
    gameDisplay.fill(WHITE)

    pygame.display.update()

    for i in range(attempts):
        m = game()
        if m == number_for_g:
            draw_text(f"You are so lucky! You guessed the number {number_for_g} in {10-(attempts - i)} attempt(s).", 50, 100, GREEN)
            pygame.display.update()
            break
        elif m < number_for_g:
            draw_text("You need to try one more time. Try a higher number!", 50, 100, RED)
            pygame.display.update()
        elif m > number_for_g:
            draw_text("You are so close. Try a lower number!", 50, 100, BLUE)
            pygame.display.update()
    
        pygame.time.delay(1000)  # Delay for 1 second before clearing the screen

        # Clear the screen for the next attempt
        gameDisplay.fill(WHITE)
        pygame.display.update()

    else:
        draw_text(f"Game over... :( Number was {number_for_g}", 50, 100, RED)
        pygame.display.update()

    # Wait for 3 seconds before quitting
    pygame.time.delay(3000)

def game():
    input_number = ''
    while True:
        draw_text(f"Guess a number from {first} to {last}: {input_number}", 50, 50, BLACK)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    try:
                        num = int(input_number)
                        if first <= num <= last:
                            return num
                        else:
                            input_number = ''
                            draw_text(f"Please enter a number between {first} and {last}", 50, 150, RED)
                            pygame.display.update()
                    except ValueError:
                        input_number = ''
                        draw_text(f"Invalid input. Please enter a number between {first} and {last}", 50, 150, RED)
                        pygame.display.update()
                elif event.key == pygame.K_BACKSPACE:
                    input_number = input_number[:-1]
                elif event.unicode.isdigit():
                    input_number += event.unicode

        pygame.display.update()

if __name__ == "__main__":
    main()
    pygame.quit()
