import pygame as PG

from config import (
    INPUT_TEXT_COLOR,
)

class Input:
    def __init__(self, surface: PG.Surface, font: PG.font, x: float, y: float, width: float, height: float, placeholder: str):
        self.surface = surface
        self.rect = PG.Rect(x, y, width, height)
        self.font = font
        self.text = placeholder
        self.color = (200, 200, 200)
        self.active = False
    
    def draw(self):
        PG.draw.rect(self.surface, self.color, self.rect, 2)
        text_surface = self.font.render(self.text, True, INPUT_TEXT_COLOR)
        self.surface.blit(text_surface, (self.rect.x + 10, self.rect.y + 7))

    def handle_event(self, event):
        if event.type == PG.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
        if event.type == PG.KEYDOWN and self.active:
            if event.key == PG.K_RETURN:
                self.active = False # deselect input field on enter
            elif event.key == PG.K_BACKSPACE:
                self.text = self.text[:-1] # remove last character
            elif event.unicode.isdigit(): # allow only numbers
                self.text += event.unicode