from core.plugin import Plugin


class TestPlugin(Plugin):

    def on_load(self, core):
        super().on_load(core)
        print("Plugin loaded")

    def on_enable(self):
        super().on_enable()
        print("Plugin enabled")

    def on_disable(self):
        super().on_disable()
        print("Plugin disabled")

    def on_unload(self):
        super().on_unload()
        print("Plugin unloaded")


plugin = TestPlugin()

plugin.on_load(None)
plugin.on_enable()
plugin.on_disable()
plugin.on_unload()