import uuid


class Controller:
    def __init__(self, name, *args, **kwargs):
        self.uuid = uuid.uuid4()
        self.name = name


class Stateful:
    def __init__(self, name, *args, **kwargs):
        self.uuid = uuid.uuid4()
        self.name = name
