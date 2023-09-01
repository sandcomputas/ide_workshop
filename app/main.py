from typing import List

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.resources.calculation_resource import CalculationResource
from app.resources.health_resource import HealthResource
from app.resources.resource import Resource


class API(FastAPI):

    def __init__(self, resources: List[Resource]):
        super().__init__()
        for resource in resources:
            resource.register(self)


if __name__ == "__main__":
    # OBS: Dette er ikke den tradisjonelle måten å sette opp et FastAPI prosjekt på, men det er det som vil
    # ligne mest på det dere vil se i Spring/.NET
    resources = [
        HealthResource(),
        CalculationResource()
    ]
    api = API(resources)
    api.mount("/", StaticFiles(directory="static", html=True), name="static")
    import uvicorn
    uvicorn.run(api, port=8080)
