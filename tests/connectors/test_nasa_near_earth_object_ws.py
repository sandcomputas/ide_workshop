import re
from pathlib import Path

from pytest_httpx import HTTPXMock

from app.connectors.nasa_near_earth_object_ws import NASANearEarthObjectWS
from app.models.near_earth_object import NearEarthObject

base_dir = f"{Path(__file__).parents[2]}"


def mock_data():
    with open(f"{base_dir}/tests/connectors/nasa_feed_response.json") as nasa_feed:
        data = nasa_feed.read()
    return data


def mock_nasa_feed(httpx_mock: HTTPXMock):
    httpx_mock.add_response(
        method="GET",
        url=re.compile('^https?:\/\/api\.nasa\.gov\/.*$'),
        json=mock_data()
    )


def test_feed(httpx_mock: HTTPXMock):
    mock_nasa_feed(httpx_mock)
    nneows = NASANearEarthObjectWS(api_key="TRENGER IKKE NØKKEL")  # Requesten er mocket ut
    r = nneows.coming_week_feed()
    for obj in r:
        assert isinstance(obj, NearEarthObject)

