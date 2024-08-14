import logging

import pymongo
import sys
from src.backend.User import User
from src.LoggerFactory import LoggerFactory


class UserDAO:

    __log = LoggerFactory.create_log(__name__)
    __CLUSTER_ID = "climatria.6oxhz.mongodb.net"
    __PRIMARY_DB = "climatria"

    def __init__(self, username, password, collection="users"):
        try:
            self.__client = pymongo.MongoClient(
                "mongodb+srv://" + username + ":" + password + "@" + self.__CLUSTER_ID)
            self.__collection = collection
            self.__log.info("Connected to MongoDB " + self.__CLUSTER_ID)
        except pymongo.errors.ConfigurationError as error:
            logging.error("Failed to Connect to Mongo due to invalid request. %s", error)
            sys.exit(1)

    def __collection_access(self):
        collection = self.__client.get_database(self.__PRIMARY_DB).get_collection(self.__collection)
        return collection

    @staticmethod
    def __transform_to_user(user_as_dict) -> User:
        return User(
            email=user_as_dict.get("_id"),
            name=user_as_dict.get("name"),
            phone_number=user_as_dict.get("phone_number"),
            ba=user_as_dict.get("ba"),
            zip_code=user_as_dict.get("zip_code"),
            last_alert=user_as_dict.get("last_alert")
        )

    def shut_down(self):
        self.__client.close()

    def find_by_id(self, user_id) -> User | None:
        collection = self.__collection_access()
        user_dict = collection.find_one({"_id": user_id})
        if user_dict is None:
            logging.info("User %s not found", user_id)
            return None

        return self.__transform_to_user(user_dict)

    def find_all(self) -> list[User]:
        collection = self.__collection_access()
        users_as_dict = collection.find({})
        # self.log.info("Fetching %s users from collection.", len(users_as_dict))
        return [self.__transform_to_user(user_dict) for user_dict in users_as_dict]

    def create(self, user):
        user_dict = user.__dict__
        collection = self.__collection_access()
        collection.insert_one(user_dict)

    def delete(self, user_id):
        collection = self.__collection_access()
        collection.delete_one({"_id": user_id})

    def truncate(self):
        self.__collection_access().drop()

