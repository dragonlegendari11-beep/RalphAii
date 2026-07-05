from core.plugin import Plugin
from plugins.windows.service import WindowsService


class WindowsPlugin(Plugin):

    def on_load(self, ralph):
        super().on_load(ralph)

        ralph.services.register(
            "windows",
            WindowsService()
        )

        print("WindowsPlugin loaded")