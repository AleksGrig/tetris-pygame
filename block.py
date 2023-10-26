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

    def get_position(self):
        return [(cell[0]+self.row_offset, cell[1]+self.column_offset) for cell in self.cells[self.rotation_state]]

    def move(self, offset):
        self.row_offset += offset[0]
        self.column_offset += offset[1]

    def draw(self, screen):
        for tile in self.get_position():
            tile_rect = pygame.Rect(
                tile[1]*self.cell_size+1, tile[0]*self.cell_size+1, self.cell_size-1, self.cell_size-1)
            pygame.draw.rect(screen, Colors.colors[self.id], tile_rect)
