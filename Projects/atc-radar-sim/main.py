import pygame as PG

from config import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    BACKGROUND_COLOR,
    FPS,
)

from grid import Grid

PG.init()
PG.font.init()
FONT = PG.font.Font(None, 18)
SCREEN = PG.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
PG.display.set_caption('ATC Radar Simulation')
CLOCK = PG.time.Clock()

GRID = Grid(surface = SCREEN)

def main():
    RUNNING = True

    while RUNNING:
        SCREEN.fill(color = BACKGROUND_COLOR)
        GRID.draw()

        PG.display.flip()
        CLOCK.tick(FPS)

        for EVENT in PG.event.get():
            if EVENT.type == PG.QUIT:
                RUNNING = False
            elif EVENT.type == PG.KEYDOWN:
                if EVENT.key == PG.K_ESCAPE:
                    RUNNING = False

    PG.quit()

if __name__ == '__main__':
    main()