from app.connectors.nasa_near_earth_object_ws import NASANearEarthObjectWS


class NearEarthAsteriodsService:

    def __init__(self):
        self.nasa = NASANearEarthObjectWS()

    def find_most_dangerous_asteroid(self):
        feed = self.nasa.coming_week_feed()



