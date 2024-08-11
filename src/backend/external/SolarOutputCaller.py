import pandas as pd

from src.backend.external.AbstractExternalCaller import AbstractExternalCaller
from src.backend.ArimaResult import ArimaResult
import pvlib


class SolarOutputCaller(AbstractExternalCaller):

    def __init__(self, lat, long):
        self.lat = lat
        self.long = long
        super().__init__()

    def fetch_timeseries_data(self) -> (pd.DataFrame(), 0):
        return pd.DataFrame(), 0
        # solar_weather_timeseries, solar_weather_metadata = pvlib.iotools.get_psm3(
        #     latitude=self.lat,
        #     longitude=self.long,
        #     names=2022,
        #     api_key=NREL_API_KEY,
        #     email=NREL_API_EMAIL,
        #     map_variables=True,
        #     leap_day=True,
        # )
        # return []

    def generate_prompt(self, arima_result: ArimaResult) -> str:
        return ("It looks like there was a Solar alert in your area. {Alert}. When solar power output drops you have to"
                " buy electricity from the grid to keep your house going. Check out this cool guide on net metering and"
                " how it effects your solar array: https://en.wikipedia.org/wiki/Net_metering")
