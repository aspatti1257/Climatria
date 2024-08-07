import unittest
from flask import Flask

app = Flask(__name__)
# import external.flask.FlaskApp  # Not unused

# This doesn't work yet. Need to figure out how to properly test.
class FlaskAppTest(unittest.TestCase):

    def setUp(self):
        local_host = "127.0.0.1"
        port = 8080
        app.run(host=local_host, port=port, debug=True)
        return

    def tearDown(self):
        app.url_map._rules.clear()
        return

    def test_basic_app(self):
        assert True

        