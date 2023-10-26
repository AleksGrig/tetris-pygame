import random
from grid import Grid
from blocks import *


class Game:
    def __init__(self) -> None:
        self.grid = Grid()
        self.blocks = []
        self.current_block = self.get_random_block()

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen)

    def move(self, offset):
        if self.grid.is_inside(self.current_block.get_positions(), offset):
            self.current_block.move(offset)

    def rotate(self):
        if self.grid.is_inside(self.current_block.get_positions_if_rotated(), (0, 0)):
            self.current_block.rotate()

    def get_random_block(self):
        if not self.blocks:
            self.blocks = [IBlock(), JBlock(), LBlock(),
                           OBlock(), TBlock(), SBlock(), ZBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
