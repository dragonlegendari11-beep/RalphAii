from core.ralph import Ralph

from plugins.memory.plugin import MemoryPlugin


ralph = Ralph()

ralph.plugins.load(MemoryPlugin())

memory = ralph.services.get("memory")

memory.remember("name", "Dragon")

print(memory.recall("name"))