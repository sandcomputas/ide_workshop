import os
from typing import List

import pytest
from fastapi.testclient import TestClient
from pydantic import parse_obj_as
from pytest_httpx import HTTPXMock

from app.main import API
from app.models.near_earth_object import NearEarthObject
from app.resources.near_earth_asteroid_resource import NearEarthAsteroidResource
from tests.connectors.test_nasa_near_earth_object_ws import mock_nasa_feed


class TestNearEarthAsteroidResource:

    def setup_method(self):
        # Runs before every test starts
        os.environ["IDE_WORKSHOP__NASA_KEY"] = "TEST"
        api = API([NearEarthAsteroidResource()])
        self.client = TestClient(api)

    @pytest.fixture
    def non_mocked_hosts(self) -> List[str]:
        return ["testserver"]

    def test_resource(self, httpx_mock: HTTPXMock):
        mock_nasa_feed(httpx_mock)
        response = self.client.get("/asteroids")
        near_earths = parse_obj_as(List[NearEarthObject], response.json())  # TODO: depricated, fix this someone
        ...
