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

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen)

    def move(self, offset):
        if self.grid.no_collision(self.current_block, offset=offset):
            self.current_block.move(offset)
        else:
            if offset[0] > 0:
                self.lock_block()

    def rotate(self):
        if self.grid.no_collision(self.current_block, rotation=1):
            self.current_block.rotate()

    def lock_block(self):
        positions = self.current_block.get_positions()
        for position in positions:
            self.grid.grid[position[0]][position[1]] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        rows_cleard = self.grid.clear_rows()
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
