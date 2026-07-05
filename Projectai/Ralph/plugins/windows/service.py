import subprocess
import webbrowser


class WindowsService:

    def open_program(self, program: str):

        if program == "browser":
            webbrowser.open("https://www.google.com")
            return

        subprocess.Popen(program)

    def shutdown(self):
        subprocess.run(["shutdown", "/s", "/t", "0"])

    def restart(self):
        subprocess.run(["shutdown", "/r", "/t", "0"])
