from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
from LoggerFactory import LoggerFactory


class ArimaProcessor:

    log = LoggerFactory.create_log(__name__)

    def __init__(self, inputs):
        self.inputs = inputs

    def analyze(self) -> bool:
        inputs = self.adf_test()

        # TODO: Iterate hyperparams to find best values.
        p = 0
        d = 0
        q = 0

        model = ARIMA(inputs, order=(p, d, q))

        model_fit = model.fit()
        # model_fit.predict()
        return True

    # Perform an augmented Dickey Fuller Test
    def adf_test(self):
        adf_test = adfuller(self.inputs)
        # self.log.info('ADF Stat determined to be: ', str(adf_test[0]))
        # self.log.info('p-value: ', str(adf_test[1]))
        if adf_test[1] > 0.05:
            return self.inputs.diff().dropna()
        else:
            return adf_test
