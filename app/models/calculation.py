from enum import Enum

from pydantic import BaseModel


class Operation(str, Enum):
    ADD = "Addition"
    SUB = "Subtract"
    MULT = "Multiply"
    DIV = "Divide"


class Calculation(BaseModel):
    parameter1: float
    parameter2: float
    operation: Operation
    answer: float | None = None

    def __eq__(self, other) -> bool:
        """Returns True if two calculations are equivalent"""
        if not isinstance(other, Calculation):
            raise NotImplemented(f"__eq__ not implement for Calculation and {type(other)}")
        if self.operation != other.operation:
            return False
        if self.parameter1 == other.parameter1 and self.parameter2 == other.parameter2:
            return True
        if self.operation in [Operation.ADD, Operation.MULT]:
            if ((self.parameter1 == other.parameter1 and self.parameter2 == other.parameter2)
                    or (self.parameter1 == other.parameter2 and self.parameter2 == other.parameter1)):
                return True
        return False
