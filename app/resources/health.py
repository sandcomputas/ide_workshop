from app.resources.resource import Resource


class Health(Resource):

    def __init__(self):
        super().__init__("/health")
        self._router.get("")(self.health_check)

    @staticmethod
    def health_check() -> str:
        return "OK"