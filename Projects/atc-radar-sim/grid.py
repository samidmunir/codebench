import pygame as PG

from config import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    MENU_HEIGHT,
    GRID_COLOR,
    GRID_SPACING,
)

class Grid:
    def __init__(self, surface: PG.Surface):
        self.surface = surface

    def draw(self):
        for x in range(0, SCREEN_WIDTH, GRID_SPACING):
            PG.draw.line(self.surface, GRID_COLOR, (x, 0), (x, SCREEN_HEIGHT - MENU_HEIGHT))

        for y in range(0, SCREEN_HEIGHT - MENU_HEIGHT, GRID_SPACING):
            PG.draw.line(self.surface, GRID_COLOR, (0, y), (SCREEN_WIDTH, y))