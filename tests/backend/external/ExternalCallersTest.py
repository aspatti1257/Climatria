import unittest
from src.backend.external.GridDataCaller import GridDataCaller
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

    def test_msg_generation(self):
        caller = GridDataCaller("ISNE")
        yhat = pd.Series([float(1)])
        conf_int = pd.DataFrame([[0, 1.5]], columns=["lower y", "upper y"])
        arima_result = ArimaResult(True, yhat, conf_int)
        msg = caller.generate_prompt(arima_result)
        assert msg is not None

