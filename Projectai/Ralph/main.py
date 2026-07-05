from core.ralph import Ralph

from plugins.memory.plugin import MemoryPlugin
from plugins.os_control.plugin import OSControlPlugin


def main():

    ralph = Ralph()

    ralph.plugins.load(MemoryPlugin())
    ralph.plugins.load(OSControlPlugin())

    memory = ralph.services.get("memory")

    if memory.recall("name") is None:
        memory.remember("name", "Dragon")

    print("========== Ralph ==========")

    while True:

        text = input("\nТы: ")

        if text.lower() == "exit":
            break

        answer = ralph.chat(text)

        print(f"\nRalph: {answer}")


if __name__ == "__main__":
    main()
