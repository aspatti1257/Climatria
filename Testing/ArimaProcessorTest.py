import unittest
import pandas as pd
from ArimaProcessor import ArimaProcessor


class ArimaProcessorTest(unittest.TestCase):

    def set_up(self):
        return

    def tear_down(self):
        return

    def test_processing(self):
        data = pd.Series([0, 0, 1, 1, 2, 2, 3, 3, 2, 2, 1, 1, 0, 0, -1, -1, -2, -2, -3, -3, -2, -2, -1, -1])

        processor = ArimaProcessor(data)
        processor.analyze()

        assert True