
from project.abs import Abstract


class Storage(Abstract):
    def __init__(self, items, capacity):
        self.items = items
        self.capacity = capacity

    def add(self, name, count):
        is_found = False
        if self.get_free_space() > count:
            for key in self.items.keys():
                if name == key:
                    self.items[key] = self.items[key] + count
                    is_found = True
                if not is_found:
                    self.items[name] = count
                print("Товар добавлен")
            else:
                print(f"Товар не может быть добавлен, так как есть место только на {self.get_free_space()} товаров")

    def remove(self, name, count):
        for key in self.items.keys():
            if name == key:
                if self.items[key] - count >= 0:
                    self.items[key] = self.items[key] - count
                else:
                    print(f"Слишком мало {name}")
        else:
            print(f"{name.title()} - нужное количество есть на складе")

    def get_free_space(self):
        return self.capacity - sum(self.items.values())

    def get_item(self):
        return self.items

    def get_unique_items_count(self):
        return len(self.items.keys())
