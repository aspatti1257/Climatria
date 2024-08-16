import unittest
from src.backend.User import User
from src.database.UserDAO import UserDAO


class UserDAOTest(unittest.TestCase):

    def setUp(self):
        self.dao = UserDAO("test_users")  # DO NOT REMOVE "test_users" argument!
        self.dao.truncate()

    def tearDown(self):
        self.dao.shut_down()

    def test_create_user(self):
        user_id = "bob@test.com"
        user = User(user_id, "bob", None, "ISNE", 12345)
        self.dao.create(user)

        user_from_db = self.dao.find_by_id(user_id)
        assert user_from_db is not None
        assert user_from_db == user

    def __create_two_users(self):
        user1_id = "ann@test.com"
        user1 = User(user1_id, "ann", "15555555555", "ISNE", 12345)
        self.dao.create(user1)

        user2_id = "jen@test.com"
        user2 = User(user2_id, "jen", "1-555-555-5555", "ISNE", 12345)
        self.dao.create(user2)
        return user1, user2

    def test_find_all(self):
        (user1, user2) = self.__create_two_users()

        users = self.dao.find_all()
        assert len(users) == 2
        assert users[0] == user1
        assert users[1] == user2

    def test_delete_user(self):
        (user1, user2) = self.__create_two_users()

        self.dao.delete(user1._id)
        user_1_from_db = self.dao.find_by_id(user1._id)
        user_2_from_db = self.dao.find_by_id(user2._id)

        assert user_1_from_db is None
        assert user_2_from_db is not None
        assert user_2_from_db == user2

    def test_truncate(self):
        (user1, user2) = self.__create_two_users()

        self.dao.truncate()
        user_1_from_db = self.dao.find_by_id(user1._id)
        user_2_from_db = self.dao.find_by_id(user2._id)

        assert user_1_from_db is None
        assert user_2_from_db is None
