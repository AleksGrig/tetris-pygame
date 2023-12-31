import pygame
import random
from grid import Grid
from blocks import *


class Game:
    def __init__(self) -> None:
        self.grid = Grid()
        self.blocks = []
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0
        self.rotate_sound = pygame.mixer.Sound("sounds/rotate.ogg")
        self.clear_sound = pygame.mixer.Sound("sounds/clear.ogg")

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen)
        if self.next_block.id == 3:
            self.next_block.draw(screen, 255, 290)
        elif self.next_block.id == 4:
            self.next_block.draw(screen, 255, 280)
        else:
            self.next_block.draw(screen, 270, 270)

    def move(self, offset):
        if self.grid.no_collision(self.current_block, offset=offset):
            self.current_block.move(offset)
        else:
            if offset[0] > 0:
                self.lock_block()

    def rotate(self):
        if self.grid.no_collision(self.current_block, rotation=1):
            self.rotate_sound.play()
            self.current_block.rotate()

    def lock_block(self):
        positions = self.current_block.get_positions()
        for position in positions:
            self.grid.grid[position[0]][position[1]] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        rows_cleard = self.grid.clear_rows()
        if rows_cleard:
            self.clear_sound.play()
            self.update_score(lines_cleared=rows_cleard)
        if not self.grid.no_collision(self.current_block):
            self.game_over = True

    def reset(self):
        self.game_over = False
        self.grid.reset()
        self.blocks = []
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0

    def update_score(self, lines_cleared=0, move_down_points=0):
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared == 3:
            self.score += 500
        elif lines_cleared == 4:
            self.score += 1000
        self.score += move_down_points

    def get_random_block(self):
        if not self.blocks:
            self.blocks = [IBlock(), JBlock(), LBlock(),
                           OBlock(), TBlock(), SBlock(), ZBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
