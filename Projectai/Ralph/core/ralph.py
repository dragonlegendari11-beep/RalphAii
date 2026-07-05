from core.intent_parser import IntentParser
from core.event_bus import EventBus
from core.plugin_manager import PluginManager
from core.service_manager import ServiceManager


class Ralph:

    def __init__(self):

        self.plugins = PluginManager(self)
        self.services = ServiceManager()
        self.events = EventBus()

        self.parser = IntentParser()

        self.running = False

    def start(self):
        self.running = True
        self.events.emit("start")
        print("Ralph запущен.")

    def stop(self):
        self.running = False
        self.events.emit("stop")
        print("Ralph остановлен.")

    def chat(self, text: str):

        intent = self.parser.parse(text)

        memory = self.services.get("memory")
        windows = self.services.get("windows")

        if intent.name == "get_name":
            return f"Тебя зовут {memory.recall('name')}."

        if intent.name == "set_name":
            name = intent.data["name"]
            memory.remember("name", name)
            self.events.emit("name_changed", name)
            return f"Хорошо. Теперь тебя зовут {name}."

        if intent.name == "open_program":
            windows.run(intent.data["program"])
            return "Открываю."

        return (
            "Пока я не умею поддерживать свободный разговор. "
            "Когда подключим AI-плагин, я смогу отвечать на такие вопросы."
        )
