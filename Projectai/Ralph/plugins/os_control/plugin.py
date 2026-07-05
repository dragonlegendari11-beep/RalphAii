import platform

from core.plugin import Plugin
from plugins.os_control.windows import WindowsControl
from plugins.os_control.linux import LinuxControl
from plugins.os_control.mac import MacControl


class OSControlPlugin(Plugin):

    IMPLEMENTATIONS = {
        "Windows": WindowsControl,
        "Linux": LinuxControl,
        "Darwin": MacControl,  # Darwin = macOS
    }

    def on_load(self, ralph):
        super().on_load(ralph)

        system = platform.system()
        impl_class = self.IMPLEMENTATIONS.get(system)

        if impl_class is None:
            raise RuntimeError(f"OS не поддерживается: {system}")

        service = impl_class()
        ralph.services.register("os", service)

        print(f"OSControlPlugin loaded ({system})")
