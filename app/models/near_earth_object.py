from enum import Enum

from pydantic import BaseModel


class Unit(str, Enum):
    km = "kilometers"
    m = "meters"


class EstimatedDiameter(BaseModel):
    unit: Unit
    min: float
    max: float


class CloseApproachData(BaseModel):
    close_approach_date_full: str
    unix_time_close_approach: int
    miss_distance_km: float
    orbiting_body: str


class NearEarthObject(BaseModel):
    id: str
    name: str
    absolute_magnitude_h: float
    estimated_diameter: EstimatedDiameter
    is_potentially_hazardous_asteroid: bool
    close_approach_data: CloseApproachData
