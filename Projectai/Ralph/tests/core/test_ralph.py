from core.ralph import Ralph
from core.plugin import Plugin


class HelloPlugin(Plugin):

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


ralph = Ralph()

ralph.plugins.load(HelloPlugin())

ralph.plugins.enable_all()

ralph.start()

ralph.stop()