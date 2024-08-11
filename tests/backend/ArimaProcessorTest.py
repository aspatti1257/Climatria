import unittest
import pandas as pd
from src.backend.ArimaProcessor import ArimaProcessor


class ArimaProcessorTest(unittest.TestCase):

    def setUp(self):
        self.data = pd.Series([0, 0, 1, 1, 2, 2, 3, 3, 2, 2, 1, 1, 0, 0, -1, -1, -2, -2, -3, -3, -2, -2, -1, -1])

    def tearDown(self):
        return

    def test_processing_no_alert(self):
        holdout_val = 0

        processor = ArimaProcessor(self.data, holdout_val)
        result = processor.analyze()
        assert result is not None
        assert not result.should_alert
        assert bool(result.conf_int.iloc[0]["upper y"] > 1.9)

    def test_processing_with_alert(self):
        holdout_val = 3

        processor = ArimaProcessor(self.data, holdout_val)
        result = processor.analyze()
        assert result is not None
        assert result.should_alert
        assert bool(result.conf_int.iloc[0]["upper y"] > 1.9)