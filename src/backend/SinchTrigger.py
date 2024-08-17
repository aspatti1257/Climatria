import re

import sinch.domains.sms.exceptions
from sinch import SinchClient
from sinch.domains.verification import StartVerificationResponse
from sinch.domains.verification import ReportVerificationByIdResponse

from src.LoggerFactory import LoggerFactory
from sinch.domains.verification.models import VerificationIdentity


class SinchTrigger:

    __log = LoggerFactory.create_log(__name__)
    __SENDING_PHONE_NUMBER = "12085813502"

    def __init__(self):
        self.__sinch_client = SinchClient(
            key_id="138af651-4dac-469f-8eeb-e46e5669230d",
            key_secret="9i.bJXxg1PKgV7QCh.iCCpBPKn",
            project_id="542c4b93-d223-4715-bf18-8497abc5e435",
            application_key="4555caf5-3bc8-408e-aca1-1c8628deee68",
            application_secret="lz5ZlO9YSE+lgUgdV/Nixw==",
        )
        self.send_count = 0

    def attempt_send_text(self, msg, phone_number) -> bool:
        if phone_number is None:
            self.__log.info("Unable to send. No phone number provided.")
            return False

        formatted_phone = self.__format_number(phone_number)

        if not re.search(re.compile("^\\+\\d{11}$"), formatted_phone):
            self.__log.info("Improperly formatted phone number: %s", formatted_phone)
            return False

        successful = self.__send_text(msg, formatted_phone)
        if successful:
            self.send_count += 1
        return successful

    def __send_text(self, msg, formatted_phone) -> bool:
        try:
            send_batch_response = self.__sinch_client.sms.batches.send(
                body=msg,
                to=[f"{formatted_phone}"],
                from_=self.__SENDING_PHONE_NUMBER,
                delivery_report="none",
                feedback_enabled=True
            )
            self.__log.debug("Successfully sent text message: %s", send_batch_response)
            return True
        except sinch.domains.sms.exceptions.SMSException as exception:
            self.__log.error("Failed to send text message: %s", exception)
            return False

    def attempt_verify(self, phone_number) -> StartVerificationResponse | None:
        formatted_phone = self.__format_number(phone_number)
        if not re.search(re.compile("^\\+\\d{11}$"), formatted_phone):
            self.__log.info("Improperly formatted phone number: %s", formatted_phone)
            return None
        try:
            response = self.__start_verify(formatted_phone)
            return response
        except sinch.domains.sms.exceptions.SMSException as exception:
            self.__log.error("Failed to start sms verification: %s", exception)
            return None
        except Exception as exception:
            self.__log.error("Failed to start sms verification: %s", exception)
            return None

    def __start_verify(self, phone_number):
        response = self.__sinch_client.verification.verifications.start_sms(
            identity=VerificationIdentity(
                type="number",
                endpoint=phone_number
            )
        )
        self.__log.info("Verified SMS with identity: %s", response)
        return response

    def report_code(self, report_id, code) -> ReportVerificationByIdResponse:
        response = self.__sinch_client.verification.verifications.report_by_id(
            id=report_id,
            verification_report_request={
                "code": code
            }
        )
        return response

    @staticmethod
    def __format_number(phone_number):
        formatted_number = phone_number.strip().replace("-", "")
        if formatted_number.startswith("+"):
            return formatted_number
        else:
            return "+" + formatted_number
