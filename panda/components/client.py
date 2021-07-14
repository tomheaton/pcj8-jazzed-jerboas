from panda.components.user import User


class Client:
    def __init__(self, ip: str, name: str, user: User = None):
        self.ip = ip
        self.name = name
        self.user = user

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

    def connect_user(self, user: User):
        self.user = user

    def disconnect_user(self):
        self.user = None
