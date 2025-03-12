import pygame as PG

from config import (
    SCREEN_HEIGHT,
    MENU_BACKGROUND_COLOR,
    MENU_WIDTH,
    MENU_HEIGHT,
    TEXT_COLOR,
)

class Menu:
    def __init__(self, surface: PG.Surface, font: PG.font):
        self.surface = surface
        self.font = font
    
    def draw(self):
        PG.draw.rect(self.surface, MENU_BACKGROUND_COLOR, (0, SCREEN_HEIGHT - MENU_HEIGHT, MENU_WIDTH, MENU_HEIGHT))

        text_surface = self.font.render('Controls: [A] Select Aircraft | [H] Change Heading | [S] Change Speed', True, TEXT_COLOR)
        self.surface.blit(text_surface, (20, SCREEN_HEIGHT - MENU_HEIGHT + 15))