import json
import os
from typing import Dict, List

from httpx import Client

from app.models.near_earth_object import NearEarthObject, EstimatedDiameter, Unit


class NASANearEarthObjectWS:
    """Connector for talking to: https://api.nasa.gov/"""
    def __init__(self, api_key: str | None = None):
        if not api_key:
            api_key = os.getenv("IDE_WORKSHOP__NASA_KEY")
        assert api_key, "Please add api key for NASA to configuration (IDE_WORKSHOP__NASA_KEY)"
        self.api_key = api_key
        self.client = Client(base_url="https://api.nasa.gov/neo")

    def coming_week_feed(self) -> List[NearEarthObject]:
        """
        Retrieve a list of Asteroids based on their closest approach date to Earth in the coming week.
        """
        response = self.client.get(f"/rest/v1/feed?api_key={self.api_key}")
        d = response.json()
        result = self._extract_all_near_earth_events(d.get("near_earth_objects", None))
        return result

    @staticmethod
    def _extract_all_near_earth_events(near_earth_feed_raw: Dict[str, Dict]) -> List[NearEarthObject]:
        """
        Goes through raw data from NASA API, extracts data we are interested in - and creates and returns instances of
        NearEarthObjects.
        """
        near_earths = []
        for key, objects in near_earth_feed_raw.items():
            for object in objects:
                near_earth_obj = NearEarthObject(
                    id=object["id"],
                    name=object["name"],
                    estimated_diameter=EstimatedDiameter(
                        unit=Unit.m,
                        min=object["estimated_diameter"]["meters"]["estimated_diameter_min"],
                        max=object["estimated_diameter"]["meters"]["estimated_diameter_max"]
                    ),
                    is_potentially_hazardous_asteroid=object["is_potentially_hazardous_asteroid"],
                    close_approach_date_full=object["close_approach_data"][0]["close_approach_date_full"],
                    miss_distance_km=object["close_approach_data"][0]["miss_distance"]["kilometers"],
                    orbiting_body=object["close_approach_data"][0]["orbiting_body"]
                )
                near_earths.append(near_earth_obj)
        return near_earths
