import os
import re
import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from src.LoggerFactory import LoggerFactory


class SMTPTrigger(object):

    __log = LoggerFactory.create_log(__name__)

    SENDER_EMAIL = "climatria@gmail.com"
    SENDER_PASSWORD = os.getenv("CLIMATRIA_EMAIL_PASSWORD")
    SMTP_SERVER = "smtp.gmail.com"
    PORT = 465

    EMAIL_REGEX = re.compile(r"^\S+@\S+\.\S+$")

    def __init__(self):
        self.__server = self.__build_server()
        self.send_count = 0

    def __build_server(self):
        try:
            server = smtplib.SMTP_SSL(self.SMTP_SERVER, self.PORT)
            server.login(self.SENDER_EMAIL, self.SENDER_PASSWORD)
            return server
        except Exception as error:
            self.__log.error("Unable to connect to email server: %s", error)
            sys.exit(1)

    def attempt_send_email(self, body, receiver_email) -> bool:
        if not self.__validate_email(receiver_email):
            self.__log.error("Invalid email address detected: %s.", receiver_email)
            return False
        successful = self.__send_email(body, receiver_email)
        if successful:
            self.__log.debug("Successfully sent email to %s.", receiver_email)
            self.send_count += 1
        return successful

    def __send_email(self, body, receiver_email) -> bool:
        try:
            content = self.__build_email(body, receiver_email)
            self.__server.sendmail(self.SENDER_EMAIL, receiver_email, content)
            return True
        except Exception as error:
            self.__log.error("Unable to send email: %s", error)
            return False

    def __validate_email(self, receiver_email) -> bool:
        return re.match(self.EMAIL_REGEX, receiver_email) is not None

    def __build_email(self, body, receiver_email) -> str:
        msg = MIMEMultipart()
        msg['From'] = self.SENDER_EMAIL
        msg['To'] = receiver_email
        msg['Subject'] = "Climatria Alert Detected"
        msg.attach(MIMEText(body, 'plain'))
        return msg.as_string()

    def close_connection(self):
        self.__server.quit()
