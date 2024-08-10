import unittest
from src.backend.ProcessingPipeline import ProcessingPipeline
from src.database.CredentialParser import CredentialParser
from src.database.UserDAO import UserDAO
from src.backend.User import User


# A full test for the entire passive data processing pipeline.
class ProcessingPipelineIT(unittest.TestCase):

    def setUp(self):
        self.dao = self.__init_mongo()
        self.dao.truncate()
        self.__populate_mongo()

    def tearDown(self):
        pass

    def __init_mongo(self):
        parser = CredentialParser("../../credentials.txt")
        creds = parser.fetch_credentials()
        dao = UserDAO(creds[0], creds[1], "test_users")
        return dao

    def __populate_mongo(self):
        user_id = "bob@test.com"
        user = User(user_id, "bob", "12033824115", "ISNE", 42.3552, -71.06578, None)
        self.dao.create(user)

    def test_full_pipeline(self):
        pipeline = ProcessingPipeline(self.dao)
        pipeline.process()
