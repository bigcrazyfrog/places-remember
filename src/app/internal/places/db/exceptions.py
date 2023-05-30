class NotFoundException(Exception):
    def __init__(self, name: str = "Object", id: str = "ID"):
        self.name = name
        self.id = id
