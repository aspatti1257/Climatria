import unittest
from src.backend.external.GridDataCaller import GridDataCaller


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

