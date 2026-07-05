import subprocess
import webbrowser

from plugins.os_control.base import BaseOSControl


class WindowsControl(BaseOSControl):

    PROGRAMS = {
        "блокнот": "notepad.exe",
        "калькулятор": "calc.exe",
        "проводник": "explorer.exe",
    }

    def open_program(self, program: str):
        if program == "browser":
            webbrowser.open("https://www.google.com")
            return
        subprocess.Popen(program)

    def shutdown(self):
        subprocess.run(["shutdown", "/s", "/t", "0"])

    def restart(self):
        subprocess.run(["shutdown", "/r", "/t", "0"])

    def screenshot(self, path: str = "screenshot.png"):
        from PIL import ImageGrab
        img = ImageGrab.grab()
        img.save(path)
        return path

    def set_volume(self, percent: int):
        # Требует pip install pycaw comtypes
        from ctypes import cast, POINTER
        from comtypes import CLSCTX_ALL
        from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMasterVolumeLevelScalar(max(0, min(percent, 100)) / 100, None)
