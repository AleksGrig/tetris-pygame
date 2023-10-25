import pygame
from colors import Colors


class Block:
    def __init__(self, id) -> None:
        self.id = id
        self.cells = []
        self.cell_size = 30
        self.rotation_state = 0

    def draw(self, screen):
        for tile in self.cells[self.rotation_state]:
            tile_rect = pygame.Rect(
                tile[1]*self.cell_size+1, tile[0]*self.cell_size+1, self.cell_size-1, self.cell_size-1)
            pygame.draw.rect(screen, Colors.colors[self.id], tile_rect)
