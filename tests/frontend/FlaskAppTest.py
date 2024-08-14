import unittest
from flask import Flask

app = Flask(__name__)
# import external.flask.FlaskApp  # Not unused


# This doesn't work yet. Need to figure out how to properly test.
class FlaskAppTest(unittest.TestCase):

    def setUp(self):
        pass


    def tearDown(self):
        pass

    def test_basic_app(self):
        assert True

        