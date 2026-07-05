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
        os_control = self.services.get("os")

        memory.log_history(text)

        if intent.name == "get_name":
            return f"Тебя зовут {memory.recall('name')}."

        if intent.name == "set_name":
            name = intent.data["name"]
            memory.remember("name", name)
            self.events.emit("name_changed", name)
            return f"Хорошо. Теперь тебя зовут {name}."

        if intent.name == "remember_fact":
            fact = intent.data["fact"]
            memory.add_fact(fact)
            self.events.emit("fact_remembered", fact)
            return "Запомнил."

        if intent.name == "create_project":
            name = intent.data["name"]
            memory.create_project(name)
            self.events.emit("project_created", name)
            return f"Создал проект «{name}»."

        if intent.name == "open_program":
            os_control.open_program(intent.data["program"])
            return "Открываю."

        if intent.name == "shutdown":
            os_control.shutdown()
            return "Выключаю компьютер."

        if intent.name == "restart":
            os_control.restart()
            return "Перезагружаю компьютер."

        if intent.name == "screenshot":
            path = os_control.screenshot()
            return f"Скриншот сохранён: {path}"

        if intent.name == "set_volume":
            os_control.set_volume(intent.data["percent"])
            return f"Громкость выставлена на {intent.data['percent']}%."

        return (
            "Пока я не умею поддерживать свободный разговор. "
            "Когда подключим AI-плагин, я смогу отвечать на такие вопросы."
        )
