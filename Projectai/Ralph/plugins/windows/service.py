import subprocess


class WindowsService:

    def open_program(self, program: str):
        subprocess.Popen(program)