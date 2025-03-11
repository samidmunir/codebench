import random as RANDOM
import string as STRING
import pygame as PG

from config import (
    FPS,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    BACKGROUND_COLOR,
    GRID_COLOR,
    GRID_SPACING,
)

def draw_grid(surface: PG.Surface):
    for x in range(0, SCREEN_WIDTH, GRID_SPACING):
        PG.draw.line(surface, GRID_COLOR, (x, 0), (x, SCREEN_HEIGHT), 1)
    for y in range(0, SCREEN_HEIGHT, GRID_SPACING):
        PG.draw.line(surface, GRID_COLOR, (0, y), (SCREEN_WIDTH, y), 1)

def main():
    PG.init()
    SCREEN = PG.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), PG.SRCALPHA)
    PG.display.set_caption("ATC Radar Simulation")
    CLOCK = PG.time.Clock()

    RUNNING = True

    while RUNNING:
        for event in PG.event.get():
            if event.type == PG.QUIT:
                RUNNING = False
        
        SCREEN.fill(BACKGROUND_COLOR)
        draw_grid(surface = SCREEN)

        PG.display.flip()
        CLOCK.tick(FPS)
    
    PG.quit()

if __name__ == "__main__":
    main()