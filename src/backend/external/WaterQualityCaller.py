import pandas as pd

from src.backend.external.AbstractExternalCaller import AbstractExternalCaller
from src.backend.ArimaResult import ArimaResult


class WaterQualityCaller(AbstractExternalCaller):

    def __init__(self, lat, long):
        self.lat = lat
        self.long = long
        super().__init__()

    def fetch_timeseries_data(self) -> (pd.DataFrame(), 0):
        return pd.DataFrame(), 0  # TODO

    def generate_prompt(self, arima_result: ArimaResult) -> str:
        return ("It looks like there was a Water Quality alert in your area. {Alert}. When water quality drops it means"
                " pollution or algae is effecting the water you use to eat, drink, shower. While sometimes its hard to "
                "effect change in your specific area around water quality you can support an organization "
                "like https://water.org to help ensure others have consistently clean water")
