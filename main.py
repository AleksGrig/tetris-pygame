import pygame
import sys
from colors import Colors
from game import Game


pygame.init()

title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)

score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Pygame Tetris")

clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)
# KEY_PRESSED = pygame.USEREVENT
# pygame.time.set_timer(KEY_PRESSED, 1000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == GAME_UPDATE and not game.game_over:
            game.move((1, 0))
        if event.type == pygame.KEYDOWN:
            if game.game_over:
                game.reset()
            else:
                if event.key == pygame.K_LEFT:
                    game.move((0, -1))
                elif event.key == pygame.K_RIGHT:
                    game.move((0, 1))
                elif event.key == pygame.K_DOWN:
                    game.move((1, 0))
                elif event.key == pygame.K_UP:
                    game.rotate()
        # elif event.type == KEY_PRESSED:
        #     keys = pygame.key.get_pressed()
        #     if keys[pygame.K_LEFT]:
        #         game.move((0, -1))
        #     elif keys[pygame.K_RIGHT]:
        #         game.move((0, 1))
        #     elif keys[pygame.K_DOWN]:
        #         game.move((1, 0))
        #     # elif keys[pygame.K_UP]:
        #     #     game.rotate()

    # drawing
    screen.fill(Colors.dark_blue)

    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (375, 180, 50, 50))
    if game.game_over:
        screen.blit(game_over_surface, (320, 450, 50, 50))

    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)

    game.draw(screen)

    pygame.display.update()
    clock.tick(60)
