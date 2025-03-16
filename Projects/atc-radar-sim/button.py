import pygame as PG

from config import (
    BUTTON_TEXT_COLOR,
)

class Button:
    def __init__(self, surface: PG.Surface, text: str, x: float, y: float, width: float, height: float, font: PG.font, action = None):
        self.surface = surface
        self.text = text
        self.rect = PG.Rect(x, y, width, height)
        self.color = (100, 100, 100)
        self.hover_color = (150, 150, 150)
        self.font = font
        self.action = action

    def draw(self):
        mouse_pos = PG.mouse.get_pos()
        color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.color
        PG.draw.rect(self.surface, color, self.rect)

        text_surface = self.font.render(self.text, True, BUTTON_TEXT_COLOR)
        text_rect = text_surface.get_rect(center = self.rect.center)
        self.surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == PG.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            if self.action:
                self.action()