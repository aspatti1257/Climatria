from src.backend.external.GridDataCaller import GridDataCaller
from src.backend.ArimaProcessor import ArimaProcessor
from src.backend.SinchTrigger import SinchTrigger


class ProcessingPipeline:

    def __init__(self, dao):
        self.dao = dao

    def process(self):
        users = self.dao.find_all()
        self.__fetch_climate_data(users)

    def __fetch_climate_data(self, users):
        trigger = SinchTrigger()
        for user in users:
            grid_data_caller = GridDataCaller(user.ba)
            grid_data, holdout = grid_data_caller.fetch_timeseries_data()
            processor = ArimaProcessor(grid_data, holdout)
            arima_result = processor.analyze()
            if arima_result.should_alert:
                msg = grid_data_caller.generate_prompt(arima_result)
                result = trigger.maybe_send_text(msg, user.phone_number)
