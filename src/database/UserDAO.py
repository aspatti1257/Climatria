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

    def shut_down(self):
        self.__client.close()

    def fetch(self, user_id) -> User | None:
        collection = self.__collection_access()
        user_dict = collection.find_one({"_id": user_id})
        if user_dict is None:
            logging.info("User %s not found", user_id)
            return None

        # This is terrible. Need smarter deserialization into strongly typed objects.
        user = User(user_dict.get("_id"), user_dict.get("name"), user_dict.get("ba"), user_dict.get("lat"),
                    user_dict.get("long"), user_dict.get("last_alert"))
        return user

    def create(self, user):
        user_dict = user.__dict__
        collection = self.__collection_access()
        collection.insert_one(user_dict)

    def delete(self, user_id):
        collection = self.__collection_access()
        collection.delete_one({"_id": user_id})

    def truncate(self):
        self.__collection_access().drop()

