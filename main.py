import pygame
import sys
from grid import Grid
from colors import Colors
from blocks import *


pygame.init()

screen = pygame.display.set_mode((301, 601))
pygame.display.set_caption("Pygame Tetris")

clock = pygame.time.Clock()

grid = Grid()
block = SBlock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # drawing
    screen.fill(Colors.dark_blue)
    grid.draw(screen)
    block.draw(screen)

    pygame.display.update()
    clock.tick(60)
