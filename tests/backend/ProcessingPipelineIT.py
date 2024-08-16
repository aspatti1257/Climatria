import unittest
from src.backend.ProcessingPipeline import ProcessingPipeline
from src.database.UserDAO import UserDAO
from src.backend.User import User


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
