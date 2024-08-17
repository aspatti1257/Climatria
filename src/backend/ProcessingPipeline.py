from src.backend.external.GridDataCaller import GridDataCaller
from src.backend.ArimaProcessor import ArimaProcessor
from src.backend.SinchTrigger import SinchTrigger
from src.LoggerFactory import LoggerFactory
from datetime import datetime, timedelta


class ProcessingPipeline:

    __log = LoggerFactory.create_log(__name__)

    def __init__(self, dao):
        self.__dao = dao
        self.__trigger = SinchTrigger()

    def process(self):
        users = self.__dao.find_all()
        self.__fetch_climate_data(users)

    def __fetch_climate_data(self, users):
        for user in users:  # TODO: Multi-threading
            if self.__user_is_eligible(user):
                grid_data_caller = GridDataCaller(user.ba)
                grid_data, holdout = grid_data_caller.fetch_timeseries_data()
                if len(grid_data) > 0:
                    processor = ArimaProcessor(grid_data, holdout)
                    arima_result = processor.analyze()
                    if arima_result.should_alert:
                        msg = grid_data_caller.generate_prompt(arima_result)
                        result = self.__trigger.maybe_send_text(msg, user.phone_number)
                        if result is not None:
                            user.last_alert = datetime.now().isoformat(timespec='milliseconds')
                            self.__dao.update(user)

        self.__log.info("Parsed %s total users and sent %s total triggers.", len(users), self.__trigger.send_count)

    # TODO: Can work this directly into the Mongo query
    @staticmethod
    def __user_is_eligible(user):
        yesterday = datetime.now() - timedelta(days=1)

        return (user.phone_number is not None and
                user.ba is not None and
                (user.last_alert is None or user.last_alert < yesterday))
