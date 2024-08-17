from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
from src.LoggerFactory import LoggerFactory
from src.backend.ArimaResult import ArimaResult
import itertools


class ArimaProcessor:

    __log = LoggerFactory.create_log(__name__)

    def __init__(self, inputs, holdout_val):
        self.inputs = inputs
        self.holdout_val = holdout_val

    def analyze(self) -> ArimaResult:
        adf_inputs = self.__adf_test()

        top_model = self.__iterate_hyperparams(adf_inputs)
        forecast = top_model.fit().get_forecast(steps=1)
        conf_int = forecast.conf_int(alpha=0.05)
        yhat = forecast.predicted_mean
        self.__log.info("Predicted mean from top model: %s", yhat)  # Forecasted values
        self.__log.info("Confidence intervals from top model prediction %s", conf_int)  # Confidence intervals

        return self.__build_result(conf_int, yhat)

    # Perform an augmented Dickey Fuller Test
    def __adf_test(self):
        adf_test = adfuller(self.inputs)
        self.__log.info("ADF Stat determined to be: %s", str(adf_test[0]))
        self.__log.info("p-value: %s", str(adf_test[1]))
        if adf_test[1] > 0.05:
            return self.inputs.diff().dropna()
        else:
            return self.inputs

    def __iterate_hyperparams(self, adf_inputs):
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
                self.__log.error("Error while performing ARIMA estimation: %s", e)
                continue
        self.__log.info("Best hyperparams (p, d, q) for ARIMA model chosen to be %s.", best_pdq)
        return top_model

    def __build_result(self, conf_int, yhat) -> ArimaResult:
        return ArimaResult(bool(conf_int.iloc[0]["upper y"] < self.holdout_val), yhat, conf_int)


