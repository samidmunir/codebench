import pygame as PG

from config_v2 import (
    SCREEN_HEIGHT,
    MENU_BACKGROUND_COLOR,
    MENU_WIDTH,
    MENU_HEIGHT,
    TEXT_COLOR,
)

from compass import Compass

class Button:
    def __init__(self, surface, text, x, y, width, height, font, action = None):
        self.surface = surface
        self.text = text
        self.rect = PG.Rect(x, y, width, height)
        self.color = (100, 100, 100)
        self.hover_color = (150, 150, 150)
        self.font = font
        self.action = action
        self.clicked = False
    
    def draw(self):
        mouse_pos = PG.mouse.get_pos()
        color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.color
        PG.draw.rect(self.surface, color, self.rect)

        text_surface = self.font.render(self.text, True, TEXT_COLOR)
        text_rect = text_surface.get_rect(center = self.rect.center)
        self.surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == PG.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            if self.action:
                self.action()

class InputField:
    def __init__(self, surface, x, y, width, height, font, placeholder = '0'):
        self.surface = surface
        self.rect = PG.Rect(x, y, width, height)
        self.font = font
        self.text = placeholder
        self.color = (200, 200, 200)
        self.active = False
    
    def draw(self):
        PG.draw.rect(self.surface, self.color, self.rect, 2)
        text_surface = self.font.render(self.text, True, TEXT_COLOR)
        self.surface.blit(text_surface, (self.rect.x + 10, self.rect.y + 5))

    def handle_event(self, event):
        if event.type == PG.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
        if event.type == PG.KEYDOWN and self.active:
            if event.key == PG.K_RETURN:
                self.active = False  # Deselect input field on Enter
            elif event.key == PG.K_BACKSPACE:
                self.text = self.text[:-1]  # Remove last character
            elif event.unicode.isdigit():  # Allow only numbers
                self.text += event.unicode

class Menu:
    def __init__(self, surface: PG.Surface, font: PG.font, aircrafts):
        self.surface = surface
        self.font = font
        self.aircrafts = aircrafts

        # Compass for selecting heading
        self.compass = Compass(surface, 750, SCREEN_HEIGHT - MENU_HEIGHT // 2)

        # Button to confirm heading
        self.buttons = [
            Button(surface, "Confirm HDG", 900, SCREEN_HEIGHT - MENU_HEIGHT + 25, 120, 30, font, self.apply_heading),
        ]

    def draw(self):
        """Draw the menu, buttons, and compass."""
        PG.draw.rect(self.surface, MENU_BACKGROUND_COLOR, (0, SCREEN_HEIGHT - MENU_HEIGHT, MENU_WIDTH, MENU_HEIGHT))

        for button in self.buttons:
            button.draw()

        self.compass.draw()

    def handle_event(self, event):
        """Handle input fields, buttons, and compass interactions."""
        # Check if a new aircraft was selected
        for aircraft in self.aircrafts:
            if aircraft.selected:
                self.compass.set_heading(aircraft.heading)  # Sync compass to aircraft heading
        
        self.compass.handle_event(event)

        for button in self.buttons:
            button.handle_event(event)

    def apply_heading(self):
        """Set the heading of the selected aircraft using the compass."""
        for aircraft in self.aircrafts:
            if aircraft.selected:
                aircraft.set_target(heading=int(self.compass.heading))
        for aircraft in self.aircrafts:
            if aircraft.selected:
                heading = int(self.heading_input.text) if self.heading_input.text else None
                speed = int(self.speed_input.text) if self.speed_input.text else None
                altitude = int(self.altitude_input.text) if self.altitude_input.text else None

                aircraft.set_target(heading if heading else int(self.compass.heading), speed, altitude)
                self.heading_input.text = ""
                self.speed_input.text = ""
                self.altitude_input.text = ""