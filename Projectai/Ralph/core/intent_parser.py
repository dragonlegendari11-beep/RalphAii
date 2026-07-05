from core.intent import Intent


class IntentParser:

    def parse(self, text: str):

        text = text.lower().strip()

        # ---------- Имя ----------

        if any(x in text for x in [
            "как меня зовут",
            "моё имя",
            "мое имя",
            "назови меня"
        ]):
            return Intent("get_name")

        # ---------- Изменение имени ----------

        rename_triggers = [
            "переименуй меня в",
            "измени моё имя на",
            "измени мое имя на",
            "зови меня",
            "теперь меня зовут"
        ]

        for trigger in rename_triggers:
            if trigger in text:
                name = text.split(trigger, 1)[1].strip()
                return Intent("set_name", {"name": name})

        # ---------- Запомнить факт ----------
        # Порядок важен: длинные триггеры проверяем раньше короткого "запомни"

        remember_triggers = [
            "запомни, что",
            "запомни что",
            "запомни"
        ]

        for trigger in remember_triggers:
            if trigger in text:
                fact = text.split(trigger, 1)[1].strip()
                if fact:
                    return Intent("remember_fact", {"fact": fact})

        # ---------- Проекты ----------

        project_triggers = ["создай проект"]

        for trigger in project_triggers:
            if trigger in text:
                name = text.split(trigger, 1)[1].strip()
                if name:
                    return Intent("create_project", {"name": name})

        # ---------- Открыть программу ----------

        if "блокнот" in text:
            return Intent("open_program", {"program": "notepad.exe"})

        if "калькулятор" in text:
            return Intent("open_program", {"program": "calc.exe"})

        if "проводник" in text:
            return Intent("open_program", {"program": "explorer.exe"})

        if "браузер" in text:
            return Intent("open_program", {"program": "browser"})

        # ---------- Управление питанием ----------

        if any(x in text for x in [
            "выключи компьютер",
            "выключи пк",
            "выключи ноутбук"
        ]):
            return Intent("shutdown")

        if any(x in text for x in [
            "перезагрузи компьютер",
            "перезагрузи пк",
            "перезагрузи ноутбук"
        ]):
            return Intent("restart")

        return Intent("chat")
