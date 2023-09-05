from typing import List

from app.connectors.nasa_near_earth_object_ws import NASANearEarthObjectWS
from app.models.near_earth_object import NearEarthObject


class NearEarthAsteroidsService:

    def __init__(self):
        self.nasa = NASANearEarthObjectWS()

    def find_most_dangerous_asteroid(self) -> List[NearEarthObject]:
        near_earths = self.nasa.coming_week_feed()
        return near_earths
