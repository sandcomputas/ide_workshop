import json
import os
from typing import Dict, List

from httpx import Client
from pydantic import BaseModel


class NearEarthObject(BaseModel):
    ...


class NearEarthObjectsList(List[NearEarthObject]):
    pass


# TODO: str should probably be a Datetime object
class NearEarthObjectsMap(Dict[str, NearEarthObject]):
    ...


class NASANearEarthObjectWS:

    def __init__(self, api_key: str | None = os.getenv("IDE_WORKSHOP__NASA_KEY")):
        assert api_key, "Please add api key for NASA to configuration (IDE_WORKSHOP__NASA_KEY)"
        self.api_key = api_key
        self.client = Client(base_url="https://api.nasa.gov/neo")

    def coming_week_feed(self) -> list[NearEarthObject]:
        """
        Retrieve a list of Asteroids based on their closest approach date to Earth
        """
        #response = self.client.get(f"/rest/v1/feed?start_date=START_DATE&end_date=END_DATE&api_key={self.api_key}")
        response = self.client.get(f"/rest/v1/feed?api_key={self.api_key}")
        ...
        d = json.loads(response.json())

        return self._parse_feed(d.get("near_earth_objects", None))  # TODO, typo in get("near...") can be a task?

    def _parse_feed(self, near_earth_feed_raw: Dict[str, Dict]) -> List[NearEarthObject]:
        """TODO: Explanation here!"""
        near_earths = []
        for key, object in near_earth_feed_raw.items():
            near_earths.append(object)
        ...
        # TODO: continue here!
