from typing import List

from app.models.calculation import Calculation


class CalculationRepository:

    def __init__(self):
        self.calculations: List[Calculation] = []

    def from_cache(self, calculation: Calculation) -> Calculation | None:
        for c in self.calculations:
            if c == calculation:
                return c
        return None

    def new_calculation(self, calculation: Calculation):
        self.calculations.append(calculation)

