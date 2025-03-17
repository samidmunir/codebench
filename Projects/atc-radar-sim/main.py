import pygame as PG
import random as RANDOM

from config import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    BACKGROUND_COLOR,
    FPS,
    MAXIMUM_AIRCRAFTS,
)

from grid import Grid
from menu import Menu
from aircraft_controller import AircraftController
from aircraft import Aircraft
from airport import Airport, Runway

PG.init()
PG.font.init()
FONT = PG.font.Font(None, 18)
SCREEN = PG.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
PG.display.set_caption('ATC Radar Simulation')
CLOCK = PG.time.Clock()

AIRCRAFT_CONTROLLER = AircraftController()

AIRCRAFTS = [
    Aircraft(SCREEN, 'DAL527', 'A359', 25.0, 100.0, 90.0, 220.0, 5000, 'airborne'),
    Aircraft(SCREEN, 'AAL223', 'A21N', 25.0, 200.0, 90.0, 250.0, 19000, 'airborne'),
    Aircraft(SCREEN, 'JBU1738', 'A21N', 25.0, 300.0, 90.0, 300.0, 37000, 'airborne'),
]

GRID = Grid(surface = SCREEN)
MENU = Menu(surface = SCREEN, font = FONT, aircrafts = AIRCRAFTS)

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

PG.time.set_timer(PG.USEREVENT, 15000)

def main():
    RUNNING = True

    while RUNNING:
        SCREEN.fill(color = BACKGROUND_COLOR)
        GRID.draw()
        MENU.draw()

        for AIRPORT in AIRPORTS:
            AIRPORT.draw()

        for AIRCRAFT in AIRCRAFTS:
            if AIRCRAFT.is_out_of_bounds():
                AIRCRAFTS.remove(AIRCRAFT)
                continue
            AIRCRAFT.move()
            AIRCRAFT.draw()

        PG.display.flip()
        CLOCK.tick(FPS)

        """
        if len(AIRCRAFTS) < MAXIMUM_AIRCRAFTS:
            ac_type, flight_number, x, y, heading, speed, altitude = AIRCRAFT_CONTROLLER.generate_random_aircraft() 
            new_aircraft = Aircraft(surface = SCREEN, flight_number = flight_number, type = ac_type, x = x, y = y, heading = heading, speed = speed, altitude = altitude)
            AIRCRAFTS.append(new_aircraft)"
        """

        for EVENT in PG.event.get():
            if EVENT.type == PG.QUIT:
                RUNNING = False
            elif EVENT.type == PG.KEYDOWN:
                if EVENT.key == PG.K_ESCAPE:
                    RUNNING = False
            elif EVENT.type == PG.USEREVENT:
                spawn_departures()
            elif EVENT.type == PG.MOUSEBUTTONDOWN:
                for AIRCRAFT in AIRCRAFTS:
                    if AIRCRAFT.x - 10 < EVENT.pos[0] < AIRCRAFT.x + 10 and AIRCRAFT.y - 10 < EVENT.pos[1] < AIRCRAFT.y + 10:
                        AIRCRAFT.toggle_selection()
                        if AIRCRAFT.selected:
                            MENU.select_aircraft()
                        else:
                            MENU.deselect_all_inputs() # clear input fields on deselect

            MENU.handle_event(event = EVENT)

    PG.quit()

def spawn_departures():
    airport = RANDOM.choice(AIRPORTS)
    spawn_location = airport.get_departure_spawn()

    new_ac_type = AIRCRAFT_CONTROLLER.generate_random_type()
    new_flight_number = AIRCRAFT_CONTROLLER.generate_random_flight_number(new_ac_type)

    if spawn_location:
        x, y, heading = spawn_location
        new_aircraft = Aircraft(surface = SCREEN, flight_number = new_flight_number, type = new_ac_type, x = x, y = y, heading = heading, speed = 150, altitude = 2500, status = 'departing')
        AIRCRAFTS.append(new_aircraft)

if __name__ == '__main__':
    main()