import unittest
import pandas as pd
from src.backend.ProcessingPipeline import ProcessingPipeline
from src.backend.SinchTrigger import SinchTrigger
from src.backend.ArimaProcessor import ArimaProcessor
from src.backend.ArimaResult import ArimaResult
from src.database.UserDAO import UserDAO
from src.backend.User import User
from datetime import datetime, timedelta
from unittest.mock import patch, PropertyMock


# A full test for the entire passive data processing pipeline.
class ProcessingPipelineIT(unittest.TestCase):

    def setUp(self):
        self.dao = UserDAO("test_users")
        self.dao.truncate()

    def tearDown(self):
        pass

    def __populate_mongo(self, user):
        self.dao.create(user)

    @patch.object(SinchTrigger, '_SinchTrigger__send_text', new_callable=PropertyMock)
    @patch.object(ArimaProcessor, '_ArimaProcessor__build_result', new_callable=PropertyMock)
    def test_full_pipeline_text(self, mock__send_text, mock__build_result):
        mock__send_text.send.return_value = "test"
        conf_int = pd.DataFrame([[-0.341145, 1.960193]], columns=["lower y", "upper y"])
        mock__build_result.send.return_value = ArimaResult(True, 2, conf_int)

        user_id = "bob@test.com"
        self.__populate_mongo(User(user_id, "bob", "12033824115", "ISNE", 12345))

        pipeline = ProcessingPipeline(self.dao)
        pipeline.process()

        user_from_db = self.dao.find_by_id(user_id)
        assert user_from_db is not None
        assert user_from_db.last_alert is not None

    def test_bogus_user(self):
        self.__populate_mongo(User("bad@test.com", "bad", "15555555555", "BOGUS", 12345))
        pipeline = ProcessingPipeline(self.dao)
        pipeline.process()

    def test_user_eligibility(self):
        pipeline = ProcessingPipeline(self.dao)

        never_sent = User("bad@test.com", "good", "15555555555", "ISNE", 12345)
        assert pipeline._ProcessingPipeline__user_is_eligible(never_sent)

        sent_last_week = User("bad@test.com", "good", "15555555555", "ISNE", 12345, datetime.now() - timedelta(days=7))
        assert pipeline._ProcessingPipeline__user_is_eligible(sent_last_week)

        sent_today = User("bad@test.com", "bad", "15555555555", "ISNE", 12345, datetime.now() - timedelta(seconds=10))
        assert not pipeline._ProcessingPipeline__user_is_eligible(sent_today)

        no_ba = User("bad@test.com", "bad", "15555555555", None, 12345)
        assert not pipeline._ProcessingPipeline__user_is_eligible(no_ba)

        no_phone_number = User("bad@test.com", "bad", None, "ISNE", 12345)
        assert not pipeline._ProcessingPipeline__user_is_eligible(no_phone_number)

