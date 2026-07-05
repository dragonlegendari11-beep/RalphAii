from core.plugin import Plugin

from plugins.memory.service import MemoryService


class MemoryPlugin(Plugin):

    def on_load(self, ralph):

        super().on_load(ralph)

        service = MemoryService()

        ralph.services.register("memory", service)

        print("MemoryPlugin loaded")