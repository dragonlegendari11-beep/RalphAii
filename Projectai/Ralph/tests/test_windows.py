from core.ralph import Ralph
from plugins.windows.plugin import WindowsPlugin


ralph = Ralph()

ralph.plugins.load(WindowsPlugin())

windows = ralph.services.get("windows")

windows.open_program("notepad.exe")