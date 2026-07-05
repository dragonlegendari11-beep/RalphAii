import json
from pathlib import Path


class JsonStorage:

    def __init__(self):
        base_dir = Path(__file__).resolve().parent
        self.path = base_dir / "memory.json"

        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.path, "w", encoding="utf8") as f:
                json.dump({}, f, indent=4)

    def load(self):
        try:
            with open(self.path, "r", encoding="utf8") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return {}

    def save(self, data):
        with open(self.path, "w", encoding="utf8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
