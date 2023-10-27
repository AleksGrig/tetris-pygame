import pygame
from colors import Colors


class Grid:
    def __init__(self) -> None:
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for i in range(self.num_cols)]
                     for j in range(self.num_rows)]

    def no_collision(self, block, offset=(0, 0), rotation=0):
        positions = block.get_positions(rotation=rotation)
        for position in positions:
            row = position[0]+offset[0]
            column = position[1]+offset[1]
            if ((row < 0) or (row >= self.num_rows) or
                (column < 0) or (column >= self.num_cols) or
                    self.grid[row][column]):
                return False
        return True

    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(
                    column*self.cell_size+1, row*self.cell_size+1, self.cell_size-1, self.cell_size-1)
                pygame.draw.rect(screen, Colors.colors[cell_value], cell_rect)
