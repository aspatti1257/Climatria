import os
import requests
import pandas as pd
import pgeocode
from datetime import datetime, timedelta
from src.LoggerFactory import LoggerFactory
from src.backend.ArimaResult import ArimaResult
from src.backend.external.AbstractExternalCaller import AbstractExternalCaller


class UltraVioletCaller(AbstractExternalCaller):

    __log = LoggerFactory.create_log(__name__)

    MEERSENS_API_KEY = os.getenv("MEERSENS_API_KEY")
    BASE_URL = f"https://api.meersens.com/environment/public"

    def __init__(self, zip_code):
        (lat, long) = self.__zip_to_lat_long(zip_code)

        self.lat = lat
        self.long = long
        super().__init__()

    def __zip_to_lat_long(self, zip_code):
        nomi = pgeocode.Nominatim('us')  # TODO: expand to other countries
        query = nomi.query_postal_code(zip_code)

        return query["latitude"], query["longitude"]

    def fetch_timeseries_data(self) -> (pd.DataFrame(), float):
        try:
            historical_data = self.__extract_historical_data()
            holdout = self.__extract_current_data()
            return historical_data, float(holdout)
        except Exception as e:
            self.__log.error(e)
            return pd.DataFrame(), 0

    def __extract_historical_data(self) -> pd.DataFrame():
        today = datetime.now()
        six_months_ago = today - timedelta(days=180)
        history_response = requests.get(f"{self.BASE_URL}/uv/history", headers={
            "apikey": self.MEERSENS_API_KEY
        }, params={
            "lat": self.lat,
            "lng": self.long,
            "from": six_months_ago.strftime("%Y-%m-%d"),
            "to": today.strftime("%Y-%m-%d"),
            "page": 1  # TODO: Paginate properly and fetch in a loop. (This can get expensive)
        })
        self.__log.info("Successfully fetched historical UV data via Meersens for longLat: [%s, %s]", self.long, self.lat)
        json_response = history_response.json()
        values = json_response["values"]
        return pd.json_normalize(values)["pollutants.uvi.value"]

    def __extract_current_data(self) -> float:
        current_response = requests.get(f"{self.BASE_URL}/uv/current", headers={
            'apikey': self.MEERSENS_API_KEY
        }, params={
            "lat": self.lat,
            "lng": self.long,
        })
        self.__log.info("Successfully fetched current UV data via Meersens for longLat: [%s,%s]", self.long, self.lat)
        json_response = current_response.json()
        return json_response["pollutants"]["uvi"]["index"]["value"]

    def generate_prompt(self, arima_result: ArimaResult) -> str:
        # TODO
        return "Looks like there is a high UV output in your area."
