import pygame
import sys
from colors import Colors
from game import Game


pygame.init()

screen = pygame.display.set_mode((301, 601))
pygame.display.set_caption("Pygame Tetris")

clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)
KEY_PRESSED = pygame.USEREVENT
pygame.time.set_timer(KEY_PRESSED, 500)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == GAME_UPDATE:
            game.move((1, 0))
        if event.type == KEY_PRESSED:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                game.move((0, -1))
            elif keys[pygame.K_RIGHT]:
                game.move((0, 1))
            elif keys[pygame.K_DOWN]:
                game.move((1, 0))
            elif keys[pygame.K_UP]:
                game.rotate()

    # drawing
    screen.fill(Colors.dark_blue)
    game.draw(screen)

    pygame.display.update()
    clock.tick(60)
