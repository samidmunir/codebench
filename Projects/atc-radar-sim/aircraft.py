import pygame as PG
import math as MATH

from config import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    MENU_HEIGHT,
    AIRCRAFT_SIZE,
    AIRCRAFT_RING_SIZE,
    AIRCRAFT_SPEED_SCALAR,
    AIRCRAFT_TURN_RATE_SCALAR,
    AIRCRAFT_SPEED_CHNG_SCALAR,
    AIRCRAFT_ALTITUDE_CHNG_SCALAR,
    AIRCRAFT_HEADING_VECTOR_LENGTH,
    AIRCRAFT_TARGET_HEADING_VECTOR_LENGTH,
    AIRCRAFT_TEXT_COLOR,
)

class Aircraft:
    def __init__(self, surface: PG.Surface, flight_number: str, type: str, x: float, y: float, heading: float, speed: float, altitude: float, status: str = ''):
        self.surface = surface
        self.color = (0, 255, 255)
        self.flight_number = flight_number
        self.type = type
        self.x = x
        self.y = y
        self.trail = []
        self.last_trail_position = (self.x, self.y)
        self.heading = heading
        self.speed = speed
        self.altitude = altitude
        self.selected = False
        self.target_heading = self.heading
        self.target_speed = self.speed
        self.target_altitude = self.altitude
        self.status = 'airborne'
    
    def draw(self):
        heading_rad = MATH.radians((self.heading - 90) % 360)
        target_heading_rad = MATH.radians((self.target_heading - 90) % 360)

        nose = (self.x + MATH.cos(heading_rad) * AIRCRAFT_SIZE, self.y + MATH.sin(heading_rad) * AIRCRAFT_SIZE)
        left_wing = (self.x + MATH.cos(heading_rad + 2.5) * AIRCRAFT_SIZE, self.y + MATH.sin(heading_rad + 2.5) * AIRCRAFT_SIZE)
        right_wing = (self.x + MATH.cos(heading_rad - 2.5) * AIRCRAFT_SIZE, self.y + MATH.sin(heading_rad - 2.5) * AIRCRAFT_SIZE)

        PG.draw.polygon(self.surface, self.color, [nose, left_wing, right_wing])

        self.draw_trail(self.surface)

        if self.heading != self.target_heading:
            PG.draw.line(self.surface, self.color, (self.x, self.y), (self.x + MATH.cos(heading_rad) * AIRCRAFT_HEADING_VECTOR_LENGTH, self.y + MATH.sin(heading_rad) * AIRCRAFT_HEADING_VECTOR_LENGTH), width = 2)
            PG.draw.line(self.surface, (0, 255, 0), (self.x, self.y), (self.x + MATH.cos(target_heading_rad) * AIRCRAFT_HEADING_VECTOR_LENGTH, self.y + MATH.sin(target_heading_rad) * AIRCRAFT_TARGET_HEADING_VECTOR_LENGTH), width = 2)
        else:
            PG.draw.line(self.surface, self.color, (self.x, self.y), (self.x + MATH.cos(heading_rad) * AIRCRAFT_HEADING_VECTOR_LENGTH, self.y + MATH.sin(heading_rad) * AIRCRAFT_HEADING_VECTOR_LENGTH), width = 2)
        
        if self.selected:
            PG.draw.circle(self.surface, (255, 255, 0), (int(self.x), int(self.y)), AIRCRAFT_RING_SIZE, width = 2)

        label1 = f'{self.flight_number} - {self.type}'
        label2 = None
        if self.altitude >= 18000:
            altitude_text = 'FL' + str(int(self.altitude / 100))
            label2 = f'{int(self.heading)}° | {int(self.speed)}kts | {altitude_text}'
        else:
            label2 = f'{int(self.heading)}° | {int(self.speed)}kts | {int(self.altitude)}ft'
        font = PG.font.Font(None, 16)
        text_surface1 = font.render(label1, True, AIRCRAFT_TEXT_COLOR)
        text_surface2 = font.render(label2, True, AIRCRAFT_TEXT_COLOR)
        self.surface.blit(text_surface1, (self.x - 5, self.y - 55))
        self.surface.blit(text_surface2, (self.x - 5, self.y - 40))

    def toggle_selection(self):
        self.selected = not self.selected

    def move(self):
        """
        if self.heading != self.target_heading:
            diff = (self.target_heading - self.heading + 360) % 360
            if diff > 180:
                self.heading -= min(1, abs(diff))
            else:
                self.heading += min(1, abs(diff))
            self.heading %= 360

        if self.speed != self.target_speed:
            speed_diff = self.target_speed - self.speed
            self.speed += min(5, max(-5, speed_diff))

        if self.altitude != self.target_altitude:
            altitude_diff = self.target_altitude - self.altitude
            self.altitude += min(100, max(-100, altitude_diff))

        heading_rad = MATH.radians((self.heading - 90) % 360)
        self.x += MATH.cos(heading_rad) * (self.speed * AIRCRAFT_SPEED_SCALAR)
        self.y += MATH.sin(heading_rad) * (self.speed * AIRCRAFT_SPEED_SCALAR)

        trail_spacing = 10
        tx = self.x - self.last_trail_position[0]
        ty = self.y - self.last_trail_position[1]
        t_distance = MATH.sqrt(tx ** 2 + ty ** 2)
        if t_distance > trail_spacing:
            self.trail.append((self.x, self.y))
            self.last_trail_position = (self.x, self.y)
        if len(self.trail) > 100:
            self.trail.pop(0)
        """
        # Gradual heading adjustment (max ±3° per frame)
        if self.heading != self.target_heading:
            diff = (self.target_heading - self.heading + 360) % 360  # Get shortest rotation
            step = min(AIRCRAFT_TURN_RATE_SCALAR, abs(diff))  # Limit heading change to 3° per frame
            if diff > 180:
                self.heading -= step  # Rotate left
            else:
                self.heading += step  # Rotate right
            self.heading %= 360  # Keep heading within 0-360

        # Gradual speed adjustment (max ±2 knots per frame)
        if self.speed != self.target_speed:
            speed_diff = self.target_speed - self.speed
            step = min(AIRCRAFT_SPEED_CHNG_SCALAR, abs(speed_diff))  # Limit speed change to 2 knots per frame
            self.speed += step if speed_diff > 0 else -step

        # Gradual altitude adjustment (max ±50 feet per frame)
        if self.altitude != self.target_altitude:
            altitude_diff = self.target_altitude - self.altitude
            step = min(AIRCRAFT_ALTITUDE_CHNG_SCALAR, abs(altitude_diff))  # Limit altitude change to 50 feet per frame
            self.altitude += step if altitude_diff > 0 else -step

        # Update position based on heading & speed
        rad = MATH.radians((self.heading - 90) % 360)
        self.x += MATH.cos(rad) * (self.speed * AIRCRAFT_SPEED_SCALAR)  # Reduced scale for smoother movement
        self.y += MATH.sin(rad) * (self.speed * AIRCRAFT_SPEED_SCALAR)

        trail_spacing = 5
        tx = self.x - self.last_trail_position[0]
        ty = self.y - self.last_trail_position[1]
        t_distance = MATH.sqrt(tx ** 2 + ty ** 2)
        if t_distance > trail_spacing:
            self.trail.append((self.x, self.y))
            self.last_trail_position = (self.x, self.y)
        if len(self.trail) > 500:
            self.trail.pop(0)

    def draw_trail(self, screen):
        # Initialize a persistent trail surface once
        if not hasattr(self, "trail_surface"):
            self.trail_surface = PG.Surface((screen.get_width(), screen.get_height()), PG.SRCALPHA)
            self.trail_surface.fill((0, 0, 0, 0))  # Fully transparent background

        # Fade out the trail over time for a smooth effect
        self.trail_surface.fill((0, 0, 0, 10), special_flags=PG.BLEND_RGBA_MULT)

        # Draw the current trail points onto the trail surface
        for i, (tx, ty) in enumerate(self.trail):
            factor = i / len(self.trail) if len(self.trail) > 0 else 0
            red = int((1 - factor) * 255)
            blue = int(factor * 255)
            alpha = int((1 - factor) * 128)  # Adjust alpha for transparency
            color = (red, 0, blue, alpha)
            PG.draw.circle(self.trail_surface, color, (int(tx), int(ty)), 3)

        # Blit the trail surface onto the main screen
        screen.blit(self.trail_surface, (0, 0))

    def is_out_of_bounds(self):
        if self.x < 25 or self.x > SCREEN_WIDTH - 25 or self.y < 25 or self.y > SCREEN_HEIGHT - MENU_HEIGHT - 25:
            return True
        else:
            return False
        
    def set_target(self, heading = None, speed = None, altitude = None):
        if heading is not None:
            self.target_heading = heading % 360
        if speed is not None:
            self.target_speed = max(100, min(600, speed))
        if altitude is not None:
            self.target_altitude = max(1000, min(40000, altitude))

    def handle_takeoff(self):
        if self.speed < 150:
            self.speed += 2
        elif self.altitude < 5000:
            self.altitude += 10
        else:
            self.status = 'airborne'
        self.move()