import time

from src.LoggerFactory import LoggerFactory

log = LoggerFactory.create_log(__name__)

def main():
    log.info("Starting internal and external data scan")
    while True:
        fetch_users()
        scan_resources()
        time.sleep(1)


def fetch_users():
    #TODO: implement
    pass


def scan_resources():
    # TODO: implement
    pass


if __name__ == "__main__":
    main()
