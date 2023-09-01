from typing import List

from app.models.calculation import Calculation


class CalculationRepository:

    def __init__(self):
        self.calculations: List[Calculation] = []

    def from_cache(self, calculation) -> Calculation | None:
        for calculation in self.calculations:
            if calculation == self.calculations:
                return calculation
        return None
