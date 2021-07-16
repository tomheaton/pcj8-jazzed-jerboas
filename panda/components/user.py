from .user_preferences import UserPreferences


class User:

    template = {
      "uuid": "",
      "username": "",
      "password": "",
      "preferences": {}
    }

    def __init__(self, uuid: str, username: str, password: str, preferences: UserPreferences = None):
        self.uuid = uuid
        self.username = username
        self.password = password
        self.preferences = UserPreferences() if preferences is None else preferences

    def get_uuid(self):
        return self.uuid

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_preferences(self):
        return self.preferences

    def serialize(self):
        string = self.template
        string["uuid"] = self.uuid
        string["username"] = self.username
        string["password"] = self.password
        # string["preferences"] = self.preferences.serialize()
        # string["preferences"] = json.dump(self.preferences.style)
        string["preferences"] = {}
        return string

    def deserialize(self, string):
        self.uuid = string["uuid"]
        self.username = string["username"]
        self.password = string["password"]
        self.preferences = UserPreferences().deserialize(string["preferences"])
        return self
