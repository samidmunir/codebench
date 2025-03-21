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
    def __init__(self, surface: PG.Surface, font: PG.font, aircrafts):
        self.surface = surface
        self.font = font
        self.aircrafts = aircrafts
        self.active_input_index = None # track active input field
        
        self.buttons = [
            Button(surface = surface, text = 'Confirm', x = 480.0, y = SCREEN_HEIGHT - MENU_HEIGHT + 25.0, width = 120.0, height = 30.0, font = font, action = self.apply_commands)
        ]

        self.inputs = [
            Input(surface = surface, font = font, x = 120.0, y = SCREEN_HEIGHT - MENU_HEIGHT + 25.0, width = 80.0, height = 30.0,  placeholder = ''),
            Input(surface = surface, font = font, x = 240.0, y = SCREEN_HEIGHT - MENU_HEIGHT + 25.0, width = 80.0, height = 30.0,  placeholder = ''),
            Input(surface = surface, font = font, x = 360.0, y = SCREEN_HEIGHT - MENU_HEIGHT + 25.0, width = 80.0, height = 30.0,  placeholder = ''),
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
        """
        for input_field in self.inputs:
            input_field.handle_event(event)

        for button in self.buttons:
            button.handle_event(event)

        if event.type == PG.KEYDOWN and event.key == PG.K_RETURN:
            self.apply_commands()
        """
        if event.type == PG.KEYDOWN:
            if event.key == PG.K_TAB:
                self.switch_focus()
            elif event.key == PG.K_RETURN:
                self.apply_commands()
            else:
                # let the active input field handle input
                if self.active_input_index is not None:
                    self.inputs[self.active_input_index].handle_event(event)
        
        for button in self.buttons:
            button.handle_event(event)

    def switch_focus(self):
        if self.active_input_index is None:
            self.active_input_index = 0 # start at the first input
        else:
            self.active_input_index = (self.active_input_index + 1) % len(self.inputs) # cycle through inputs

        for i, input_field in enumerate(self.inputs):
            input_field.active = (i == self.active_input_index)

    def apply_commands(self):
        for AIRCRAFT in self.aircrafts:
            if AIRCRAFT.selected:
                heading = int(self.inputs[0].text) if self.inputs[0].text else None
                speed = int(self.inputs[1].text) if self.inputs[1].text else None
                altitude = int(self.inputs[2].text) if self.inputs[2].text else None
                AIRCRAFT.set_target(heading, speed, altitude)
                for input_field in self.inputs:
                    input_field.text = ''
                    input_field.active = False # deselect all fields
                self.active_input_index = None # reset active field
                AIRCRAFT.toggle_selection()

    def select_aircraft(self):
        self.active_input_index = 0

        for i, input_field in enumerate(self.inputs):
            input_field.active = (i == 0)

    def deselect_all_inputs(self):
        for input_field in self.inputs:
            input_field.text = ''
            input_field.active = False
        self.active_input_index = None