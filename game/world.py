import pygame
from bird import Bird

width = 900
height = 600
groundLine = 500

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE_SKY = (90, 150, 250)
BROWN_GROUND = (100, 40, 10)


# TEMPORARY
bird = Bird(100, 100, 20)


def draw_bird(surf):
    bird.draw(surf)


def move_bird():
    bird.move()


def calculate():
    move_bird()
