from plugins.memory.storage import JsonStorage


class MemoryService:

    def __init__(self):

        self.storage = JsonStorage()

        self.memory = self.storage.load()

    def remember(self, key, value):

        self.memory[key] = value

        self.storage.save(self.memory)

    def recall(self, key):

        return self.memory.get(key)

    def forget(self, key):

        if key in self.memory:

            del self.memory[key]

            self.storage.save(self.memory)