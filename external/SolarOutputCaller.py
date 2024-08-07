from external.AbstractExternalCaller import AbstractExternalCaller


class SolarOutputCaller(AbstractExternalCaller):

    def __init__(self, lat, long):
        self.lat = lat
        self.long = long
        super().__init__()

    def fetch_timeseries_data(self):
        #TODO
        return []
