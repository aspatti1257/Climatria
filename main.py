import time

from src.LoggerFactory import LoggerFactory
from src.database.UserDAO import UserDAO
from src.database.CredentialParser import CredentialParser
from src.backend.ProcessingPipeline import ProcessingPipeline

log = LoggerFactory.create_log(__name__)


def main():
    log.info("Initiating Mongo Connection")
    dao = init_db_connection()

    log.info("Starting internal and external data scan")
    while True:
        pipeline = ProcessingPipeline(dao)
        pipeline.process()
        time.sleep(600)  # ten minute wait between processing


def init_db_connection():
    parser = CredentialParser("credentials.txt")
    creds = parser.fetch_credentials()
    dao = UserDAO(creds[0], creds[1])
    return dao


if __name__ == "__main__":
    main()
