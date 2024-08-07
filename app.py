import requests
import schedule
from threading import Thread
import time
from flask import Flask

from LoggerFactory import LoggerFactory

log = LoggerFactory.create_log(__name__)
app = Flask(__name__)
import external.flask.FlaskApp # Not unused!


def main():
    # TODO - figure out if this needs to use multiprocessing or not.
    # thread = Thread(target=scanning_thread)
    # thread.start()
    # thread.join()

    setup_flask()
    # Schedule the job to run every day at time X


def scanning_thread():
    log.info("Starting internal and external data scan")
    while True:
        fetch_users()
        scan_resources()
        time.sleep(1)


def setup_flask():
    local_host = "127.0.0.1"
    port = 8080
    log.info("Setting up the Flask application on host: %s and port %s.", local_host, port)

    app.run(host=local_host, port=port, debug=True)


# @app.route("/")
# def index():
#     return "Congratulations, it's a web app!"

def fetch_users():
    #TODO: implement
    pass

def scan_resources():
    # TODO: implement
    pass


if __name__ == "__main__":
    main()
