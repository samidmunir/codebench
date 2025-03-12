import pygame as PG

from config import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    BACKGROUND_COLOR,
    FPS,
)

from menu import Menu
from grid import Grid
from aircraft import Aircraft

PG.init()
PG.font.init()
FONT = PG.font.Font(None, 18)
SCREEN = PG.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
PG.display.set_caption('ATC Radar Simulation')
CLOCK = PG.time.Clock()

MENU = Menu(surface = SCREEN, font = FONT)
GRID = Grid(surface = SCREEN)

AIRCRAFT = Aircraft(SCREEN, 'DAL527', 'A359', 500.0, 500.0, 90.0, 250.0, 12000)

def main() -> None:
    RUNNING = True

    while RUNNING:
        SCREEN.fill(color = BACKGROUND_COLOR)
        
        MENU.draw()
        GRID.draw()

        AIRCRAFT.update()
        AIRCRAFT.draw()

        PG.display.flip()
        CLOCK.tick(FPS)

        for event in PG.event.get():
            if event.type == PG.QUIT:
                RUNNING = False
            elif event.type == PG.KEYDOWN:
                if event.key == PG.K_ESCAPE:
                    RUNNING = False
            
            if event.type == PG.MOUSEBUTTONDOWN:
                if AIRCRAFT.x - 10 < event.pos[0] < AIRCRAFT.x + 10 and AIRCRAFT.y - 10 < event.pos[1] < AIRCRAFT.y + 10:
                    AIRCRAFT.toggle_selection()

            MENU.handle_event(event)
    
    PG.quit()

if __name__ == '__main__':
    main()