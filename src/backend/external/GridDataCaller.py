from src.backend.external.AbstractExternalCaller import AbstractExternalCaller


class GridDataCaller(AbstractExternalCaller):

    def __init__(self, ba):
        self.ba = ba
        super().__init__()

    def fetch_timeseries_data(self):
        #TODO
        return []
