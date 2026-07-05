class Plugin:
    """Базовый класс для всех плагинов Ralph."""

    def __init__(self):
        self.core = None
        self.enabled = False

    def on_load(self, core):
        """Вызывается при загрузке плагина."""
        self.core = core

    def on_enable(self):
        """Вызывается при включении плагина."""
        self.enabled = True

    def on_disable(self):
        """Вызывается при отключении плагина."""
        self.enabled = False

    def on_unload(self):
        """Вызывается при выгрузке плагина."""
        self.core = None