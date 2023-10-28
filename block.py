import pygame
from colors import Colors


class Block:
    def __init__(self, id) -> None:
        self.id = id
        self.cells = []
        self.cell_size = 30
        self.rotation_state = 0
        self.row_offset = 0
        self.column_offset = 0
        self.move((0, 3))

    def get_positions(self, rotation=0):
        return [(cell[0]+self.row_offset, cell[1]+self.column_offset) for cell in self.cells[(self.rotation_state+rotation) % 4]]

    def move(self, offset):
        self.row_offset += offset[0]
        self.column_offset += offset[1]

    def rotate(self):
        self.rotation_state += 1
        self.rotation_state %= 4

    def draw(self, screen, offsetx=11, offsety=11):
        for tile in self.get_positions():
            tile_rect = pygame.Rect(
                tile[1]*self.cell_size+offsetx, tile[0]*self.cell_size+offsety, self.cell_size-1, self.cell_size-1)
            pygame.draw.rect(screen, Colors.colors[self.id], tile_rect)
