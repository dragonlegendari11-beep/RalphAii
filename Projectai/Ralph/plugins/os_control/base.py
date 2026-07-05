class BaseOSControl:
    """Общий контракт. Каждая ОС реализует эти методы своим способом."""

    def open_program(self, program: str):
        raise NotImplementedError

    def shutdown(self):
        raise NotImplementedError

    def restart(self):
        raise NotImplementedError

    def screenshot(self, path: str = "screenshot.png"):
        raise NotImplementedError

    def set_volume(self, percent: int):
        raise NotImplementedError