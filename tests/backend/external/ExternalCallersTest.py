import unittest
from src.backend.external.GridDataCaller import GridDataCaller
from src.backend.external.SolarOutputCaller import SolarOutputCaller
from src.backend.external.WaterQualityCaller import WaterQualityCaller
from src.backend.external.UltraVioletCaller import UltraVioletCaller
from src.backend.ArimaResult import ArimaResult
import pandas as pd


class ExternalCallersTest(unittest.TestCase):

    def setUp(self):
        return

    def tearDown(self):
        return

    def test_eia_data(self):
        caller = GridDataCaller("ISNE")
        data, holdout = caller.fetch_timeseries_data()
        assert data is not None
        assert len(data) > 0
        assert type(holdout) is float

    def test_bogus_eia_data(self):
        caller = GridDataCaller("BOGUS")
        data, holdout = caller.fetch_timeseries_data()
        assert data is not None
        assert len(data) == 0
        assert holdout == 0

    def test_solar_data(self):
        caller = SolarOutputCaller(42.39426863401848, -71.10615991672452)
        data, holdout = caller.fetch_timeseries_data()

        assert True

    def test_water_data(self):
        caller = WaterQualityCaller(1, 2)

        data, holdout = caller.fetch_timeseries_data()
        assert True

    def test_uv_data(self):
        caller = UltraVioletCaller("02145")
        data, holdout = caller.fetch_timeseries_data()

        assert data is not None
        assert len(data) > 0
        assert type(holdout) is float


    def test_msg_generation(self):
        caller = GridDataCaller("ISNE")
        yhat = pd.Series([float(1)])
        conf_int = pd.DataFrame([[0, 1.5]], columns=["lower y", "upper y"])
        arima_result = ArimaResult(True, yhat, conf_int)
        msg = caller.generate_prompt(arima_result)
        assert msg is not None
        assert str(conf_int.iloc[0]["upper y"]) in msg



