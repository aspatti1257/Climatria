from src.backend.external.GridDataCaller import GridDataCaller
from src.backend.external.UltraVioletCaller import UltraVioletCaller
from src.backend.ArimaProcessor import ArimaProcessor
from src.backend.SinchTrigger import SinchTrigger
from src.backend.SMTPTrigger import SMTPTrigger
from src.LoggerFactory import LoggerFactory
from datetime import datetime, timedelta


class ProcessingPipeline:

    __log = LoggerFactory.create_log(__name__)

    def __init__(self, dao):
        self.__dao = dao
        self.__phone_trigger = SinchTrigger()
        self.__email_trigger = SMTPTrigger()

    def process(self):
        users = self.__dao.find_all()
        self.__fetch_climate_data(users)

    def __cleanup(self):
        self.__email_trigger.close_connection()

    def __fetch_climate_data(self, users):
        for user in users:  # TODO: Multi-threading
            if self.__user_is_eligible(user):
                alerts = []
                for caller in [UltraVioletCaller(user.zip_code), GridDataCaller(user.ba)]:
                    historical_data, holdout = caller.fetch_timeseries_data()
                    if len(historical_data) > 0 and historical_data.nunique() > 1:
                        processor = ArimaProcessor(historical_data, holdout)
                        arima_result = processor.analyze()
                        if arima_result.should_alert:
                            alerts.append(caller.generate_prompt(arima_result))
                if len(alerts) > 0:
                    self.__process_alert("\n\n".join(alerts), user)

        total_sends = self.__phone_trigger.send_count + self.__email_trigger.send_count
        self.__log.info("Parsed %s total users and sent %s total triggers.", len(users), total_sends)
        self.__cleanup()

    def __process_alert(self, msg, user):
        successful_send = self.__attempt_send(msg, user)
        if successful_send:
            user.last_alert = datetime.now().isoformat(timespec='milliseconds')
            self.__dao.update(user)
        else:
            self.__log.debug("Failed to send both phone and email for user %s.", user)

    def __attempt_send(self, msg, user) -> bool:
        text_result = self.__phone_trigger.attempt_send_text(msg, user.phone_number)
        return text_result if text_result else self.__email_trigger.attempt_send_email(msg, user.get_id())

    # TODO: Can work this directly into the Mongo query
    @staticmethod
    def __user_is_eligible(user):
        yesterday = datetime.now() - timedelta(days=1)

        return (user.phone_number is not None and
                user.ba is not None and
                (user.last_alert is None or user.last_alert < yesterday))
