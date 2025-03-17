import pygame as PG
import math as MATH
import random as RANDOM

from config import (
    MENU_TEXT_COLOR,
    RUNWAY_COLOR,
    AIRPORT_SIZE,
)

class Runway:
    """Represents a single runway with heading, length, and optional parallel designation."""
    def __init__(self, x, y, length, width, heading, parallel=""):
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self.heading = heading % 360  # Ensure heading is within 0-360
        self.parallel = parallel  # "L", "R", or "" for single runways
        self.label = f"{int(self.heading / 10):02d}{self.parallel}"  # Runway label

    def draw(self, surface):
        """Draw the runway with correct orientation."""
        rad = MATH.radians((self.heading - 90) % 360)  # Convert heading to radians
        
        # Calculate runway endpoints
        x1 = self.x - MATH.cos(rad) * (self.length / 2)
        y1 = self.y - MATH.sin(rad) * (self.length / 2)
        x2 = self.x + MATH.cos(rad) * (self.length / 2)
        y2 = self.y + MATH.sin(rad) * (self.length / 2)
        
        # Draw the runway
        PG.draw.line(surface, RUNWAY_COLOR, (x1, y1), (x2, y2), self.width)

        # Draw the runway label at one end
        font = PG.font.Font(None, 18)
        label_surface = font.render(self.label, True, MENU_TEXT_COLOR)
        surface.blit(label_surface, (x1 + 5, y1 - 10))


class Airport:
    """Represents an airport with multiple runways and a label."""
    def __init__(self, surface: PG.Surface, name: str, code: str, x: float, y: float, runways=None):
        self.surface = surface
        self.name = name
        self.code = code
        self.x = x
        self.y = y
        self.runways = runways if runways else []  # List of runways
        self.color = (255, 255, 0)  # Yellow for airport marker

    def draw(self):
        """Draw the airport marker and its runways."""
        # Draw airport symbol
        PG.draw.circle(self.surface, self.color, (int(self.x), int(self.y)), AIRPORT_SIZE)

        # Draw all runways
        for runway in self.runways:
            runway.draw(self.surface)

        # Draw airport name/code
        font = PG.font.Font(None, 18)
        # label = font.render(f"{self.code} - {self.name}", True, TEXT_COLOR)
        label = font.render(f"{self.code}", True, (self.color))
        self.surface.blit(label, (self.x - 40, self.y - 40))

        PG.draw.circle(self.surface, (0, 255, 0), (self.x, self.y), 150, 2)

    def get_departure_spawn(self):
        if not self.runways:
            return None
        
        runway = RANDOM.choice(self.runways)

        return (runway.x, runway.y, runway.heading)