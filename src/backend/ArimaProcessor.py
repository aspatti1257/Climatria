from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
from src.LoggerFactory import LoggerFactory
import itertools


class ArimaProcessor:

    __log = LoggerFactory.create_log(__name__)

    def __init__(self, inputs, holdout_val):
        self.inputs = inputs
        self.holdout_val = holdout_val

    def analyze(self) -> bool:  # TODO: Don't return a simple bool but forecast, confidence intervals.
        adf_inputs = self._adf_test()

        top_model = self._iterate_hyperparams(adf_inputs)
        forecast = top_model.fit().get_forecast(steps=1)
        conf_int = forecast.conf_int(alpha=0.05)
        yhat = forecast.predicted_mean
        self.__log.info(yhat)  # Forecasted values
        self.__log.info(conf_int)  # Confidence intervals
        return bool(conf_int.iloc[0]["upper y"] < self.holdout_val)

    # Perform an augmented Dickey Fuller Test
    def _adf_test(self):
        adf_test = adfuller(self.inputs)
        # self.log.info('ADF Stat determined to be: ', str(adf_test[0]))
        # self.log.info('p-value: ', str(adf_test[1]))
        if adf_test[1] > 0.05:
            return self.inputs.diff().dropna()
        else:
            return self.inputs

    def _iterate_hyperparams(self, adf_inputs):
        # Heavily adapted from https://medium.com/pythons-gurus/arima-model-selection-and-hyperparameter-tuning-7e53f687596a
        p = d = q = range(0, 4)
        pdq = list(itertools.product(p, d, q))
        best_aic = float("inf")
        best_pdq = None
        top_model = None
        for param in pdq:
            try:
                model = ARIMA(adf_inputs.astype(float), order=param)
                results = model.fit()
                if results.aic < best_aic:
                    best_aic = results.aic
                    best_pdq = param
                    top_model = model
            except ValueError as e:
                self.__log.error(e)
                continue
        self.__log.info(best_pdq)
        return top_model

