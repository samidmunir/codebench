import pygame as PG

from config import (
    SCREEN_HEIGHT,
    MENU_HEIGHT,
)

class Label:
    def __init__(self, surface: PG.Surface, font: PG.font, text_color, text: str, x: float, y: float):
        self.surface = surface
        self.font = font
        self.text_color = text_color
        self.text = text
        self.x = x
        self.y = y

    def draw(self):
        text_label = self.font.render(self.text, True, self.text_color)
        self.surface.blit(source = text_label, dest = (self.x, self.y))