from core.plugin import Plugin
from core.plugin_manager import PluginManager


class DummyCore:
    pass


class TestPlugin(Plugin):

    def on_load(self, core):
        super().on_load(core)
        print("Loaded")

    def on_enable(self):
        super().on_enable()
        print("Enabled")

    def on_disable(self):
        super().on_disable()
        print("Disabled")

    def on_unload(self):
        super().on_unload()
        print("Unloaded")


core = DummyCore()

manager = PluginManager(core)

manager.load(TestPlugin())

print("----")

manager.enable_all()

print("----")

manager.disable_all()

print("----")

manager.unload_all()