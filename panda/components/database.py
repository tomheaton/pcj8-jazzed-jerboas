import json
import os
from panda.components.user import User


class Database:
    template = {
        "users": [
            {
                "uuid": "123",
                "username": "test",
                "password": "test",
                "preferences": {
                    "name": "bold cyan",
                    "border": "bold green",
                    "message": "bold white",
                    "message_border": "bold magenta",
                }
            },
            {
                "uuid": "546j5mummy-j45b6",
                "username": "test_username_two",
                "password": "test_password_two",
                "preferences": {
                    "name": "bold cyan",
                    "border": "bold green",
                    "message": "bold white",
                    "message_border": "bold magenta",
                }
            }
        ],
        "chatrooms": [
            {
                "uuid": "53245b6",
                "name": "test_room",
                "password": "test_password",
                "preferences": {
                    "name": "bold cyan",
                    "border": "bold green",
                    "message": "bold white",
                    "message_border": "bold magenta",
                }
            },
            {
                "uuid": "546j1my-j45b6",
                "username": "test_room_two",
                "password": "test_room_two",
                "preferences": {
                    "name": "bold cyan",
                    "border": "bold green",
                    "message": "bold white",
                    "message_border": "bold magenta",
                }
            }
        ]
    }

    def __init__(self, location):
        # self.location = os.path.expanduser(location)
        self.location = location
        self.load(self.location)

    def load(self, location):
        if os.path.exists(location):
            self.database = json.load(open(location, "r"))
        else:
            self.database = self.template

    def dump(self):
        json.dump(self.database, open(self.location, "w+"), indent=2)
        try:
            json.dump(self.database, open(self.location, "w+"), indent=2)
        except Exception as e:
            print(f"Error dumping database to file: {e}")

    def reset(self):
        self.database = self.template
        self.dump()

    def get(self, key):
        try:
            return self.database.get(key)
        except KeyError:
            print(f"No key (of value {key}) found in database.")

    def set(self, key, value):
        try:
            self.database[str(key)] = value
            self.dump()
        except Exception as e:
            print(f"Error saving values to database: {e}")

    def delete(self, key):
        try:
            return self.database.get(key)
        except KeyError:
            print(f"No key (of value {key}) found in database.")

    def put_user(self, user: User):
        obj = user.serialize()
        self.database["users"].append(obj)
        self.dump()

    def get_user(self, uuid):
        pass

    def print_uuids(self):
        for user in self.database["users"]:
            print(f"uuid: {user.get('uuid')}")

    def search_uuid(self, uuid):
        for user in self.database["users"]:
            if uuid == user.get("uuid"):
                print("found user in database")
                return user
        print("user not found")

    def search_username(self, username):
        for user in self.database["users"]:
            if username == user.get("username"):
                print("found user in database")
                return user
        print("user not found")
        return None

    def get_chatrooms(self):
        for room in self.database["chatrooms"]:
            print(f"chatroom found: {room}")
        pass
