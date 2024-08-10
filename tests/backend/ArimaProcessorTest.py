import unittest
import pandas as pd
from src.backend.ArimaProcessor import ArimaProcessor


class ArimaProcessorTest(unittest.TestCase):

    def setUp(self):
        return

    def tearDown(self):
        return

    def test_processing(self):
        data = pd.Series([0, 0, 1, 1, 2, 2, 3, 3, 2, 2, 1, 1, 0, 0, -1, -1, -2, -2, -3, -3, -2, -2, -1, -1])
        holdout_val = 0

        processor = ArimaProcessor(data, holdout_val)
        result = processor.analyze()
        assert not result