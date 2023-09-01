from fastapi.testclient import TestClient
from starlette.status import HTTP_200_OK

from app.main import API
from app.resources.calculation_resource import CalculationResource
from app.models.calculation import Operation, Calculation


class TestCalculationResource:

    def setup_method(self):
        # Runs before every test starts
        api = API([CalculationResource()])
        self.client = TestClient(api)

    def test_calculation_add(self):
        req = Calculation(parameter1=2.0, parameter2=3.0, operation=Operation.ADD)
        response = self.client.post("/calculation", json=req.model_dump())
        assert response.status_code == HTTP_200_OK
        assert Calculation(**response.json()).answer == 5.0

    def test_calculation_sub(self):
        ...

    def test_calculation_mult(self):
        ...

    def test_calculation_div(self):
        ...

    def test_calculation_cache(self):
        ...

