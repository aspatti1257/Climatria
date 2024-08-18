import pandas as pd
import requests

from src.backend.external.AbstractExternalCaller import AbstractExternalCaller
from src.backend.ArimaResult import ArimaResult


class WaterQualityCaller(AbstractExternalCaller):

    def __init__(self, lat, long):
        self.lat = lat
        self.long = long
        super().__init__()

    def fetch_timeseries_data(self) -> (pd.DataFrame(), 0):
        # TODO: This doesn't work. Needs to be fixed up.
        url = "https://labs-beta.usgs.gov/monitoring-location/graphql"

        body = {
            "operationName": "GetLocations",
            "query": "\n  query GetLocations (\n    $northEastBound: InputPoint!,\n    $southWestBound: InputPoint!,\n    $locationTypes: [MonitoringLocationSiteType!],\n    $ageOfDataYear: Int,\n    $keywords: [String!],\n    $ivDataOnly: Boolean\n    ) {\n    getByBoundingBox(\n      northEastBound: $northEastBound,\n      southWestBound: $southWestBound,\n      locationTypes: $locationTypes,\n      ageOfDataYear: $ageOfDataYear,\n      keywords: $keywords,\n      ivDataOnly: $ivDataOnly\n    ) {\n      count\n      features {\n        type\n        geometry {\n          type\n          coordinates\n        }\n        properties {\n          id\n          agencyCd\n          locationType\n          locationSubType\n          locationName\n          locationNumber\n          keywords\n        }\n      }\n    }\n  }",
            "variables": {
                "northEastBound": {
                    "x": -88.10186999999998,
                    "y": 44.42120000000004
                },
                "southWestBound": {
                    "x": -87.91786999999998,
                    "y": 44.60520000000004
                },
                "locationTypes": [
                    "SURFACE_WATER"
                ],
                "ageOfDataYear": 2018,
                "keywords": [
                    "Turbidity",
                    "pH"
                ],
                "ivDataOnly": False
            }
        }
        try:
            response = requests.post(url=url, json=body)
            print("response status code: ", response.status_code)
            if response.status_code == 200:
                print("response : ", response.content)
        except Exception as e:
            print(e)

        return pd.DataFrame(), 0  # TODO

    def generate_prompt(self, arima_result: ArimaResult) -> str:
        return ("It looks like there was a Water Quality alert in your area. {Alert}. When water quality drops it means"
                " pollution or algae is effecting the water you use to eat, drink, shower. While sometimes its hard to "
                "effect change in your specific area around water quality you can support an organization "
                "like https://water.org to help ensure others have consistently clean water")
