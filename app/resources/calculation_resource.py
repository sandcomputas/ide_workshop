from app.models.calculation import Calculation
from app.resources.resource import Resource
from app.services.calculation_service import CalculationService


class CalculationResource(Resource):

    def __init__(self):
        super().__init__("/calculation")
        self.calc_service = CalculationService()
        self._router.post("")(self.calculator)

    def calculator(self, calculation: Calculation) -> Calculation:
        return self.calc_service.calculate(calculation)
