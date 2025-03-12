import pygame as PG

from config import (
    SCREEN_HEIGHT,
    MENU_BACKGROUND_COLOR,
    MENU_WIDTH,
    MENU_HEIGHT,
    TEXT_COLOR,
)

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
    def __init__(self, surface: PG.Surface, font: PG.font):
        self.surface = surface
        self.font = font

        # Button positions
        self.buttons = [
            Button(surface, "Confirm", 490, SCREEN_HEIGHT - MENU_HEIGHT + 25, 120, 30, font),
        ]

        self.heading_input = InputField(surface, 130, SCREEN_HEIGHT - MENU_HEIGHT + 25, 80, 30, font, "")
        self.speed_input = InputField(surface, 250, SCREEN_HEIGHT - MENU_HEIGHT + 25, 80, 30, font, "")
        self.altitude_input = InputField(surface, 370, SCREEN_HEIGHT - MENU_HEIGHT + 25, 80, 30, font, "")
    
    def draw(self):
        PG.draw.rect(self.surface, MENU_BACKGROUND_COLOR, (0, SCREEN_HEIGHT - MENU_HEIGHT, MENU_WIDTH, MENU_HEIGHT))

        # Draw buttons
        for button in self.buttons:
            button.draw()

        # Draw input fields
        self.heading_input.draw()
        self.speed_input.draw()
        self.altitude_input.draw()

        # Draw labels
        heading_label = self.font.render("Heading:", True, TEXT_COLOR)
        speed_label = self.font.render("Speed:", True, TEXT_COLOR)
        altitude_label = self.font.render("Altitude:", True, TEXT_COLOR)

        self.surface.blit(heading_label, (130, SCREEN_HEIGHT - MENU_HEIGHT + 10))
        self.surface.blit(speed_label, (250, SCREEN_HEIGHT - MENU_HEIGHT + 10))
        self.surface.blit(altitude_label, (370, SCREEN_HEIGHT - MENU_HEIGHT + 10))

    def handle_event(self, event):
        self.heading_input.handle_event(event)
        self.speed_input.handle_event(event)
        self.altitude_input.handle_event(event)

        for button in self.buttons:
            button.handle_event(event)