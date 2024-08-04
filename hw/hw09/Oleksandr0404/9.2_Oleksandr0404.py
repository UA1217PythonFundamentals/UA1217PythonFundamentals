import pygame

FPS = 60

WIDTH_DISPLAY = 500
HEIGHT_DISPLAY = 500

RECTANGLE = [50, 50, 40, 60]  # [x, y, width, height]
DELTA_STEP = 5

WHITE_COLOR = (255, 255, 255)
RED_COLOR = (250, 0, 0)

pygame.init()

gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY), pygame.RESIZABLE)

pygame.display.set_caption("My first game")

run = True
clock = pygame.time.Clock()

while run:
    pygame.time.delay(100)
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and RECTANGLE[0] > 0:
        RECTANGLE[0] -= DELTA_STEP
    if keys[pygame.K_RIGHT] and RECTANGLE[0] < WIDTH_DISPLAY - RECTANGLE[2]:
        RECTANGLE[0] += DELTA_STEP
    if keys[pygame.K_UP] and RECTANGLE[1] > 0:
        RECTANGLE[1] -= DELTA_STEP
    if keys[pygame.K_DOWN] and RECTANGLE[1] < HEIGHT_DISPLAY - RECTANGLE[3]:
        RECTANGLE[1] += DELTA_STEP

    gameDisplay.fill(WHITE_COLOR) 

    pygame.draw.rect(gameDisplay, RED_COLOR, RECTANGLE)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()