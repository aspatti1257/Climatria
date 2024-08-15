import sys
import os

# Add the root directory of the project to the PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from flask import Flask
from routes.UserRoutes import user_blueprint
from src.LoggerFactory import LoggerFactory

# Set up the logger
log = LoggerFactory.create_log(__name__)

app = Flask(__name__)

# Register the blueprint
app.register_blueprint(user_blueprint)


def setup_flask():
    local_host = "127.0.0.1"
    port = 8080
    log.info("Setting up the Flask application on host: %s and port %s.", local_host, port)

    app.run(host=local_host, port=port, debug=True)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response


@app.route('/', methods=['GET'])
def root():
    return 'basic app works'


setup_flask()