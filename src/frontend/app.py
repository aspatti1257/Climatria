from flask import Flask

from src.LoggerFactory import LoggerFactory

log = LoggerFactory.create_log(__name__)
app = Flask(__name__)

def setup_flask():
    local_host = "127.0.0.1"
    port = 8080
    log.info("Setting up the Flask application on host: %s and port %s.", local_host, port)

    app.run(host=local_host, port=port, debug=True)


@app.route('/', methods=['GET'])
def root():
    return 'basic app works'


@app.route('/signup', methods=['PUT'])
def signup(foo):
    # TODO
    return "stuff happened " + foo


setup_flask()
