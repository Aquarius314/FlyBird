import pygame
import world

print("GAME IS ON")
pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((world.width, world.height))


def display_screen():
    pygame.display.update()
    clock.tick(60)
    screen.fill(world.BLUE_SKY)    # BACKGROUND
    pygame.draw.rect(screen, world.BROWN_GROUND, \
                     pygame.Rect(0, world.groundLine, world.width, world.height-world.groundLine))
    world.draw_bird(screen)
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
    world.calculate()
    # render
    display_screen()

pygame.quit()
