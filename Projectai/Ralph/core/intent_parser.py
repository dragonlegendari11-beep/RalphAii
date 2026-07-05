from core.intent import Intent


class IntentParser:

    def parse(self, text: str):

        text = text.lower()

        # ---------- Имя ----------

        if any(x in text for x in [
            "как меня зовут",
            "моё имя",
            "мое имя",
            "назови меня"
        ]):
            return Intent("get_name")

        # ---------- Изменение имени ----------

        triggers = [
            "переименуй меня в",
            "измени моё имя на",
            "измени мое имя на",
            "зови меня",
            "теперь меня зовут"
        ]

        for trigger in triggers:

            if trigger in text:

                name = text.split(trigger, 1)[1].strip()

                return Intent(
                    "set_name",
                    {
                        "name": name
                    }
                )

        # ---------- Блокнот ----------

        if "блокнот" in text:

            return Intent(
                "open_program",
                {
                    "program": "notepad.exe"
                }
            )

        return Intent("chat")