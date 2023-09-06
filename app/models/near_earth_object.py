from enum import Enum

from pydantic import BaseModel


class Unit(str, Enum):
    km = "kilometers"
    m = "meters"


class EstimatedDiameter(BaseModel):
    unit: Unit
    min: float
    max: float


class NearEarthObject(BaseModel):
    id: str
    name: str
    estimated_diameter: EstimatedDiameter
    is_potentially_hazardous_asteroid: bool
    miss_distance_km: float
    orbiting_body: str
    close_approach_date_full: str
