class Message:
    def __init__(self, uuid: str, content: str):
        self.uuid = uuid
        self.content = content

    def get_uuid(self):
        return self.uuid

    def get_content(self):
        return self.content
