import pygame
from colors import Colors


class Grid:
    def __init__(self) -> None:
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for i in range(self.num_cols)]
                     for j in range(self.num_rows)]

    def reset(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column] = 0

    def is_row_full(self, row):
        for column in range(self.num_cols):
            if not self.grid[row][column]:
                return False
        return True

    def clear_row(self, row):
        for column in range(self.num_cols):
            self.grid[row][column] = 0

    def move_row_down(self, row, offset):
        for column in range(self.num_cols):
            self.grid[row+offset][column] = self.grid[row][column]
            self.grid[row][column] = 0

    def clear_rows(self):
        completed = 0
        for row in range(self.num_rows-1, 0, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed:
                self.move_row_down(row, completed)
        return completed

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
