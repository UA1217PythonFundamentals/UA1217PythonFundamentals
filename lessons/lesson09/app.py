import pygame

pygame.init()

WIDTH = 1200
HEIGHT = 800

gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)
# Loop until the user clicks the close button.

done = False
# Used to manage how fast the screen updates
FPS = 60

clock = pygame.time.Clock()

POINTS = []
tank = [20, 20, 20, 20]
pixel = None
KEYDOWNS = set()


font = pygame.font.SysFont('Calibri', 12, True, False)
tank_icon = pygame.image.load("lessons\\lesson09\\tank.png")

# -------- Main Program Loop -----------
while not done:
    # print("start fps")
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        # print(event)
        data = event.dict
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        # --- Game logic should go here
        # --- Drawing code should go here
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.

        elif event.type == pygame.KEYDOWN:
            data = event.dict
            KEYDOWNS.add(data["key"])
            if 32 in KEYDOWNS:
                pixel = [tank[0] +260, tank[1]+76, 20, 10]
            # if data["key"] == 1073741906:
            #     tank[1] -= 5
            # elif data["key"] == 1073741903:
            #     tank[0] += 5
            # elif data["key"] == 1073741905:
            #     tank[1] += 5
            # elif data["key"] == 1073741904:
            #     tank[0] -= 5
            print(event)
        elif event.type == pygame.KEYUP:
            KEYDOWNS.remove(data["key"])
        elif event.type == pygame.MOUSEBUTTONUP:
            print(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            data = event.dict
            print(data)
            if data["button"] == 1:
                print(f"add {data["pos"]}")
                POINTS.append(data["pos"])
            elif data["button"] == 3:
                if POINTS:
                    tail = POINTS.pop()
                    print(f"remove {tail}")
            print(POINTS)
    gameDisplay.fill(WHITE)



    if 1073741906 in KEYDOWNS and tank[1] > 5:
        tank[1] -= 5
    if 1073741903 in KEYDOWNS and tank[0] < WIDTH -25:
        tank[0] += 5
    if 1073741905 in KEYDOWNS and tank[1] < HEIGHT -25:
        tank[1] += 5
    if 1073741904 in KEYDOWNS and tank[0] > 5:
        tank[0] -= 5


    text = font.render(f"[{tank[0]}, {tank[1]}]",True, (0,0,0))
    gameDisplay.blit(text, [tank[0], tank[1]-15])
    gameDisplay.blit(tank_icon, [tank[0], tank[1]])


    if len(POINTS) > 1:
        pygame.draw.polygon(gameDisplay, (0, 255, 0), POINTS, width=1)

        
    
    
    pygame.draw.rect(gameDisplay, (255, 0, 0), pygame.Rect(*tank), width=0)
    if pixel:
        pygame.draw.rect(gameDisplay, (255, 0, 0), pygame.Rect(*pixel), width=0)
        pixel[0] += 5

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.update()



    # --- Limit to 60 frames per second
    clock.tick(FPS)
    # print("end fps")

print("end game")