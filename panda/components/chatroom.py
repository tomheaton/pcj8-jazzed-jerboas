from .user import User

MAX_CAPACITY = 16


class ChatRoom:

    template = {
        "name": "",
        "uuid": "",
        "users": {},
        "private": "",
        "capacity": 0
    }

    def __init__(self, name: str, uuid: str, users: list[User] = None, private: bool = False,
                 capacity: int = MAX_CAPACITY):
        self.name = name
        self.uuid = uuid
        self.users = [] if users is None else users
        self.private = private
        self.capacity = capacity

    def get_name(self):
        return self.name

    def get_uuid(self):
        return self.uuid

    def is_private(self):
        return self.private

    def get_capacity(self):
        return self.capacity

    def get_users(self):
        return self.users

    def get_user_count(self):
        return len(self.users)

    def purge(self):
        self.users = []

    def serialize(self):
        pass

    def deserialize(self):
        pass
