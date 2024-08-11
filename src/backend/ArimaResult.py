class ArimaResult:

    def __init__(self, should_alert, yhat, conf_int):
        self.should_alert = should_alert
        self.yhat = yhat
        self.conf_int = conf_int
