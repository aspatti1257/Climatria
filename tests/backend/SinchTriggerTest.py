import unittest
from src.backend.SinchTrigger import SinchTrigger
from unittest.mock import patch, PropertyMock


class SinchTriggerTest(unittest.TestCase):

    @patch.object(SinchTrigger, '_SinchTrigger__send_text', new_callable=PropertyMock)
    def test_valid_phone_send(self, mock__send_text):
        mock__send_text.send.return_value = "test"
        trigger = SinchTrigger()

        valid_nums = [
            "15555555555",
            "1-555-555-5555",
            "1-555-555-5555   ",
            "   1-555-555-5555"
        ]

        for num in valid_nums:
            result = trigger.maybe_send_text("foo", num)
            assert result is not None

    def test_invalid_phone_number(self):
        invalid_nums = [
            "5555555555",  # not 11 digits
            "555-5555",    # not 11 digits
            None
        ]

        for num in invalid_nums:
            trigger = SinchTrigger()
            response = trigger.maybe_send_text("foo", num)
            assert response is None
