from app.repositories.calculation_repository import CalculationRepository
from app.models.calculation import Operation, Calculation


class CalculationService:

    def __init__(self):
        # TODO: kanskje ha et repository som cacher resultater (kanskje skjer det noe feil under denne cachingine
        self.calculation_repository = CalculationRepository()

    def calculate(self, calculation: Calculation) -> Calculation:
        answer_from_cache = self.calculation_repository.from_cache(calculation)
        if answer_from_cache:
            return answer_from_cache

        match calculation.operation:
            case Operation.ADD:
                # DO add
                calculation.answer = self.add(calculation.parameter1, calculation.parameter2)
            case Operation.SUB:
                # DO sub
                calculation.answer = self.sub(calculation.parameter1, calculation.parameter2)
            case Operation.MULT:
                # DO mult
                calculation.answer = self.mult(calculation.parameter1, calculation.parameter2)
            case Operation.DIV:
                # DO div TODO: kanskje division by zero error?
                calculation.answer = self.div(calculation.parameter1, calculation.parameter2)
            case _:
                raise Exception("Operation not valid")

        self.calculation_repository.new_calculation(calculation)
        return calculation

    def add(self, param1, param2):
        return param1 + param2

    def sub(self, param1, param2):
        return param1 - param2

    def mult(self, param1, param2):
        return param1 * param2

    def div(self, param1, param2):
        return param1 / param2
