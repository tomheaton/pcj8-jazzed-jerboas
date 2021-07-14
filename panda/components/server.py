from panda.components.chatroom import ChatRoom
from panda.components.user import User


class Server:
    def __init__(self, ip: str, name: str, users: list[User] = None, chatrooms: list[ChatRoom] = None):
        self.ip = ip
        self.name = name
        self.users = [] if users is None else users
        self.chatrooms = [] if chatrooms is None else chatrooms

    def get_ip(self):
        return self.ip

    def get_name(self):
        return self.name

    def get_users(self):
        return self.users

    def get_chatrooms(self):
        return self.chatrooms

    def print_info(self):
        print(f"[Server] IP: {self.ip}, Hostname: {self.name}")

    def add_user(self, user: User):
        self.users.append(user)

    def purge(self):
        self.users = []
