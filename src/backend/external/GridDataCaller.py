from src.backend.external.AbstractExternalCaller import AbstractExternalCaller
from src.backend.ArimaResult import ArimaResult
import json
import os
import requests
import datetime
import pandas as pd


class GridDataCaller(AbstractExternalCaller):

    EIA_API_KEY = os.getenv('EIA_API_KEY')
    API_URL = f"https://api.eia.gov/v2/electricity/rto/daily-region-data/data/?api_key={EIA_API_KEY}"
    MAX_ROW_COUNT = 5000

    def __init__(self, ba):
        self.__ba = ba
        super().__init__()

    def fetch_timeseries_data(self) -> tuple:
        start_page = 0
        rows_fetched = 0
        df = pd.DataFrame()
        while True:
            offset = start_page * self.MAX_ROW_COUNT
            response_content = self.__recursively_fetch_data(offset)
            df = pd.concat([df, pd.DataFrame(response_content["data"])])

            rows_fetched += len(response_content['data'])
            rows_total = int(response_content["total"])

            if rows_fetched >= rows_total:
                break
            else:
                start_page += 1
        if df.size < 2:
            self._log.info("No data detected for BA: %s.", self.__ba)
            return pd.Series(), 0
        formatted_df, holdout = self.__format_for_analysis(df)
        return formatted_df, holdout

    def __recursively_fetch_data(self, offset):
        today = datetime.date.today()
        end_date = today.isoformat()
        start_date = (today - datetime.timedelta(days=(365 * 10))).isoformat()
        response_content = self.__send_request(self.API_URL, {
            "X-Params": json.dumps(
                {
                    "frequency": "daily",
                    "data": ["value"],
                    "facets": { "timezone": ["Eastern"],
                                "respondent": [self.__ba],
                                "type": ["D", "NG", "TI"]},
                    "start": start_date,
                    "end": end_date,
                    "sort": [{"column": "period", "direction": "desc"}],
                    "offset": offset,
                    "length": self.MAX_ROW_COUNT,
                }
            )
        })

        return response_content

    def __send_request(self, api_url, headers):
        response = requests.get(api_url, headers=headers)

        if response.status_code >= 400:
            self._log.error(f"Response status code from {api_url} is {response.status_code}. "
                            f"Reason for failed request: {response.reason}")
            response.raise_for_status()
        response_content = response.json()
        if "response" in response_content:
            response_content = response_content["response"]

        self._log.info(f"{len(response_content['data'])} rows fetched")
        return response_content

    def __format_for_analysis(self, df) -> (pd.DataFrame, float):
        training_data = df.iloc[:(len(df) - 1)]
        holdout_data = float(df.tail(1)['value'])
        return pd.Series(list(training_data["value"])), holdout_data

    def generate_prompt(self, arima_result: ArimaResult) -> str:
        # TODO: Check units here to make sure this even makes sense.
        max_val = arima_result.conf_int.iloc[0]["upper y"]
        problem = f"Grid usage is above the expected upper confidence level of {max_val} kWh."
        return (f"It looks like there was an Electric Grid alert in your area. {problem}. When the grid gets dirty one"
                " easy thing you can do is buy Renewable Energy Credits to show your support for clean energy, which"
                " you can do here: https://terrapass.com/product/productres-recs/")
