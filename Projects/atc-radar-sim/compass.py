import pygame as PG
import math as MATH

from config_v2 import (
    COMPASS_COLOR,
    COMPASS_RADIUS,
    TEXT_COLOR
)

class Compass:
    """A draggable compass to set aircraft heading."""
    def __init__(self, surface: PG.Surface, x, y):
        self.surface = surface
        self.x = x
        self.y = y
        self.heading = 90  # Default heading
        self.dragging = False

    def draw(self):
        """Draw the compass with a heading indicator."""
        # Draw outer compass circle
        PG.draw.circle(self.surface, COMPASS_COLOR, (self.x, self.y), COMPASS_RADIUS, 2)

        # Draw heading text
        font = PG.font.Font(None, 20)
        heading_text = font.render(f"{int(self.heading)}°", True, TEXT_COLOR)
        self.surface.blit(heading_text, (self.x + 25, self.y - COMPASS_RADIUS))

        # Draw heading indicator line
        angle_rad = MATH.radians(self.heading - 90)
        indicator_x = self.x + MATH.cos(angle_rad) * COMPASS_RADIUS
        indicator_y = self.y + MATH.sin(angle_rad) * COMPASS_RADIUS
        PG.draw.line(self.surface, TEXT_COLOR, (self.x, self.y), (indicator_x, indicator_y), 3)

    def handle_event(self, event):
        """Handle mouse interaction with the compass."""
        if event.type == PG.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            distance = MATH.sqrt((mouse_x - self.x) ** 2 + (mouse_y - self.y) ** 2)
            if COMPASS_RADIUS - 10 <= distance <= COMPASS_RADIUS + 10:
                self.dragging = True

        elif event.type == PG.MOUSEBUTTONUP:
            self.dragging = False

        elif event.type == PG.MOUSEMOTION and self.dragging:
            mouse_x, mouse_y = event.pos
            angle = MATH.degrees(MATH.atan2(mouse_y - self.y, mouse_x - self.x)) + 90
            self.heading = (angle + 360) % 360  # Keep heading within 0-360

    def set_heading(self, heading):
        """Update compass heading to match selected aircraft."""
        self.heading = heading % 360