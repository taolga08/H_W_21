from abc import ABC, abstractmethod


class Abstract(ABC):
    @abstractmethod
    def add(self, name, count):
        pass

    @abstractmethod
    def remove(self, name, count):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_item(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass
