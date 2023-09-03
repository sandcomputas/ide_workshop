import json

from fastapi.testclient import TestClient
from starlette.status import HTTP_200_OK

from app.main import API
from app.resources.health_resource import HealthResource


class TestHealthResource:

    def setup_method(self):
        # Runs before every test starts
        api = API([HealthResource()])
        self.client = TestClient(api)

    def test_health_ok(self):
        response = self.client.get("/health")
        assert response.status_code == HTTP_200_OK, "Response should always be 200 ok"
        assert json.loads(response.json())["status"] == "OK"
