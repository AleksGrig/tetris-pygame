import pygame
from colors import Colors


class Grid:
    def __init__(self) -> None:
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for i in range(self.num_cols)]
                     for j in range(self.num_rows)]

    def is_inside(self, block, offset):
        positions = block.get_position()
        for position in positions:
            if ((position[0]+offset[0] < 0) or
                (position[0]+offset[0] >= self.num_rows) or
                (position[1]+offset[1] < 0) or
                    (position[1]+offset[1] >= self.num_cols)):
                return False
        return True

    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(
                    column*self.cell_size+1, row*self.cell_size+1, self.cell_size-1, self.cell_size-1)
                pygame.draw.rect(screen, Colors.colors[cell_value], cell_rect)
