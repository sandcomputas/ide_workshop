from app.models.calculation import Calculation, Operation
from app.services.calculation_service import CalculationService


class TestCalculationService:

    def setup_method(self):
        self.calc_service = CalculationService()

    def test_cache(self):
        """
        CalculationService is supposed to cache results, so that we never have to do the same calculation twice.
        """
        calc = Calculation(parameter1=2.0, parameter2=3.0, operation=Operation.ADD)
        self.calc_service.calculate(calc)
        self.calc_service.calculate(calc)
        assert self.calc_service.cache_miss == 1
