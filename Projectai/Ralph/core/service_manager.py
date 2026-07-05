class ServiceManager:
    """Хранилище сервисов Ralph."""

    def __init__(self):
        self._services = {}

    def register(self, name: str, service):
        if name in self._services:
            raise ValueError(f"Service '{name}' already registered")

        self._services[name] = service

    def unregister(self, name: str):
        self._services.pop(name, None)

    def get(self, name: str):
        return self._services.get(name)

    def has(self, name: str):
        return name in self._services

    def all(self):
        return self._services