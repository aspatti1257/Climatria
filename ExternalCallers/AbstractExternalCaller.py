from abc import ABC, abstractmethod

import pandas as pd
from LoggerFactory import LoggerFactory


class AbstractExternalCaller(ABC):

    log = LoggerFactory.create_log(__name__)

    def __init__(self):
        return

    @abstractmethod
    def fetch_timeseries_data(self) -> pd.DataFrame:
        pass
