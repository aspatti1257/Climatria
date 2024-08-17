import unittest
from src.backend.SMTPTrigger import SMTPTrigger
from unittest.mock import patch, PropertyMock


class SMTPTriggerTest(unittest.TestCase):

    def setUp(self):
        self.trigger = SMTPTrigger()

    def tearDown(self):
        self.trigger.close_connection()

    @patch.object(SMTPTrigger, '_SMTPTrigger__send_email', new_callable=PropertyMock)
    def test_send(self, mock_send_email):
        mock_send_email.send.return_value = True
        result = self.trigger.attempt_send_email("Email from test_send", "aspatti1257@gmail.com")
        assert result
        assert self.trigger.send_count == 1

    def test_bogus_email(self):
        result = self.trigger.attempt_send_email("bar", "ClearlyFakeEmail")
        assert not result
