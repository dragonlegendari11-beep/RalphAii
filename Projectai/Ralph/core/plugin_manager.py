from core.plugin import Plugin


class PluginManager:

    def __init__(self, core):
        self.core = core
        self.plugins = []

    def load(self, plugin: Plugin):
        plugin.on_load(self.core)
        self.plugins.append(plugin)

    def enable_all(self):
        for plugin in self.plugins:
            plugin.on_enable()

    def disable_all(self):
        for plugin in self.plugins:
            plugin.on_disable()

    def unload_all(self):
        for plugin in self.plugins:
            plugin.on_unload()

        self.plugins.clear()