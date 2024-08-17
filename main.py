import time

from src.LoggerFactory import LoggerFactory
from src.database.UserDAO import UserDAO
from src.backend.ProcessingPipeline import ProcessingPipeline

log = LoggerFactory.create_log(__name__)


def main():
    log.info("Initiating Mongo Connection")
    dao = UserDAO()

    log.info("Starting internal and external data scan")
    while True:
        pipeline = ProcessingPipeline(dao)
        pipeline.process()
        time.sleep(600)  # ten minute wait between processing


if __name__ == "__main__":
    main()
