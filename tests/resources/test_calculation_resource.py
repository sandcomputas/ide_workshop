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
        param1 = 2.0
        param2 = 3.0
        expected_result = param1 + param2
        self._test_calculation(param1, param2, operation=Operation.ADD, expected_result=expected_result)

    def test_calculation_sub(self):
        param1 = 2.0
        param2 = 3.0
        expected_result = param1 - param2
        self._test_calculation(param1, param2, operation=Operation.SUB, expected_result=expected_result)

    def test_calculation_mult(self):
        param1 = 2.0
        param2 = 3.0
        expected_result = param1 * param2
        self._test_calculation(param1, param2, operation=Operation.MULT, expected_result=expected_result)

    def test_calculation_div(self):
        param1 = 2.0
        param2 = 3.0
        expected_result = param1 / param2
        self._test_calculation(param1, param2, operation=Operation.DIV, expected_result=expected_result)

    def test_cache(self):
        # Note: Not really a test of cache - see tests/services/test_calculation_service.py
        self.test_calculation_add()
        self.test_calculation_add()

    def _test_calculation(self, param1: float, param2: float, operation: Operation, expected_result: float):
        req = Calculation(parameter1=param1, parameter2=param2, operation=operation)
        response = self.client.post("/calculation", json=req.model_dump())
        assert response.status_code == HTTP_200_OK
        assert Calculation(**response.json()).answer == expected_result

