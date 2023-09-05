from typing import List

from app.models.near_earth_object import NearEarthObject
from app.resources.resource import Resource
from app.services.near_earth_asteroids_service import NearEarthAsteroidsService


class NearEarthAsteroidResource(Resource):

    def __init__(self):
        super().__init__("/asteroids")
        self.service = NearEarthAsteroidsService()
        self._router.get("")(self.asteroids)

    def asteroids(self) -> List[NearEarthObject]:
        return self.service.find_most_dangerous_asteroid()




