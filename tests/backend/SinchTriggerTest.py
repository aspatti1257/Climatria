import unittest
from src.backend.SinchTrigger import SinchTrigger
from unittest.mock import patch, PropertyMock


class SinchTriggerTest(unittest.TestCase):

    def setUp(self):
        self.trigger = SinchTrigger()

    def tearDown(self):
        pass

    @patch.object(SinchTrigger, '_SinchTrigger__send_text', new_callable=PropertyMock)
    def test_valid_phone_send(self, mock__send_text):
        mock__send_text.send.return_value = True

        valid_nums = [
            "15555555555",
            "1-555-555-5555",
            "1-555-555-5555   ",
            "   1-555-555-5555"
        ]

        for num in valid_nums:
            result = self.trigger.attempt_send_text("foo", num)
            assert result
        assert self.trigger.send_count == len(valid_nums)

    def test_invalid_phone_number(self):
        invalid_nums = [
            "5555555555",  # not 11 digits
            "555-5555",    # not 11 digits
            None
        ]

        for num in invalid_nums:
            response = self.trigger.attempt_send_text("foo", num)
            assert not response
        assert self.trigger.send_count == 0

    @patch.object(SinchTrigger, '_SinchTrigger__start_verify', new_callable=PropertyMock)
    def test_verify_valid(self, mock_verify):
        mock_verify.send.return_value = True
        response = self.trigger.attempt_verify("+15555555555")
        assert response is not None

    def test_verify_invalid(self):
        response = self.trigger.attempt_verify("555-555-5555")
        assert response is None
