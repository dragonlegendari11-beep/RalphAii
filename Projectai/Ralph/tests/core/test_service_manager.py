from core.service_manager import ServiceManager


class MemoryService:
    def remember(self):
        print("Memory works")


services = ServiceManager()

memory = MemoryService()

services.register("memory", memory)

print(services.has("memory"))

services.get("memory").remember()

services.unregister("memory")

print(services.has("memory"))