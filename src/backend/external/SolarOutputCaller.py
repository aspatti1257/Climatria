import pandas as pd

from src.backend.external.AbstractExternalCaller import AbstractExternalCaller
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
