import requests
import schedule
import time

from LoggerFactory import LoggerFactory

log = LoggerFactory.create_log(__name__)


def main():
    # Schedule the job to run every day at time X
    while True:
        fetch_users()
        scan_resources()
        time.sleep(60)


def fetch_users():
    #TODO: implement
    pass

def scan_resources():
    # TODO: implement
    pass


if __name__ == "__main__":
    main()
