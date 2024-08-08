import time

from src.LoggerFactory import LoggerFactory
from src.database.UserDAO import UserDAO
from src.database.CredentialParser import CredentialParser

log = LoggerFactory.create_log(__name__)


def main():
    log.info("Initiating Mongo Connection")
    dao = init_db_connection()

    log.info("Starting internal and external data scan")
    while True:
        fetch_users()
        scan_resources()
        time.sleep(1)


def init_db_connection():
    parser = CredentialParser("credentials.txt")
    creds = parser.fetch_credentials()
    dao = UserDAO(creds[0], creds[1])
    return dao



def fetch_users():
    #TODO: implement
    pass


def scan_resources():
    # TODO: implement
    pass


if __name__ == "__main__":
    main()
