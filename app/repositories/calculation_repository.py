from typing import List

from app.models.calculation import Calculation


class NotFoundInCacheException(Exception):

    def __init__(self):
        super().__init__("Calculation not found in cache. I am afraid you have to calculate this without my help")


class CalculationRepository:

    def __init__(self):
        self.calculations: List[Calculation] = []

    def from_cache(self, calculation: Calculation) -> Calculation | None:
        for c in self.calculations:
            if c == calculation:
                return c
        raise NotFoundInCacheException()

    def new_calculation(self, calculation: Calculation):
        self.calculations.append(calculation)
