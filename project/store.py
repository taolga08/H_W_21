
from project.storage import Storage


class Store(Storage):
    def __init__(self, items: dict, capacity: int = 100):
        super().__init__(items, capacity)
