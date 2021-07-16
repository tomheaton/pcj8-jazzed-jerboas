# ChatRoom Class

class Chatroom:
    def __init__(self, name: str, users: list):
        self.name = name
        self.users = [] if users is None else users


