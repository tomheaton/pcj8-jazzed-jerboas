class UserPreferences:

    template = {
        "name": "bold cyan",
        "border": "bold green",
        "message": "bold white",
        "message_border": "bold magenta"
      }

    def __init__(self, name: str = None, border: str = None, message: str = None, message_border: str = None):
        # TODO: maybe clean this up?
        # self.update(name, border, message, message_border)
        self.name = "bold cyan" if name is None else name
        self.border = "bold green" if border is None else border
        self.message = "bold white" if message is None else message
        self.message_border = "bold magenta" if message_border is None else message_border

    def reset(self):
        # TODO: use style dict instead.
        # self.styles = self.templates
        self.name = "bold cyan"
        self.border = "bold green"
        self.message = "bold white"
        self.message_border = "bold magenta"

    def update(self, name: str = None, border: str = None, message: str = None, message_border: str = None):
        self.name = "bold cyan" if name is None else name
        self.border = "bold green" if border is None else border
        self.message = "bold white" if message is None else message
        self.message_border = "bold magenta" if message_border is None else message_border

    # TODO: fix this.
    def serialize(self):
        string = self.template
        string["name"] = self.name
        string["border"] = self.border
        string["message"] = self.message
        string["message_border"] = self.message_border
        return string

    # TODO: this.
    def deserialize(self, string):
        pass
