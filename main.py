import time

from src.LoggerFactory import LoggerFactory
from src.database.UserDAO import UserDAO
from src.database.CredentialParser import CredentialParser
from src.backend.external.GridDataCaller import GridDataCaller
from src.backend.ArimaProcessor import ArimaProcessor
from src.backend.SinchTrigger import SinchTrigger

log = LoggerFactory.create_log(__name__)


def main():
    log.info("Initiating Mongo Connection")
    dao = init_db_connection()

    log.info("Starting internal and external data scan")
    while True:
        users = fetch_users(dao)
        scan_resources(users)
        time.sleep(60)


def init_db_connection():
    parser = CredentialParser("credentials.txt")
    creds = parser.fetch_credentials()
    dao = UserDAO(creds[0], creds[1])
    return dao


def fetch_users(dao):
    return dao.fetch_users()


def scan_resources(users):
    trigger = SinchTrigger()
    for user in users:
        grid_data_caller = GridDataCaller(user.ba)
        grid_data_caller.fetch_timeseries_data()
        processor = ArimaProcessor(grid_data_caller)
        should_alert = processor.analyze()
        if should_alert:
            result = trigger.maybe_send_text("test", user.phone_number)


if __name__ == "__main__":
    main()
