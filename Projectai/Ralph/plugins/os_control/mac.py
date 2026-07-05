import subprocess

from plugins.os_control.base import BaseOSControl


class MacControl(BaseOSControl):

    PROGRAMS = {
        "блокнот": "TextEdit",
        "калькулятор": "Calculator",
        "проводник": "Finder",
    }

    def open_program(self, program: str):
        if program == "browser":
            subprocess.Popen(["open", "https://www.google.com"])
            return
        subprocess.Popen(["open", "-a", program])

    def shutdown(self):
        subprocess.run(["osascript", "-e", 'tell app "System Events" to shut down'])

    def restart(self):
        subprocess.run(["osascript", "-e", 'tell app "System Events" to restart'])

    def screenshot(self, path: str = "screenshot.png"):
        subprocess.run(["screencapture", path])
        return path

    def set_volume(self, percent: int):
        percent = max(0, min(percent, 100))
        subprocess.run(["osascript", "-e", f"set volume output volume {percent}"])
