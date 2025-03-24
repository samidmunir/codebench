import pygame as PG

class Particle:
    def __init__(self, x, y):
        self.pos = PG.math.Vector2(x, y)
        self.vel = PG.math.Vector2(2.5, 0)  # base rightward flow
        self.age = 0
        self.max_age = 300

    def update(self, flow_field_fn):
        # Apply influence of the flow field near the wing
        self.vel += flow_field_fn(self.pos)
        self.pos += self.vel
        self.age += 1

    def draw(self, surface):
        PG.draw.circle(surface, (0, 255, 255), (int(self.pos.x), int(self.pos.y)), 2)