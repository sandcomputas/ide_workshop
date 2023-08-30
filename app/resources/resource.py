from fastapi import APIRouter, FastAPI


class Resource:
    def __init__(self, prefix: str = ""):
        self._router = APIRouter()
        self._prefix = prefix

    def register(self, api: FastAPI):
        api.include_router(self._router, prefix=self._prefix)
