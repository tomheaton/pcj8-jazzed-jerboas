# TODO: split these into separate files.

class ChatRoom:
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

    def serialize(self):
        # TODO: this.
        return {}


class Server:
    def __init__(self, ip: str, name: str, chatrooms: list[ChatRoom] = None):
        self.ip = ip
        self.name = name
        self.chatrooms = [] if chatrooms is None else chatrooms

    def get_ip(self):
        return self.ip

    def get_name(self):
        return self.name

    def get_chatrooms(self):
        return self.chatrooms

    def print_info(self):
        print(f"[Server] IP: {self.ip}, Hostname: {self.name}")


class Client:
    def __init__(self, ip: str, name: str):
        self.ip = ip
        self.name = name

    def get_ip(self):
        return self.ip

    def get_name(self):
        return self.name

    def print_info(self):
        print(f"[Client] IP: {self.ip}, Hostname: {self.name}")

    def connect_to_server(self):
        pass

    def send_message(self, message: str):
        pass

    def send_loop(self):
        pass

    def receive_loop(self):
        pass

    async def connect_to_server2(self):
        # await sio.connect(URL)
        # await sio.wait()
        pass


class UserPreferences:
    def __init__(self, name: str = None, border: str = None, message: str = None, message_border: str = None):
        self.name = "bold cyan" if name is None else name
        self.border = "bold green" if border is None else border
        self.message = "bold white" if message is None else message
        self.message_border = "bold magenta" if message_border is None else message_border

    def reset(self):
        self.name = "bold cyan"
        self.border = "bold green"
        self.message = "bold white"
        self.message_border = "bold magenta"

    def update(self, name: str = None, border: str = None, message: str = None, message_border: str = None):
        self.name = "bold cyan" if name is None else name
        self.border = "bold green" if border is None else border
        self.message = "bold white" if message is None else message
        self.message_border = "bold magenta" if message_border is None else message_border


class User:
    def __init__(self, name: str, uuid: str, preferences: UserPreferences = None):
        self.name = name
        self.uuid = uuid
        self.preferences = UserPreferences() if preferences is None else preferences

    def get_name(self):
        return self.name

    def get_uuid(self):
        return self.uuid

    def get_preferences(self):
        return self.preferences


class Message:
    def __init__(self, uuid: str, content: str):
        self.uuid = uuid
        self.content = content

    def get_uuid(self):
        return self.uuid

    def get_content(self):
        return self.content
