from core.ralph import Ralph
from plugins.memory.plugin import MemoryPlugin

ralph = Ralph()
ralph.plugins.load(MemoryPlugin())

memory = ralph.services.get("memory")

memory.set_profile("name", "Dragon")
print("Profile name:", memory.get_profile("name"))

memory.add_fact("любит Python")
print("Facts:", memory.get_facts())

project = memory.create_project("Ralph")
print("Project:", project)

memory.add_note("не забыть подключить AI-плагин")
print("Notes:", memory.get_notes())

memory.set_setting("voice", "male")
print("Setting voice:", memory.get_setting("voice"))

print("History:", memory.get_history())