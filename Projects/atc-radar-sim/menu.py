import pygame as PG

from config import (
    SCREEN_HEIGHT,
    MENU_WIDTH,
    MENU_HEIGHT,
    MENU_BACKGROUND_COLOR,
    MENU_TEXT_COLOR,
)

from button import Button
from input_field import Input
from label import Label

class Menu:
    def __init__(self, surface: PG.Surface, font: PG.font):
        self.surface = surface
        self.font = font
        
        self.buttons = [
            Button(surface = surface, text = 'Confirm', x = 480.0, y = SCREEN_HEIGHT - MENU_HEIGHT + 25.0, width = 120.0, height = 30.0, font = font, action = None)
        ]

        self.inputs = [
            Input(surface = surface, font = font, x = 120.0, y = SCREEN_HEIGHT - MENU_HEIGHT + 25.0, width = 80.0, height = 30.0,  placeholder = '000'),
            Input(surface = surface, font = font, x = 240.0, y = SCREEN_HEIGHT - MENU_HEIGHT + 25.0, width = 80.0, height = 30.0,  placeholder = '000'),
            Input(surface = surface, font = font, x = 360.0, y = SCREEN_HEIGHT - MENU_HEIGHT + 25.0, width = 80.0, height = 30.0,  placeholder = '000'),
        ]

        self.labels = [
            Label(surface = surface, font = font, text_color = MENU_TEXT_COLOR, text = 'Heading:', x = 120, y = SCREEN_HEIGHT - MENU_HEIGHT + 10.0),
            Label(surface = surface, font = font, text_color = MENU_TEXT_COLOR, text = 'Speed:', x = 240, y = SCREEN_HEIGHT - MENU_HEIGHT + 10.0),
            Label(surface = surface, font = font, text_color = MENU_TEXT_COLOR, text = 'Altitude:', x = 360, y = SCREEN_HEIGHT - MENU_HEIGHT + 10.0),
        ]

    def draw(self):
        PG.draw.rect(self.surface, MENU_BACKGROUND_COLOR, (0, SCREEN_HEIGHT - MENU_HEIGHT, MENU_WIDTH, MENU_HEIGHT))

        for button in self.buttons:
            button.draw()

        for input_field in self.inputs:
            input_field.draw()

        for label in self.labels:
            label.draw()

    def handle_event(self, event):
        self.inputs[0].handle_event(event)
        self.inputs[1].handle_event(event)
        self.inputs[2].handle_event(event)

        for button in self.buttons:
            button.handle_event(event)