import pygame

print("GAME IS ON")
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

clock = pygame.time.Clock()
screen = pygame.display.set_mode((900, 600))


def display_screen():
    pygame.display.update()
    clock.tick(60)
    screen.fill((0, 0, 0))    # BACKGROUND
    pygame.draw.circle(screen, RED, (100, 200), 40, 20)
    return


# MAIN LOOP
running = True
counter = 0
while running:
    # counter for autoclose
    counter += 1
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # autoclose
    if counter > 100:
        running = False
    # calculate here

    # render
    display_screen()

pygame.quit()
