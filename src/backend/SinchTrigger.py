import re

from sinch import SinchClient
from src.LoggerFactory import LoggerFactory


class SinchTrigger:

    __log = LoggerFactory.create_log(__name__)
    __SENDING_PHONE_NUMBER = "12085813502"

    def __init__(self):
        self.sinch_client = SinchClient(
            key_id="138af651-4dac-469f-8eeb-e46e5669230d",
            key_secret="9i.bJXxg1PKgV7QCh.iCCpBPKn",
            project_id="542c4b93-d223-4715-bf18-8497abc5e435"
        )
        self.send_count = 0

    def maybe_send_text(self, msg, phone_number):
        if phone_number is None:
            self.__log.info("Unable to send. No phone number provided.")
            return None

        formatted_phone = phone_number.strip().replace("-", "")

        if not re.search(re.compile("^\\d{11}$"), formatted_phone):
            self.__log.info("Improperly formatted phone number: %s", formatted_phone)
            return None

        return self.__send_text(msg, formatted_phone)

    def __send_text(self, msg, formatted_phone):
        send_batch_response = self.sinch_client.sms.batches.send(
            body=msg,
            to=[f"{formatted_phone}"],
            from_=self.__SENDING_PHONE_NUMBER,
            delivery_report="none",
            feedback_enabled=True
        )
        self.__log.info(send_batch_response)
        self.send_count += 1
        return send_batch_response
