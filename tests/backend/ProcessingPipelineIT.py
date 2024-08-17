import unittest
from src.backend.ProcessingPipeline import ProcessingPipeline
from src.database.UserDAO import UserDAO
from src.backend.User import User
from datetime import datetime, timedelta


# A full test for the entire passive data processing pipeline.
class ProcessingPipelineIT(unittest.TestCase):

    def setUp(self):
        self.dao = UserDAO("test_users")
        self.dao.truncate()

    def tearDown(self):
        pass

    def __populate_mongo(self, user):
        self.dao.create(user)

    def test_full_pipeline(self):
        self.__populate_mongo(User("bob@test.com", "bob", "12033824115", "ISNE", 12345))
        pipeline = ProcessingPipeline(self.dao)
        pipeline.process()

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

