import subprocess

from plugins.os_control.base import BaseOSControl


class LinuxControl(BaseOSControl):

    PROGRAMS = {
        "блокнот": "gedit",
        "калькулятор": "gnome-calculator",
        "проводник": "nautilus",
    }

    def open_program(self, program: str):
        if program == "browser":
            subprocess.Popen(["xdg-open", "https://www.google.com"])
            return
        subprocess.Popen([program])

    def shutdown(self):
        subprocess.run(["systemctl", "poweroff"])

    def restart(self):
        subprocess.run(["systemctl", "reboot"])

    def screenshot(self, path: str = "screenshot.png"):
        subprocess.run(["gnome-screenshot", "-f", path])
        return path

    def set_volume(self, percent: int):
        percent = max(0, min(percent, 100))
        subprocess.run(["amixer", "-D", "pulse", "sset", "Master", f"{percent}%"])
