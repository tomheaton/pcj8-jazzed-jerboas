class ChatRoom:

    template = {}

    def __init__(self, name: str, uuid: str, private: bool, capacity: int, users: list[str]):
        self.name = name
        self.uuid = uuid
        self.private = private
        self.capacity = capacity
        self.users = users

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
