import pandas as pd

from src.backend.external.AbstractExternalCaller import AbstractExternalCaller
from src.backend.ArimaResult import ArimaResult
from src.LoggerFactory import LoggerFactory
import pvlib
import datetime
import requests
import os


class SolarOutputCaller(AbstractExternalCaller):

    __log = LoggerFactory.create_log(__name__)

    __NREL_API_KEY = os.getenv("NREL_API_KEY")
    __NREL_API_EMAIL = os.getenv("NREL_API_EMAIL")

    def __init__(self, lat, long):
        self.lat = lat
        self.long = long
        super().__init__()

    def fetch_timeseries_data(self) -> (pd.DataFrame(), 0):
        # TODO: In order for this to work we need current solar data. Not just historical.
        # year = datetime.datetime.now().year
        year = 2022
        try:
            solar_weather_timeseries, solar_weather_metadata = pvlib.iotools.get_psm3(
                latitude=self.lat,
                longitude=self.long,
                names=year,
                api_key=self.__NREL_API_KEY,
                email=self.__NREL_API_EMAIL,
                map_variables=True,
                leap_day=True,
            )
        except requests.HTTPError as err:
            self.__log.error(err.response.text)


        return pd.DataFrame(), 0

    def generate_prompt(self, arima_result: ArimaResult) -> str:
        return ("It looks like there was a Solar alert in your area. {Alert}. When solar power output drops you have to"
                " buy electricity from the grid to keep your house going. Check out this cool guide on net metering and"
                " how it effects your solar array: https://en.wikipedia.org/wiki/Net_metering")
