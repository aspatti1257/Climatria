import unittest
from src.backend.User import User
from src.database.UserDAO import UserDAO
from src.database.CredentialParser import CredentialParser


class UserDAOTest(unittest.TestCase):

    def setUp(self):
        parser = CredentialParser("../../credentials.txt")
        creds = parser.fetch_credentials()
        self.dao = UserDAO(creds[0], creds[1], "test_users")  # DO NOT REMOVE "test_users" argument!
        self.dao.truncate()

    def tearDown(self):
        self.dao.shut_down()

    def test_create_user(self):
        user_id = "bob@test.com"
        user = User(user_id, "bob", "ISNE", 42.3552, -71.06578, None)
        self.dao.create(user)

        user_from_db = self.dao.fetch(user_id)
        assert user_from_db is not None
        assert user_from_db == user

    def test_delete_user(self):
        user1_id = "ann@test.com"
        user1 = User(user1_id, "ann", "ISNE", 42.3552, -71.06578, None)
        self.dao.create(user1)

        user2_id = "jen@test.com"
        user2 = User(user2_id, "jen", "ISNE", 42.3552, -71.06578, None)
        self.dao.create(user2)

        self.dao.delete(user1_id)
        user_1_from_db = self.dao.fetch(user1_id)
        user_2_from_db = self.dao.fetch(user2_id)

        assert user_1_from_db is None
        assert user_2_from_db is not None
        assert user_2_from_db == user2

    def test_truncate(self):
        user1_id = "ann@test.com"
        user1 = User(user1_id, "ann", "ISNE", 42.3552, -71.06578, None)
        self.dao.create(user1)

        user2_id = "jen@test.com"
        user2 = User(user2_id, "jen", "ISNE", 42.3552, -71.06578, None)
        self.dao.create(user2)

        self.dao.truncate()
        user_1_from_db = self.dao.fetch(user1_id)
        user_2_from_db = self.dao.fetch(user2_id)

        assert user_1_from_db is None
        assert user_2_from_db is None
