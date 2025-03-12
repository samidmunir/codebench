import pygame as PG
import math as MATH

from config import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    AIRCRAFT_SIZE,
    AIRCRAFT_RING_SIZE,
    AIRCRAFT_SPEED_SCALAR,
    TEXT_COLOR
)

class Aircraft:
    def __init__(self, surface: PG.Surface, flight_number: str, type: str, x: float, y: float, heading: float, speed: float, altitude: float):
        self.surface = surface
        self.color = (0, 255, 255)
        self.flight_number = flight_number
        self.type = type
        self.x = x
        self.y = y
        self.heading = heading
        self.speed = speed
        self.altitude = altitude
        self.selected = False
    
    def draw(self):
        heading_rad = MATH.radians((self.heading - 90) % 360)

        nose = (self.x + MATH.cos(heading_rad) * AIRCRAFT_SIZE, self.y + MATH.sin(heading_rad) * AIRCRAFT_SIZE)
        left_wing = (self.x + MATH.cos(heading_rad + 2.5) * AIRCRAFT_SIZE, self.y + MATH.sin(heading_rad + 2.5) * AIRCRAFT_SIZE)
        right_wing = (self.x + MATH.cos(heading_rad - 2.5) * AIRCRAFT_SIZE, self.y + MATH.sin(heading_rad - 2.5) * AIRCRAFT_SIZE)

        PG.draw.polygon(self.surface, self.color, [nose, left_wing, right_wing])

        if self.selected:
            PG.draw.circle(self.surface, (0, 255, 255), (int(self.x), int(self.y)), AIRCRAFT_RING_SIZE, width = 2)

        label1 = f'{self.flight_number} - {self.type}'
        label2 = f'{self.heading}° | {self.speed}kts | {self.altitude}ft'
        font = PG.font.Font(None, 16)
        text_surface1 = font.render(label1, True, TEXT_COLOR)
        text_surface2 = font.render(label2, True, TEXT_COLOR)
        self.surface.blit(text_surface1, (self.x - 5, self.y - 45))
        self.surface.blit(text_surface2, (self.x - 5, self.y - 30))
    
    def toggle_selection(self):
        self.selected = not self.selected

    def update(self):
        heading_rad = MATH.radians((self.heading - 90) % 360)
        self.x += MATH.cos(heading_rad) * (self.speed * AIRCRAFT_SPEED_SCALAR)
        self.y += MATH.sin(heading_rad) * (self.speed * AIRCRAFT_SPEED_SCALAR)

        if self.x < 0 or self.x > SCREEN_WIDTH or self.y < 0 or self.y > SCREEN_HEIGHT:
            self.x = self.x % SCREEN_WIDTH
            self.y = self.y % SCREEN_HEIGHT