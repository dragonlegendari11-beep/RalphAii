class EventBus:
    def __init__(self):
        self._listeners = {}

    def subscribe(self, event: str, callback):
        self._listeners.setdefault(event, []).append(callback)

    def unsubscribe(self, event: str, callback):
        if event in self._listeners:
            self._listeners[event].remove(callback)

    def emit(self, event: str, *args, **kwargs):
        for callback in self._listeners.get(event, []):
            callback(*args, **kwargs)