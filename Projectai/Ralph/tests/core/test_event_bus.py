from core.event_bus import EventBus


def plugin1(name):
    print(f"Plugin1: {name}")


def plugin2(name):
    print(f"Plugin2: {name}")


bus = EventBus()

bus.subscribe("hello", plugin1)
bus.subscribe("hello", plugin2)

print("== Первый вызов ==")
bus.emit("hello", "Dragon")

bus.unsubscribe("hello", plugin1)

print("== Второй вызов ==")
bus.emit("hello", "Ralph")