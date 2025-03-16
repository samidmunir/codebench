from config import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
)

from aircraft import Aircraft

import random as RANDOM

class AircraftController:
    def __init__(self):
        self.airline_ICAO = ['AAL', 'UAL', 'SWA', 'BAW', 'ACA', 'DAL', 'UAE', 'FIN']
        self.ac_types = ['A318', 'A319', 'A320', 'A321', 'A332', 'A333', 'A343', 'A346', 'A359', 'A35K', 'B736', 'B737', 'B738', 'B739', 'B744', 'B748', 'B752', 'B753', 'B763', 'B764', 'B772', 'B77L', 'B77W', 'B788', 'B789', 'B78X', 'C152']

    def generate_random_type(self) -> str:
        ac_type = RANDOM.choice(self.ac_types)
        return ac_type

    def generate_random_flight_number(self, ac_type: str):
        if ac_type == 'C152':
            flight_number = 'NW'
            flight_number += str(RANDOM.randint(0, 999))
            flight_number += RANDOM.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
            return flight_number
        else:
            flight_number = ''
            random_airline = RANDOM.choice(self.airline_ICAO)
            random_flight_number = RANDOM.randint(1000, 9000)
            flight_number += random_airline
            flight_number += str(random_flight_number)
            return flight_number

    def generate_random_position(self):
        x = RANDOM.randint(0 + 100, SCREEN_WIDTH - 100)
        y = RANDOM.randint(0 + 100, SCREEN_HEIGHT - 100)
        return (x, y)
    
    def generate_random_heading(self):
        heading = RANDOM.randint(0, 360)
        return heading
    
    def generate_random_speed(self, ac_type):
        if ac_type == 'C152':
            speed = RANDOM.randint(50, 120)
        else:
            speed = RANDOM.randint(240, 600)
        return speed
    
    def generate_random_altitude(self):
        altitude = RANDOM.randint(1500, 40000)
        return altitude

    def generate_random_aircraft(self) -> Aircraft:
        ac_type = self.generate_random_type()
        flight_number = self.generate_random_flight_number(ac_type = ac_type)
        x, y = self.generate_random_position()
        heading = self.generate_random_heading()
        speed = self.generate_random_speed(ac_type = ac_type)
        altitude = self.generate_random_altitude()
        return (ac_type, flight_number, x, y, heading, speed, altitude)
