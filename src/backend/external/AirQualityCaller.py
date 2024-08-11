import pandas as pd

from src.backend.external.AbstractExternalCaller import AbstractExternalCaller
from src.backend.ArimaResult import ArimaResult


class AirQualityCaller(AbstractExternalCaller):

    def __init__(self, lat, long):
        self.lat = lat
        self.long = long
        super().__init__()

    def fetch_timeseries_data(self) -> (pd.DataFrame(), 0):
        return pd.DataFrame(), 0  # TODO

    def generate_prompt(self, arima_result: ArimaResult) -> str:
        return ("It looks like there was an Air Quality alert in your area. {Alert}. Planting trees is an easy and "
                "satisfying way to help clean up the air that positively impacts generations in the future. "
                "Organizations like Arbor Day https://www.arborday.org/ are great sources to contribute to "
                "afforestation.")
