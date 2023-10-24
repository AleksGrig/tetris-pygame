import pygame
import sys


dark_blue = (44, 44, 127)

pygame.init()

screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Pygame Tetris")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # drawing
    screen.fill(dark_blue)

    pygame.display.update()
    clock.tick(60)
