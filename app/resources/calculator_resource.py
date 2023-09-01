from enum import Enum

from app.resources.resource import Resource


class Operation(str, Enum):
    ADD = "Addition"
    SUB = "Subtract"
    MULT = "Multiply"
    DIV = "Divide"


# TODO: move to models folder
class Calculation:
    parameter1: float
    parameter2: float
    operation: Operation
    answer: float


# TODO: move to service folder
class CalculatorService:

    def __init__(self):
        # TODO: kanskje ha et repository som cacher resultater (kanskje skjer det noe feil under denne cachingine
        ...

    def calculate(self, calculation: Calculation) -> Calculation:
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
        return calculation

class CalculatorResource(Resource):

    def __init__(self):
        super().__init__("/calculator")
        self.calc_service = CalculatorService()
        self._router.post("")(self.calculator)

    def calculator(self, calculation: Calculation):
        ...
