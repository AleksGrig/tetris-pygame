import pygame
import sys
from colors import Colors
from game import Game


pygame.init()

screen = pygame.display.set_mode((301, 601))
pygame.display.set_caption("Pygame Tetris")

clock = pygame.time.Clock()

game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.move((0, -1))
            elif event.key == pygame.K_RIGHT:
                game.move((0, 1))
            elif event.key == pygame.K_DOWN:
                game.move((1, 0))

    # drawing
    screen.fill(Colors.dark_blue)
    game.draw(screen)

    pygame.display.update()
    clock.tick(60)
