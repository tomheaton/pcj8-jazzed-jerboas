# Server Utilities
import os
import uuid
from components.database import Database
from components.user import User


# TODO: create first time initialization function.
def generate_salt():
    return os.urandom(32).hex()


def generate_uuid():
    return uuid.uuid4().hex


def create_database(location):
    print("creating database...")
    database = Database(location)
    return database


def login_user(username, password, salt, database) -> bool:
    user = database.search_username(username)
    if user is not None:
        print(test_password(password, user.get("password"), salt))
        return test_password(password, user.get("password"), salt)
    else:
        return False


def register_user(username, password, salt, database) -> bool:
    user = User(generate_uuid(), username, generate_key(password, salt), salt)
    database.put_user(user)
    return True


def generate_key(password, salt):
    key = password + salt
    return key


def test_password(password, key, salt) -> bool:
    new_key = password + salt
    return new_key == key


def create_chatroom():
    pass


def join_chatroom():
    pass


def generate_chatrooms():
    pass


# def chatroom_pop():
#     pass
#
#
# def chatroom_pop_users(chatrooms: list[ChatRoom]):
#     for room in chatrooms:
#         room.purge()
#
#
# def server_pop_users(users: list[User]):
#     users.purge()
