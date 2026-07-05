from core.intent_parser import IntentParser

parser = IntentParser()

phrases = [
    "как меня зовут",
    "переименуй меня в Дракон",
    "запомни что я люблю Python",
    "открой блокнот",
    "открой калькулятор",
    "открой проводник",
    "открой браузер",
    "выключи компьютер",
    "перезагрузи пк",
    "расскажи анекдот",
]

for text in phrases:
    intent = parser.parse(text)
    print(f"{text!r} -> {intent.name} {intent.data}")
