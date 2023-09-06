from typing import List

from app.connectors.nasa_near_earth_object_ws import NASANearEarthObjectWS
from app.models.near_earth_object import NearEarthObject


class NearEarthAsteroidsService:

    def __init__(self):
        self.nasa = NASANearEarthObjectWS()

    def find_hazardous_asteroid(self) -> List[NearEarthObject]:
        near_earths = self.nasa.coming_week_feed()
        hazardous_asteroids = []

        # TODO: Bug kan være at vi gjør en feil true / false evaluation
        for asteroid in near_earths:
            if asteroid.is_potentially_hazardous_asteroid:
                hazardous_asteroids.append(asteroid)

        hazardous_asteroids.sort(key=lambda x: x.miss_distance_km)

        return hazardous_asteroids
