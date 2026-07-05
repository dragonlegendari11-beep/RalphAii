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

    if intent.name == "remember_fact":
        fact = intent.data["fact"]
        facts = memory.recall("facts") or []
        facts.append(fact)
        memory.remember("facts", facts)
        self.events.emit("fact_remembered", fact)
        return "Запомнил."

    if intent.name == "open_program":
        windows.open_program(intent.data["program"])
        return "Открываю."

    if intent.name == "shutdown":
        windows.shutdown()
        return "Выключаю компьютер."

    if intent.name == "restart":
        windows.restart()
        return "Перезагружаю компьютер."

    return (
        "Пока я не умею поддерживать свободный разговор. "
        "Когда подключим AI-плагин, я смогу отвечать на такие вопросы."
    )
