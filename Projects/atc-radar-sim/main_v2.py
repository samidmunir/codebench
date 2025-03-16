import pygame as PG

from config_v2 import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    BACKGROUND_COLOR,
    FPS,
)

from menu import Menu
from grid_v2 import Grid
from aircraft import Aircraft
from airport import Airport, Runway

PG.init()
PG.font.init()
FONT = PG.font.Font(None, 18)
SCREEN = PG.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
PG.display.set_caption('ATC Radar Simulation')
CLOCK = PG.time.Clock()

ac1 = Aircraft(SCREEN, 'DAL527', 'A359', 25.0, 100.0, 90.0, 200.0, 40000)
ac2 = Aircraft(SCREEN, 'AAL59K', 'B772', 25.0, 150.0, 90.0, 250.0, 34000)
ac3 = Aircraft(SCREEN, 'BAW189', 'B789', 25.0, 200.0, 90.0, 350.0, 40000)
ac4 = Aircraft(SCREEN, 'DAL1147', 'B38M', 25.0, 250.0, 90.0, 400.0, 38000)
ac5 = Aircraft(SCREEN, 'AAL223', 'A21N', 25.0, 300.0, 90.0, 450.0, 36000)
ac6 = Aircraft(SCREEN, 'JBU1738', 'A21N', 25.0, 350.0, 90.0, 500.0, 38000)
ac7 = Aircraft(SCREEN, 'BAW182', 'A35K', 25.0, 400.0, 90.0, 550.0, 40000)
ac8 = Aircraft(SCREEN, 'ACA115', 'B77W', 25.0, 450.0, 90.0, 550.0, 40000)
ac9 = Aircraft(SCREEN, 'UAE10J', 'B78X', 25.0, 500.0, 90.0, 600.0, 40000)
AIRCRAFTS = []
AIRCRAFTS.append(ac1)
AIRCRAFTS.append(ac2)
AIRCRAFTS.append(ac3)
AIRCRAFTS.append(ac4)
AIRCRAFTS.append(ac5)
AIRCRAFTS.append(ac6)
AIRCRAFTS.append(ac7)
AIRCRAFTS.append(ac8)
AIRCRAFTS.append(ac9)

AIRPORTS = [
    Airport(SCREEN, 'John F. Kennedy Intl', 'KJFK',  1000, 400, [
        Runway(990, 390, 150, 5, 220, 'R'),
        Runway(990, 390, 150, 5, 40, 'L'),
        Runway(1010, 410, 150, 5, 220, 'L'),
        Runway(1010, 410, 150, 5, 40, 'R'),
        Runway(1000, 380, 175, 5, 310, 'R'),
        Runway(1000, 380, 175, 5, 130, 'L'),
        Runway(970, 400, 200, 5, 310, 'L'),
        Runway(970, 400, 200, 5, 130, 'R'),
    ]),
    Airport(SCREEN, 'Newark Liberty Intl', 'KEWR', 250, 450, [
        Runway(240, 440, 150, 5, 220, 'R'),
        Runway(240, 440, 150, 5, 40, 'L'),
        Runway(260, 460, 150, 5, 220, 'L'),
        Runway(260, 460, 150, 5, 40, 'R'),
        Runway(260, 410, 125, 5, 290),
        Runway(260, 410, 125, 5, 110),
    ]),
    Airport(SCREEN, 'LaGuardia Airport', 'KLGA', 600, 200, [
        Runway(600, 200, 130, 5, 220),
        Runway(600, 200, 130, 5, 40),
        Runway(600, 200, 130, 5, 310),
        Runway(600, 200, 130, 5, 130),
    ]),
]

MENU = Menu(surface = SCREEN, font = FONT, aircrafts = AIRCRAFTS)
GRID = Grid(surface = SCREEN)

def main() -> None:
    RUNNING = True

    while RUNNING:
        SCREEN.fill(color = BACKGROUND_COLOR)
        
        MENU.draw()
        GRID.draw()

        for airport in AIRPORTS:
            airport.draw()

        for aircraft in AIRCRAFTS:
            aircraft.update()
            aircraft.draw()

        PG.display.flip()
        CLOCK.tick(FPS)

        for event in PG.event.get():
            if event.type == PG.QUIT:
                RUNNING = False
            elif event.type == PG.KEYDOWN:
                if event.key == PG.K_ESCAPE:
                    RUNNING = False
            elif event.type == PG.MOUSEBUTTONDOWN:
                for aircraft in AIRCRAFTS:
                    if aircraft.x - 10 < event.pos[0] < aircraft.x + 10 and aircraft.y - 10 < event.pos[1] < aircraft.y + 10:
                        aircraft.toggle_selection()

            MENU.handle_event(event)
    
    PG.quit()

if __name__ == '__main__':
    main()